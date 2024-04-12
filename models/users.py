import uuid
from extensions import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
    first_name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    marital_status = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    cellphone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    vehicles = db.relationship("Vehicle", backref="owner", lazy=True)
    driver_details = db.relationship(
        "DriverDetails", uselist=False, backref="user", lazy=True
    )

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "surname": self.surname,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "marital_status": self.marital_status,
            "address": self.address,
            "email": self.email,
            "cellphone": self.cellphone,
            "password": self.password,
        }
