#!/bin/bash
curl -s "$1" | grep -o "my index page\|my index page is so cool! Mainly because it’s in Python" || echo "Unknown response"

