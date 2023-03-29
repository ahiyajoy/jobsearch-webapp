import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp

# Configure application
app = Flask(__name__)


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///jobs.db")


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/jobs")
def jobs():

    q = request.args.get("q")
    if q:
        jobs = db.execute("SELECT JOB_TITLE, PREVAILING_WAGE, WORKSITE_STATE FROM jobs WHERE JOB_TITLE LIKE ? LIMIT 100", "%" + q + "%")
    else:
        jobs = []
    return jobs

@app.route("/search")
def search():

    return render_template("searched.html")







