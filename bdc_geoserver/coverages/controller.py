import os
from flask import request
from flask_restplus import Resource, marshal

from bdc_geoserver.coverages import ns
from bdc_geoserver.coverages.business import CoverageBusiness
from bdc_geoserver.coverages.parsers import validate
from bdc_geoserver.utils.helpers import return_response

api = ns

@api.route('/<workspace>')
@api.route('/<workspace>/<coveragestore>/<coverage>')
class CoverageController(Resource):

    def get(self, workspace, coveragestore=None, coverage=None):
        try:
            """
            Endpoint responsável listar as coverage store de um workspace
            """
            layers = CoverageBusiness.get_coverages(workspace)
            coverages = layers['coverageStores']['coverageStore'] if type(layers['coverageStores']) != str else []
            
            return return_response({
                "success": True,
                "coverageStore": coverages
            }, 200)

        except Exception as e:
            return return_response({
                "success": False,
                "message": str(e)
            }, 500)
    
    def delete(self, workspace, coveragestore, coverage):
        try:
            """
            Endpoint responsável despublicar um layer
            """
            status = CoverageBusiness.unpublish(workspace, coveragestore, coverage)
            if not status:
                raise Exception('Error unpublish mosaic!')

            return return_response({
                "success": True,
                "message": "Mosaic unpublish!"
            }, 200)

        except Exception as e:
            return return_response({
                "success": False,
                "message": str(e)
            }, 500)
            

@api.route('/')
class CoverageController(Resource):

    def post(self):
        try:
            """
            Endpoint responsável publicar um mosaico (rasters)
            """
            data, status = validate(request.json, 'publish_raster')
            if status is False:
                return return_response(data, 400)

            status = CoverageBusiness.publish(data)
            if not status:
                raise Exception('Error publishing mosaic!')

            return return_response({
                "success": True,
                "message": "Mosaic published!"
            }, 201)

        except Exception as e:
            return return_response({
                "success": False,
                "message": str(e)
            }, 500)
