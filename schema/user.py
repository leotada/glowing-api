from schema.base import ma


class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
