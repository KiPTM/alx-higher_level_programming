#!/bin/bash
# Send POST request to URL with specified parameters and display response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
