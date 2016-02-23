# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'VERSION')) as f:
    VERSION = f.read()

requires = [
    'tornado'
]

setup(
    name='gwmanager',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/eduardosan/window-manager.git',
    license='CPL v3.0',
    author='Eduardo Santos',
    author_email='eduardo@eduardosan.com',
    description='Manage Gnome Windows',
    install_requires=requires,
)
