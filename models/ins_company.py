from extension import db


class InsuranceCompany(db.Model):
    __tablename__ = "insurance_company"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    logo_link = db.Column(db.String(255), nullable=False)
    monthly_premium = db.Column(db.String(50), nullable=False)
    excess = db.Column(db.String(50), nullable=False)
    additional_factor = db.Column(db.Float, nullable=False)
    full_license_excess_factor = db.Column(db.Float, nullable=False)
    partial_license_excess_factor = db.Column(db.Float, nullable=False)
    financial_stability_rating = db.Column(db.String(255))
    years_in_business = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "logo_link": self.logo_link,
            "monthly_premium": self.monthly_premium,
            "excess": self.excess,
            "additional_factor": self.additional_factor,
            "full_license_excess_factor": self.full_license_excess_factor,
            "partial_license_excess_factor": self.partial_license_excess_factor,
            "financial_stability_rating": self.financial_stability_rating,
            "years_in_business": self.years_in_business,
        }
