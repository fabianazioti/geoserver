# Geoserver - Brazil Data Cube
API to publish layers and cubes in Geoserver

## Structure

- [`bdc_geoserver`](./bdc_geoserver) python scripts to manage the layers in Geoserver
- [`spec`](./spec) Spec of API bdc_geoserver
- [`docs`](./docs) Documentation of bdc_geoserver
- [`tests`](./tests) Tests of API bdc_geoserver

## Installation

### Requirements

Make sure you have the following libraries installed:

- [`Python 3`](https://www.python.org/)
- [`postgresql`](https://www.postgresql.org/download/)
- [`postgis`](https://postgis.net/)
- [`Geoserver`](http://geoserver.org/)

After that, install Python dependencies with the following command:

```bash
pip3 install -r requirements.txt
```

## Running

- copy files with cubes to folder `./files/`
- create database Postgresql with spatial exension (POSTGIS)
- set environment variable:
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

```
python3 manager.py run
```

### Running with docker
You can configure the environment to run through Docker containers. In order to do that, build the image brazildatacube/geoserver:0.1:
```
docker build --tag brazildatacube/geoserver:0.1 -f docker/Dockerfile .
```

After that, you can run the application with command:

```
docker run --interactive \
           --tty \
           --detach \
           --name geoserver_app \
           --publish 5000:5000 \
           brazildatacube/geoserver:0.1
```

or with compose:
```
TAG=0.1 docker-compose up -d
```

You can also generate the documentation on http://localhost:5001:
```
docker run --rm \
           --interactive \
           --name geoserver_app_docs \
           --publish 5001:5001 \
           brazildatacube/geoserver:0.1 \
           python3 manage.py docs --serve
```

And run the tests:
```
docker run --rm \
           --interactive \
           --name geoserver_app_test \
           brazildatacube/geoserver:0.1 \
           python3 manage.py test
```