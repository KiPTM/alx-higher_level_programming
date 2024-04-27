#!/usr/bin/python3
"""
Sends a request to a URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, prints an error message with the status code.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except Exception as e:
        print(e)
