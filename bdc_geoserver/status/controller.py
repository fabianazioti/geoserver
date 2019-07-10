from bdc_geoserver.status import ns
from bdc_core.utils.flask import APIResource

api = ns

@api.route('/')
class StatusController(APIResource):
    
    def get(self):
        """
        Returns application status
        """
        return {
            "status": "Running",
            "success": True
        }
