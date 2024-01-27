from database import db


class BankAccountModel(db.Model):
    __tablename__ = 'bank_account'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    value = db.Column(db.DECIMAL(15, 2), nullable=False)
