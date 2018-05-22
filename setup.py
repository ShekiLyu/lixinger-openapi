# -*- coding: utf-8 -*-
from pip.req import parse_requirements
import lixinger
from setuptools import (
    find_packages,
    setup,
)

version = lixinger.__version__

requirements = [str(ir.req) for ir in parse_requirements("requirements.txt", session=False)]

setup(
    name='lixinger-openapi',
    version=version,
    description='lixinger openapi',
    packages=find_packages(),
    author='sheki lyu',
    author_email='lvxueji@gmail.com',
    license='Apache License v2',
    install_requires=requirements,
    package_data={'': ['*.*']},
    url='https://github.com/ShekiLyu/lixinger-openapi',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
