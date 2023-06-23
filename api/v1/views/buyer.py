#!/usr/bin/python3
"""
new view for Farmer object that handles all default RESTful API
"""
from models import storage
from models.buyer import Buyer


from flask import Flask, jsonify, abort, request
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views

@app_views.route('/buyers', methods=['GET'], strict_slashes=False)
def get_buyers():
    """retrieve a list all farmers"""
    all_buyer = []
    buyers = storage.all("Buyer").values()
    for buyer in buyers:
        all_buyer.append(buyer.to_dict())
    return jsonify(all_buyer), 200


@app_views.route('/buyer/<string:buyer_id>',
                methods=['GET'], strict_slashes=False)
def get_buyer(buyer_id):
    """retrieve a farmer"""
    all_buyers = []
    buyers = storage.all("Buyer").values()
    for buyer in buyers:
        all_buyers.append(buyer.to_dict())
    for buyer in all_buyers:
        if buyer.get("id") == buyer_id:
            return jsonify(buyer)
    abort(404)

@app_views.route('/buyers/<string:buyer_id>',
                methods=['DELETE'], strict_slashes=False)
def delete_buyer(buyer_id):
    """delete a buyer account"""
    buyers = storage.all("Buyer")
    try:
        key = "Buyer." + buyer_id
        storage.delete(buyers[key])
        storage.save()
        return jsonify({}), 200
    except BaseException:
        abort(404)

@app_views.route('/buyers/', methods=['POST'], strict_slashes=False)
def post_buyer():
    """Create a buyer"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    else:
        request_body = request.get_json()
    if 'email' not in request_body:
        abort(400, 'Missing email')
    elif 'password' not in request_body:
        abort(400, 'Missing password')
    else:
        email = request_body['email']
        password = request_body['password']
        class_name = 'Buyer'  

        # Check if the email already exists for the Buyer class
        duplicate_email = storage.check_duplicate_email(email, class_name)

        if duplicate_email:
            abort(400, 'Email address already exists')

        # Create a new Buyer object
        buyer = Buyer(email=email, password=password)

        # Set other attributes of the farmer object based on request_body
        if 'username' in request_body:
            buyer.username = request_body['username']
        if 'location' in request_body:
            buyer.location = request_body['location']
        if 'contact_information' in request_body:
            buyer.contact_information = request_body['contact_information']

        # Save the farmer object to the database
        storage.new(buyer)
        storage.save()

        return jsonify(buyer.to_dict()), 201

@app_views.route('/buyers/<string:buyer_id>/',
                methods=['PUT'], strict_slashes=False)
def put_buyer(buyer_id):
    """Updates the farmer account"""
    buyers = storage.all(Buyer)
    key = 'Buyer.' + buyer_id
    try:
        buyer = buyers[key]
    except BaseException:
        abort(404)
    if request.is_json:
        request_body = request.get_json()
    else:
        abort(400, 'Not a JSON')
    for key, value in request_body.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(buyer, key, value)
    storage.save()
    return jsonify(buyer.to_dict()), 200