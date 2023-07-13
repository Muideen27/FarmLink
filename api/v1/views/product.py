#!/usr/bin/python3
"""
new view for product objects that handles all default RESTful api actions
"""
from models import storage
from models.farmer import Farmer
from models.product import Product
from flask import jsonify, abort, request, url_for, render_template
from api.v1.views import app_views
from werkzeug.utils import secure_filename
import os


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

@app_views.route('/products/<string:product_id>/image', 
                 methods=['DELETE'], strict_slashes=False)
def delete_product_image(product_id):
    """Delete the farmer's image"""
    products = storage.all('Product')
    key = "Product." + product_id
    try:
        product = products[key]
    except BaseException:
        abort(404)

    image_path = os.path.join(os.path.expanduser('~/FarmLink/image1/'), product_id + '.jpg')
    default_image_path = '/home/bucha/FarmLink/image1/default1.png'

    if image_path == default_image_path:
        abort(400, "Cannot delete the default image")

    if os.path.exists(image_path):
        os.remove(image_path)

    # Check if the farmer has any other images
    has_other_images = any(
        os.path.exists(os.path.join(os.path.expanduser('~/FarmLink/image1/'), f'{id}.jpg'))
        for id in products.keys() if id != key
    )

    # If the farmer doesn't have any other images, assign the default image
    if not has_other_images and not os.path.exists(image_path):
        if not os.path.exists(default_image_path):
            os.rename(default_image_path, image_path)

    return jsonify({'message': 'Image deleted successfully'}), 200

@app_views.route('/products/<string:product_id>/upload-image', 
                 methods=['POST'], strict_slashes=False)
def upload_product_image(product_id):
    """Uploads an image for the farmer"""
    products = storage.all(Farmer)
    key = 'Product.' + product_id
    try:
        product = products[key]
    except BaseException:
        abort(404)
     # Check if an image file is included in the request
    if 'image' not in request.files:
        abort(400, 'No image file provided')

    image_file = request.files['image']

    # Check if the file has an allowed extension
    allowed_extensions = ['jpg', 'jpeg', 'png']
    if not allowed_file(image_file.filename, allowed_extensions):
        abort(400, 'Invalid file type. Allowed file types are: JPG, JPEG, PNG')

    # Check if the file size is within the allowed limit (e.g., 5MB)
    max_file_size = 5 * 1024 * 1024  # 5MB
    if image_file.content_length > max_file_size:
        abort(400, 'File size exceeds the limit')
    
     # Generate a secure filename and save the file
    filename = secure_filename(product_id + '.jpg')
    filepath = os.path.join(os.path.expanduser('~/FarmLink/image1/'), filename)
    
    # Delete the existing image file if it exists
    if os.path.exists(filepath):
        os.remove(filepath)
    # Save the new image file
    image_file.save(filepath)
    
    return jsonify({'message': 'Image uploaded successfully'}), 200

def allowed_file(filename, allowed_extensions):
    """Check if the file has an allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in allowed_extensions



# @app_views.route('/farmers/<string:farmer_id>/products/', methods=['POST'], strict_slashes=False)
# def post_product(farmer_id):
#     """creates a product"""
#     request_body = request.form

#     if 'name' not in request_body:
#         abort(400, 'Missing name')
#     if 'price' not in request_body:
#         abort(400, 'Missing price')

#     name = request_body['name']
#     price = request_body['price']
#     # Increment number based on name
#     number = storage.get_number_by_name(farmer_id, name)
#     if number is None:
#         number = 1
#     else:
#         number += 1
#     request_body = request.form.to_dict(flat=False)
#     request_body.update({"farmer_id": farmer_id})

#     product = Product(**request_body)

#     if 'description' in request_body:
#         product.description = request_body['description']
#     if 'location' in request_body:
#         product.location = request_body['location']
#     if 'quantity' in request_body:
#         product.quantity = request_body['quantity']
#     if 'availability_status' in request_body:
#         product.availability_status = request_body['availability_status']

#     # Print the number based on the name
#     print(f"Number for product {name}: {number}")
#     # Save the product
#     storage.new(product)
#     storage.save()

#     # Return a response indicating success
#     return jsonify(message="Product created successfully"), 201


# @app_views.route('/farmers/<string:farmer_id>/products/', methods=['POST'], strict_slashes=False)
# def post_product(farmer_id):
#     """creates a product"""
#     name = request.form['name']
#     description = request.form['description']
#     location = request.form['location']
#     price = request.form['price']
#     availability = request.form['availability']
#     image_file = request.files['image']

#     # Save the image file
#     if image_file:
#         # Generate a unique filename
#         filename = secure_filename(image_file.filename)
#         filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         image_file.save(filepath)

#         # Create the product and set the image field
#         product = Product(
#             name=name,
#             description=description,
#             location=location,
#             price=price,
#             availability=availability,
#             image=url_for('uploaded_file', filename=filename)  # Save the image URL
#         )
#     storage.new(product)
#     storage.save()

#     return render_template('home1.html')

