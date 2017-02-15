import sqlite3

def init_db():
    """Initializes the sql file to create database"""
    with sqlite3.connect('bangazon.db') as conn:
        #-----> The following line creates the database-comment out after initial tables are created
        # f = open('populateDB.sql', 'r')
        #-----> The following line populates the database - Comment in, after creating the table initially
        f = open('fixture_populateDB.sql', 'r')
        sql = f.read()
        c = conn.cursor()
        c.executescript(sql)
    c.close()

if __name__ == '__main__':
    init_db()