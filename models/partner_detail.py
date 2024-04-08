from extension import db


class PartnerSection(db.Model):
    __tablename__ = "partner_section"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(500), nullable=False)
    partner_id = db.Column(db.Integer, db.ForeignKey("partner.id"), nullable=False)
    partner = db.relationship(
        "Partner", backref=db.backref("partner_sections", cascade="all, delete-orphan")
    )

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image_url": self.image_url,
            "partner": self.partner,
        }


class Feature(db.Model):
    __tablename__ = "feature"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(200), nullable=False)
    partner_section_id = db.Column(db.Integer, db.ForeignKey("partner_section.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "partner_section_id": self.partner_section_id,
        }
