from flask import Flask, request, render_template
from poetic.analysis import lexer as poetic


app = Flask(__name__)


@app.route("/")
def landing():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def analysis_process():
    code = request.form['code']
    tokens = poetic.rock_tokens(code)
    return render_template('index.html', tokens=tokens)
