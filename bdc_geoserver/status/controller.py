from bdc_geoserver.status import ns
from bdc_geoserver.helpers import APIResource

api = ns

@api.route('/')
class StatusController(APIResource):
    
    def get(self):
        """
        Endpoint responsável por retornar o status da aplicação
        """
        return {
            "status": "Running",
            "success": True
        }
