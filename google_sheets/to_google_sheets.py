# pip install gspread
# pip install oauth2client

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import datetime

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('db_sbc.json', scope)
client = gspread.authorize(creds)
document = client.open('march_sbc')
sheet_list = document.worksheets()
if not any(sheet.title == datetime.date.today().strftime("%d/%m/%Y") for sheet in sheet_list):
    new_sheet = document.add_worksheet(title=datetime.date.today().strftime("%d/%m/%Y"), rows='1000', cols='10')
    first_line = ["time", "user_id", "username", "orders", "payment_sum"]
    for i in range(1, len(first_line) + 1):
        new_sheet.update_cell(1, i, first_line[i - 1])
else:
    today_s_sheet = document.worksheet(datetime.date.today().strftime("%d/%m/%Y"))
    today_s_sheet.update_cell(2, 2, "data")
