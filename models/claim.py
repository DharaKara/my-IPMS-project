# import uuid
# from extension import db

# class Claim(db.Model):
#     __tablename__ = "claims"
#     id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
#     claim_number = db.Column(db.String(20), unique=True, nullable=False)
#     description = db.Column(db.Text, nullable=False)
#     status = db.Column(db.String(50), nullable=False)
#     policy_id = db.Column(db.String(36), db.ForeignKey("policies.id"), nullable=False)
#     policy = db.relationship("Policy", backref=db.backref("claims", lazy=True))
#     customer_id = db.Column(
#         db.String(36), db.ForeignKey("customers.id"), nullable=False
#     )
#     customer = db.relationship("Customer", backref=db.backref("claims", lazy=True))
