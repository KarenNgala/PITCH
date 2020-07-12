from app import app
from flask import render_template

@app.route('/')
def landing_page():
    return render_template('index.html')

@app.route('/pitches')
def home():
    return render_template('pitches.html')

@app.route('/pitches/<category>')
def categories(category):
    return render_template('categories.html')