from flask import Blueprint, render_template

# from extension import db
from models.faqs import FAQS

faqs_bp = Blueprint("faqs_bp", __name__)


@faqs_bp.route("/faqs")
def faqs():
    # Fetch claims from the database
    faqs = FAQS.query.all()
    return render_template("faqs.html", faqs=faqs)
