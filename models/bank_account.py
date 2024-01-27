from decimal import Decimal

from database import db


class BankAccountModel(db.Model):
    __tablename__ = 'bank_account'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    value = db.Column(db.DECIMAL(15, 2), nullable=False, default=Decimal(0))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def withdraw(self, value: Decimal) -> Decimal:
        if self.value > value:
            self.value -= value
            return value

    def deposit(self, value: Decimal) -> None:
        self.value += value
