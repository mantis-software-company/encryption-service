from marshmallow import Schema, fields


class BaseResponse(Schema):
    data = fields.Dict()
    message = fields.String()
    statusCode = fields.String()
    exceptionDetail = fields.String()

    class Meta:
        ordered = True


class Request(Schema):
    text = fields.String()


class Response(BaseResponse):
    data = fields.Nested(Request)
