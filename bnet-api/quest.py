#!/usr/bin/env python3

# author: Dylan Riley
# contact: hi@dylan.tech
# copyright: https://dylan.tech
# version: 2023-02-03
# description: Battle.net Quest API Endpoints

import json
import requests
import utilities as util


def quests_index():
    url = "https://us.api.blizzard.com/data/wow/quest/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

def quest(quest_id):
    # TODO: quest_id must be > 1
    url = "https://us.api.blizzard.com/data/wow/quest/{}?namespace=static-us&locale=en_US&access_token={}".format(quest_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

def quest_categories_index():
    url = "https://us.api.blizzard.com/data/wow/quest/category/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

def quest_category(quest_category_id):
    url = "https://us.api.blizzard.com/data/wow/quest/category/{}?namespace=static-us&locale=en_US&access_token={}".format(quest_category_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

def quest_areas_index():
    url = "https://us.api.blizzard.com/data/wow/quest/area/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

def quest_area(quest_area_id):
    url = "https://us.api.blizzard.com/data/wow/quest/area/{}?namespace=static-us&locale=en_US&access_token={}".format(quest_area_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

def quest_types_index():
    url = "https://us.api.blizzard.com/data/wow/quest/type/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

def quest_type(quest_type_id):
    url = "https://us.api.blizzard.com/data/wow/quest/type/1?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

