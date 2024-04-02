from flask import Blueprint, render_template
from app import Policy, db

policy_bp = Blueprint("policy_bp", __name__)


@policy_bp.route("/policies")
def policy():
    policy = Policy.query.all()
    return render_template("policies.html", policy=policy)


@policy_bp.route("/policies/<id>")
def product_details(id):
    policy = Policy.query.get_or_404(id)
    return render_template("policies-details.html", policy=policy)
