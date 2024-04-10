from flask import Blueprint, render_template
from flask_login import login_required

home_bp = Blueprint("home_bp", __name__)


@home_bp.route("/")
@login_required
def index_page():
    return render_template("index.html")
