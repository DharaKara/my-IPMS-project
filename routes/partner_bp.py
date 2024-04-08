from flask import Blueprint, render_template

# from extension import db
from models.partner import Partner
from models.partner_detail import PartnerSection, Feature

partner_bp = Blueprint("partner_bp", __name__)


@partner_bp.route("/partners")
def partner():
    partner = Partner.query.all()
    return render_template("partners.html", partner=partner)


@partner_bp.route("/partner/<partner_id>")
def partner_details(partner_id):
    partner = Partner.query.get_or_404(partner_id)
    partner_sections = PartnerSection.query.filter_by(partner_id=partner_id).all()
    # Fetch features for each partner section
    for section in partner_sections:
        section.features = Feature.query.filter_by(partner_section_id=section.id).all()
    return render_template(
        "partner-details.html", partner=partner, partner_sections=partner_sections
    )


# @partner_bp.route("/partner/id")
# def partner_details():
#     # partner = Partner.query.get_or_404(id)
#     return render_template("partner-details.html")
