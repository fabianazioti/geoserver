import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from bdc_geoserver.base_sql import db
from bdc_geoserver.blueprint import blueprint
from bdc_geoserver.config import get_settings
from bdc_geoserver.coverages.utils import generate_props_datastore

flask_bcrypt = Bcrypt()

def create_app(config):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config)
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.register_blueprint(blueprint)

        # DB
        db.init_app(app)
        db.app = app

        # generate infos to connect database by os.environ
        generate_props_datastore()

        flask_bcrypt.init_app(app)
        
    return app, db

app, db = create_app(get_settings(os.environ.get('ENVIRONMENT', 'DevelopmentConfig')))

CORS(app, resorces={r'/d/*': {"origins": '*'}})