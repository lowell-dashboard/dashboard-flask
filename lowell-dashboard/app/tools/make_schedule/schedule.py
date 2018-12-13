from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import json
import os

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1rIpxKuWzxgg-TOT0xrsjL6L4X4cSw9Wo1PoKIs1afkM'
SAMPLE_RANGE_NAME = 'A3:G68'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    path = os.path.dirname(os.path.abspath(__file__))
    store = file.Storage(f'{path}/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(f'{path}/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('sheets', 'v4', http=creds.authorize(Http()))

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Name, Major:')
        MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        MONTHS = [month.upper() for month in MONTHS]
        schedule = {}
        current_month = ""
        for row in values:
            g_row = row[6]
            if g_row in MONTHS:
                schedule[g_row] = list()
                current_month = g_row
                continue
            schedule[current_month].append(g_row)
            # Print columns A and E, which correspond to indices 0 and 4.
            # print('%s' % (g_row,))
        print(schedule)
        with open('../result.json', 'w') as f:
            json.dump(schedule, f, indent=4, sort_keys=True)

# if __name__ == '__main__':
#     main()