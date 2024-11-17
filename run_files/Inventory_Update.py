"""Has not been changed from the csv/dataframfe style to the better way seen in product and order
    in other words not guaranteed to work"""


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
session = shopify.Session(shop_url, api_version, ac_tok)
shopify.ShopifyResource.activate_session(session)


Locations = shopify.Location.find()
inventory_list = []
for location in Locations:
    print("current location",location)
    Inventory_Levels = shopify.Location.inventory_levels(location)
    for inventory_level in Inventory_Levels:
        id = inventory_level.attributes["inventory_item_id"]
        inventory_item = shopify.InventoryItem.find(id)
        time.sleep(0.2)
        inventory_list.append(inventory_item.attributes)
    while Inventory_Levels.has_next_page():
        Inventory_Levels = Inventory_Levels.next_page()
        print("next page")
        for inventory_level in Inventory_Levels:
            id = inventory_level.attributes["inventory_item_id"]
            inventory_item = shopify.InventoryItem.find(id)
            time.sleep(0.2)
            inventory_list.append(inventory_item.attributes)

inventory_df = pd.DataFrame(inventory_list)
inventory_df.to_csv('inventory.csv', index=False)

print("Authenticating Google API...")
try:
    creds=getCred(SCOPES)
    print("Credentials Refreshed and Adquired")
except google.auth.exceptions.RefreshError:
    print("Refresh Error, deleting token.json")
    os.remove("../token.json")
    creds = getCred(SCOPES)
    print("Credentials Refreshed and Adquired")
#Step 3
print("Writing to Inventory Google Sheet")
with open('inventory.csv',encoding="utf8") as f:
    reader = csv.reader(f)
    ti = list(tuple(line) for line in reader)

UpdateValue(creds, spreadsheetID=GoogleSheetID, range='Inventory!A1', values=ti)

os.remove(project_path + "/run_files/inventory.csv")

