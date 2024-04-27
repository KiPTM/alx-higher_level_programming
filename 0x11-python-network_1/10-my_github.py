#!/usr/bin/python3
"""
Displays your GitHub id using the GitHub API and Basic Authentication.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    try:
        response = requests.get("https://api.github.com/user", auth=(username, password))
        if response.status_code == 200:
            user_data = response.json()
            print(user_data['id'])
        else:
            print(None)
    except Exception as e:
        print(e)
