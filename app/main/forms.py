from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField ,SubmitField
from wtforms.validators import Required


# CATEGORY_CHOICES=['Elevator Pitches', 'Pickup lines', 'Funny']

class EditProfile(FlaskForm):
    about = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Update')


class PitchForm(FlaskForm):
    # pitch_category = SelectField('Choose a category', choices=[CATEGORY_CHOICES], validators=[Required()])
    pitch_category = TextAreaField('Category can only be Elevator Pitches, Pickup lines and Funny', validators=[Required()])
    pitch_text = TextAreaField('Your pitch here', validators=[Required()]) 
    submit = SubmitField('Post')


class CommentForm(FlaskForm):
    # pitch_category = SelectField('Choose a category', choices=[CATEGORY_CHOICES], validators=[Required()])
    pitch_comment = TextAreaField('Make a comment', validators=[Required()])
    submit = SubmitField('Comment')