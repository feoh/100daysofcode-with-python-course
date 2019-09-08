from flask import Flask, render_template
from data import running_windows_processes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", running_windows_processes=running_windows_processes)


if __name__ == "__main__":
    app.run()
