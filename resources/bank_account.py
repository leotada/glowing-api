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
