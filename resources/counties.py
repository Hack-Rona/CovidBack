import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required, current_use

county = Blueprint('county', 'county')

# used from flask react hmwk
@county.route('/', methods=["GET"])
def show_all_counties():
    try:
        counties = [model_to_dict(county) for county in models.County.select()]
        print(counties)
        return jsonify(data=counties, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@county.route('/', methods=["POST"])
def create_county():
    payload = request.get_json()
    print(type(payload), 'payload')
    new_county = models.County.create(**payload)
    county_dict = model_to_dict(new_county)
    return jsonify(data=county_dict, status={"code": 201, "message": "Success"})

#individual show route
@county.route('/<id>', methods=["GET"])
def show_one_county(id):
    county = models.County.get_by_id(id)
    print(county.__dict__)
    return jsonify(data=model_to_dict(county), status={"code": 200, "message": "Success"})

#update route
@county.route('/<id>', methods=["PUT"])
def change_county(id):
    payload = request.get_json()
    query = models.County.update(**payload).where(models.County.id == id)
    query.execute()
    return jsonify(data=model_to_dict(models.County.get_by(id)),
    status={"code":200, "message": "Success"})


#delete route
@county.route('/<id>', methods=["DELETE"])
def delete_county(id):
    query = models.County.delete().where(models.County.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})