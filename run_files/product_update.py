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

#Initialize shopify API session
session = shopify.Session(shop_url, api_version, ac_tok)
shopify.ShopifyResource.activate_session(session)

#Gather product list 
products_list = []
print("Start retrieving")
products = get_all_resources(shopify.Product)
print("Finished retrieving")

#Format into a list of tuples
row = []
for product in products:
    for key,value in product.attributes.items():
        row.append(str(value))
    products_list.append(tuple(row))
    row = []


#Get credentials for Google API usage
print("Authenticating Google API...")
try:
    creds=getCred(SCOPES)
    print("Credentials Refreshed and Adquired")
except google.auth.exceptions.RefreshError:
    print("Refresh Error, deleting token.json")
    os.remove("../token.json")
    creds = getCred(SCOPES)
    print("Credentials Refreshed and Adquired")

#Write to specified Google Sheets
print("Writing to Products Google Sheet")
UpdateValue(creds, spreadsheetID=GoogleSheetID, range='Products!A2', values= products_list)

