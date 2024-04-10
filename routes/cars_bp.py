# from flask import Blueprint, render_template, request, redirect, url_for
# from models.vehicles import Vehicle
# from extension import db

# cars_bp = Blueprint("cars_bp", __name__)


# @cars_bp.route("/car")
# def add_car():
#     # policy = Policy.query.get_or_404(id)
#     return render_template("add-car.html")


# @cars_bp.route("/car_summary", methods=["GET", "POST"])
# def car_summary():
#     if request.method == "POST":
#         year = request.form["year"]
#         make = request.form["make"]
#         model = request.form["model"]
#         description = request.form["description"]
#         coverage = request.form["coverage"]
#         parking_location = request.form["parking_location"]

#         # Create a new Vehicle object
#         vehicle = Vehicle(
#             year=year,
#             make=make,
#             model=model,
#             description=description,
#             coverage=coverage,
#             parking_location=parking_location,
#             user_id=current_user.id,  # Assuming user is logged in
#         )

#         # Add the new vehicle to the database
#         db.session.add(vehicle)
#         db.session.commit()

#         return redirect(url_for("car_summary"))  # Redirect to car summary page
#     else:
#         return render_template("add-car.html")
