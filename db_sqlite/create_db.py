import sqlite3


# create a connection to the database
def create_db_if_not_exists():
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')

    # create a cursor object
    c = conn.cursor()

    # create a table called 'bot_users'
    c.execute('''CREATE TABLE IF NOT EXISTS bot_users
                 (time TEXT, user_id INTEGER PRIMARY KEY, username TEXT, \
                 orders TEXT, payment_sum INTEGER, lang TEXT, payment_type TEXT, num_order INTEGER)''')
    conn.commit()
    conn.close()
