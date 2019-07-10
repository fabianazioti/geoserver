import os
from flask import request
from flask_restplus import marshal

from bdc_geoserver.coverages import ns
from bdc_geoserver.coverages.business import CoverageBusiness
from bdc_geoserver.coverages.parsers import validate
from bdc_core.utils.flask import APIResource

api = ns

@api.route('/<workspace>')
@api.route('/<workspace>/<coveragestore>/<coverage>')
class CoverageController(APIResource):

    def get(self, workspace, coveragestore=None, coverage=None):
        """
        List of coverages store for a workspace in geoserver
        """
        layers = CoverageBusiness.get_coverages(workspace)
        coverages = layers['coverageStores']['coverageStore'] if type(layers['coverageStores']) != str else []
        
        return {
            "success": True,
            "coverageStore": coverages
        }
    
    def delete(self, workspace, coveragestore, coverage):
        """
        Unpublish a layer/coverage in geoserver
        """
        status = CoverageBusiness.unpublish(workspace, coveragestore, coverage)
        if not status:
            raise Exception('Error unpublish mosaic!')

        return {
            "success": True,
            "message": "Mosaic unpublish!"
        }
            

@api.route('/')
class CoveragesController(APIResource):

    def post(self):
        """
        Publish a layer/image_mosaic in geoserver
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