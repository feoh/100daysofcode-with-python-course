import flask
from game_logic.roll import total_dice_rolls


def build_views(app):

    @app.route('/roller/roll_turn/<int:num_dice>')
    def roll_turn(num_dice):
        score = total_dice_rolls(num_dice=num_dice)
        return flask.jsonify(score)
