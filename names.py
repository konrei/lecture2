from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    names = ["Samet", "Eren", "Ömer"]
    return render_template("names.html", names=names)
