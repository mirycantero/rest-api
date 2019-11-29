from .base import db
from ..schemas import CerealSchema

from sqlalchemy.sql import expression


class Cereal(db.Model):
    name = db.Column(db.String(80), primary_key=True)
    mfr = db.Column(db.String(10), nullable=True)
    type = db.Column(db.String(10), nullable=True)
    calories = db.Column(db.Float, nullable=True)
    protein = db.Column(db.Float, nullable=True)
    fat = db.Column(db.Float, nullable=True)
    sodium = db.Column(db.Float, nullable=True)
    fiber = db.Column(db.Float, nullable=True)
    carbo = db.Column(db.Float, nullable=True)
    sugars = db.Column(db.Float, nullable=True)
    potass = db.Column(db.Float, nullable=True)
    vitamins = db.Column(db.Float, nullable=True)
    shelf = db.Column(db.Float, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    cups = db.Column(db.Float, nullable=True)
    rating = db.Column(db.Float, nullable=True)
    active = db.Column(db.Boolean, server_default=expression.true())

    @staticmethod
    def get_cereals():
        cereals = Cereal.query.filter_by(active=True).all()
        return CerealSchema(many=True).dump(cereals)

    @staticmethod
    def get_cereal(name):
        cereal = Cereal.query.filter_by(name=name, active=True).first()
        return CerealSchema().dump(cereal)

    @staticmethod
    def post_cereal(cereal):
        cereal = Cereal(
            name=cereal.get('name'),
            calories=cereal.get('calories'),
            protein=cereal.get('protein'),
            fat=cereal.get('fat'),
            sodium=cereal.get('sodium'),
            fiber=cereal.get('fiber'),
            carbo=cereal.get('carbo'),
            sugars=cereal.get('sugars'),
            potass=cereal.get('potass'),
            vitamins=cereal.get('vitamins')
        )
        db.session.add(cereal)
        db.session.commit()

        return CerealSchema().dump(cereal)

    @staticmethod
    def put_cereal(name, cereal):
        Cereal.query.filter_by(name=name).update(dict(
            calories=cereal.get('calories'),
            protein=cereal.get('protein'),
            fat=cereal.get('fat'),
            sodium=cereal.get('sodium'),
            fiber=cereal.get('fiber'),
            carbo=cereal.get('carbo'),
            sugars=cereal.get('sugars'),
            potass=cereal.get('potass'),
            vitamins=cereal.get('vitamins')
        ))
        db.session.commit()

        cereal = Cereal.query.filter_by(name=name).first()
        return CerealSchema().dump(cereal)

    @staticmethod
    def delete_cereal(name):
        Cereal.query.filter_by(name=name).update(dict(active=False))
        db.session.commit()

        return {}
