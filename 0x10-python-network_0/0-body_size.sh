#!/bin/bash

# Check if a URL is provided as argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the provided URL and display the size of the body of the response in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
