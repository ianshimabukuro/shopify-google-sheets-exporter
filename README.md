# Export Orders and Products from Shopify to a Google Sheet
This program was designed to utilize the Shopify API and Google Sheets API in order to automatically export 
all orders and products to a specific google sheet

## Usage
### Installation
1. Install the necessary dependencies on the requirements.txt

### Files
Credential.json: This is the file you get from Google Cloud after you created your application on the platform.It contains the authentication info necessary
for utilizing the Google API with defined scopes.
  
token.json: This is a credential file used to connected to the Google API. It is created automatically, so no need to do anything with it.

chromedriver: This is the driver used by selenium to automate Google Chrome browser. Always download the most recent version and the one compatible
with your computer and browser. Has to be kept inside the project folder

### Info
Use the account associated with the Google Cloud account that the credentials.json was downloaded from when authenticating api
Always set download and project paths adequately, with "/" not "\"

### Steps
Step 1: Initialize Shopify API Session
Step 2: Obtain data from the session and store into a list
Step 3: Authentication of Google API Credentials
Step 4: Write to specific google sheet 




