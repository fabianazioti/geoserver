import os
from pathlib import Path


def generate_props_datastore():
    '''
        Generating indexer.properties file with database connection information
        -> generate file and save to /bdc_geoserver/coverages/properties_files
    '''
    properties_path = Path(
        '{}/properties_files/'.format(os.path.dirname(__file__)))
    f = open('{}/datastore.properties'.format(properties_path), 'w+')

    # pylint: disable=anomalous-backslash-in-string
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
preparedStatements=true'''.format(
        os.environ.get('POSTGRES_HOST'), os.environ.get(
            'POSTGRES_PORT'), os.environ.get('POSTGRES_DATABASE'),
        os.environ.get('POSTGRES_USER'), os.environ.get('POSTGRES_PASSWORD'))
    f.write(content_datastore_properties)
    f.close()


def generate_props_indexer(cube_name):
    # pylint: disable=line-too-long
    '''
        Generating indexer.properties file with with the columns of the table in the database
        -> generate file and save to /bdc_geoserver/coverages/properties_files
    '''
    properties_path = Path(
        '{}/properties_files/'.format(os.path.dirname(__file__)))
    f = open('{}/indexer.properties'.format(properties_path), 'w+')

    content_indexer_properties = '''TimeAttribute=ingestion
ElevationAttribute=elevation
Schema=*the_geom:Polygon,location:String,ingestion:java.util.Date,elevation:Integer
PropertyCollectors=TimestampFileNameExtractorSPI[timeregex](ingestion)
CoverageNameCollectorSPI=org.geotools.gce.imagemosaic.namecollector.FileNameRegexNameCollectorSPI:regex=({})'''.format(
        os.environ.get('SUFFIX_NAME_CUBE', '_MEDIAN'))
    f.write(content_indexer_properties)
    f.close()
