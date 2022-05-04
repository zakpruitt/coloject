import sqlite3
import threading


class Color:
    def __init__(self):
        self.conn = sqlite3.connect(
            './data/database.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS color(
                                id TEXT PRIMARY KEY,
                                hex TEXT NOT NULL,
                                apperance INTEGER NOT NULL)
                            ''')

    def insert_color(self, color):
        try:
            self.lock.acquire(True)
            self.cursor.execute('''
                                INSERT OR IGNORE INTO color VALUES(?, ?, ?)
                                ''', color)
            self.conn.commit()
        finally:
            self.lock.release()

    def increment_apperance(self, hex):
        try:
            self.lock.acquire(True)
            self.cursor.execute('''
                                UPDATE color SET apperance = apperance + 1 WHERE hex = ?
                                ''', (hex,))
            self.conn.commit()
        finally:
            self.lock.release()

    def exists(self, hex):
        try:
            self.lock.acquire(True)
            self.cursor.execute('''
                                SELECT * FROM color WHERE hex = ?
                                ''', (hex,))
            return self.cursor.fetchone() is not None
        finally:
            self.lock.release()
