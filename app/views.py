from flask import render_template, flash, request, redirect, url_for, session
from flask_oauth import OAuth
from app import app
from app import db
from models import User, bcrypt
from forms import LoginForm, SignupForm
from flask_login import login_user, login_required, logout_user, current_user


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


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
