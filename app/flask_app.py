from flask import Flask, request, render_template
from poetic.analysis import lexer as poetic
from poetic.analysis import syntax as hairmetal


app = Flask(__name__)


@app.route("/")
def landing():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def analysis_process():
    code = request.form['code']
    code = code.replace('\r', '')
    syntax = hairmetal.syntactic_ballad(code)
    tokens = poetic.rock_tokens(code)
    return render_template('index.html', tokens=tokens, syntax=syntax)
