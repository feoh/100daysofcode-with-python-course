from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

import data_models

if __name__ == "__main__":
    engine: Engine = create_engine("sqlite:///homeinventory-orm.sqlite")
    room = data_models.Room(name="Living Room", description="A non descript living room")
    data_models.ModelBase.metadata.create_all(engine)

    session_factory = sessionmaker(bind=engine)




