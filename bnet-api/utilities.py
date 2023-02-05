#!/usr/bin/env python3

# author: Dylan Riley
# contact: hi@dylan.tech
# copyright: https://dylan.tech
# version: 2023-02-04
# description: Utilities to accompany the Battle.net API

import os
import json
import time
import requests


def write_json(json_in, filename = str(time.time())):
    """
    Writes the input JSON data to a file.

    This function takes a dictionary or list as input (`json_in`), and writes it to a JSON file. The file name is generated based on the current time by default, but can be specified as an argument. The file is saved in the "out" directory, with a ".json" extension.

    Parameters:
    json_in (dict or list): The input JSON data to be written to the file.
    filename (str, optional): The name of the file to be written, without the ".json" extension. Defaults to the current time as a string.

    Returns:
    None: This function does not return a value.
    """
    with open("out/{}.json".format(filename), "w", encoding="utf-8") as f:
        json.dump(json_in, f, ensure_ascii=False, indent=4)
    return

def get_access_token():
    """
    This function retrieves an access token from the Battle.net API by making a POST request to the API's token endpoint.
    The client credentials required for the API request are obtained from the environment variables BNET_CLIENT_ID and BNET_CLIENT_SECRET.

    Returns:
        str: The access token returned from the API.

    Raises:
        requests.exceptions.HTTPError: If the API request fails, an exception is raised indicating the error.
    """
    url = "https://us.battle.net/oauth/token"
    data = { "grant_type": "client_credentials" }

    client_id = os.environ.get("BNET_CLIENT_ID")
    client_secret = os.environ.get("BNET_CLIENT_SECRET")
    auth = (client_id, client_secret)

    response = requests.post(url, data=data, auth=auth)
    response.raise_for_status()

    access_token = response.json().get("access_token")
    return access_token

