import uuid
from extensions import db


class FAQS(db.Model):
    __tablename__ = "faqs"
    id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.Text, nullable=False)
