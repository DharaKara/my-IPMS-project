import uuid
import datetime
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user, login_required
from models.users import User
from extension import db
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
            user_db_data = user_from_db.to_dict()
            print(user_db_data, form_password)
            if not check_password_hash(user_db_data["password"], form_password):
                raise ValidationError("Invalid password")


class ProfileEditForm(FlaskForm):
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=50)]
    )
    surname = StringField("Surname", validators=[DataRequired(), Length(min=2, max=50)])
    dob_day = SelectField(
        "Day",
        coerce=int,
        validators=[DataRequired()],
        choices=[(i, i) for i in range(1, 32)],
    )
    dob_month = SelectField(
        "Month",
        coerce=int,
        validators=[DataRequired()],
        choices=[(i, i) for i in range(1, 13)],
    )
    dob_year = SelectField(
        "Year",
        coerce=int,
        validators=[DataRequired()],
        choices=[(i, i) for i in range(1920, 2023)],
    )
    gender = SelectField(
        "Gender",
        choices=[("male", "Male"), ("female", "Female")],
        validators=[DataRequired()],
    )
    marital_status = SelectField(
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
        "Address", validators=[DataRequired(), Length(min=10, max=200)]
    )
    email = StringField("Email", validators=[DataRequired()])
    cellphone = StringField(
        "Cellphone Number", validators=[DataRequired(), Length(min=10, max=10)]
    )
    submit = SubmitField("Save Changes")

    def process_formdata(self, valuelist):
        super().process_formdata(valuelist)
        self.dob_day.choices = [(i, i) for i in range(1, 32)]
        self.dob_month.choices = [(i, i) for i in range(1, 13)]
        self.dob_year.choices = [(i, i) for i in range(1920, 2023)]


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
        login_user(user_from_db)  # token is issued - (cookies) stored browser
        flash("Logged in successfully", "success")
        return redirect(url_for("cars_bp.add_car"))  # Redirect to home page
    flash("Invalid email or password", "error")
    return render_template("login.html", form=form)


@users_bp.route("/profile", methods=["GET", "POST"])
@login_required
def edit_profile():
    form = ProfileEditForm(obj=current_user)

    if form.validate_on_submit():
        # Update user's profile only if data has changed
        for field in form:
            if field.name != "submit":
                if (
                    field.name == "dob_day"
                    or field.name == "dob_month"
                    or field.name == "dob_year"
                ):
                    # If the field is part of date of birth, combine them to update date_of_birth
                    day = form.dob_day.data
                    month = form.dob_month.data
                    year = form.dob_year.data
                    setattr(
                        current_user, "date_of_birth", datetime.date(year, month, day)
                    )
                elif getattr(current_user, field.name) != field.data:
                    setattr(current_user, field.name, field.data)

        try:
            db.session.commit()
            flash("Profile updated successfully", "success")
            return redirect(url_for("users_bp.profile"))
        except Exception as e:
            db.session.rollback()
            flash(f"Error occurred: {str(e)}", "error")

    return render_template("profile.html", form=form)


@users_bp.route("/logout")
@login_required
def logout_page():
    logout_user()
    flash("Logged out successfully", "success")
    return redirect(url_for("home_bp.index_page"))
