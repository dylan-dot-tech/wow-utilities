#!/usr/bin/env python3

# author: Dylan Riley
# contact: hi@dylan.tech
# copyright: https://dylan.tech
# version: 2023-02-03
# description: Utilities to accompany the Battle.net API

import os
import json
import requests


def write_json(json_in):
    with open('out.json', 'w', encoding='utf-8') as f:
        json.dump(json_in, f, ensure_ascii=False, indent=4)
    return

def get_access_token():
    data = { "grant_type": "client_credentials" }
    client_id = os.environ['BNET_CLIENT_ID']
    client_secret = os.environ['BNET_CLIENT_SECRET']
    response = requests.post("https://us.battle.net/oauth/token", data=data, auth=(client_id, client_secret))
    json = response.json()
    return json["access_token"]

