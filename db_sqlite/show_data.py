import sqlite3 as lite

conn = lite.connect('./clients_stand_by.db')
cur = conn.cursor()


def get_posts():
    cur.execute("SELECT * FROM bot_users ")
    print(cur.fetchall())


get_posts()

def get_one_raw(id_: str):
    cur.execute('SELECT * FROM bot_users WHERE user_id = ?', (id_,))
    row = cur.fetchone()
    print(row)

# get_one_raw("244623926")
