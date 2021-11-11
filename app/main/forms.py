from wtforms import StringField,TextAreaField, SubmitField, SelectField
from wtforms.validators import Required, Email, Length
from flask_wtf import FlaskForm

from app.models import Comment

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell Us About Yourself...',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    bio = TextAreaField('About...', validators=[Required(), Length(1, 100)])
    submit = SubmitField('Submit')


class PitchForm(FlaskForm):
    pitch_title = StringField('Pitch title', validators=[Required()])
    category = SelectField('Post category',choices=[('Select a category','Select a category'),('Funny', 'Funny'),('Motivational','Motivational'),('life','life'),('Career','Career')], validators=[Required()])
    pitch = StringField('What do you have in mind?', validators=[Required()])
    submit = SubmitField('Submit')

    


class CommentForm(FlaskForm):
    body = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('Submit')