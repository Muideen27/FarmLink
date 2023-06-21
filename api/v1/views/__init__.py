#!/usr/bin/python3
"""
this module creates app_views which is an instance of Blueprint
"""
from flask import Blueprint


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.farmer import *
"""
from api.v1.views.buyer import *
from api.v1.views.product import *
from api.v1.views.order import *
from api.v1.views.review import *
"""
