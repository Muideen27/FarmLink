#!/usr/bin/python3
"""
new view for Farmer object that handles all default RESTful API
"""
from models import storage
from models.farmer import Farmer


from flask import Flask, jsonify, abort, request
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
        all_farmers.append()