from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.models import User, Board


class SignupForm(Form):
    """
    Signup form structure
    """
    email = StringField("Email", validators=[DataRequired("Please enter your email address"), Email(
        "Please enter a valid email address"), Length(min=6, max=50)])
    username = StringField("Username", validators=[DataRequired(
        "Please enter your username"), Length(min=3, max=25)])
    password = PasswordField("Password", validators=[DataRequired(
        "Please enter your password"), Length(min=6, message="Passwords must be 6 characters or more.")])
    confirm = PasswordField("Repeat Password", validators=[DataRequired(
        "Please re-enter your password"), EqualTo("password", message="Passwords must match.")])
    submit = SubmitField('Get Started')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class LoginForm(Form):
    """
    Login form structure
    """
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")

class BoardForm(Form):
    """
    Creates a board form structure
    """
    board_title = StringField("Title: ", validators=[Length(min=1, message="Title is too short")])
    submit = SubmitField("Add Board")
