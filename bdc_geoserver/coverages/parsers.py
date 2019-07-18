from datetime import datetime
from cerberus import Validator


def publish_raster():
    return {
        'workspace': {"type": "string", "empty": False, "required": True},
        'datastore': {"type": "string", "empty": False, "required": True},
        'layer': {"type": "string", "empty": False, "required": True},
        'path': {"type": "string", "empty": False, "required": True},
        'description': {"type": "string", "empty": True, "required": False},
        'projection': {"type": "string", "empty": False, "required": True}
    }


def validate(data, type_schema):
    schema = eval('{}()'.format(type_schema))

    v = Validator(schema)
    if not v.validate(data):
        return v.errors, False
    return data, True
