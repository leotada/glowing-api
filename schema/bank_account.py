from schema.base import ma


class BankAccountSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "value", "user_id")


bank_account_schema = BankAccountSchema()
