from database.ConexaoSQL_v2 import Vendor
from database.ConexaoSQL_v2 import db
from flask_restful import Resource
from flask import request


def Vendor_function(name, cnpj, city):
    vendor = Vendor(name=name, cnpj=cnpj, city=city)
    db.session.add(vendor)
    db.session.commit()


def get_user(self):
    vendor = Vendor.query.all()
    results = [ 
        {
            "id":vendor_s.id,
            "name":vendor_s.name,
            "cnpj":vendor_s.cnpj,
            "city":vendor_s.city
        } for vendor_s in vendor]

    return {"count": len(results), "vendor": results}


def delete_user(id):
    vendor = db.session.query(Vendor).filter_by(id=id).first()
    db.session.delete(vendor)
    db.session.commit()
    return '', 204


def update_user(id, name, cnpj, city):
    print(id)
    product = db.session.query(Vendor).filter_by(id=id).first()
    product.name = name
    product.cnpj = cnpj
    product.city = city
    db.session.commit()


class Vendor_item(Resource):
    def get(self):
        get_report = get_user(self)
        return get_report

    def post(self):
        json_data = request.get_json()
        name_id = str(json_data['name'])
        cnpj_id = str(json_data['cnpj'])
        city_id = str(json_data['city'])
        Vendor_item_reports = Vendor_function(name_id, cnpj_id, city_id)
        return Vendor_item_reports

    def delete(self):
        json_data = request.get_json()
        delete_id = str(json_data['id'])
        delete_user_reports = delete_user(delete_id)
        return delete_user_reports

    def put(self):
        json_data = request.get_json()
        update_id = str(json_data['id'])
        name_id = str(json_data['name'])
        cnpj_id = str(json_data['cnpj'])
        city_id = str(json_data['city'])
        update_reports = update_user(update_id, name_id, cnpj_id, city_id)
        return update_reports
