from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from app import Contact, db

contact_bp = Blueprint("contact_bp", __name__)


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


@contact_bp.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST" and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # Create a new contact object and add it to the database
        new_contact = Contact(name=name, email=email, message=message)
        try:
            db.session.add(new_contact)
            db.session.commit()
            flash("Your message has been sent!", "success")
            return redirect(url_for("contact_bp.contact"))
        except Exception as e:
            db.session.rollback()
            return f"<h2>Error occurred while sending message: {str(e)}</h2>", 500

    return render_template("contact.html", form=form)
