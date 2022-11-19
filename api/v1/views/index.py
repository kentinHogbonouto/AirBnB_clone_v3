#!/usr/bin/python3
"""This module is a blueprint"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def status():
        return jsonify({'status': 'OK'})

@app_views.route("/stats", strict_slashes=False)
def stats():
        return jsonify({
                "amenities": storage.count("Amenity"),
                "places": storage.count("Place"),
                "reviews": storage.count("Review"),
                "states": storage.count("state"),
                "users": storage.count("User")
        })
