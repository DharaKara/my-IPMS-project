import uuid
from extension import db


class FAQS(db.Model):
    __tablename__ = "faqs"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)
