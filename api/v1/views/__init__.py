#!/usr/bin/python3
"""This module creates a Blueprint"""
from flask import Blueprint


app_views = Blueprint("app_views", __name__)
from api.v1.views.index import *
