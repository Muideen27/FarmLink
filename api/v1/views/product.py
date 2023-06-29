#!/usr/bin/python3
"""
new view for product objects that handles all default RESTful api actions
"""
from models import storage
from models.farmer import Farmer
from models.product import Product
from flask import jsonify, abort, request
from api.v1.views import app_views

@app_views.route('/farmers/<string:farmer_id>/products',
                 methods=['GET'], strict_slashes=False)
def get_products(farmer_id):
    """
    retrieve the list of product objects that is associated with a particular farmer
    """
    farmer = storage.get(Farmer, farmer_id)
    if farmer is None:
        abort(404)
    all_products = []
    for product in farmer.products:
        all_products.append(product.to_dict())
    return jsonify(all_products)

@app_views.route('/products/<string:product_id>/',
                methods =['GET'], strict_slashes=False)
def get_product(product_id):
    """
    retrieve the product object based on the id
    """
    product = storage.get(Product, product_id)
    if product is None:
        abort(404)
    else:
        return jsonify(product.to_dict())
    
@app_views.route('/products/<string:product_id>',
                    methods=['DELETE'], strict_slashes=False)
def delete_product(product_id):
    """deletes a product"""
    products = storage.all("Product")
    try:
        key = "Product." + product_id
        storage.delete(products[key])
        storage.save()
        return jsonify({}), 200
    except BaseException:
        abort(404)

@app_views.route('/farmers/<string:farmer_id>/products/',
                 methods=['POST'], strict_slashes=False)
def post_product(farmer_id):
    """creates a product"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    else:
        request_body = request.get_json()

    if 'name' not in request_body:
        abort(400, 'Missing name')
    if 'price' not in request_body:
        abort(400, 'Missing price')
    
    name = request_body['name']
    price = request_body['price']
    # Increment number based on name
    number = storage.get_number_by_name(farmer_id, name)
    if number is None:
        number = 1
    else:
        number += 1
    request_body.update({"farmer_id": farmer_id})
    
    product = Product(**request_body)
    
    if 'description' in request_body:
        product.description = request_body['description']
    if 'location' in request_body:
        product.location = request_body['location']
    if 'quantity' in request_body:
        product.quantity = request_body['quantity']
    if 'availability_status' in request_body:
        product.availability_status = request_body['availability_status']

    
    # Print the number based on the name
    print(f"Number for product {name}: {number}")
    # Save the product
    storage.new(product)
    storage.save()

    # Return a response indicating success
    return jsonify(message="Product created successfully"), 201

