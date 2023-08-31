#!/bin/bash
# This script sends a GET request to an URL with curl, and display the body of the response

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the provided URL and store the response
response=$(curl -s -w "%{http_code}" "$1")

# Check if the response status code is 200
if [ "$response" == "200" ]; then
    # Display only the body of the response
    curl -s "$1"
fi
