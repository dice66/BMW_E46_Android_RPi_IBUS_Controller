"""
The setup.py module is responsible for describing the metadata necessary
for building and installing the Python project.
"""
from distutils.core import setup


setup(
    name='ConnectedCarController',
    version='1.0.0',
    packages=['controllers', 'interfaces', ],
    license=open('LICENSE.txt').read(),
    long_description=open('README.txt').read(),
)
