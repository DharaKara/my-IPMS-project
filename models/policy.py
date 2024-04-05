import uuid
from extension import db

# class Policy(db.Model):
#     __tablename__ = "policies"
#     id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
#     policy_number = db.Column(db.String(20), unique=True, nullable=False)
#     type = db.Column(db.String(50), nullable=False)
#     premium = db.Column(db.Float, nullable=False)
#     start_date = db.Column(db.Date, nullable=False)
#     end_date = db.Column(db.Date, nullable=False)
#     user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
#     user = db.relationship("User", backref=db.backref("policies", lazy=True))


class Policy(db.Model):
    __tablename__ = "policy"
    id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
    name = db.Column(db.String(100), nullable=False)
    image_link = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_link": self.image_link,
            "summary": self.summary,
        }
