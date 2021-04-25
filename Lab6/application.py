# from Lab3 import *
import requests
import json
from flask import Flask, render_template
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('dish_shop.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello, World!'

@app.route('/index')
def index():
	conn = get_db_connection()
	posts = conn.execute('SELECT * FROM posts').fetchall()
	conn.close()
	return render_template('index.html', posts = posts)