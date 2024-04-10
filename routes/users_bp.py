import uuid
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    RadioField,
    SelectField,
    TextAreaField,
    ValidationError,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    # Regexp
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user

from models.users import User
from extensions import db

users_bp = Blueprint("users_bp", __name__)


class RegistrationForm(FlaskForm):
    first_name = StringField(
        "First Name",
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=50,
                message="First name must be between 2 and 50 characters long",
            ),
        ],
    )
    surname = StringField(
        "Surname",
        validators=[
            DataRequired(),
            Length(
                min=2,
                max=50,
                message="Surname must be between 2 and 50 characters long",
            ),
        ],
    )
    dob_day = SelectField(
        "Day",
        coerce=int,
        validators=[DataRequired()],
        choices=[(str(i), str(i)) for i in range(1, 32)],
    )
    dob_month = SelectField(
        "Month",
        coerce=int,
        validators=[DataRequired()],
        choices=[(str(i), str(i)) for i in range(1, 13)],
    )
    dob_year = SelectField(
        "Year",
        coerce=int,
        validators=[DataRequired()],
        choices=[(str(i), str(i)) for i in range(1920, 2023)],
    )
    gender = RadioField(
        "Gender",
        choices=[("male", "Male"), ("female", "Female")],
        validators=[DataRequired()],
    )
    marital_status = RadioField(
        "Marital Status",
        choices=[
            ("single", "Single"),
            ("cohabitating", "Co-habitating"),
            ("married", "Married"),
            ("divorced", "Divorced"),
            ("separated", "Separated"),
            ("widowed", "Widowed"),
        ],
        validators=[DataRequired()],
    )
    address = TextAreaField(
        "Address",
        validators=[
            DataRequired(),
            Length(
                min=10,
                max=200,
                message="Address must be between 10 and 200 characters long",
            ),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Invalid email address"),
            Length(max=100, message="Email must be less than 100 characters"),
        ],
    )
    cellphone = StringField(
        "Cellphone Number",
        # validators=[
        #     DataRequired(),
        #     Regexp(
        #         r"^\+?1?\d{9,15}$",
        #         message="Invalid phone number format. Please enter a valid phone number.",
        #     ),
        # ],
        validators=[
            DataRequired(),
            Length(
                min=10, max=10, message="Cellphone number must be 10 characters only"
            ),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=12,
                message="Password must be between 8 and 12 characters long",
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already registered")

    def validate_cellphone(self, field):
        if User.query.filter_by(cellphone=field.data).first():
            raise ValidationError("Cellphone is already registered")


class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(message="Invalid email address"),
            Length(max=100, message="Email must be less than 100 characters"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(
                min=8,
                max=12,
                message="Password must be between 8 and 12 characters long",
            ),
        ],
    )
    submit = SubmitField("Log In")

    def validate_email(self, field):
        user_from_db = User.query.filter_by(email=field.data).first()
        if not user_from_db:
            raise ValidationError("Email does not exist")

    def validate_password(self, field):
        user_from_db = User.query.filter_by(email=self.email.data).first()
        if user_from_db:
            form_password = field.data
            print(user_from_db, form_password)
            if not check_password_hash(user_from_db.password, form_password):
                raise ValidationError("Invalid password")


@users_bp.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        password_hash = generate_password_hash(form.password.data)
        print(form.password.data, password_hash)

        dob = f"{str(form.dob_year.data)}-{str(form.dob_month.data)}-{str(form.dob_day.data)}"

        new_user = User(
            id=str(uuid.uuid4()),
            first_name=form.first_name.data,
            surname=form.surname.data,
            date_of_birth=dob,
            gender=form.gender.data,
            marital_status=form.marital_status.data,
            address=form.address.data,
            email=form.email.data,
            cellphone=form.cellphone.data,
            password=password_hash,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("User successfully registered", "success")  # confirmation message
            return redirect(url_for("users_bp.login_page")), 200
        except Exception as e:
            db.session.rollback()
            flash(f"Error occurred: {str(e)}", "error")  #  error message
    return render_template("register.html", form=form)


@users_bp.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user_from_db = User.query.filter_by(email=form.email.data).first()  # added
        if user_from_db and user_from_db.check_password(form.password.data):
            login_user(user_from_db)  # token is issued - (cookies) stored browser
            print("hi")
            flash("Logged in successfully", "success")
            return redirect(url_for("home_bp.index_page"))  # Redirect to home page
        else:
            flash("Invalid email or password", "error")
    return render_template("login.html", form=form)


@users_bp.route("/logout")
def logout_page():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for("index_page"))
