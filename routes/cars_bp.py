from flask import Blueprint, render_template, flash, redirect, url_for, request
from extension import db
from models.driver_details import DriverDetails
from models.vehicles import Vehicle
from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired

cars_bp = Blueprint("cars_bp", __name__)


class AddCarForm(FlaskForm):
    year = SelectField(
        "Year",
        choices=[(str(year), str(year)) for year in range(1920, 2023)],
        validators=[DataRequired()],
    )
    make = StringField("Make", validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    coverage = SelectField(
        "Coverage Type",
        choices=[
            ("Comprehensive", "Comprehensive"),
            ("Third Party Fire And Theft", "Third Party Fire and Theft"),
            ("Third Party Only", "Third Party Only"),
        ],
        validators=[DataRequired()],
    )
    parking_location = SelectField(
        "Parking Location",
        choices=[
            ("Access Controlled Area", "Access Controlled Area"),
            ("Basement Electronic Access", "Basement - Electronic Access"),
            ("Basement No Electronic Access", "Basement - No Electronic Access"),
            ("Locked Garage", "Locked Garage"),
            ("On Pavement/In Street", "On Pavement/In Street"),
            ("Open Parking Lot", "Open Parking Lot"),
            ("Yard - No Locked Gates", "Yard - No Locked Gates"),
            ("Yard - Locked Gates", "Yard - Locked Gates"),
        ],
        validators=[DataRequired()],
    )


class AddDriverForm(FlaskForm):
    licence_type = SelectField(
        "License Type",
        choices=[
            ("RSA Driver Licence", "RSA Driver Licence"),
            ("RSA Leaner Licence", "RSA Leaner Licence"),
            ("International Driver Licence", "International Driver Licence"),
        ],
        validators=[DataRequired()],
    )
    month = SelectField(
        "Month",
        choices=[(str(month), str(month)) for month in range(1, 13)],
        validators=[DataRequired()],
    )
    year = SelectField(
        "Year",
        choices=[(str(year), str(year)) for year in range(1920, 2023)],
        validators=[DataRequired()],
    )
    car_ins = RadioField(
        "Car Insurance",
        choices=[("Yes", "Yes"), ("No", "No")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Get Quote")


@cars_bp.route("/add_car", methods=["GET", "POST"])
@login_required
def add_car():
    form = AddCarForm()
    if form.validate_on_submit():
        try:
            year = form.year.data
            make = form.make.data
            model = form.model.data
            description = form.description.data
            coverage = form.coverage.data
            parking_location = form.parking_location.data
            curr_user = current_user
            new_vehicle = Vehicle(
                year=year,
                make=make,
                model=model,
                description=description,
                user_id=curr_user.id,
                coverage=coverage,
                parking_location=parking_location,
            )
            db.session.add(new_vehicle)
            db.session.commit()
            return redirect(url_for("cars_bp.car_summary"))
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            db.session.rollback()
            return redirect(url_for("cars_bp.add_car"))
    return render_template("add-car.html", form=form)


@cars_bp.route("/car_summary", methods=["GET"])
@login_required
def car_summary():
    vehicles = Vehicle.query.all()
    return render_template("cars-summary.html", vehicles=vehicles)


@cars_bp.route("/delete_car/<car_id>", methods=["POST"])
@login_required
def delete_car(car_id):
    try:
        car = Vehicle.query.get(car_id)
        db.session.delete(car)
        db.session.commit()
        return redirect(url_for("cars_bp.car_summary"))
    except Exception as e:
        print(f"An error occurred while deleting the car: {str(e)}")
        db.session.rollback()
        return redirect(url_for("cars_bp.car_summary"))


@cars_bp.route("/edit_car/<car_id>", methods=["GET", "POST"])
@login_required
def edit_car(car_id):
    try:
        car = Vehicle.query.get(car_id)
        if request.method == "POST":
            car.year = request.form.get("year")
            car.make = request.form.get("make")
            car.model = request.form.get("model")
            car.description = request.form.get("description")
            car.coverage = request.form.get("coverage")
            car.parking_location = request.form.get("parking_location")
            db.session.commit()
            return redirect(url_for("cars_bp.car_summary"))
        return render_template("edit-car.html", car=car)
    except Exception as e:
        print(f"An error occurred while editing the car: {str(e)}")
        db.session.rollback()
        return redirect(url_for("cars_bp.car_summary"))


@cars_bp.route("/add_driver", methods=["GET", "POST"])
@login_required
def add_driver():
    form = AddDriverForm()
    if form.validate_on_submit():
        try:
            # Getting the selected value of car_ins
            has_car_insurance = form.car_ins.data == "Yes"

            new_driver = DriverDetails(
                license_type=form.licence_type.data,
                issue_month=form.month.data,
                issue_year=form.year.data,
                has_car_insurance=has_car_insurance,  # Using the selected value
                user_id=current_user.id,
            )
            db.session.add(new_driver)
            db.session.commit()
            flash("Driver details added successfully", "success")
            return redirect(url_for("quotes_bp.compare_quotes"))
        except Exception as e:
            flash(f"An error occurred while adding driver details: {str(e)}", "error")
            db.session.rollback()
    return render_template("add-driver.html", form=form)
