#!/bin/bash
#script that takes url, send request and displays size of body
curl -sI "$1" | grep Content-Length | cut -d ' ' -f 2
