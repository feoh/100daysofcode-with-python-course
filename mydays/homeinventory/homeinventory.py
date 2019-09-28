import sqlite3
from contextlib import contextmanager

table_defs = {'rooms':'room_id INTEGER PRIMARY KEY, room_name TEXT NOT NULL',
              'items':'item_id INTEGER PRIMARY KEY,'
                      'item_name TEXT NOT NULL,'
                      'item_value INTEGER NOT NULL,'
                      'item_room INTEGER NOT NULL,'
                      'FOREIGN KEY(item_room) REFERENCES rooms(room_id)'}


@contextmanager
def db_access():
    conn = sqlite3.connect('homeinventory.sqlite3')
    cursor = conn.cursor()
    yield cursor
    conn.close()


def does_table_exist(name_to_check):
    with db_access() as db:
        db.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name_to_check}';")
        result = db.fetchone()
        return bool(result)


def create_table(table_to_create):
    with db_access() as db:
        command = f"create table {table_to_create}"
        command += f"({table_defs[table_to_create]})"
        db.execute(command)


def init_db():
    db: sqlite3.Cursor
    with db_access() as db:
        for table_name in table_defs.keys():
            if not does_table_exist(table_name):
                create_table(table_name)


def scrub(dirty):
    return ''.join([c for c in dirty if c.isalnum()])


def add_room():
    raw_room_name = input("Please enter a room to add:")
    room_name = scrub(raw_room_name)
    print(f"room name: {room_name}")
    db: sqlite3.Cursor
    with db_access() as db:
        db.execute(f"INSERT INTO rooms('room_name') values('{room_name}');")
        db.connection.commit()
    return True

def find_room_by_id(room_id):
    db: sqlite3.Cursor
    with db_access() as db:
        db.execute('select room_name from rooms;')
        room_names = db.fetchall()
    return room_names[room_id][0]


def choose_room():
    db: sqlite3.Cursor
    with db_access() as db:
        db.execute('select room_name from rooms;')
        room_names = db.fetchall()
        for room_num, room_name in enumerate(room_names):
            print(f"{room_num + 1}. {room_name[0]}")

        picked_room_num = input("Please choose a room number: ")
        while True:
            try:
                picked_room = room_names[int(picked_room_num) - 1][0]
                return (picked_room_num, picked_room)
            except IndexError:
                print("Invalid choice. Please try again!")


def add_item_to_room():
    item_name = input("Please enter an item name to add:")
    print(f"Item name: {item_name}")
    item_value = input("Please enter an item's value in whole dollars:")
    print(f"Item value: {item_value}")
    item_room = input("Please enter the number of the room this item is in:")
    print(f"This item is in room: {item_room}")
    db: sqlite3.Cursor
    with db_access() as db:
        db.execute(f"INSERT INTO items('item_name', 'item_value', 'item_room') values('{item_name}','{item_value}','{item_room}');")
        db.connection.commit()
    return True


def view_inventory():
    with db_access() as db:
        db.execute("select * from 'items';")
        all_items = db.fetchall()
        for item_tuple in all_items:
            (item_id, item_name, item_value, item_room) = item_tuple
            print(f"Item Name: {item_name} Item Value: {item_value} Room: {item_room}")
    return True


def grand_total_value():
    with db_access() as db:
        db.execute('select sum(item_value) from items;')
        grand_total = db.fetchone()[0]
        print(f"Grand Total: {grand_total}")
    return True


def menu():
    menu_choices = {'Add a Room':add_room,
                    'Add Items To Room':add_item_to_room,
                    'View Inventory':view_inventory,
                    'Grand Total Value':grand_total_value}

    choice_names = list(menu_choices.keys())
    print("CrapCo Home Inventory Application")
    print("---------------------------------")
    for number, choice in enumerate(choice_names):
        print(f"{number + 1}. {choice}")

    while True:
        pick = input(f"Please type q or a number: 1-{len(choice_names)}: ")
        if pick.lower() == 'q':
            print("Bye bye!")
            exit()
        try:
            key = choice_names[int(pick) - 1]
            print(f"key: {key}")
            menu_choices[key]()
        except IndexError:
            print("Invalid choice! START AGAIN!")


if __name__ == "__main__":
    init_db()
    menu()






