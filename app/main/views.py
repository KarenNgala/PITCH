from . import main
from flask import render_template, request, redirect, url_for, abort
from ..models import User, Pitches
from flask_login import login_required, current_user
from .forms import EditProfile, PitchForm
from .. import db, photos


@main.route('/')
def landing_page():
    return render_template('index.html')


@main.route('/pitches')
def home():
    pitches=Pitches.query.all()
    return render_template('pitches.html', pitches=pitches)


@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def pitch_form():
    form = PitchForm()
    if form.validate_on_submit():
        category=form.pitch_category.data
        text = form.pitch_text.data
        new_pitch = Pitches(category=category, text=text, user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.home'))
    return render_template('new_pitch.html', pitch_form=form)


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
