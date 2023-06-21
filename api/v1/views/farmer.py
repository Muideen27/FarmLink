#!/usr/bin/python3
"""
new view for Farmer object that handles all default RESTful API
"""
from models import storage
from models.farmer import Farmer


from flask import Flask, jsonify, abort, request
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views

@app_views.route('/farmers', methods=['GET'], strict_slashes=False)
def get_farmers():
    """retrieve a list all farmers"""
    all_farmers = []
    farmers = storage.all("Farmer").values()
    for farmer in farmers:
        all_farmers.append(farmer.to_dict())
    return jsonify(all_farmers)


@app_views.route('/farmers/<string:farmer_id>',
                methods=['GET'], strict_slashes=False)
def get_farmer(farmer_id):
    """retrieve a farmer"""
    all_farmers = []
    farmers = storage.all("Farmer").values()
    for farmer in farmers:
        all_farmers.append(farmer.to_dict())
    for farmer in all_farmers:
        if farmer.get("id") == farmer_id:
            return jsonify(farmer)
    abort(404)

@app_views.route('/farmers/<string:farmer_id>',
                methods=['DELETE'], strict_slashes=False)
def delete_farmer(farmer_id):
    """delete a farmer account"""
    farmers = storage.all("Farmer")
    try:
        key = "Farmer." + farmer_id
        storage.delete(farmers[key])
        storage.save()
        return jsonify({}), 200
    except BaseException:
        abort(404)

@app_views.route('/register_farmers', methods=['POST'], strict_slashes=False)
def post_farmers():
    """Create a Farmer"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    else:
        request_body = request.get_json()
    if 'email' not in request_body:
        abort(400, 'Missing email')
    if 'email' in request_body and 