#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    content = response.read()
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", content.decode('utf8'))
