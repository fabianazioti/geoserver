import os
from flask import request
from flask_restplus import Resource, marshal

from bdc_geoserver.coverages import ns
from bdc_geoserver.coverages.business import CoverageBusiness
from bdc_geoserver.coverages.parsers import validate
from bdc_geoserver.coverages.utils import return_response

bdc_geoserver = ns

@bdc_geoserver.route('/<workspace>')
@bdc_geoserver.route('/<workspace>/<coveragestore>/<coverage>')
class CoverageController(Resource):

    def get(self, workspace, coveragestore=None, coverage=None):
        try:
            """
            Endpoint responsável listar as coverage store de um workspace
            """
            layers = CoverageBusiness.get_coverages(workspace)

            return return_response({
                "success": True,
                "coverages": layers['coverages']
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
            

@bdc_geoserver.route('/')
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
