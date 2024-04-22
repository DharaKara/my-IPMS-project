from extension import db


class InsuranceCompany(db.Model):
    __tablename__ = "insurance_company"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    logo_link = db.Column(db.String(255), nullable=False)
    monthly_premium = db.Column(db.String(50), nullable=False)
    excess = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "logo_link": self.logo_link,
            "monthly_premium": self.monthly_premium,
            "excess": self.excess,
        }
