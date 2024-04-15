from flask import Blueprint, render_template, request, redirect, url_for

# from models.vehicles import Vehicle
from extension import db

quotes_bp = Blueprint("quotes_bp", __name__)


@quotes_bp.route("/car")
def get_quote():
    # policy = Policy.query.get_or_404(id)
    return render_template("add-car.html")


# @quotes_bp.route("/car/result", methods=["GET", "POST"])
# def quote_result():
#     if request.method == "POST":
#         # Handle form submission and perform calculation
#         vehicle_year = int(request.form["year"])
#         driver_age = int(request.form["age"])
#         coverage_limits = float(request.form["coverage_limits"])
#         deductible = float(request.form["deductible"])

#         # Perform a basic quote calculation (this is a placeholder, not realistic)
#         base_rate = 500  # Base rate for insurance
#         age_factor = driver_age * 0.1  # Age factor (just an example)
#         year_factor = (
#             2024 - vehicle_year
#         ) * 0.05  # Vehicle year factor (just an example)
#         coverage_factor = (
#             coverage_limits * 0.02
#         )  # Coverage limits factor (just an example)
#         deductible_factor = deductible * 0.01  # Deductible factor (just an example)

#         # Total quote calculation
#         total_quote = (
#             base_rate + age_factor + year_factor + coverage_factor - deductible_factor
#         )

#         # Format the total quote to display
#         formatted_quote = "${:,.2f}".format(total_quote)

#         return render_template("quote-result.html", quote=formatted_quote)

#     return render_template("get_quote.html")
