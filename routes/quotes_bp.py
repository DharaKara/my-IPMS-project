from flask import Blueprint, render_template, redirect, url_for
from models.users import User
from models.ins_company import InsuranceCompany
from models.partner import Partner
from flask_login import login_required, current_user
import datetime

# from models.vehicles import Vehicle
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


# @quotes_bp.route("/get_quote", methods=["GET", "POST"])
# @login_required
# def get_quote():
#     # Retrieve user information
#     user = User.query.filter_by(id=current_user.id).first()

#     # Calculate user's age based on date of birth
#     today = datetime.date.today()
#     age = (
#         today.year
#         - user.date_of_birth.year
#         - (
#             (today.month, today.day)
#             < (user.date_of_birth.month, user.date_of_birth.day)
#         )
#     )

#     # Assume some basic premium calculation logic based on age and coverage type
#     # These are just placeholders and need to be replaced with actual logic based on your requirements
#     coverage_type = "comprehensive"  # Assuming user selects comprehensive coverage
#     base_premium = 1000  # Placeholder for base premium

#     if age < 25:
#         premium_per_month = (
#             base_premium * 1.5
#         )  # Young drivers might have higher premiums
#     elif age >= 25 and age < 50:
#         premium_per_month = base_premium  # Standard premium for middle-aged drivers
#     else:
#         premium_per_month = base_premium * 0.8  # Discounted premium for older drivers

#     # Save the quote to the database
#     quote = Quote(
#         user_id=current_user.id,
#         premium_per_month=premium_per_month,
#         excess=500,  # Placeholder for excess
#     )
#     db.session.add(quote)
#     db.session.commit()

#     # Retrieve quotes for rendering
#     quotes = Quote.query.filter_by(user_id=current_user.id).all()
#     return render_template("quote_calculated.html", quotes=quotes)
