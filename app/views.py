from flask import render_template, flash, request, redirect, url_for, session
from flask_oauth import OAuth
from app import app
from app import db, models
from models import User, List, Card, bcrypt
from forms import LoginForm, SignupForm, ListForm
from flask_login import login_user, login_required, logout_user, current_user


@app.route('/', methods=['GET'])
def index():
    lists = List.query.filter_by(user_id=current_user.id)
    all_lists = 0
    for i in lists:
        all_lists += 1
    return render_template('index.html', lists=lists, all_lists=all_lists)

@app.route('/lists/create', methods=['GET', 'POST'])
def create_list():
    form = ListForm()
    if request.method == "POST":
        if form.validate_on_submit():
            add_name= models.List(request.form['list_name'], current_user.id)            
            db.session.add(add_name)
            db.session.commit()

            return redirect(url_for('index'))
        else:
            flash('Invalid Please try again.')
    return render_template('list_c.html', form=form)

@app.route('/list/<l_id>', methods=['GET'])
def cards(l_id):
    cards = Card.query.filter_by(user_id=current_user.id, list_id=l_id)
    all_cards = 0
    for i in cards:
        all_cards += 1
    return render_template('cards.html', cards=cards, all_cards=all_cards)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            email = form.email.data
            password = form.password.data

            user = User.query.filter_by(email=email).first()
            if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
                login_user(user)
                flash('Login successful!')
                return redirect(url_for('index'))
            else:
                error = 'Invalid username or password. Please try again.'
    return render_template('login.html', form=form, error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were just logged out!')
    return redirect(url_for('login'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user = User(
                email=form.email.data,
                username=form.username.data,
                password=form.password.data
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            flash('Invalid credentials. Please try again.')
    return render_template('signup.html', form=form)
