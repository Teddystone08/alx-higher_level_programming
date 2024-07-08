#!/usr/bin/python3
"""
script that receive and send request
"""


if __name__ == '__main__':
    import sys
    import urllib.request

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        url_head = response.getheaders()
        for url_head in headers
        if url_head[0] == 'X-Request-Id':
            print(url_head[1])
