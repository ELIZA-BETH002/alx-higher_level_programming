#!/usr/bin/python3

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    body = response.read()
    utf8_content = body.decode('utf-8')

print("Body response:")
print("    - type:", type(body))
print("    - content:", body)
print("    - utf8 content:", utf8_content)
