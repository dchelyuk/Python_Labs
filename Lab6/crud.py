from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')

db = SQLAlchemy(app)
ma = Marshmallow(app)


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


class DishwareItemSchema(ma.Schema):
    class Meta:
        fields = ('price', '_weight_in_g', 'country_origin', '_brand', '_code', '_name', 'category')


dishware_item_schema = DishwareItemSchema()
dishware_items_schema = DishwareItemSchema(many=True)


@app.route("/dishwareitem", methods=["POST"])
def add_dishware_item():
    data = dishware_item_schema.load(request.json)
    new_dishware_item = DishwareItem(**data)
    db.session.add(new_dishware_item)
    db.session.commit()
    return dishware_item_schema.jsonify(new_dishware_item)


@app.route("/dishwareitem", methods=["GET"])
def get_dishware_item():
    all_dishware_items = DishwareItem.query.all()
    result = dishware_items_schema.dump(all_dishware_items)
    return dishware_items_schema.jsonify(result)


@app.route("/dishwareitem/<id>", methods=["GET"])
def dishware_item_detail(id):
    dishware_item = DishwareItem.query.get(id)
    return dishware_item_schema.jsonify(dishware_item)


@app.route("/dishwareitem/<id>", methods=["POST", "PUT"])
def dishware_item_update(id):
    dishware_item = DishwareItem.query.get(id)
    if not DishwareItem:
        os.abort()
    dishware_item.price = request.json['price']
    dishware_item._weight_in_g = request.json['_weight_in_g']
    dishware_item.country_origin = request.json['country_origin']
    dishware_item._brand = request.json['_brand']
    dishware_item._code = request.json['_code']
    dishware_item._name = request.json['_name']
    dishware_item.category = request.json['category']

    db.session.commit()
    return dishware_item_schema.jsonify(dishware_item)


@app.route("/dishwareitem/<id>", methods=["DELETE"])
def dishware_item_delete(id):
    dishware_item = DishwareItem.query.get(id)
    if not DishwareItem:
        os.abort()
    db.session.delete(dishware_item)
    db.session.commit()

    return dishware_item_schema.jsonify(dishware_item)


if __name__ == '__main__':
    app.run(debug=True)
