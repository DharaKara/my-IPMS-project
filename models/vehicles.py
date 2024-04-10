import uuid
from extensions import db
from sqlalchemy.orm import relationship


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
    year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="vehicles")

    def to_dict(self):
        return {
            "id": self.id,
            "year": self.year,
            "make": self.make,
            "model": self.model,
            "description": self.description,
            "user_id": self.user_id,
        }
