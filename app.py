# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
import string
import random
import pandas as pd 
from datetime import datetime
import model
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())

@app.route('/game')
def game():
    props = {
        "letter":random.choice(string.ascii_letters), 
        "categories": model.get_list()
    }
    return render_template("game.html", props=props, time=datetime.now())
