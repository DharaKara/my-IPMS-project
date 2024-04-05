from datetime import datetime
import uuid
from extension import db
from flask_login import UserMixin


# class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.now)
# car_insurance_quotes = db.relationship(
#     "CarInsuranceQuote", backref="user", lazy=True
# )


class User(UserMixin, db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    first_name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    marital_status = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    cellphone = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
