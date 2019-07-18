"""
Brazil Data Cube package
"""

import os
from flask import Flask
from flask_cors import CORS

from bdc_geoserver.base_sql import db
from bdc_geoserver.blueprint import blueprint
from bdc_geoserver.config import get_settings
from bdc_geoserver.coverages.utils import generate_props_datastore


def create_app(config):
    internal_app = Flask(__name__)

    with internal_app.app_context():
        internal_app.config.from_object(config)
        internal_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        internal_app.register_blueprint(blueprint)

        # DB
        db.init_app(internal_app)
        db.app = internal_app

        # generate infos to connect database by os.environ
        generate_props_datastore()

    return internal_app, db


app, db = create_app(get_settings(os.environ.get('ENVIRONMENT',
                                                 'DevelopmentConfig')))

CORS(app, resorces={r'/d/*': {"origins": '*'}})
