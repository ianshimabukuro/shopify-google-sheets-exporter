from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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