#!/usr/bin/env python
from setuptools import setup

files = [
    "ansible/modules/kong",
    "ansible/module_utils/kong",
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
    packages=files,
    install_requires = [
        'ansible>=2.1.0',
        'ansible-dotdiff'
    ],
)
