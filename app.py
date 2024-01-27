from decimal import Decimal

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from database import db



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo.db'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    from models.usermodel import UserModel
    from models.bank_account import BankAccountModel
    from schema.base import ma
    db.init_app(app)
    ma.init_app(app)
    from resources.users import Users, UserById
    from resources.bank_account import BankAccountById, BankAccount

    CORS(app)
    api = Api(app)

    api.add_resource(Users, '/users')
    api.add_resource(UserById, '/users/<id>')
    api.add_resource(BankAccountById, '/bank_account/<id>')
    api.add_resource(BankAccount, '/bank_account')

    with app.app_context():
        db.drop_all()
        db.create_all()

        # Dados iniciais
        user = UserModel(name='Leonardo')
        db.session.add(user)
        db.session.commit()

        cc = BankAccountModel(name='corrente', value=Decimal(1000), user=user)
        cp = BankAccountModel(name='poupança', value=Decimal(1), user=user)
        db.session.add(cc)
        db.session.add(cp)
        db.session.commit()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
