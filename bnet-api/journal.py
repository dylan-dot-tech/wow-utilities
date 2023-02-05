#!/usr/bin/env python3

# author: Dylan Riley
# contact: hi@dylan.tech
# copyright: https://dylan.tech
# version: 2023-02-03
# description: Battle.net Journal API Endpoints

import json
import requests
import utilities as util


# Lists all game expansion names, id's, and respective API endpoints
def journal_expansions_index():
    url = "https://us.api.blizzard.com/data/wow/journal-expansion/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists all dungeon & raid names, id's, and respective API endpoints for a given journal_expansion_id
def journal_expansion(journal_expansion_id):
    url = "https://us.api.blizzard.com/data/wow/journal-expansion/{}?namespace=static-us&locale=en_US&access_token={}".format(journal_expansion_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists all encounter names, id's, and respective API endpoints
def journal_encounters_index():
    url = "https://us.api.blizzard.com/data/wow/journal-encounter/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

# Lists name, description, creature, item, section, instance, category, and mode metadata & respective API endpoints for a given journal_encounter_id
def journal_encounter(journal_encounter_id):
    url = "https://us.api.blizzard.com/data/wow/journal-encounter/{}?namespace=static-us&locale=en_US&access_token={}".format(journal_encounter_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

def journal_encounter_search(instance_name):
    # Example instance_name: Deadmines
    url = "https://us.api.blizzard.com/data/wow/search/journal-encounter?namespace=static-us&instance.name.en_US={}&orderby=id&_page=1&access_token={}".format(instance_name, util.get_access_token())
    response = requests.get(url)
    return response.json()

def journal_instances_index():
    url = "https://us.api.blizzard.com/data/wow/journal-instance/index?namespace=static-us&locale=en_US&access_token={}".format(util.get_access_token())
    response = requests.get(url)
    return response.json()

def journal_instance(journal_instance_id):
    url = "https://us.api.blizzard.com/data/wow/journal-instance/{}?namespace=static-us&locale=en_US&access_token={}".format(journal_instance_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

def journal_instance_media(journal_instance_id):
    url = "https://us.api.blizzard.com/data/wow/media/journal-instance/{}?namespace=static-us&locale=en_US&access_token={}".format(journal_instance_id, util.get_access_token())
    response = requests.get(url)
    return response.json()

