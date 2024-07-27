#!/usr/bin/env python3

from functools import wraps
from flask import request, current_app, jsonify
from jwt import decode as jwt_decode

from os import getenv


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
        if not token:
            return (
                jsonify(
                    {
                        "message": "Authentication Token is missing!",
                        "data": None,
                        "error": "Unauthorized",
                    }
                ),
                401,
            )

        try:
            data = jwt_decode(
                token,
                getenv("SECRET_KEY"),
                algorithms=["HS256"],
                verify_signature=True,
            )
            current_user = "A"
            # current_user = models.User().get_by_id(data["user_id"])
            # if current_user is None:
            #     return {
            #         "message": "Invalid Authentication token!",
            #         "data": None,
            #         "error": "Unauthorized",
            #     }, 401
            # if not current_user["active"]:
            #     abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e),
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated
