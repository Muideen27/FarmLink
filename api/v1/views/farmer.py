#!/usr/bin/python3
"""
new view for Farmer object that handles all default RESTful API
"""
from models import storage
from models.farmer import Farmer
import os
from flask import Flask, jsonify, abort, request, send_file, session
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user, login_required, logout_user


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

@app_views.route('/farmers/<string:farmer_id>/image', 
                 methods=['GET'], strict_slashes=False)
def get_farmer_image(farmer_id):
    """Retrieves the image for the farmer"""
    farmers = storage.all(Farmer)
    key = 'Farmer.' + farmer_id
    try:
        farmer = farmers[key]
    except BaseException:
        abort(404)

    # Construct the file path for the farmer's image
    filepath = '/home/bucha/FarmLink/image/' + farmer_id + '.jpg'

    # Check if the file exists
    if not os.path.exists(filepath):
        filepath = '/home/bucha/FarmLink/image/default1.png'

    # Retrieve the image file
    return send_file(filepath, mimetype='image/jpeg')

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

@app_views.route('/farmers/<string:farmer_id>/image', 
                 methods=['DELETE'], strict_slashes=False)
def delete_image(farmer_id):
    """Delete the farmer's image"""
    farmers = storage.all('Farmer')
    key = "Farmer." + farmer_id
    try:
        farmer = farmers[key]
    except BaseException:
        abort(404)

    image_path = os.path.join(os.path.expanduser('~/FarmLink/image/'), farmer_id + '.jpg')
    default_image_path = '/home/bucha/FarmLink/image/default1.png'

    if image_path == default_image_path:
        abort(400, "Cannot delete the default image")

    if os.path.exists(image_path):
        os.remove(image_path)

    # Check if the farmer has any other images
    has_other_images = any(
        os.path.exists(os.path.join(os.path.expanduser('~/FarmLink/image/'), f'{id}.jpg'))
        for id in farmers.keys() if id != key
    )

    # If the farmer doesn't have any other images, assign the default image
    if not has_other_images and not os.path.exists(image_path):
        if not os.path.exists(default_image_path):
            os.rename(default_image_path, image_path)

    return jsonify({'message': 'Image deleted successfully'}), 200

@app_views.route('/farmers/', methods=['POST'], strict_slashes=False)
def post_farmers():
    """Create a Farmer"""
    if not request.is_json:
        abort(400, 'Not a JSON')
    else:
        request_body = request.get_json()
    if 'email' not in request_body:
        abort(400, 'Missing email')
    elif 'hashed_password' not in request_body:
        abort(400, 'Missing password')
    else:
        email = request_body['email']
        hashed_password = request_body['hashed_password']
        class_name = 'Farmer'

        # Check if the email already exists for the Farmer class
        duplicate_email = storage.check_duplicate_email(email, class_name)

        if duplicate_email:
            abort(400, 'Email address already exists')

        # Set other attributes of the farmer object based on request_body
        username = request_body.get('username', '')
        location = request_body.get('location', '')
        contact_information = request_body.get('contact_information', '')

        if hashed_password:
            farmer = Farmer(username=username, hashed_password=hashed_password,
                    email=email, location=location, contact_information=contact_information)
        else:
        # Handle the case when the password is empty
            abort(400, 'Password must be non-empty')

        # Save the farmer object to the database
        storage.new(farmer)
        storage.save()

        # return jsonify(farmer.to_dict(exclude=['products', 'review'])), 201
        return jsonify({'message': 'Created successfully'}), 201

@app_views.route('/farmers/<string:farmer_id>/upload-image', 
                 methods=['POST'], strict_slashes=False)
def upload_farmer_image(farmer_id):
    """Uploads an image for the farmer"""
    farmers = storage.all(Farmer)
    key = 'Farmer.' + farmer_id
    try:
        farmer = farmers[key]
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
    filename = secure_filename(farmer_id + '.jpg')
    filepath = os.path.join(os.path.expanduser('~/FarmLink/image/'), filename)
    
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


@app_views.route('/protected', methods=['GET'], strict_slashes=False)
@login_required
def protected_route():
    # Only authenticated users can access this route
    return jsonify({'message': 'You are authenticated'})

@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login():
    if current_user.is_authenticated:
        return jsonify({'message': 'You are already logged in'})

    email = request.form.get('email')
    password = request.form.get('password')

    # Perform authentication here and retrieve the user object
    user = storage.authenticate_user(email, password, "Farmer")

    if user:
        if login_user(user):
            return jsonify({'message': 'Login successful'})
        else:
            return jsonify({'message': 'Failed to login'})
    return jsonify({'message': 'Invalid Email or password'})

@app_views.route('/farmers/<string:farmer_id>/',
                methods=['PUT'], strict_slashes=False)
def put_farmer(farmer_id):
    """Updates the farmer account"""
    farmers = storage.all(Farmer)
    key = 'Farmer.' + farmer_id
    try:
        farmer = farmers[key]
    except BaseException:
        abort(404)
    if request.is_json:
        request_body = request.get_json()
    else:
        abort(400, 'Not a JSON')
    for key, value in request_body.items():
        if key != 'id' and key != 'created_at' and key != 'updated_at':
            setattr(farmer, key, value)
    storage.save()
    return jsonify(farmer.to_dict()), 200

