from oauth2client.service_account import ServiceAccountCredentials
import gspread
import datetime

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('db_sbc.json', scope)
client = gspread.authorize(creds)
document = client.open('march_sbc')
sheet_list = document.worksheets()


def check_existence(name_sheet: str):
    if any(sheet.title == datetime.date.today().strftime("%d/%m/%Y") for sheet in sheet_list):
        return 1
    else:
        return 0


def create_new_sheet(name_date: str):
    if check_existence(name_date):
        new_sheet = document.add_worksheet(title=datetime.date.today().strftime("%d/%m/%Y"), rows='1000', cols='10')
        first_line = ["time", "user_id", "username", "orders", "payment_sum", "language"]
        for i in range(1, len(first_line) + 1):
            new_sheet.update_cell(1, i, first_line[i - 1])


def add_users_string(data_user: list):
    sheet_adding = client.open("march_sbc",).worksheet(datetime.date.today().strftime("%d/%m/%Y"))
    for i in range(1, len(data_user) + 1):
        sheet_adding.update_cell(1, i, sheet_adding[i - 1])