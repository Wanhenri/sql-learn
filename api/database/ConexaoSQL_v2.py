from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///conexaosql.db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    code = db.Column(db.String(20))
    price = db.Column(db.Float(precision='4,2'), nullable=True)

    def __init__(self, name, code, price):
        self.name = name
        self.code = code
        self.price = price


class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    cnpj = db.Column(db.String(20))
    city = db.Column(db.String(20))

    def __init__(self, name, cnpj, city):
        self.name = name
        self.cnpj = cnpj
        self.city = city


db.create_all()
