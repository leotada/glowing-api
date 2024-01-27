from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_restful import Api

from database import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exemplo.db'
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    with app.app_context():
        from models.user import User
        db.init_app(app)
        from resources.users import Users, UserById

    CORS(app)
    api = Api(app)

    api.add_resource(Users, '/users')
    api.add_resource(UserById, '/users/<id>')

    with app.app_context():
        db.drop_all()
        db.create_all()

        # Dados iniciais
        user = User(name='s', email='leo@leo.com')
        db.session.add(user)
        db.session.commit()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
