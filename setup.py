# -*- coding: utf-8 -*-
from pip.req import parse_requirements
import lixinger_openapi as lo
from setuptools import (
    find_packages,
    setup,
)

version = lo.__version__

requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='lixinger_openapi',
    version=version,
    description='lixinger openapi',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    author='sheki lyu',
    author_email='lvxueji@gmail.com',
    license='Apache License v2',
    install_requires=requirements,
    url='https://github.com/ShekiLyu/lixinger-openapi',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
