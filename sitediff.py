import ssl 
import sys, getopt
import re
import os
import difflib
import requests
import yaml
from yaml.loader import SafeLoader

cache_path = '.cache_sitediff'

def diff_files(file1_path, file2_path):
    if os.path.isfile(file1_path) and  os.path.isfile(file2_path):
        with open(file1_path) as file_1:
            file_1_text = file_1.readlines()
    
        with open(file2_path) as file_2:
            file_2_text = file_2.readlines()
        
        for line in difflib.unified_diff(
            file_1_text, file_2_text, lineterm=''):
            print(line)

def generate_name_from_url(url):
    return re.sub('[^A-Za-z0-9]+', '_', url)

def get_url_data(url):
    import urllib.request
    context = ssl._create_unverified_context()
    web_url  = urllib.request.urlopen(url, context=context)
    data = web_url.read()
    return data

def create_cache_folder(cache_path):
    try: 
        os.makedirs(cache_path, exist_ok = True) 
    except OSError as error: 
        print(error) 

def create_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

def read_url_file(yml_file):
    with open(yml_file) as f:
        data = yaml.load(f, Loader=SafeLoader)
        return data

def process_url(url):
    file_name = cache_path + "/" + generate_name_from_url(url)
    create_cache_folder(cache_path)
    create_file(file_name+"-latest", get_url_data(url))
    diff_files(file_name, file_name+"-latest")
    os.replace(file_name+"-latest", file_name)

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hu:o:",["url=","file="])
    except getopt.GetoptError:
        print('sitediff.py [--url <website_url>] [--file <inputfile>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('sitediff.py [--url <website_url>] [--file <inputfile>]')
            sys.exit()
        elif opt in ("-u", "--url"):
            process_url(arg)
        elif opt in ("-f", "--file"):
            urls = read_url_file(arg)
            for item in urls:
                process_url(item['url'])

if __name__ == "__main__":
   main(sys.argv[1:])

