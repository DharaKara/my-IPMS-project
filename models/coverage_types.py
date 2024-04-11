import uuid
from extensions import db


class CoverageType(db.Model):
    __tablename__ = "coverage_types"
    id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
    name = db.Column(db.String(50), nullable=False)
    vehicles = db.relationship("Vehicle", backref="coverage_type", lazy=True)

    def to_dict(self):
        return {"id": self.id, "name": self.name}
