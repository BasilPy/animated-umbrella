# pip install gspread
# pip install oauth2client

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import datetime

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('dbsbc-db.json', scope)
client = gspread.authorize(creds)
document = client.open('march_sbc')
sheet = document.worksheet(datetime.date.today().strftime("%d/%m/%Y"))
sheet.insert_row("me", 12)

