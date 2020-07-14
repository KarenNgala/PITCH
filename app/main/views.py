from . import main
from flask import render_template
from flask_login import login_required

@main.route('/')
def landing_page():
    return render_template('index.html')

@main.route('/pitches')
def home():
    return render_template('pitches.html')

@main.route('/pitches/<category>')
def categories(category):
    return render_template('categories.html')

@main.route('/comments')
@login_required
def comments():
    return render_template('comments.html')