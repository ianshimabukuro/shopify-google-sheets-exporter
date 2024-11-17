import shopify
import pandas as pd
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os.path
import csv
import google.auth.exceptions
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

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
def getCred(SCOPES):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds
def UpdateValue(creds,spreadsheetID,range,values):
    try:
        # initiate service with autenticator
        service = build("sheets", "v4", credentials=creds)
         # Call the Sheets API
        sheet = service.spreadsheets()
        value_range_body = {
            'majorDimension': 'ROWS',
            'values': values
        }
        # Update Values
        sheet.values().update(spreadsheetId=spreadsheetID, range=range, valueInputOption='USER_ENTERED',
                          body=value_range_body).execute()
        print("Update Succesful")
    except HttpError as err:
        print(err)

#All passwords and values
#Shopify
client_id = ''
client_secret =  ''
redirect_uri = ''
shop_url = ''
api_version =''
ac_tok=""


SCOPES=""
GoogleSheetID=''
#using forward slash
project_path = 'r'


#Initialize shopify API session
session = shopify.Session(shop_url, api_version, ac_tok)
shopify.ShopifyResource.activate_session(session)

#Gather product list
products_list = []
print("Start retrieving")
products = get_all_resources(shopify.Product)
print("Finished retrieving")
row = []
for product in products:
    for key,value in product.attributes.items():
        print(type(value))
        row.append(str(value))
    products_list.append(tuple(row))
    print(row)
    row = []

#Get credentials for Google API usage
print("Authenticating Google API...")
try:
    creds=getCred(SCOPES)
    print("Credentials Refreshed and Adquired")
except google.auth.exceptions.RefreshError:
    print("Refresh Error, deleting token.json")
    os.remove("token.json")
    creds = getCred(SCOPES)
    print("Credentials Refreshed and Adquired")

#Write to specified Google Sheets
print("Writing to Products Google Sheet")
UpdateValue(creds, spreadsheetID=GoogleSheetID, range='Products!A2', values= products_list)


