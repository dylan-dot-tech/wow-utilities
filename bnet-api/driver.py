#!/usr/bin/env python3

# author: Dylan Riley
# contact: hi@dylan.tech
# copyright: https://dylan.tech
# version: 2023-02-06
# description: Seed DB with Quest Areas

import sqlite3
import quest as q
import journal as j
import mount as m
import utilities as util


def seed_db_zones():
    payload = []
    data = q.quest_areas_index()
    for area in data["areas"]:
        id = area["id"]
        world = ""
        continent = ""
        zone = area["name"]
        subzone = ""
        payload.append((id, world, continent, zone, subzone))

    # Write to DB
    conn = sqlite3.connect("../sql/wow-utilities.db")
    cur = conn.cursor()
    cur.executemany("INSERT INTO quest_areas VALUES (?, ?, ?, ?, ?)", payload)
    conn.commit()
    return


def seed_mounts():
    payload = []
    data = m.mounts_index()
    for mount in data["mounts"]:
        id = mount["id"]
        name = mount["name"]
        payload.append((id, name))

    # Write to DB
    conn = sqlite3.connect("../sql/wow-utilities.db")
    cur = conn.cursor()
    cur.executemany("INSERT INTO mounts VALUES (?, ?)", payload)
    conn.commit()
    return

