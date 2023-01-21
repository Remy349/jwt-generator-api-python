from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint("user", __name__)


@bp.route("/<string:username>", methods=["GET"])
@login_required
def profile(username):
    print(username)
    return render_template("user/profile.html")
