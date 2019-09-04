from .base import db
from ..schemas import IndustrySchema, StateSchema, GenderSchema, ProjectSchema


class Industry(db.Model):
    __tablename__ = 'industries'

    industry_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)

    def get_industries():
        industries = Industry.query.all()
        return IndustrySchema(many=True).dump(industries)


class State(db.Model):
    __tablename__ = 'states'

    state_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=True)

    def get_states():
        states = State.query.all()
        return StateSchema(many=True).dump(states)


class Gender(db.Model):
    __tablename__ = 'genders'

    gender_id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10), nullable=True)

    def get_genders():
        genders = Gender.query.all()
        return GenderSchema(many=True).dump(genders)


class Project(db.Model):
    __tablename__ = 'projects'

    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(100), nullable=True)

    def get_projects():
        projects = Project.query.all()
        return ProjectSchema(many=True).dump(projects)
