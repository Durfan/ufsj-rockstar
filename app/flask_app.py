from flask import Flask, request, render_template
from poetic.analysis import lexer


app = Flask(__name__)


@app.route("/")
def landing():
    return render_template('index.html')