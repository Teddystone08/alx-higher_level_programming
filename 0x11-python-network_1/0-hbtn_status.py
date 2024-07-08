#!/usr/bin/python3

"""
script to fetch url
"""


if __name__ == '__main__':
    import urllib.request
    url = 'alx-intranet.hbtn.io/status'
    with urllibe.request.urlopen(url) as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(body)))
        print('\t- content: {}'.format(body))
        print('\t- utf8 content: {}'.format(body.decode('utf-8')))
