.. _installation:

Installation
============

Python Version
--------------

You must use `bdc_geoserver` with Python 3+ and PyPy or Docker.

Dependencies
------------

These distributions will be installed automatically when installing wtss.

* `Flask <http://flask.pocoo.org/>`_ microframework for Python based on Wekzeug.
* `Flask-Cors <https://flask-cors.readthedocs.io/en/latest/>`_ Flask extension for handling Cross Origin Resource Sharing (CORS)
* `flask-restplus <https://flask-restplus.readthedocs.io/en/stable/>`_ an extension for Flask that adds support for quickly building REST APIs.
* `jsonschema <https://python-jsonschema.readthedocs.io/en/stable/>`_ an implementation of JSON Schema for Python.

Install Geoserver
-------------

Within the activated environment, use the following command to install Flask:

.. code-block:: sh
    $ pip install bdc-geoserver

or with REST API and Docker => `Github <https://github.com/brazil-data-cube/geoserver>`