from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from ..models import Comment, User,Pitch
from flask_login import login_required, current_user
from .. import db,photos
from .forms import UpdateProfile, PitchForm, CommentForm

# @main.route('/')
# def index():
#     '''
#     View root page function that returns the index page and its data.
#     '''
#     pitch_form = PitchForm()
#     all_pitches = Pitch.query.order_by(Pitch.date_posted).all()
#     return render_template('index.html', pitches = all_pitches)

@main.route('/')
def index():
    pitch_form = PitchForm()
    pitches = Pitch.query.all()
    Funny = Pitch.query.filter_by(category = 'Funny').all() 
    Business = Pitch.query.filter_by(category = 'Business').all()
    Motivational = Pitch.query.filter_by(category = 'Motivational').all()
    religious = Pitch.query.filter_by(category = 'Religious').all()
    life = Pitch.query.filter_by(category = 'life').all()
    Career = Pitch.query.filter_by(category = 'Career').all()
    all_pitches = Pitch.query.order_by(Pitch.date_posted).all()
    return render_template('index.html', pitches = all_pitches,Funny = Funny, Business = Business,Motivational= Motivational,religious = religious, life = life, Career = Career)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/add_comment', methods=['GET', 'POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comment(name=form.name.data)
        db.session.add(comment)
        db.session.commit()
        flash('Category added successfully.')
        return redirect(url_for('.index'))
    return render_template('add_category.html', form=form)

@main.route('/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        title = pitch_form.pitch_title.data
        pitch = pitch_form.pitch.data
        category = pitch_form.category.data
        new_pitch = Pitch(pitch=pitch,title=title, user=current_user, category=category)
        new_pitch.save_post()
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))

   
    return render_template('pitch.html',pitch_form = pitch_form)