from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

ModelBase = declarative_base()


class Player(ModelBase):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f'Player Name: {self.name}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }


class HighScore(ModelBase):
    __tablename__ = "highscores"
    high_score_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'), unique=True)
    high_score = Column(Integer, nullable=False)

    def __repr__(self):
        return f"""
        Player Name: {self.player_id}
        High Score: {self.high_score}"""

    def to_json(self):
        return {
            'high_score_id': self.high_score_id,
            'player_id': self.player_id,
            'high_score': self.high_score
        }

class Score(ModelBase):
    __tablename__ = "scores"
    score_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    score = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Player Name: {self.player_id} Score: {self.score}'

    def to_json(self):
        return {
            'score_id': self.score_id,
            'player_id': self.player_id,
            'score': self.score
        }
