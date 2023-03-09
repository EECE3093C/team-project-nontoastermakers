import sqlite3

connection = sqlite3.connectionect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO users (username, password, firstname, lastname, email) VALUES (?,?,?,?,?)",
            ('User1', 'password', 'firstame', 'lastname', 'email')
            )

connection.commit()
connection.close()
