import unittest, os
from json import loads as json_loads

from bdc_geoserver import app as geoserver_app
from bdc_geoserver.config import get_settings


class TestListCoverage(unittest.TestCase):
    def setUp(self):
        app = geoserver_app.test_client()
        self.response = app.get('/geoserver/status')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_response_format(self):
        self.assertEqual(self.response.content_type, 'application/json')