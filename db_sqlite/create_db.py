import sqlite3

# create a connection to the database
conn = sqlite3.connect('./clients_stand_by.db')

# create a cursor object
c = conn.cursor()

# create a table called 'bot_users'
c.execute('''CREATE TABLE bot_users
             (time TEXT, user_id INTEGER PRIMARY KEY, username TEXT, orders TEXT, payment_sum INTEGER, lang TEXT)''')
conn.commit()
conn.close()
