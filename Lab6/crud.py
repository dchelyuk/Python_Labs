from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)


'''class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email'''


class DishwareItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.FLOAT, nullable=False)
    _weight_in_g = db.Column(db.FLOAT, nullable=False)
    country_origin = db.Column(db.String(80), nullable=False)
    _brand = db.Column(db.String(80), nullable=False)
    _code = db.Column(db.Integer, unique=True)
    _name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80))

    def __init__(self, price: float, _weight_in_g: float, country_origin: str, _brand: str, _code: int, _name: str,
                 category: str):
        self.price = price
        self._weight_in_g = _weight_in_g
        self.country_origin = country_origin
        self._brand = _brand
        self._code = _code
        self._name = _name
        self.category = category


'''class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)'''


class DishwareItemSchema(ma.Schema):
    class Meta:
        fields = ('price', '_weight_in_g', 'country_origin', '_brand', '_code', '_name', 'category')


dishware_item_schema = DishwareItemSchema()
dishware_items_schema = DishwareItemSchema(many=True)


'''# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']

    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)'''


@app.route("/dishwareitem", methods=["POST"])
def add_dishware_item():
    price = request.json['price']
    _weight_in_g = request.json['_weight_in_g']
    country_origin = request.json['country_origin']
    _brand = request.json['_brand']
    _code = request.json['_code']
    _name = request.json['_name']
    category = request.json['category']

    new_dishware_item = DishwareItem(price, _weight_in_g, country_origin, _brand, _code, _name, category)

    db.session.add(new_dishware_item)
    db.session.commit()

    return jsonify(new_dishware_item)


'''# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)'''


@app.route("/dishwareitem", methods=["GET"])
def get_dishware_item():
    all_dishware_items = DishwareItem.query.all()
    result = dishware_item_schema.dump(all_dishware_items)
    return jsonify(result.data)


'''# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)'''


@app.route("/dishwareitem/<id>", methods=["GET"])
def dishware_item_detail(id):
    dishware_item = DishwareItem.query.get(id)
    return dishware_item_schema.jsonify(dishware_item)


'''# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username

    db.session.commit()
    return user_schema.jsonify(user)'''


@app.route("/dishwareitem/<id>", methods=["PUT"])
def dishware_item_update(id):
    dishware_item = DishwareItem.query.get(id)
    price = request.json['price']
    _weight_in_g = request.json['_weight_in_g']
    country_origin = request.json['country_origin']
    _brand = request.json['_brand']
    _code = request.json['_code']
    _name = request.json['_name']
    category = request.json['category']

    dishware_item.price = price
    dishware_item._weight_in_g = _weight_in_g
    dishware_item.country_origin = country_origin
    dishware_item._brand = _brand
    dishware_item._code = _code
    dishware_item._name = _name
    dishware_item.category = category

    db.session.commit()
    return dishware_item_schema.jsonify(dishware_item)


'''# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)'''


@app.route("/dishwareitem/<id>", methods=["DELETE"])
def dishware_item_delete(id):
    dishware_item = DishwareItem.query.get(id)
    db.session.delete(dishware_item)
    db.session.commit()

    return dishware_item_schema.jsonify(dishware_item)


if __name__ == '__main__':
    app.run(debug=True)
