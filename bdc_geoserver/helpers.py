import locale
import os

from pathlib import Path
from flask import Response, json, request
from flask_restplus import Resource, utils
from functools import wraps
from werkzeug.exceptions import HTTPException
from contextlib import contextmanager

@contextmanager
def setlocale():
    saved = locale.setlocale(locale.LC_ALL)
    try:
        yield locale.setlocale(locale.LC_ALL, os.environ.get('LC_ALL', 'pt_BR.UTF-8'))
    finally:
        locale.setlocale(locale.LC_ALL, saved)


def return_response(data, status_code, dumps=True):
    data = json.dumps(data) if dumps else data
    return Response(data, status_code, content_type='application/json')


def replaceList(my_string, list_strs, new_value):
    for s in list_strs:
        my_string = my_string.replace(s, new_value)
    return my_string

class APIResource(Resource):
    """
    API Resource for Brazil Data Cube Modules (bdc)
    It aims to override `dispatch_request` member in order to
    handle status_code and error message through exception contexts.
    The exceptions must inherit from @APIError.
    
    """
    def dispatch_request(self, *args, **kwargs):
        try:
            return super().dispatch_request(*args, **kwargs)
        except HTTPException as e:
            return return_response({
                "code": e.code,
                "message": e.description
            }, e.code)
