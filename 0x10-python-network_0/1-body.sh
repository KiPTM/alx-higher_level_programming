#!/bin/bash

# Check if a URL is provided as argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send GET request to the provided URL and display only the body of a 200 status code response
curl -s -o /dev/null -w "%{http_code}" "$1" | {
    read status_code
    if [ "$status_code" == "200" ]; then
        curl -s "$1"
    else
        echo "Error: Status code $status_code"
    fi
}
