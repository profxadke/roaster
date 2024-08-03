#!/usr/bin/env python3


import readline
from sys import argv
from requests import post


# TODO: ofc, refactor and make code modular than simply running this as a python script.


args = argv[1:]
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://github-roast.pages.dev',
    'priority': 'u=1, i',
    'referer': 'https://github-roast.pages.dev/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}


if len(args) >= 1:
    username = args[0]
else:
    username = input("Enter someone's GitHub username you wish to roast: ")
    print()

json_data = {
    'username': username,
    'language': 'english',
}; resp = post('https://github-roast.pages.dev/llama', headers=headers, json=json_data)


print(resp.json()['roast'])
