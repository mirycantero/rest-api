from .base import db
from ..schemas import EmployeeSchema
from ..models import Company, Gender


class Employee(db.Model):
    __tablename__ = 'employees'

    employee_id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(
        db.Integer,
        db.ForeignKey("companies.company_id"),
        nullable=True
    )
    gender_id = db.Column(
        db.Integer,
        db.ForeignKey("genders.gender_id"),
        nullable=True
    )
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)

    company = db.relationship('Company', uselist=False)
    gender = db.relationship('Gender', uselist=False)

    def get_employees():
        employees = (
            db.session
            .query(
                Employee.employee_id,
                Employee.name,
                Employee.email,
            )
            .join(Company, Company.company_id == Employee.company_id)
            .join(Gender, Gender.gender_id == Employee.gender_id)
            .all()
        )

        return EmployeeSchema(many=True).dump(employees)


class EmployeeHasProject(db.Model):
    __tablename__ = 'employee_has_project'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.employee_id"),
        nullable=True
    )
    project_id = db.Column(
        db.Integer,
        db.ForeignKey("projects.project_id"),
        nullable=True
    )

    employees = db.relationship('Employee')
    projects = db.relationship('Project')
