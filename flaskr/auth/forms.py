from flaskr import db
from flask import flash
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from sqlalchemy.orm.exc import NoResultFound

from flaskr.models import User


class SignInForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        try:
            user = db.session.execute(
                db.select(User).filter_by(username=username.data)
            ).scalar_one()

            if user is not None:
                flash("Please use a different username!", "error")
                raise ValidationError("Username field error!")
        except NoResultFound:
            pass

    def validate_email(self, email):
        try:
            user = db.session.execute(
                db.select(User).filter_by(email=email.data)
            ).scalar_one()

            if user is not None:
                flash("Please use a different email address!", "error")
                raise ValidationError("Email address field error!")
        except NoResultFound:
            pass
