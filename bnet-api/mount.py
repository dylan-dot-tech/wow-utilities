#!/usr/bin/env python3

# author: Dylan Riley
# contact: hi@dylan.tech
# copyright: https://dylan.tech
# version: 2023-02-06
# description: Battle.net Mount API Endpoints

import json
import requests
import utilities as util


# Returns an index of mounts
def mounts_index():
    url = "https://us.api.blizzard.com/data/wow/mount/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

# Returns a mount by ID
def mount(mount_id):
    url = "https://us.api.blizzard.com/data/wow/mount/{}?namespace=static-us&locale=en_US&access_token={}".format(mount_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

# Performs a search of mounts.
# For more detail see: https://develop.battle.net/documentation/world-of-warcraft/guides/search
def mount_search(mount_name):
    url = "https://us.api.blizzard.com/data/wow/search/mount?namespace=static-us&name.en_US={}&orderby=id&_page=1&access_token={}".format(mount_name, util.get_access_token())
    response = requests.get(url)
    return response.json()

