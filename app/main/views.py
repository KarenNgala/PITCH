from . import main
from flask import render_template, request, redirect, url_for, abort
from ..models import User
from flask_login import login_required
from .forms import EditProfile
from .. import db, photos


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


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user=user)


@main.route('/user/<name>/edit', methods=['GET','POST'])
@login_required
def edit_profile(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)

    form=EditProfile()
    if form.validate_on_submit():
        user.about=form.about.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', name=user.username))
    return render_template('profile/edit_profile.html', form=form)


@main.route('/user/<name>/edit/pic', methods=['POST'])
@login_required
def update_pic(name):
    user=User.query.filter_by(username=name).first()
    if 'photo' in request.files:
        filename=photos.save(request.files['photo'])
        path=f'photos/{filename}'
        user.avatar=path
        db.session.commit()
    return redirect(url_for('main.profile', name=name))