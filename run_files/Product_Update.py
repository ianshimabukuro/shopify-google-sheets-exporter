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

#Gather product list and make a csv file
products_list = []
print("Start retrieving")
products = get_all_resources(shopify.Product)
print("Finished retrieving")
for product in products:
    products_list.append(product.attributes)
products_df = pd.DataFrame(products_list)
products_df.to_csv('products.csv', index=False)

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
with open('products.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    tp = list(tuple(line) for line in reader)
UpdateValue(creds, spreadsheetID=GoogleSheetID, range='Products!A1', values=tp)

#Delete created csv file
os.remove("C:/Users/akio_/PycharmProjects/ShopifyAPIGSExporter/products.csv")
