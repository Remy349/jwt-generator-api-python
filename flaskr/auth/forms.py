from flaskr import db
from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from flaskr.models import User


class SignInForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = db.session.execute(
            db.select(User).filter_by(username=username.data)
        ).scale_one()

        if user is not None:
            raise ValidationError("Please use a different username!")

    def validate_email(self, email):
        user = db.session.execute(
            db.select(User).filter_by(email=email.data)
        ).scale_one()

        if user is not None:
            raise ValidationError("Please use a different email address!")
