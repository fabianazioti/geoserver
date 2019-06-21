import os
import re

import requests
from requests.auth import HTTPBasicAuth

class CoverageServices():
    
    @classmethod
    def get_base_url(cls, content_type='application/json'):
        headers = {
            "content-type": content_type
        }
        base_url = os.environ.get('URL_GEOSERVER', 'http://localhost:8081/geoserver')
        auth = HTTPBasicAuth(
            os.environ.get('USER_GEOSERVER', 'admin'),
            os.environ.get('PASSWORD_GEOSERVER', 'geoserver')
        )
        return '{}'.format(base_url), headers, auth


    @classmethod
    def get_coverages(cls, workspace):
        base_url, headers, auth = cls.get_base_url()
        base_url += '/rest/workspaces/{}/coveragestores.json'.format(workspace)
        r = requests.get(base_url, headers=headers, verify=False, auth=auth)
        if r and r.status_code in (200, 201):
            return r
        return None


    @classmethod
    def create_coveragestore(cls, workspace, datastore, layer, path):
        base_url, headers, auth = cls.get_base_url(content_type='text/plain')
        base_url += '/rest/workspaces/{}/coveragestores/{}/external.imagemosaic?configure=all&coverageName={}'.format(workspace, datastore, layer)
            
        r = requests.put(base_url, headers=headers, data=path, verify=False, auth=auth)
        if r and r.status_code in (200, 201):
            return r
        return None


    @classmethod
    def publish_layer(cls, workspace, datastore, layer, bodyXML):
        base_url, headers, auth = cls.get_base_url(content_type='text/xml')
        headers = dict(headers, **{"Content-Length": str(len(bodyXML))})

        base_url += '/rest/workspaces/{}/coveragestores/{}/coverages/{}'.format(workspace, datastore, layer)
        body = re.sub(r'/(\r\n\t|\n|\r\t)/gm', '', bodyXML)
            
        r = requests.put(base_url, headers=headers, data=body, verify=False, auth=auth)
        if r and r.status_code in (200, 201):
            return r
        return None


    @classmethod
    def unpublish(cls, workspace, layer):
        base_url, headers, auth = cls.get_base_url(content_type='text/xml')
        base_url += '/rest/layers/{}:{}.xml'.format(workspace, layer)

        r = requests.delete(base_url, headers=headers, verify=False, auth=auth)
        if r and r.status_code in (200, 201):
            return r
        return None


    @classmethod
    def remove(cls, workspace, coverage_store, layer):
        base_url, headers, auth = cls.get_base_url(content_type='text/plain')
        base_url += '/rest/workspaces/{}/coveragestores/{}?recurse=true'.format(workspace, coverage_store)

        r = requests.delete(base_url, headers=headers, verify=False, auth=auth)
        if r and r.status_code in (200, 201):
            return r
        return None