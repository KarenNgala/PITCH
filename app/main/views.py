from . import main
from flask import render_template, request, redirect, url_for, abort
from ..models import User, Pitches, Comments
from flask_login import login_required, current_user
from .forms import EditProfile, PitchForm, CommentForm
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


@main.route('/pitches/<pitch_category>')
def categories(pitch_category):
    pitch = Pitches.get_category(pitch_category)
    return render_template('categories.html', pitch=pitch)


@main.route('/comments/<int:pitch_id>', methods=['GET','POST'])
@login_required
def pitch_comments(pitch_id):
    comments = Comments.get_comments(pitch_id)
    pitch = Pitches.query.get(pitch_id)

    form = CommentForm()
    if form.validate_on_submit():
        comment = form.pitch_comment.data
        new_comment = Comments(comment=comment, pitch_id=pitch_id, user_id=current_user.get_id())
        new_comment.save_comment()
        return redirect(url_for('main.pitch_comments',pitch_id = pitch_id))
    return render_template('comments.html', comment_form=form, comments=comments, pitch = pitch)


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
