from database.ConexaoSQL_v2 import Product
from database.ConexaoSQL_v2 import db
from flask_restful import Resource
from flask import request


def Product_function(product, code, price):
    product = Product(name=product, code=code, price=price)
    db.session.add(product)
    db.session.commit()

def get_user(self):
    product = Product.query.all()
    results = [ 
        {
            "id":products.id,
            "name":products.name,
            "code":products.code,
            "price":products.price
        } for products in product]
     
    return {"count": len(results), "product": results}


def delete_user(id):
    product = db.session.query(Product).filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()


def update_user(id, name, code, price):
    print(id)
    product = db.session.query(Product).filter_by(id=id).first()
    product.name = name
    product.code = code
    product.price = price
    db.session.commit()


class Product_item(Resource):
    def get(self):
        get_report = get_user(self)
        return get_report

    def post(self):
        json_data = request.get_json()
        product_id = str(json_data['name'])
        code_id = str(json_data['code'])
        price_id = str(json_data['price'])
        Product_reports = Product_function(product_id, code_id, price_id)
        return Product_reports

    def delete(self):
        json_data = request.get_json()
        delete_id = str(json_data['id'])
        delete_user_reports = delete_user(delete_id)
        return delete_user_reports

    def put(self):
        json_data = request.get_json()
        update_id = str(json_data['id'])
        name_id = str(json_data['name'])
        code_id = str(json_data['code'])
        price_id = str(json_data['price'])
        update_reports = update_user(update_id, name_id, code_id, price_id)
        return update_reports
