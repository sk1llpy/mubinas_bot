import sqlite3 as sq

def connect():
    return sq.connect('mubina.db')

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        user_id BIGINT
    )""")

    conn.commit()
    conn.close()

def add_user(user_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(f"""INSERT INTO users VALUES ({user_id})""")

    conn.commit()
    conn.close()

def get_user(user_id):
    conn = connect()
    cur = conn.cursor()

    data = cur.execute(f"""SELECT * FROM users WHERE user_id = {user_id}""").fetchall()

    conn.commit()
    conn.close()

    return data
