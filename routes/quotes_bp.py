from flask import Blueprint, render_template, redirect, url_for
from models.users import User
from models.ins_company import InsuranceCompany
from models.partner import Partner
from flask_login import login_required, current_user
import datetime

from extension import db

quotes_bp = Blueprint("quotes_bp", __name__)

# Constants for premium calculation
BASE_PREMIUM_AGE_RANGES = {(0, 25): 350, (25, 30): 300, (30, 40): 250, (60, 100): 200}


def calculate_monthly_premium(user, company):
    user_age = calculate_age(user.date_of_birth)
    base_premium = BASE_PREMIUM_AGE_RANGES.get(age_range_for_premium(user_age), 50)

    premium = base_premium
    premium *= vehicle_risk_factor(user.vehicles)
    premium *= coverage_factor(user.vehicles)

    company_risk_factor = calculate_company_risk_factor(company)
    premium *= company_risk_factor

    return round(premium, 2)


def calculate_age(date_of_birth):
    today = datetime.date.today()
    age = (
        today.year
        - date_of_birth.year
        - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
    )
    return age


def age_range_for_premium(age):
    for age_range, _ in BASE_PREMIUM_AGE_RANGES.items():
        if age_range[0] <= age < age_range[1]:
            return age_range
    return (0, 100)


def vehicle_risk_factor(vehicles):
    risk_factor = 1
    for vehicle in vehicles:
        if vehicle.year < 2010:
            risk_factor += 0.1
        if vehicle.make == "Toyota":
            risk_factor += 0.05
        if vehicle.model == "Sedan":
            risk_factor += 0.05
    return risk_factor


def coverage_factor(vehicles):
    coverage_factor = 1
    for vehicle in vehicles:
        if vehicle.coverage == "Comprehensive":
            coverage_factor += 0.1
    return coverage_factor


def calculate_company_risk_factor(company):
    base_risk_factor = float(company.additional_factor)
    if company.years_in_business < 5:
        base_risk_factor += 0.1
    elif company.years_in_business >= 10:
        base_risk_factor -= 0.1
    if company.financial_stability_rating == "Excellent":
        base_risk_factor -= 0.05
    elif company.financial_stability_rating == "Poor":
        base_risk_factor += 0.1

    return base_risk_factor


@quotes_bp.route("/compare-quotes")
@login_required
def compare_quotes():
    insurance_companies = InsuranceCompany.query.all()
    for company in insurance_companies:
        monthly_premium = calculate_monthly_premium(current_user, company)
        company.monthly_premium = monthly_premium

    return render_template(
        "quote-calculated.html",
        insurance_companies=insurance_companies,
        calculate_monthly_premium=calculate_monthly_premium,
        user=current_user,
    )


@quotes_bp.route("/interested/<int:partner_id>", methods=["POST"])
def interested(partner_id):
    partner = InsuranceCompany.query.get_or_404(partner_id)
    # Here you can process the form data or send an email, etc.
    return redirect(url_for("quotes_bp.thank_you", partner_id=partner_id))


@quotes_bp.route("/thank-you/<int:partner_id>")
def thank_you(partner_id):
    partner = InsuranceCompany.query.get_or_404(partner_id)
    return render_template("thank_you.html", partner=partner)
