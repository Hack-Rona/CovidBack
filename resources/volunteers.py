import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required, current_use

volunteer = Blueprint('volunteer', 'volunteer')

# used from flask react hmwk
@volunteer.route('/', methods=["GET"])
def show_all_vols():
    try:
        volunteers = [model_to_dict(volunteer) for volunteer in models.Volunteer.select()]
        print(volunteers)
        return jsonify(data=volunteers, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@volunteer.route('/', methods=["POST"])
def create_vols():
    payload = request.get_json()
    print(type(payload), 'payload')
    new_volunteer = models.Volunteer.create(**payload)
    volunteer_dict = model_to_dict(new_volunteer)
    return jsonify(data=volunteer_dict, status={"code": 201, "message": "Success"})

#individual show route
@volunteer.route('/<id>', methods=["GET"])
def show_one_vol(id):
    volunteer = models.Volunteer.get_by_id(id)
    print(volunteer.__dict__)
    return jsonify(data=model_to_dict(volunteer), status={"code": 200, "message": "Success"})

#delete route
@volunteer.route('/<id>', methods=["DELETE"])
def delete_volunteer(id):
    query = models.Volunteer.delete().where(models.Volunteer.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})
