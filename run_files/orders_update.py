import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print(sys.path)

import shopify
from ids_passwords_strings.values import*
import pandas as pd
from google_modules.googleSheets import*
from google_modules.googleAuth import*
from shopify_modules.utility import *
import os.path
import csv
import google.auth.exceptions



session = shopify.Session(shop_url, api_version, ac_tok)
shopify.ShopifyResource.activate_session(session)

orders_list = []
print("Start retrieving")
orders = get_all_resources(shopify.Order, status = 'any')
print("Finished retrieving")

row = []
for order in orders:
    for key,value in order.attributes.items():
        row.append(str(value))
    orders_list.append(tuple(row))
    row = []

print("Authenticating Google API...")
try:
    creds=getCred(SCOPES)
    print("Credentials Refreshed and Adquired")
except google.auth.exceptions.RefreshError:
    print("Refresh Error, deleting token.json")
    os.remove("../token.json")
    creds = getCred(SCOPES)
    print("Credentials Refreshed and Adquired")

print("Writing to Orders Google Sheet")
UpdateValue(creds, spreadsheetID=GoogleSheetID, range='Orders!A2', values=orders_list)
