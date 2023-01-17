from flaskr import db
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, logout_user, login_user
from .forms import SignUpForm, SignInForm

from flaskr.models import User

bp = Blueprint("auth", __name__)


@bp.route("/sign-in", methods=["GET", "POST"])
def signin():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = SignInForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember_me = form.remember_me.data

        user = db.session.execute(
            db.select(User).filter_by(username=username)
        ).scalar_one()

        if user is None or not user.check_password(password):
            flash("Invalid username or password!")
            return redirect(url_for("auth.signin"))

        login_user(user, remember=remember_me)

        return redirect(url_for("main.index"))

    return render_template("auth/sign-in.html", title="Sign In", form=form)


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
