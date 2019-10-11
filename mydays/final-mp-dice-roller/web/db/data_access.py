from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data_models import Player, Score, HighScore, ModelBase
engine = None

def init_engine():
    global engine
    engine = create_engine("sqlite:///final-dice-roller.sqlite")
    ModelBase.metadata.create_all(engine)
    return engine


def initialize_orm():
    global engine

    if not engine:
        engine = init_engine()

    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_player(name):
    session = initialize_orm()
    player = Player(name=name)
    session.add(player)
    session.commit()
    return True


def get_all_players():
    session = initialize_orm()
    all_players_query = session.query(Player).all()

    all_players_json = [p.to_json() for p in all_players_query]
    return all_players_json


def record_score(player_id, current_score):
    session = initialize_orm()
    score = Score(player_id=player_id, score = current_score)
    session.add(score)
    session.commit()
    return True


def check_high_score(player_id, current_score):
    """Query for scores > current_score, and if there are none, this is a high score!"""
    session = initialize_orm()
    current_highscore_query = session.query(HighScore)\
        .filter(HighScore.player_id == player_id).first()

    current_highscore = current_highscore_query.high_score

    print(current_highscore)
    if current_score > current_highscore:
        return True
    else:
        return False


def record_high_score(player_id, current_score):
    session = initialize_orm()
    # First delete existing high score if any. We don't care either way
    session.query(HighScore) \
        .filter(HighScore.player_id == player_id).delete()

    highscore = HighScore(player_id=player_id, high_score=current_score)
    session.add(highscore)
    session.commit()

    # If we got here the commit was successful!
    return True


def get_all_high_scores():
    session = initialize_orm()
    all_high_scores_query = session.query(HighScore).all()

    all_high_scores_json = [hs.to_json() for hs in all_high_scores_query]

    return all_high_scores_json


def get_all_scores():
    session = initialize_orm()
    all_scores = session.query(Score)
    return all_scores
