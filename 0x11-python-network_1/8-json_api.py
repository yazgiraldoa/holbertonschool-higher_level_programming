#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    try:
        data = sys.argv[1]
    except IndexError:
        data = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': data})
    try:
        response = r.json()
        if len(response) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response['id'], response['name']))
    except ValueError as e:
        print("Not a valid JSON")
