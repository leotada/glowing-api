from decimal import Decimal

from flask import make_response, jsonify, request
from flask_restful import Resource

from database import db
from models.bank_account import BankAccountModel
from schema.bank_account import bank_account_schema


class BankAccountById(Resource):
    def get(self, id):
        bank_account = BankAccountModel.query.filter_by(id=id).first()
        result = bank_account_schema.dump(bank_account)
        return make_response(jsonify(result), 200)


class BankAccount(Resource):
    def put(self):
        bank_account_from = BankAccountModel.query.filter_by(id=request.json['from']).first()
        bank_account_to = BankAccountModel.query.filter_by(id=request.json['to']).first()
        value = Decimal(request.json['value'])
        # start transaction
        bank_account_from.withdraw(value)
        bank_account_to.deposit(value)
        # db.session.add(bank_account1)
        # db.session.add(bank_account2)
        db.session.commit()
        return make_response(jsonify({"status": "success"}), 200)
