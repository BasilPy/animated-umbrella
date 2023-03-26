from oauth2client.service_account import ServiceAccountCredentials
import gspread
import datetime

scope = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name('./google_sheets/dbsbc-db.json', scope)
client = gspread.authorize(creds)
document = client.open('march_sbc')
sheet_list = document.worksheets()


def check_existence(name_sheet: str):
    if any(sheet.title == name_sheet for sheet in sheet_list):
        return 1
    else:
        return 0


def create_or_open(name_date: str):
    if not check_existence(name_date):
        new_sheet = document.add_worksheet(title=name_date, rows='1000', cols='12')
        first_line = ["time", "user_id", "username",
                      "order", "payment_sum", "language", "payment_type", "order_number"]
        return new_sheet
    else:
        return document.worksheet(name_date)


def add_users_string(data_user: list):
    sheet_adding = create_or_open(datetime.date.today().strftime("%d/%m/%Y"))
    row_data = [data_user]
    sheet_adding.append_rows(row_data)


