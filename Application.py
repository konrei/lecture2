from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "MAKE IT RAINGURL, MAKE IT RAIN!"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>Oh yeah hey {name} hey wassup?</h1>"
