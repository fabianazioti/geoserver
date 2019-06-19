import locale
import os

from pathlib import Path
from flask import Response, json
from contextlib import contextmanager

@contextmanager
def setlocale():
    saved = locale.setlocale(locale.LC_ALL)
    try:
        yield locale.setlocale(locale.LC_ALL, os.environ.get('LC_ALL', 'pt_BR.UTF-8'))
    finally:
        locale.setlocale(locale.LC_ALL, saved)


def return_response(data, status_code, dumps=True):
    data = json.dumps(data) if dumps else data
    return Response(data, status_code, content_type='application/json')


def replaceList(my_string, list_strs, new_value):
    for s in list_strs:
        my_string = my_string.replace(s, new_value)
    return my_string

def generate_props_datastore():
    '''
        Gerando arquivo datastore.properties com as informações de conexão com o banco
        -> gerar arquivo e salvar em /bdc_geoserver/coverages/properties_files
    '''
    properties_path = Path('{}/properties_files/'.format(os.path.dirname(__file__)))
    f = open('{}/datastore.properties'.format(properties_path), 'w+')

    content_datastore_properties = '''SPI=org.geotools.data.postgis.PostgisNGDataStoreFactory 
host={} 
port={} 
database={}  
schema=public 
user={} 
passwd={} 
Loose\ bbox=true 
Estimated\ extends=false 
validate\ connections=true  
Connection\ timeout=10 
preparedStatements=true 
    '''.format(
            os.environ.get('POSTGRES_HOST'), os.environ.get('POSTGRES_PORT'), os.environ.get('POSTGRES_DATABASE'),
            os.environ.get('POSTGRES_USER'), os.environ.get('POSTGRES_PASSWORD'))
    f.write(content_datastore_properties)
    f.close()
