import json
import os
import shutil
from pathlib import Path
from copy import deepcopy

from bdc_geoserver.coverages.services import CoverageServices
from bdc_geoserver.coverages.utils import generate_props_indexer
from bdc_geoserver.helpers import replaceList
from bdc_geoserver.base_sql import db

class CoverageBusiness():

    @classmethod
    def get_coverages(cls, workspace):
        coverages = CoverageServices.get_coverages(workspace).content
        return json.loads(coverages)

    @classmethod
    def publish(cls, data):
        datastore = replaceList(data['datastore'], ['.', '-', '_', '.', '~', '@', '!', '/'], '')
        layer = replaceList(data['layer'], ['.', '-', '_', '.', '~', '@', '!', '/'], '')

        ''' gerando arquivo indexer.properties '''
        generate_props_indexer(deepcopy(layer))

        '''
            Copiar arquivos listados (.properties) para dentro da pasta do mosaico
            -> indexer.properties
            -> datastore.properties
            -> timeregex.properties
        '''
        properties_path = Path('{}/properties_files/'.format(os.path.dirname(__file__)))
        datacube_path = Path('{}/{}/'.format(os.environ.get('PATH_CUBES_FILE'), layer))
        for filename in os.listdir(properties_path):
            shutil.copy2('{}/{}'.format(properties_path, filename), '{}/{}'.format(datacube_path, filename))

        ''' 
            Criando coverageStore
        '''
        path = '{}{}'.format(os.environ.get('PATH_BASE_GEOSERVER'), data['path'])
        result_create = CoverageServices.create_coveragestore(data['workspace'], datastore, layer, path)
        if not result_create:
            return False

        ''' 
            Publicando a coverage 
        '''
        bodyXML = "<coverage> \
            <name>{}</name> \
            <nativeName>{}</nativeName> \
            <title>{}</title> \
            <enabled>true</enabled> \
            <description>{}</description> \
            <srs>{}</srs> \
            <metadata> \
                <entry key=\"time\"> \
                <dimensionInfo> \
                    <enabled>true</enabled> \
                    <presentation>LIST</presentation> \
                    <units>ISO8601</units> \
                    <defaultValue> \
                        <strategy>MAXIMUM</strategy> \
                    </defaultValue> \
                </dimensionInfo> \
                </entry> \
            </metadata> \
        </coverage>".format(layer, layer, layer, data['description'], data['projection'].replace(" ", ""))

        result_publish = CoverageServices.publish_layer(data['workspace'], datastore, layer, bodyXML)
        if not result_publish:
            return False
        return True

    @classmethod
    def unpublish(cls, workspace, datastore, layer):
        ''' Despublicando e removendo uma coverage '''
        
        unpublish = CoverageServices.unpublish(workspace, layer)
        if not unpublish:
            raise Exception('Error unpublish layer')

        remove = CoverageServices.remove(workspace, datastore, layer)
        if not remove:
            raise Exception('Error remove layer')
        
        ''' Removendo arquivos de configuração '''
        datacube_path = Path('{}/{}/'.format(os.environ.get('PATH_CUBES_FILE'), layer))
        for filename in os.listdir(datacube_path):
            if filename.find('.properties') > 0 or filename.find('.dat') > 0:
                os.remove('{}/{}'.format(datacube_path, filename))

        ''' Excluindo tabela do banco - gerado pelo geoserver '''
        db.engine.execute('DROP TABLE IF EXISTS "{}{}"'.format(layer, os.environ.get('SUFFIX_NAME_CUBE', '_MEDIAN')))
        return True