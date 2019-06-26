from flask import Blueprint
from flask_restplus import Api

from bdc_geoserver.coverages.controller import api as coverage_ns
from bdc_geoserver.status.controller import api as status_ns

blueprint = Blueprint('geoserver', __name__)

api = Api(blueprint, doc=False)

api.add_namespace(coverage_ns)
api.add_namespace(status_ns)