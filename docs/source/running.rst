.. _running:

Running
=======
In order to run BDC_GEOSERVER, you must define variable `ENVIRONMENT`. By default, the application runs on development mode. You can change to
`ProductionConfig` or `TestingConfig` with the following command:

.. code-block:: sh

    $ export ENVIRONMENT=ProductionConfig
    $ python manager.py run

It will runs on host `0.0.0.0` with port `5000`. You can access directly through `http://127.0.0.1:5000/geoserver/status`

others available environment variable:
 - GEOSERVER_URL = link geoserver with port (127.0.0.1:8080)
 - GEOSERVER_USER = user to authentication in geoserver
 - GEOSERVER_PASSWORD = password to authentication in geoserver
 - ENVIRONMENT = env ([DevelopmentConfig, ProductionConfig, TestingConfig])
 - KEYSYSTEM = key to hash crypto
 - PATH_BASE_GEOSERVER = base path to layers geoserver (file:///home/data/cubes)
 - PATH_CUBES_FILE = base path to layers local or into container (/data/bdc/files)
 - POSTGRES_DATABASE = name database
 - POSTGRES_USER = user database
 - POSTGRES_PASSWORD = password database
 - POSTGRES_HOST = host database
 - POSTGRES_PORT = port database
 - SUFFIX_NAME_CUBE = title suffix (applied when not publish all bands) - (_MEDIAN_RGB)
