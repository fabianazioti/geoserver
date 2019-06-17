import jwt
import json
from copy import deepcopy

from bdc_geoserver.coverages.services import CoverageServices
from bdc_geoserver.coverages.utils import replaceList

class CoverageBusiness():

    @classmethod
    def get_coverages(cls, workspace, datastore):
        layers = CoverageServices.get_coverages(workspace, datastore).content
        return json.loads(layers)

    @classmethod
    def publish(cls, data):
        datastore = replaceList(data['datastore'], ['.', '-', '_', '.', '~', '@', '!', '/'], '')
        layer = replaceList(data['layer'], ['.', '-', '_', '.', '~', '@', '!', '/'], '')    

        '''
            1) Criando tabela do mosaico no banco
            -> fid serial primary key,
            -> the_geom geometry(Type, Proj) not null,
            -> location varchar(255) not null, (path file)
            -> timestamp timestamp

            2) Criando indice espacial
            -> create index spatial_index_name on table using gist(the_geom);
        '''
        # TODO:       

        '''
            Inserindo as informações das features na tabela criada acima
            -> varre os arquivos, pegando (PATH, GEOMETRY, DATE)
        '''
        # TODO:

        '''
            Criar os arquivos de configurações para leitura do geoserver
            -> layer.properties
            -> datastore.properties
        '''
        # TODO:

        ''' 
            Criando coverageStore
        '''
        path = 'file://{}'.format(data['path'])
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
        
        try:
            unpublish = CoverageServices.unpublish(workspace, layer)
            if not unpublish:
                raise Exception('Error unpublish layer')
        except Exception as e:
            pass

        remove = CoverageServices.remove(workspace, datastore, layer)
        if not remove:
            raise Exception('Error remove layer')
        return True