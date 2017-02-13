import sqlite3

def init_db():
    """Initializes the sql file to create database"""
    with sqlite3.connect('bangazon.db') as conn:
        f = open('populateDB.sql', 'r')
        sql = f.read()
        c = conn.cursor()
        c.executescript(sql)
    c.close()

if __name__ == '__main__':
    init_db()