#!/bin/bash
# script that takes url and displays all http methods the server accepts
curl "$1" -X OPTIONS -sI | grep Allow: | cut -d' ' -f2-
