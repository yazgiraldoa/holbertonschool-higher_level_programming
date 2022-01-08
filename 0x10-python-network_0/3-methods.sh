#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept
curl -sI "Allow" "$1" | grep -i "Allow:" | cut --complement -d " " -f1
