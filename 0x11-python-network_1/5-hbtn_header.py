#!/usr/bin/python3
"""
Script that accept url input, send and displays variable in header
"""

import request
import sys

url = sys.argv[1]

url_res = request.get(url)
request_id = response.hearder.get('X-Request-Id')
print(request_id)
