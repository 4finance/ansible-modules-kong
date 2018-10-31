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

long_description=open('README.md', 'r').read()
version=open('VERSION', 'r').read()

setup(
    name='ansible-modules-kong',
    version=version,
    description='Ansible Modules for Kong 0.14.x',
    long_description=long_description,
    author='Roman Komkov',
    author_email='roman.komkov@4finance.com',
    url='https://github.com/4finance/ansible-modules-kong',
    py_modules=py_files,
    packages=files,
    install_requires = [
        'ansible>=2.1.0',
        'ansible-dotdiff'
    ],
)
