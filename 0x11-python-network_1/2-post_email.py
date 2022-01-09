#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email": sys.argv[2]})
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data, method="POST")
    with request.urlopen(req) as response:
        content = response.read()
        print(content.decode('utf8'))
