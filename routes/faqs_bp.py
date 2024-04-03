from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from app import FAQS, db

faqs_bp = Blueprint("faqs_bp", __name__)


@faqs_bp.route("/faqs")
def faqs():
    # Fetch claims from the database
    faqs = FAQS.query.all()
    return render_template("faqs.html", faqs=faqs)
