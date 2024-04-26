#!/bin/bash
# Send GET request to URL with custom header and display response body
curl -s -H "X-School-User-Id: 98" "$1"
