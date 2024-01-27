from schema.base import ma


class BankAccountSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "value")


bank_account_schema = BankAccountSchema()
