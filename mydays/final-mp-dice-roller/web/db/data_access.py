from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

import data_models

engine = None

def init_engine():
    engine: Engine = create_engine("sqlite:///final-dice-roller.sqlite")
    data_models.ModelBase.metadata.create_all(engine)
    return Engine


def initialize_orm():
    global engine

    if not engine:
        engine = init_engine()

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_player(name):
    session = initialize_orm()
    player = data_models.Player(name=name)
    session.add(player)
    session.commit()


def record_score(player_id, current_score):
    session = initialize_orm()
    score = data_models.Score(player_id = player_id, score = current_score)
    session.add(score)
    session.commit()


def check_high_score(player_id, current_score):
    """Query for scores > current_score, and if there are none, this is a high score!"""
    session = initialize_orm()
    possible_highscore = session.query(data_models.Score).filter(data_models.Score.score > current_score)
    if possible_highscore:
        return True
    else:
        return False


def record_high_score(player_id, current_score):
    session = initialize_orm()
    highscore = data_models.HighScore(player_id=player_id, high_score=current_score)
    session.add(highscore)
    session.commit(highscore)


def get_all_high_scores():
    session = initialize_orm()
    all_high_scores = session.query(data_models.HighScore)
    return all_high_scores


def get_all_scores(player_id):
    session = initialize_orm()
    all_scores = session.query(data_models.Score)
    return all_scores

