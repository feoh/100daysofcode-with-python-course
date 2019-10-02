from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()

class Room(ModelBase):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
