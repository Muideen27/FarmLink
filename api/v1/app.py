#!/usr/bin/python3
"""file that contains error handler and others"""
from flask import Flask, jsonify, request, url_for, current_app, render_template, send_from_directory
from models import storage
from api.v1.views import app_views
from models.farmer import Farmer
from models.product import Product
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
from flask_wtf import CSRFProtect
from werkzeug.utils import secure_filename
import logging


app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)
app.register_blueprint(app_views, url_prefix='/api/v1')
app.config['UPLOAD_FOLDER'] = '/home/bucha/FarmLink/image1'


secret_key = os.urandom(24)
app.secret_key = secret_key

app.debug = True

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'app_views.login_post'


@app.errorhandler(404)
def handle_404(error):
    """custom JSON 404 error"""

    return jsonify({"error": "Not found"}), 404

# print("Farmer ID:", farmer_id)

@login_manager.user_loader
def load_user(farmer_id):
    farmer = storage.get(Farmer, farmer_id)
    return farmer


@app.teardown_appcontext
def teardown_appcontext(exception=None):
    """
        Teardown method for storage session
    """
    storage.close()

logging.basicConfig(level=logging.DEBUG)

@app.route('/uploaded-file/<filename>')
def uploaded_file(filename):
    """Endpoint for serving uploaded files"""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/farmers/<string:farmer_id>/products/', methods=['POST'], strict_slashes=False)
def post_product(farmer_id):
    """creates a product"""
    name = request.form['name']
    description = request.form['description']
    location = request.form['location']
    price = float(request.form['price'])
    availability = request.form['availability']
    image_file = request.files['image']

    # Save the image file
    if image_file:
        # Generate a unique filename
        filename = secure_filename(image_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(filepath)

        logging.debug(f"name: {name}")
        logging.debug(f"description: {description}")
        logging.debug(f"location: {location}")
        logging.debug(f"price: {price}")
        logging.debug(f"availability: {availability}")
        logging.debug(f"filepath: {filepath}")


        # Create the product and set the image field
        product = Product(
            name=name,
            description=description,
            location=location,
            price=price,
            availability_status=availability,
            image=url_for('uploaded_file', filename=filename)  # Save the image URL
        )
    storage.new(product)
    storage.save()

    return render_template('home1.html')



if __name__ == "__main__":
    host = os.environ.get("FARMLINK_API_HOST", "0.0.0.0")
    port = int(os.environ.get("FARMLINK_API_PORT", 5000))

    app.run(host=host, port=port, threaded=True)
