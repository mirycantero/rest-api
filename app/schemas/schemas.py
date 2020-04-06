from app.models.db import ma


class CerealSchema(ma.Schema):
    class Meta:
        fields = ('name', 'calories', 'protein', 'fat', 'sodium',
                  'fiber', 'carbo', 'sugars', 'potass', 'vitamins')
