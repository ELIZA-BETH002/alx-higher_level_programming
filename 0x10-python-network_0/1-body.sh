#!/bin/bash
# This script sends a GET request to an URL with curl, and display the body of the response

url=$1

# Send a GET request to the URL
response=$(curl -s -X GET "$url")

# Check the status code of the response
status_code=$(echo "$response" | head -1 | awk '{print $2}')

# Only display the body of the response if the status code is 200
if [ "$status_code" == "200" ]; then
  echo "$response" | tail -n +2
fi
