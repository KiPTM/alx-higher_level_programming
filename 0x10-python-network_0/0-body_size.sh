#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl, and displays a specific message based on the response
curl -s "$1" | grep -o "my index page\|my index page is so cool! Mainly because it’s in Python" || echo "Unknown response"
