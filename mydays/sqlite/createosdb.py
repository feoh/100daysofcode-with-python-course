import sqlite3

with sqlite3.connect('operatingsystems.db') as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE OperatingSystems (name TXT, platform TXT, still_used INTEGER)""")
