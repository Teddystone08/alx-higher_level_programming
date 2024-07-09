#!/usr/bin/python3
"""
Script for fetch url
"""

if __name__ == "__main__":
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    print('Body response:')
    print('\t- type:', type(response.content.decode()))
    print('\t- content:', response.content.decode())
