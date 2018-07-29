from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def index():
#    return render_template("index.html")

@app.route("/")
def index():
    headline = "Hello, world! Again :("
    return render_template("index.html", headline=headline)


@app.route("/bye")
def bye():
    headline = "Goodbyeee"
    return render_template("index.html", headline=headline)
