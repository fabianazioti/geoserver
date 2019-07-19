#!/usr/bin/env python

from setuptools import find_packages, setup


setup(
    name='bdc_geoserver',
    version='0.2',
    description='Brazilian Data Cube Geoserver Package',
    author='Admin',
    author_email='admin@admin.com',
    license="MIT",
    packages=find_packages(),
    url='https://github.com/brazil-data-cube/geoserver',
    include_package_data=True,
)
