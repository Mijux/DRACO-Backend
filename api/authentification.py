#!/usr/sbin/env python3

from flask import Blueprint

"""
This module manage authentification api
"""

authentification = Blueprint("authentification", __name__)


@authentification.route("/login")
def login():
    pass


def logout():
    pass
