import shopify
from values import*
import pandas as pd
from googleSheets import*
from googleAuth import*
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

products_list = []
products = get_all_resources(shopify.Product)
for product in products:
    products_list.append(product.attributes)
products_df = pd.DataFrame(products_list)
#json_data=products_df.to_json(orient='records')

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
print("Writing to Products Google Sheet")
with open('products.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    tp = list(tuple(line) for line in reader)
print(tp)
UpdateValue(creds, spreadsheetID=GoogleSheetID, range='Products!A1', values=json_data)
os.remove("C:/Users/akio_/PycharmProjects/ShopifyAPIGSExporter/products.csv")
