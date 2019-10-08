from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

import data_models


def initialize_orm():
    engine: Engine = create_engine("sqlite:///final-dice-roller.sqlite")
    data_models.ModelBase.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def create_player(name, session):
    player = data_models.Player(name=name)
    session.add(player)
    session.commit()

def record_score(player_id, current_score, session):
    score = data_models.Score(player_id = player_id, score = current_score)
    session.add(score)
    session.commit()


def check_highscore(player_id, current_score, session):
    """Query for scores > current_score, and if there are none, this is a high score!"""
    possible_highscore = session.query(data_models.Score).filter(data_models.Score.score > current_score)
    if possible_highscore:
        return True
    else:
        return False



def record_highscore(player_id, current_score, session):
    highscore = data_models.HighScore(player_id=player_id, high_score=current_score)
    session.add(highscore)
    session.commit(highscore)


if __name__ == "__main__":
    session = initialize_orm()
    print(session)

