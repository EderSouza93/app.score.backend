from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')