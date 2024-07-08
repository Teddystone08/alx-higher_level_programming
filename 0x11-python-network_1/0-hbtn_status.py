#!/usr/bin/python3
import urllib.request

with urllibe.request.urlopen(https: // alx-intranet.hbtn.io/status)
as response:
    content = response.read().decode('utf-8')
    print("Body response:")
    print(f"\t- type: {content-type}")
    print(f"\t- content: {conten}")
