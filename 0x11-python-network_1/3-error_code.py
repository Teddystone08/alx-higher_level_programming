#!/usr/bin/python3
"""
Script the accept url input. send and displays response
"""


if __name__ == "__main__":

    import urllib.request
    import urllib.error
    import sys

    url = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(url) as response:
            url_input = response.read()
            print(url_input.decode('utf-8'))

    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
