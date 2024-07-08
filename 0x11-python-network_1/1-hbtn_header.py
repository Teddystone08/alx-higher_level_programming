#!/usr/bin/python3
"""
script that receive and send request
"""


if __name__ == '__main__':
    import sys
    import urllib.request
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        url_head = response.info()
        print(url_head['X-Request-Id'])
