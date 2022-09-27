![GitHub](https://img.shields.io/github/license/costaconrado/sitediff?style=for-the-badge)

# sitediff

Python 3 command line tool that scrapes the plain text of a given website url or a yml file and shows a diff in the content compared to the previous run of that same program for that website.

## Quick start

```sh
$ pip install -r requirements.txt
$ python3 sitediff.py --url https://subversion.apache.org/security/
```

## working with YAML
You can run this given the following example YAML
```sh
$ python3 sitediff.py --file example.yml
```
```yml
---
- url: https://subversion.apache.org/security/
- url: https://curl.haxx.se/docs/security.html
- url: http://web.mit.edu/Kerberos/advisories/
- url: https://www.samba.org/samba/history/security.html
- url: https://www.mozilla.org/en-US/security/advisories/
```