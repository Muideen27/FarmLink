#!/usr/bin/python3
"""file that contains error handler and others"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from models.farmer import Farmer
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import os
from flask_wtf import CSRFProtect



app = Flask(__name__, static_folder='static')
csrf = CSRFProtect(app)
app.register_blueprint(app_views, url_prefix='/api/v1')

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

if __name__ == "__main__":
    host = os.environ.get("FARMLINK_API_HOST", "0.0.0.0")
    port = int(os.environ.get("FARMLINK_API_PORT", 5000))

    app.run(host=host, port=port, threaded=True)
