#!/usr/bin/env python3

import sqlite3

is_still_used = 1
is_not_still_used = 0
done = ""
with sqlite3.connect('operatingsystems.db') as connection:
    c = connection.cursor()

    while done is not "q":
        fields = []
        name = input("Name: ")
        fields.append(name)
        platform = input("Platform: ")
        fields.append(platform)
        stillused = input("Still In Wide Use? (Y/N)")

        if stillused == "y":
            fields.append(is_still_used)
        else:
            fields.append(is_not_still_used)

        c.execute("""INSERT INTO OperatingSystems VALUES (?,?,?)""", fields)
        done = input("Enter q to quit adding rows. Anything else to continue")

