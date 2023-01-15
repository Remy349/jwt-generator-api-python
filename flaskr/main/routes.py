from flask import Blueprint, render_template

bp = Blueprint("main", __name__)


@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    return render_template("index.html")
