import sqlite3


class SQLWorker:
    current_orger: int = None

    def __init__(self, current_orger: int = 0):
        self.current_orger = current_orger

    def id_exists(self, id_: str):
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

    def add_new_bot_client(self, time: str, id_: str, name: str):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        default = "ru"
        if self.id_exists(id_) == 0:
            # time TEXT, user_id INTEGER PRIMARY KEY, username TEXT, \
            #    orders TEXT, payment_sum INTEGER, lang TEXT, payment_type TEXT)
            #  time, user_id, username, orders, payment_sum, language, payment_type
            c.execute(f"INSERT INTO bot_users VALUES ('{time}',{id_}, '{name}', '', '', '{default}', '', {-1})")
        else:
            c.execute(f'UPDATE bot_users SET time = ?, orders = ?, payment_sum = ?\
                  WHERE user_id = {id_}', (time, "", 0))
        conn.commit()
        conn.close()

    def update_lang(self, id_: str, language: str):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        c.execute('UPDATE bot_users SET lang = ? WHERE user_id = ?', (language, id_))
        conn.commit()
        conn.close()

    def get_user_lang(self, id_: str):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        c.execute('SELECT lang FROM bot_users WHERE user_id = ?', (id_,))
        str_lang = str(*c.fetchone()[::])
        # print("str::", str_lang)
        conn.commit()
        conn.close()
        return str_lang

    def update_order_and_payment(self, id_: str, order: str, cost: int):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        c.execute(f'UPDATE bot_users SET orders = orders || ?, payment_sum = payment_sum + ? \
                  WHERE user_id = {id_}',
                  (" \n" + order, cost))
        conn.commit()
        conn.close()

    def get_order_and_total_cost(self, id_: str):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        c.execute('SELECT orders, payment_sum FROM bot_users WHERE user_id = ?', (id_,))
        values = c.fetchone()
        print()
        data = [str(values[0]), str(values[1])]
        conn.commit()
        conn.close()
        return data

    def clear_by_id(self, id_: str):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        print("d")
        c.execute('UPDATE bot_users SET orders = ?, payment_sum = ? WHERE user_id = ?', (" ", 0, id_))
        print("a")
        conn.commit()
        conn.close()

    def get_one_raw(self, id_: str):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM bot_users WHERE user_id = ?', (id_,))
        row = cur.fetchone()
        return row

    def update_time(self, id_: str, time: str):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        c.execute(f'UPDATE bot_users SET time = ? \
                  WHERE user_id = ?', (time, id_))
        conn.commit()
        conn.close()

    def update_payment_type_and_num_order(self, time_: str, id_: str, payment_type_: str, num: int):
        conn = sqlite3.connect('./db_sqlite/clients_stand_by.db')
        c = conn.cursor()
        #printint
        c.execute(f'UPDATE bot_users SET time = ?, payment_type = ?, num_order = ?\
                  WHERE user_id = ?', (time_, payment_type_, str(num), id_))
        conn.commit()
        conn.close()
