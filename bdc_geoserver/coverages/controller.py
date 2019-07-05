import os
from flask import request
from flask_restplus import marshal

from bdc_geoserver.coverages import ns
from bdc_geoserver.coverages.business import CoverageBusiness
from bdc_geoserver.coverages.parsers import validate
from bdc_geoserver.helpers import APIResource

api = ns

@api.route('/<workspace>')
@api.route('/<workspace>/<coveragestore>/<coverage>')
class CoverageController(APIResource):

    def get(self, workspace, coveragestore=None, coverage=None):
        """
        Endpoint responsável listar as coverage store de um workspace
        """
        layers = CoverageBusiness.get_coverages(workspace)
        coverages = layers['coverageStores']['coverageStore'] if type(layers['coverageStores']) != str else []
        
        return {
            "success": True,
            "coverageStore": coverages
        }
    
    def delete(self, workspace, coveragestore, coverage):
        """
        Endpoint responsável despublicar um layer
        """
        status = CoverageBusiness.unpublish(workspace, coveragestore, coverage)
        if not status:
            raise Exception('Error unpublish mosaic!')

        return {
            "success": True,
            "message": "Mosaic unpublish!"
        }
            

@api.route('/')
class CoverageController(APIResource):

    def post(self):
        """
        Endpoint responsável publicar um mosaico (rasters)
        """
        data, status = validate(request.json, 'publish_raster')
        if status is False:
            return return_response(data, 400)

        status = CoverageBusiness.publish(data)
        if not status:
            raise Exception('Error publishing mosaic!')

        return {
            "success": True,
            "message": "Mosaic published!"
        }