#!/usr/bin/python3
"""
new view for Farmer object that handles all default RESTful API
"""
from models import storage
from models.farmer import Farmer
import os
from flask import jsonify, abort, request, send_file, render_template, redirect, url_for, flash
from sqlalchemy.exc import IntegrityError
from api.v1.views import app_views
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user, login_required, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash


@app_views.route('/', strict_slashes=False)
def home():
    """
        Route for landing page
    """
    return render_template('home.html')

@app_views.route('/index', strict_slashes=False)
def home_index():
    """
	handles request to custom template with farmers
	"""
    products = list(storage.all("Product").values())
    return render_template('home1.html', products=products)

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

@app_views.route('/signup/', methods= ['GET'], strict_slashes=False)
def signup():
    return render_template('landingpage.html')

@app_views.route('/signup/', methods=['POST'], strict_slashes=False)
def post_farmers():
    """Create a Farmer"""
    username = request.form.get('username')
    hashed_password = request.form.get('hashed_password')
    email = request.form.get('email')
    location = request.form.get('location')
    contact_information = request.form.get('contact_information')
    class_name = 'Farmer'

    # Check if the email already exists for the Farmer class
    duplicate_email = storage.check_duplicate_email(email, class_name)

    if duplicate_email:
        flash('Email address already exists', 'error')
        return redirect(url_for('app_views.home_index', error=True))
        # return render_template('landingpage.html')

    farmer = None

    if hashed_password:
        farmer = Farmer(username=username, hashed_password=generate_password_hash(hashed_password),
                        email=email, location=location, contact_information=contact_information)
    else:
        error_message = 'Password must not be empty'
        return render_template('signup.html', error_message=error_message)

    # Save the farmer object to the database
    storage.new(farmer)
    storage.save()

    return redirect(url_for('app_views.login_get'))

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

@app_views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app_views.home_index'))

@app_views.route('/profile', methods=['GET'], strict_slashes=False)
@login_required
def profile():
    # Only authenticated users can access this route
    farmer_id = current_user.id
    farmer = storage.get(Farmer, farmer_id)
    if farmer is None:
        abort(404, 'Farmer not found')
    return render_template('product-form.html', farmer_id=farmer_id, name=current_user.username, farmer=farmer)

@app_views.route('/login', methods=['GET'], strict_slashes=False)
def login_get():
    return render_template('login1.html')

@app_views.route('/login', methods=['POST'], strict_slashes=False)
def login_post():
    if current_user.is_authenticated:
        return jsonify({'message': 'You are already logged in'})

    email = request.form.get('email')
    password = request.form.get('password')

    # Perform authentication here and retrieve the user object
    user = storage.authenticate_user(email, password, "Farmer")
    print(user)
    if user is None or (user.email != email and not check_password_hash(user.hashed_password, password)):
        flash('Please check your login details and try again.')
        return redirect(url_for('app_views.login_get'))
    login_user(user)
    return redirect(url_for('app_views.profile'))
    
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

