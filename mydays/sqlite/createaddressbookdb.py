import sqlite3

connection = sqlite3.connect('addressbook.db')

c = connection.cursor()

c.execute("""CREATE TABLE Details (name TXT, address TXT, phone_number INT)""")
connection.close()

