#!/usr/bin/python3
"""
new view for product objects that handles all default RESTful api actions
"""
from models import storage
from models.farmer import Farmer
from models.product import Product
from flask import Flask, jsonify, abort, request
from api.v1.views import app_views

@app_views.route('/farmers/<string:farmer_id>/products',
                 methods=['GET'], strict_slashes=False)
def get_product(farmer_id):
    """
    retrieve the list of product objects that is associated with a particular farmer
    """
    farmer = storage.get("Farmer", farmer_id)
    if farmer is None:
        abort(404)
    all_products = []
    for product in farmer.products:
        all_products.append(product.to_dict())
    return jsonify(all_products)

@pp_views.route('/products/<string:product_id>/',
                methods =['GET'], strict_slashes=False)
def get_product(product_id):
    """
    retrieve the product object based on the id
    """
    product = storage.get("Product", product_id)
    if product is None:
        abort(404)
    else:
        return jsonify(product.to_dict())


    
