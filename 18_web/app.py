import json
from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
@app.post("/")
def index():
    return render_template("index.html", name="Karla")


@app.route("/pessoas/<is_active>/")
def pessoas(is_active):
    pessoas = get_pessoas(is_active=is_active.lower() == "active")
    return render_template("pessoas.html", pessoas=pessoas)


def get_pessoas(is_active=None):
    with open("data.json") as datafile:
        data = json.loads(datafile.read())

    if is_active is not None:
        return [pessoa for pessoa in data if pessoa["is_active"] == is_active]
    return data
