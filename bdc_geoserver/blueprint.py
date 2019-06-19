from flask import Blueprint
from flask_restplus import Api

from bdc_geoserver.coverages.controller import bdc_geoserver as coverage_ns

blueprint = Blueprint('geoserver', __name__)

bdc_geoserver = Api(blueprint, doc=False)

bdc_geoserver.add_namespace(coverage_ns)