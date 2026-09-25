import sqlite3

DATABASE = "wallet.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            private_key TEXT NOT NULL,
            public_key TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_id INTEGER NOT NULL,
            receiver_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            sender_old_balance REAL NOT NULL,
            sender_new_balance REAL NOT NULL,
            receiver_old_balance REAL NOT NULL,
            receiver_new_balance REAL NOT NULL,
            timestamp TEXT NOT NULL,
            transaction_hash TEXT NOT NULL,
            signature TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
