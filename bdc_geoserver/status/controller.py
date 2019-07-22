from bdc_core.utils.flask import APIResource
from bdc_geoserver.status import ns

api = ns


@api.route('/')
class StatusController(APIResource):

    def get(self):
        """
        Returns application status
        """
        return {
            "status": "Running"
        }
