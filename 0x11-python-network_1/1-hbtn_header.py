#!/usr/bin/python3
"""
script that receive and send request
"""


if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        head = response.input()
        print(head['X-Request-Id'])
