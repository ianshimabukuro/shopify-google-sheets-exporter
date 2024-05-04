import shopify
from ids_passwords_strings.values import*
import pandas as pd
from google_modules.googleSheets import*
from google_modules.googleAuth import*
import os.path
import csv
import google.auth.exceptions


def get_all_resources(resource_type, **kwargs):
    resource_count = resource_type.count(**kwargs)
    resources = []
    if resource_count > 0:
        page=resource_type.find(**kwargs)
        resources.extend(page)
        while page.has_next_page():
            page = page.next_page()
            resources.extend(page)
    return resources

session = shopify.Session(shop_url, api_version, ac_tok)
shopify.ShopifyResource.activate_session(session)

inventory_list = []
inventory = get_all_resources(shopify.InventoryItem)
for inventory_item in inventory:
    inventory_list.append(inventory_item.attributes)
inventory_df = pd.DataFrame(inventory_list)
inventory_df.to_csv('inventory.csv', index=False)

print("Authenticating Google API...")
try:
    creds=getCred(SCOPES)
    print("Credentials Refreshed and Adquired")
except google.auth.exceptions.RefreshError:
    print("Refresh Error, deleting token.json")
    os.remove("token.json")
    creds = getCred(SCOPES)
    print("Credentials Refreshed and Adquired")
#Step 3
print("Writing to Inventory Google Sheet")
with open('inventory.csv',encoding="utf8") as f:
    reader = csv.reader(f)
    ti = list(tuple(line) for line in reader)

UpdateValue(creds, spreadsheetID=GoogleSheetID, range='Inventory!A1', values=ti)
os.remove("C:/Users/akio_/PycharmProjects/ShopifyAPIGSExporter/venv/inventory.csv")
