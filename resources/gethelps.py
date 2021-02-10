import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required, current_use

gethelp = Blueprint('gethelps', 'gethelp')

# used from flask react hmwk
@gethelp.route('/', methods=["GET"])
def show_all_help():
    try:
        gethelps = [model_to_dict(gethelp) for gethelp in models.Gethelp.select()]
        print(gethelps)
        return jsonify(data=gethelps, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@gethelp.route('/', methods=["POST"])
def create_helps():
    payload = request.get_json()
    print(type(payload), 'payload')
    new_gethelp = models.Gethelp.create(**payload)
    gethelp_dict = model_to_dict(new_gethelp)
    return jsonify(data=gethelp_dict, status={"code": 201, "message": "Success"})

#individual show route
@gethelp.route('/<id>', methods=["GET"])
def show_one_help(id):
    gethelp = models.Gethelp.get_by_id(id)
    print(gethelp.__dict__)
    return jsonify(data=model_to_dict(gethelp), status={"code": 200, "message": "Success"})

#delete route
@gethelp.route('/<id>', methods=["DELETE"])
def delete_help(id):
    query = models.Gethelp.delete().where(models.Gethelp.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})
