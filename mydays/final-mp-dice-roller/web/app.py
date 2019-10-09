import flask
import data_access

app = flask.Flask(__name__)

def main():
    app.run(debug=True)


@app.route('/roller/high_scores')
def high_scores():
    return flask.jsonify(data_access.get_all_high_scores())


@app.errorhandler(404)
def not_found(_):
    return "Yo where the Justice err.. page at? Not found."


if __name__ == '__main__':
    main()
