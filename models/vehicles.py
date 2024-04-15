import uuid
from extension import db


class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
    year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    coverage = db.Column(db.String(100), nullable=False)
    parking_location = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "year": self.year,
            "make": self.make,
            "model": self.model,
            "description": self.description,
            "coverage": self.coverage,
            "parking_location": self.parking_location,
            "user_id": self.user_id,
        }


# class Vehicle(db.Model):
#     __tablename__ = "vehicles"
#     id = db.Column(db.String(36), primary_key=True, default=(lambda: str(uuid.uuid4())))
#     year = db.Column(db.Integer, nullable=False)
#     make = db.Column(db.String(50), nullable=False)
#     model = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.String(100), nullable=False)
#     user_id = db.Column(db.String(36), db.ForeignKey("users.id"), nullable=False)
#     coverage_id = db.Column(
#         db.String(36), db.ForeignKey("coverage_types.id"), nullable=False
#     )
#     parking_location_id = db.Column(
#         db.String(36), db.ForeignKey("parking_locations.id"), nullable=False
#     )

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "year": self.year,
#             "make": self.make,
#             "model": self.model,
#             "description": self.description,
#             "user_id": self.user_id,
#             "coverage_id": self.coverage_id,
#             "parking_location_id": self.parking_location_id,
#         }
