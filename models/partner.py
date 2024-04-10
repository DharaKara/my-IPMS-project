from extensions import db


class Partner(db.Model):
    __tablename__ = "partner"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
