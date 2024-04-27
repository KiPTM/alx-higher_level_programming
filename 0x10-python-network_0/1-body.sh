#!/bin/bash
# This script sends a GET request to the URL and displays the body of the response for a 200 status code
curl -s -o /dev/null -w "%{http_code}" "$1" | { read code; [ $code -eq 200 ] && curl -s "$1"; }
