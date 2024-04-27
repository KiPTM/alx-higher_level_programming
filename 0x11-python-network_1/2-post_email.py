#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter and displays the body of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = "email=" + email
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
