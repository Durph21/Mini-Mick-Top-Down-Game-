from flask import Flask, render_template, request, make_response, redirect, url_for, session, g
from database import get_db, close_db
from functools import wraps
from flask_session import Session

app = Flask(__name__)
# app.teardown_appcontext(close_db)
# app.config["SECRET_KEY"] = "new-secret-key"
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/game")
def game():
    return render_template("game.html")

# @app.route("/store_score", methods = ["POST"])
# def store_score():
#     score = int(request.form(["score"])) 
#     db = get_db()
#     db.execute("""INSERT INTO leader_board (score)
#                             VALUES ? ;""", (score,))
#     return "success"

# @app.route("/leader_board")
# def leader_board():
#     db = get_db()
#     db.execute("""SELECT * FROM leader_board""")
#     return render_template("leader_board.html")
