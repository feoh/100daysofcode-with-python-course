import sqlite3

with sqlite3.connect('operatingsystems.db') as connection:
    c = connection.cursor()

    all_rows = c.execute("""select * from OperatingSystems""")
    print("Operating System Database Report")
    print("--------------------------------")
    print()

    for row in all_rows:
        print(f"Name: {row[0]}")
        print(f"Platform: {row[1]}")
        print(f"Still In Wide Use?: {row[2]}")
        print()
