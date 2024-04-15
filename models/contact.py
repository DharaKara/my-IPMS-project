from datetime import datetime, timezone
import uuid
from extension import db


class Contact(db.Model):
    __tablename__ = "contact"
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
