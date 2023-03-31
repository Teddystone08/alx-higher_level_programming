#!/bin/bash
# script that takes URL argument, send Get request and display response
curl "$1" -sX GET -H "X-School-User-Id: 98"
