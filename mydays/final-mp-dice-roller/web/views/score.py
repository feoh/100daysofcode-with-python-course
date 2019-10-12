import flask
import data_access


def build_views(app):
    @app.route('/roller/get_all_players')
    def get_all_players():
        return flask.jsonify(data_access.get_all_players())

    @app.route('/roller/record_score/<int:player_id>/<int:current_score>', methods=['PUT'])
    def record_score(player_id, current_score):
        return flask.jsonify(data_access.record_score(player_id=player_id, current_score=current_score))

    @app.route('/roller/record_high_score/<int:player_id>/<int:current_score>', methods=['PUT'])
    def record_high_score(player_id, current_score):
        return flask.jsonify(data_access.record_high_score(player_id=player_id, current_score=current_score))

    @app.route('/roller/check_high_score/<int:player_id>/<int:current_score>')
    def check_high_score(player_id, current_score):
        return flask.jsonify(data_access.check_high_score(player_id=player_id, current_score=current_score))

    @app.route('/roller/create_player/<string:name>', methods=['POST'])
    def create_player(name):
        return flask.jsonify(data_access.create_player(name=name))

    @app.route('/roller/find_player/<string:name>')
    def find_player(name):
        return flask.jsonify(data_access.find_player(name=name))

    @app.route('/roller/get_all_high_scores')
    def get_all_high_scores():
        all_high_scores = data_access.get_all_high_scores()
        return flask.jsonify(all_high_scores)

    @app.route('/roller/get_all_scores')
    def get_all_scores():
        all_scores = data_access.get_all_scores()
        return flask.jsonify(all_scores)

    @app.errorhandler(404)
    def not_found(_):
        return "Yo where the Justice err.. page at? Not found."
