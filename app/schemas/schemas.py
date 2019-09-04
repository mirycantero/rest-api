from ..models.base import ma
# from marshmallow import post_dump


class IndustrySchema(ma.Schema):
    class Meta:
        fields = ('industry_id', 'name')


class StateSchema(ma.Schema):
    class Meta:
        fields = ('state_id', 'name')


class GenderSchema(ma.Schema):
    class Meta:
        fields = ('gender_id', 'gender')


class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('project_id', 'name', 'description')


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('employee_id', 'company', 'gender', 'name', 'email')
