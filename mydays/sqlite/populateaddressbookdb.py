#!/usr/bin/env python3

import sqlite3

done = ""
with sqlite3.connect('addressbook.db') as connection:
    c = connection.cursor()

    while done is not "q":
        fields = []
        name = input("Name: ")
        fields.append(name)
        address = input("Address: ")
        fields.append(address)
        phonenumber = input("Phone Number: ")
        fields.append(phonenumber)
        c.execute("""INSERT INTO Details VALUES (?,?,?)""", fields)
        done = input("Enter q to quit adding rows. Anything else to continue")

