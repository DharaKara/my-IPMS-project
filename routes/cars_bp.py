from flask import Blueprint, render_template, flash, redirect, url_for
from extensions import db
from models.driver_details import DriverDetails
from models.vehicles import Vehicle
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
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
            ("comprehensive", "Comprehensive"),
            ("third_party_fire_and_theft", "Third Party Fire and Theft"),
            ("third_party_only", "Third Party Only"),
        ],
        validators=[DataRequired()],
    )
    parking_location = SelectField(
        "Parking Location",
        choices=[
            ("access_controlled_area", "Access Controlled Area"),
            ("basement_electronic_access", "Basement - Electronic Access"),
            ("basement_no_electronic_access", "Basement - No Electronic Access"),
            ("locked_garage", "Locked Garage"),
            ("on_pavement_or_in_street", "On Pavement/In Street"),
            ("open_parking_lot", "Open Parking Lot"),
            ("yard_no_locked_gates", "Yard - No Locked Gates"),
            ("yard_locked_gates", "Yard - Locked Gates"),
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
    car_ins = BooleanField("Comprehensive Car Insurance")


@cars_bp.route("/add_car", methods=["GET", "POST"])
def add_car():
    form = AddCarForm()
    if form.validate_on_submit():
        # Create a new vehicle object and add it to the database
        new_vehicle = Vehicle(
            year=form.year.data,
            make=form.make.data,
            model=form.model.data,
            description=form.description.data,
            coverage_id=form.coverage.data,
            parking_location_id=form.parking_location.data,
            user_id="user_id",
        )
        db.session.add(new_vehicle)
        db.session.commit()
        flash("Car added successfully", "success")
        return redirect(url_for("cars_bp.car_summary"))
    return render_template("add-car.html", form=form)


@cars_bp.route("/car_summary", methods=["GET"])
def car_summary():
    vehicles = Vehicle.query.all()
    return render_template("car-summary.html", vehicles=vehicles)


@cars_bp.route("/add_driver", methods=["GET", "POST"])
def add_driver():
    form = AddDriverForm()
    if form.validate_on_submit():
        new_driver = DriverDetails(
            license_type=form.licence_type.data,
            issue_month=form.month.data,
            issue_year=form.year.data,
            has_car_insurance=form.car_ins.data,
            user_id="user_id",
        )
        db.session.add(new_driver)
        db.session.commit()
        flash("Driver details added successfully", "success")
        return redirect(url_for("cars_bp.car_summary"))
    return render_template("add-driver.html", form=form)
