# import uuid
# from flask import Blueprint, render_template, redirect, url_for, flash
# from models.vehicles import Vehicle
# from extensions import db
# from flask_login import current_user, login_required
# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField, SelectField
# from wtforms.validators import DataRequired
# from models.coverage_types import CoverageType
# from models.parking_locations import ParkingLocation

# cars_bp = Blueprint("cars_bp", __name__)


# class AddCarForm(FlaskForm):
#     year = SelectField(
#         "Year",
#         coerce=int,
#         validators=[DataRequired()],
#         choices=[(i, i) for i in range(1920, 2023)],
#     )
#     make = StringField("Make", validators=[DataRequired()])
#     model = StringField("Model", validators=[DataRequired()])
#     description = TextAreaField("Description", validators=[DataRequired()])
#     coverage_type = SelectField(
#         "Coverage Type",
#         coerce=str,
#         validators=[DataRequired()],
#         choices=[(ct.id, ct.name) for ct in CoverageType.query.all()],
#     )
#     parking_location = SelectField(
#         "Parking Location",
#         coerce=str,
#         validators=[DataRequired()],
#         choices=[(pl.id, pl.name) for pl in ParkingLocation.query.all()],
#     )
#     submit = SubmitField("Add Car")


# @cars_bp.route("/car", methods=["GET", "POST"])
# @login_required
# def add_car():
#     # form = AddCarForm()
#     # if form.validate_on_submit():
#     #     new_vehicle = Vehicle(
#     #         id=str(uuid.uuid4()),
#     #         year=form.year.data,
#     #         make=form.make.data,
#     #         model=form.model.data,
#     #         description=form.description.data,
#     #         user_id=current_user.id,
#     #     )
#     #     try:
#     #         db.session.add(new_vehicle)
#     #         db.session.commit()
#     #         flash("Car successfully added", "success")
#     #         return redirect(url_for("cars_bp.car_summary"))
#     #     except Exception as e:
#     #         db.session.rollback()
#     #         flash(f"Error occurred: {str(e)}", "error")
#     return render_template("add-car.html")


# # @cars_bp.route("/car_summary", methods=["GET", "POST"])
# # def car_summary():
# #     if request.method == "POST":
# #         year = request.form["year"]
# #         make = request.form["make"]
# #         model = request.form["model"]
# #         description = request.form["description"]
# #         coverage = request.form["coverage"]
# #         parking_location = request.form["parking_location"]

# #         # Create a new Vehicle object
# #         vehicle = Vehicle(
# #             year=year,
# #             make=make,
# #             model=model,
# #             description=description,
# #             coverage=coverage,
# #             parking_location=parking_location,
# #             user_id=current_user.id,
# #         )

# #         # Add the new vehicle to the database
# #         db.session.add(vehicle)
# #         db.session.commit()

# #         return redirect(url_for("car_summary"))  # Redirect to car summary page
# #     else:
# #         return render_template("add-car.html")
