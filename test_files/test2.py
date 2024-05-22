import shopify
import time
from ids_passwords_strings.values import*
import pandas as pd
from google_modules.googleSheets import*
from google_modules.googleAuth import*
from shopify_modules.utility import *
import os.path
import csv
import google.auth.exceptions
locations_ids=[43039096968, 60906668168, 60919185544, 45357269128,65552973960]
inventoryItemId=34766209908872
session = shopify.Session(shop_url, api_version, ac_tok)
shopify.ShopifyResource.activate_session(session)


Locations = shopify.Location.find()
inventory_list = []
for location in Locations:
    Inventory_Levels = shopify.Location.inventory_levels(location)
    for inventory_level in Inventory_Levels:
        id = inventory_level.attributes["inventory_item_id"]
        inventory_item = shopify.InventoryItem.find(id)
        time.sleep(0.2)
        inventory_list.append(inventory_item.attributes)
    while Inventory_Levels.has_next_page():
        Inventory_Levels = Inventory_Levels.next_page()
        for inventory_level in Inventory_Levels:
            id = inventory_level.attributes["inventory_item_id"]
            inventory_item = shopify.InventoryItem.find(id)
            time.sleep(0.2)
            inventory_list.append(inventory_item.attributes)

