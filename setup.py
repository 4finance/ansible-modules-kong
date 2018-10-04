#!/usr/bin/env python
from setuptools import setup

py_files = [
    "ansible/module_utils/kong",
    "ansible/module_utils/kong_certificate",
    "ansible/module_utils/kong_consumer",
    "ansible/module_utils/kong_helpers",
    "ansible/module_utils/kong_plugin",
    "ansible/module_utils/kong_route",
    "ansible/module_utils/kong_service",
]
files = [
    "ansible/modules/kong",
]

long_description=open('README.rst', 'r').read()
version=open('VERSION', 'r').read()

setup(
    name='ansible-kong',
    version=version,
    description='Kong 0.14.x module and Python library for Ansible',
    long_description=long_description,
    author='Roman Komkov',
    author_email='roman.komkov@4finance.com',
    url='https://github.com/decayofmind/ansible-kong-module',
    packages=files,
    package_dir={'ansible': ''},
    install_requires = [
        'ansible>=2.1.0',
        'ansible-dotdiff'
    ],
)
