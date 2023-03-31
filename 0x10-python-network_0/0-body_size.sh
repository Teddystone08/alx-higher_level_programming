#!/bin/bash
#script that takes url, send request and displays body size
curl -sI "$@" -X GET | grep Content-Length | cut -d: -f2 | tr -d ' '
