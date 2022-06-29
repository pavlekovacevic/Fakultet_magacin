from marshmallow import fields, Schema
from marshmallow.validate import Length

class CreateCategoryInputSchema(Schema):
    title = fields.Str(required=True, validate=Length(max=20))
    content = fields.Str(required=True, validate=Length(max=200))


class CreateProductInputSchema(Schema):
    username = fields.Str(required=True, validate=Length(max=20), unique=True)
    description = fields.Str(required=True, validate=Length(max=200))
    name = fields.Str(required=True, validate=Length(max=20))