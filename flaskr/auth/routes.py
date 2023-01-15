from flask import Blueprint, render_template
from .forms import SignUpForm

bp = Blueprint("auth", __name__)


@bp.route("/sign-up", methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        print(username, email, password)

        return "OK!!!"

    return render_template("auth/sign-up.html", title="Sign Up", form=form)
