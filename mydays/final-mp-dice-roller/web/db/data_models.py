from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()


class Player(ModelBase):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Player Name: {self.name}'


class HighScore(ModelBase):
    __tablename__ = "highscores"
    high_score_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), unique=True)
    high_score = Column(Integer, nullable=False)

    def __repr__(self):
        return f"""
        Player Name: {self.player_id}
        High Score: {self.high_score}"""


class Score(ModelBase):
    __tablename__ = "scores"
    score_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    score = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Player Name: {self.player_id} Score: {self.score}'
