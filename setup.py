"""
This solves the problem of relative imports.
To install use following command in setup.py directory 
    $ pip install -e .  #For virtual env other than conda 
    $ conda develop setup.py # For conda virtual env
Direct imports from root directory will be enabled

Courtesy : https://stackoverflow.com/a/50194143

Note: There is a chance of interference from poetry (package manager used in this project)
 .lock and .toml, temporarily move poetry files somewhere else and install this package 
"""

from setuptools import setup, find_packages

setup(
    name='sentiment_project',
    version='1.0',
    packages=find_packages(),
    )