# Export Orders and Products from Shopify to a Google Sheet
This program was designed to utilize the Shopify API and Google Sheets API in order to automatically export 
all orders and products to a specific google sheet

## Usage
### Installation
Install the necessary dependencies on the requirements.txt

### Files
Credential.json: This is the file you get from Google Cloud after you created your application on the platform.It contains the authentication info necessary
for utilizing the Google API with defined scopes.
  
token.json: This is a credential file used to connected to the Google API. It is created automatically, so no need to do anything with it.

### Info
Use the account associated with the Google Cloud account that the credentials.json was downloaded from when authenticating api
Always set download and project paths adequately, with "/" not "\"

### Steps in each individual run file
1. Initialize Shopify API Session
2. Obtain data from the session and store into a list
3. Authentication of Google API Credentials
4. Write to specific google sheet
   
### ids, secrets, codes
You can get the access code in the passwords_ids file through the oauth_routine. The rest has to be managed in their own respective api platforms.




