#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL using curl, and displays a specific message based on the response

response=$(curl -s "$1")

if [[ $response == *"my index page"* ]]; then
    echo "GET / => \"my index page\""
elif [[ $response == *"my index page is so cool! Mainly because it’s in Python"* ]]; then
    echo "GET / => \"my index page is so cool! Mainly because it’s in Python\""
else
    echo "Unknown response"
fi
