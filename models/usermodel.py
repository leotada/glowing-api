from database import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    bank_accounts = db.relationship('BankAccountModel', backref='user', lazy='dynamic')


