from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

ModelBase = declarative_base()

class Room(ModelBase):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    items = relationship("Item", backref="room")

    def __repr__(self):
        return f"Room Name: {self.name} Room Description: {self.description}"


class Item(ModelBase):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)
    description = Column(String)
    room_id = Column(Integer, ForeignKey('rooms.id'))

    def __repr__(self):
        return f"""
        Item Name: {self.name}
        Item Value: {self.value}
        Item Description: {self.description}
        Location: {self.room.name}"""
