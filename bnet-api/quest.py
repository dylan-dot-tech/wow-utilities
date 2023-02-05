#!/usr/bin/env python3

# author: Dylan Riley
# contact: hi@dylan.tech
# copyright: https://dylan.tech
# version: 2023-02-03
# description: Battle.net Quest API Endpoints

import json
import requests
import utilities as util


# Lists respective API endpoints for quest: categories, areas, and types
def quests_index():
    url = "https://us.api.blizzard.com/data/wow/quest/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists quest metadata for a given quest_id:
# id, title, area, requirements, rewards
def quest(quest_id):
    # TODO: quest_id must be > 1
    url = "https://us.api.blizzard.com/data/wow/quest/{}?namespace=static-us&locale=en_US&access_token={}".format(quest_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists quest category name, id, and respective API endpoint
# Example: Seasonal, Warlock, Engineering, PvP, etc.
def quest_categories_index():
    url = "https://us.api.blizzard.com/data/wow/quest/category/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists all quest names, id's, and respective API endpoints for a given quest_category_id
def quest_category(quest_category_id):
    url = "https://us.api.blizzard.com/data/wow/quest/category/{}?namespace=static-us&locale=en_US&access_token={}".format(quest_category_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists all quest area names, id's, and respective API endpoints
def quest_areas_index():
    url = "https://us.api.blizzard.com/data/wow/quest/area/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists all quest names, id's, and respective API endpoints for a given quest_area_id
def quest_area(quest_area_id):
    url = "https://us.api.blizzard.com/data/wow/quest/area/{}?namespace=static-us&locale=en_US&access_token={}".format(quest_area_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists all quest type names, id's, and respective API endpoints
# Example: PvP, Raid, Dungeon, Group
def quest_types_index():
    url = "https://us.api.blizzard.com/data/wow/quest/type/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists all quest names, id's, and respective API endpoints for a given quest_type_id
def quest_type(quest_type_id):
    url = "https://us.api.blizzard.com/data/wow/quest/type/1?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

