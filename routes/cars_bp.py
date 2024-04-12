from flask import Blueprint, render_template

# redirect, url_for, flash

# from models.vehicles import Vehicle
# from extensions import db
# from flask_login import login_required

# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField, SelectField
# from wtforms.validators import DataRequired
# from models.coverage_types import CoverageType
# from models.parking_locations import ParkingLocation

cars_bp = Blueprint("cars_bp", __name__)


@cars_bp.route("/add_car", methods=["GET", "POST"])
def add_car():
    return render_template("add-car.html")


@cars_bp.route("/car_summary", methods=["GET", "POST"])
def car_summary():
    return render_template("cars-summary.html")


@cars_bp.route("/add_driver", methods=["GET", "POST"])
def add_driver():
    return render_template("add-driver.html")
