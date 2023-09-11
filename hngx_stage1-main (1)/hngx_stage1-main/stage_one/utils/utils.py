import datetime
import json
import logging
import os
import traceback
from flask import jsonify, redirect, url_for, make_response
from stage_one.utils.constants import _Const

cache_constants = _Const()


class Responses:
    @staticmethod
    def error_response(*, message, status_code):
        if not isinstance(message, dict):
            message = str(message)
        return jsonify(message=message, status='error'), status_code

    @staticmethod
    def custom_response(**data):
        response = {
            "status": "success",
            "message": message,
            "data": data,
        }
        return make_response(response, status_code)

    @staticmethod
    def resource_not_found(err):
        return Responses.error_response(message=err, status_code=404)

    @staticmethod
    def internal_server_error(e):
        logging.critical(
            f"\n{'='*30} SERVER ERROR {datetime.datetime.now()} {'='*30}\n\n {traceback.format_exc()}\n{'='*24} END SERVER ERROR {'='*24}\n",
        )
        return Responses.error_response(
            message="Internal server error.", status_code=500)
