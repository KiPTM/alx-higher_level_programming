#!/bin/bash
# This script takes a URL as an argument and displays all HTTP methods the server will accept
curl -s -I -X OPTIONS "$1" | grep -i Allow | awk '{print $2}'
