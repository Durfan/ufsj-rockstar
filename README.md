# ROCKSTAR Poetic Analysis

Web App/Analisador sintatico para ROCKSTAR. Reconhece (ou não) a estrutura da linguagem por meio do parser PLY (Python Lex-Yacc).

## Install (w/ Virtual Environment)

```sh
git clone https://github.com/Durfan/ufsj-rockstar.git
cd ufsj-rockstar
python3 -m venv .venv
source .venv/bin/activate
pip install Flask
```

### Serving Flask app (development)

```sh
export FLASK_APP=app/flask_app
export FLASK_ENV=development
flask run
```
Open: http://127.0.0.1:5000