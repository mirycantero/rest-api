from .base import db


class Company(db.Model):
    __tablename__ = 'companies'

    company_id = db.Column(db.Integer, primary_key=True)
    industry_id = db.Column(
        db.Integer,
        db.ForeignKey("industries.industry_id"),
        nullable=True
    )
    state_id = db.Column(
        db.Integer,
        db.ForeignKey("states.state_id"),
        nullable=True
    )
    name = db.Column(db.String(100), nullable=True)

    industry = db.relationship('Industry', uselist=False)
    state = db.relationship('State', uselist=False)
