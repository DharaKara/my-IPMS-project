from flask import Blueprint, render_template, redirect, url_for
from models.users import User
from models.ins_company import InsuranceCompany
from models.partner import Partner
from flask_login import login_required, current_user
import datetime

from extension import db

quotes_bp = Blueprint("quotes_bp", __name__)


@quotes_bp.route("/compare-quotes")
@login_required
def compare_quotes():
    insurance_companies = InsuranceCompany.query.all()
    return render_template(
        "quote-calculated.html", insurance_companies=insurance_companies
    )


@quotes_bp.route("/interested/<int:partner_id>", methods=["POST"])
def interested(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    # Here you can process the form data or send an email, etc.
    return redirect(url_for("quotes_bp.thank_you", partner_id=partner_id))


@quotes_bp.route("/thank-you/<int:partner_id>")
def thank_you(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    return render_template("thank_you.html", partner=partner)
