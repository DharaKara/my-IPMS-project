import uuid
from extensions import db


class DriverDetails(db.Model):
    __tablename__ = "driver_details"
    id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
    license_type = db.Column(db.String(50), nullable=False)
    issue_month = db.Column(db.Integer, nullable=False)
    issue_year = db.Column(db.Integer, nullable=False)
    has_car_insurance = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "license_type": self.license_type,
            "issue_month": self.issue_month,
            "issue_year": self.issue_year,
            "has_car_insurance": self.has_car_insurance,
            "user_id": self.user_id,
        }
