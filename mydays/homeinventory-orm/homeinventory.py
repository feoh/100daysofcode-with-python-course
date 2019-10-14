from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

import data_models


def initialize_orm():
    engine: Engine = create_engine("sqlite:///homeinventory-orm.sqlite")
    data_models.ModelBase.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def add_room(session):
    name = input("Please enter a room to add:")
    print(f"Room name: {name}")
    description = input("Please enter what the room looks like:")
    print(f"Room description: {description}")
    room = data_models.Room(name=name, description=description)
    session.add(room)
    session.commit()


def add_item(session):
    name = input("Please enter the name of an item to add:")
    print(f"Item name: {name}")
    description = input("Please enter what the item looks like:")
    print(f"Item Description: {description}")
    value = input(f"How much is the item worth in whole dollars?")
    print(f"Item Value: {value}")
    print("Please choose which room the item is in:")
    room_id = choose_room(session)
    item = data_models.Item(name=name, value=value, description=description, room_id=room_id)
    session.add(item)
    session.commit()


def choose_room(session):
    rooms: data_models.Room = session.query(data_models.Room)

    room_names = get_room_names(rooms)
    for room_num, room_name in enumerate(room_names):
        print(f"{room_num + 1}. {room_name}")

    picked_room_num = input("Please choose a room number: ")
    while True:
        try:
            picked_room = room_names[int(picked_room_num) - 1][0]
            return picked_room_num
        except IndexError:
            print("Invalid choice. Please try again!")


def get_room_names(rooms):
    room_names = [room.name for room in rooms]
    return room_names


def view_inventory(session):
    items = session.query(data_models.Item)
    for item in items:
        print(item)

    return True


def grand_total(session):
    items = session.query(data_models.Item)
    total = sum(item.value for item in items)
    print(f"Grand Total Value: {total}")


def menu(session):

    menu_choices = {'Add a Room':add_room,
                    'Add Items To Room':add_item,
                    'View Inventory':view_inventory,
                    'Grand Total Value':grand_total}

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
            menu_choices[key](session)
        except IndexError:
            print("Invalid choice! START AGAIN!")


if __name__ == "__main__":
    session = initialize_orm()
    menu(session)

