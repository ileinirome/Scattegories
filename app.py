# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
import string
import random
import pandas as pd 
from datetime import datetime
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
    df = pd.read_csv (r'list.csv')
    print(df)
    rows = df.size
    print(df.iloc[15,0])

    props = {
        "letter":random.choice(string.ascii_letters), 
        "category_1":df.iloc[random.randint(0,rows),0][3::],
        "category_2":df.iloc[random.randint(0,rows),0][3::],
        "category_3":df.iloc[random.randint(0,rows),0][3::]
    }
    return render_template("game.html", props=props, time=datetime.now())
