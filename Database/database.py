import sqlite3
connection = sqlite3.connect('ourDatabase.db')
cur = connection.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS accounts (FirstName TEXT,LastName TEXT, Email TEXT, Password TEXT)')
connection.commit()
connection.close()
