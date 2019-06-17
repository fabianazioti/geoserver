import os
from flask import request
from flask_restplus import Resource, marshal

from bdc_geoserver.coverages import ns
from bdc_geoserver.coverages.business import GeoserverBusiness
from bdc_geoserver.coverages.parsers import validate
from bdc_geoserver.coverages.utils import return_response

bdc_geoserver = ns

@bdc_geoserver.route('/<workspace>/<datastore>')
@bdc_geoserver.route('/<workspace>/<datastore>/<layer>')
class CoverageController(Resource):

    def get(self, workspace, datastore, layer=None):
        try:
            """
            Endpoint responsável listar as layers de um workspace
            """
            layers = CoverageBusiness.get_coverages(workspace, datastore)

            return return_response({
                "success": True,
                "coverages": layers['coverages']
            }, 200)

        except Exception as e:
            return return_response({
                "success": False,
                "message": str(e)
            }, 500)
    
    def delete(self, workspace, datastore, layer):
        try:
            """
            Endpoint responsável despublicar um layer
            """
            status = CoverageBusiness.unpublish(workspace, datastore, layer)
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
            

@bdc_geoserver.route('/coverage')
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
            }, 200)

        except Exception as e:
            return return_response({
                "success": False,
                "message": str(e)
            }, 500)
