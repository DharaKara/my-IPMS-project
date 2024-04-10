import uuid
from extensions import db


class CarInsuranceQuote(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    coverage_type = db.Column(db.String(100), nullable=False)
    premium_amount = db.Column(db.Float, nullable=False)
    additional_benefits = db.Column(db.Text, nullable=True)
    provider_id = db.Column(
        db.String(36), db.ForeignKey("car_insurance_provider.id"), nullable=False
    )
    provider = db.relationship(
        "CarInsuranceProvider", backref=db.backref("quotes", lazy=True)
    )
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    user = db.relationship(
        "User", backref=db.backref("car_insurance_quotes", lazy=True)
    )
