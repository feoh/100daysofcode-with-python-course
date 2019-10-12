import flask
from views import score
from views import gameplay

app = flask.Flask(__name__)


def build_views():
    score.build_views(app)
    gameplay.build_views(app)


def main():
    build_views()
    app.run(debug=True)


if __name__ == '__main__':
    main()
