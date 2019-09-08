import sqlite3

with sqlite3.connect('addressbook.db') as connection:
    c = connection.cursor()

    all_rows = c.execute("""select * from Details""")
    print("Address Book Database Report")
    print("----------------------------")
    print()

    for row in all_rows:
        print(f"Name: {row[0]}")
        print(f"Address: {row[1]}")
        print(f"Phone Number:: {row[2]}")
        print()
