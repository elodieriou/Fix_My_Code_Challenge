#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
