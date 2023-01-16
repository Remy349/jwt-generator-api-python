from flaskr import db
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, logout_user
from .forms import SignUpForm

from flaskr.models import User

bp = Blueprint("auth", __name__)


@bp.route("/sign-up", methods=["GET", "POST"])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("auth.signin"))

    return render_template("auth/sign-up.html", title="Sign Up", form=form)


@bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("main.index"))
