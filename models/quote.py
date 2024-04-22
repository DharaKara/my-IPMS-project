from extension import db


class Quote(db.Model):
    __tablename__ = "quotes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    partner_id = db.Column(db.Integer, db.ForeignKey("partner.id"), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    premium_per_month = db.Column(db.Float, nullable=False)
    excess = db.Column(db.Float, nullable=False)
