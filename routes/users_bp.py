from flask import Blueprint, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, EqualTo, ValidationError
from extension import db
from models.user import User

users_bp = Blueprint("users_bp", __name__)


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(message="Username is required"),
            Length(min=6, message="Username must be at least 6 characters long"),
        ],
    )
    email = StringField(
        "Email",
        validators=[
            InputRequired(message="Email is required"),
            Email(message="Invalid email address"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(message="Password is required"),
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
            InputRequired(message="Please confirm your password"),
            EqualTo("password", message="Passwords must match"),
        ],
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username is already taken")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("Email is already registered")


class LoginForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            InputRequired(message="Username is required"),
            Length(min=6, message="Username must be at least 6 characters long"),
        ],
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired(message="Password is required"),
            Length(
                min=8,
                max=12,
                message="Password must be between 8 and 12 characters long",
            ),
        ],
    )
    submit = SubmitField("Log In")

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if not user:
            raise ValidationError("Username does not exist")

    def validate_password(self, field):
        user = User.query.filter_by(username=self.username.data).first()
        if user and user.password != field.data:
            raise ValidationError("Incorrect password")


@users_bp.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            return "<h2>User has been registered</h2>", 201
        except Exception as e:
            db.session.rollback()
            return f"<h2>Error happened {str(e)}</h2>", 500
    return render_template("register.html", form=form)


@users_bp.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        # Perform login logic here
        return "<h2>Logged in successfully</h2>", 200
    return render_template("login.html", form=form)
