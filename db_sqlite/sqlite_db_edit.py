import sqlite3


def id_exists(id_: str):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    c = conn.cursor()
    c.execute('SELECT EXISTS(SELECT 1 FROM bot_users WHERE user_id = ? LIMIT 1)', (id_,))
    result = c.fetchone()[0]
    conn.commit()
    conn.close()
    if result == 1:
        print('ID', id_, 'exists')
        return 1
    else:
        print('ID', id_, 'does not exist')
        return 0


def add_new_bot_client(time: str, id_: str, name: str):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    c = conn.cursor()
    default = "ru"
    if id_exists(id_) == 0:
        # time, user_id, username, orders, payment_sum, language
        c.execute(f"INSERT INTO bot_users VALUES ('{time}',{id_}, '{name}', '', '', '{default}')")
    else:
        c.execute(f'UPDATE bot_users SET orders = ?, payment_sum = ?\
              WHERE user_id = {id_}', ("", 0))
    conn.commit()
    conn.close()


def update_lang(id_: str, language: str):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    c = conn.cursor()
    c.execute('UPDATE bot_users SET lang = ? WHERE user_id = ?', (language, id_))
    conn.commit()
    conn.close()


def get_user_lang(id_: str):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    c = conn.cursor()
    c.execute('SELECT lang FROM bot_users WHERE user_id = ?', (id_,))
    str_lang = str(*c.fetchone()[::])
    print("str::", str_lang)
    conn.commit()
    conn.close()
    return str_lang


def update_order_and_payment(id_: str, order: str, cost: int):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    c = conn.cursor()
    c.execute(f'UPDATE bot_users SET orders = orders || ?, payment_sum = payment_sum + ? \
              WHERE user_id = {id_}',
              (" \n" + order, cost))
    conn.commit()
    conn.close()


def get_order_and_total_cost(id_: str):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    c = conn.cursor()
    c.execute('SELECT orders, payment_sum FROM bot_users WHERE user_id = ?', (id_,))
    values = c.fetchone()
    print()
    data = [str(values[0]), str(values[1])]
    conn.commit()
    conn.close()
    return data


def clear_by_id(id_: str, time: str):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    c = conn.cursor()
    print("d")
    c.execute('UPDATE bot_users SET time = ?, orders = ?, payment_sum = ? WHERE user_id = ?', (time, " ", 0, id_))
    print("a")
    conn.commit()
    conn.close()


def get_one_raw(id_: str):
    conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM bot_users WHERE user_id = ?', (id_,))
    row = cur.fetchone()
    return row
