#!/bin/bash
# This script sends a GET request to the URL and displays the body of the response if the status code is 200
curl -s -o /dev/null -w "%{http_code}\n" "$1" | { read code; [ $code -eq 200 ] && curl -s "$1"; }
