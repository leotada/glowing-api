from flask import make_response, jsonify, request
from flask_restful import Resource

from database import db
from models.user import User
from schema.user import user_schema, users_schema


class Users(Resource):
    def get(self):
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return make_response(jsonify(result), 200)

    def post(self):
        user = User(name=request.json['name'], email=request.json['email'])
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return make_response(jsonify(result), 200)

    def put(self):
        user = User.query.filter_by(id=request.json['id']).first()
        user.name = request.json['name']
        user.email = request.json['email']
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return make_response(jsonify(result), 200)


class UserById(Resource):
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        return make_response(jsonify({"status": "success"}), 200)

    def get(self, id):
        user = User.query.filter_by(id=id).first()
        result = user_schema.dump(user)
        return make_response(jsonify(result), 200)
