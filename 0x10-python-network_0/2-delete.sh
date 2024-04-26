#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response

# Check if a URL is provided as argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send DELETE request to the provided URL and display the body of the response
curl -X DELETE -s "$1"
