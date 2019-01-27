import os
from glob import glob

from setuptools import setup, find_packages

setup(
    name='zmei-gen-flutter',
    version='0.1.0',
    packages=find_packages(),
    url='',
    license='GPLv3',
    author='Alex Rudakov',
    author_email='ribozz@gmail.com',
    description='FLutter generator for Zmei',
    long_description='',

    install_requires=[
        "zmei-cli>=2.1.1",
    ],

    entry_points={
        'zmei.grammar.tokens': [
            'zmei_flutter = zmei_gen_flutter.grammar.tokens:tokens',
        ],
        'zmei.grammar.pages': [
            'zmei_flutter = zmei_gen_flutter.grammar.struct:pages',
        ],
        'zmei.generator': [
            'zmei_flutter_flutter = zmei_gen_flutter.generator.flutter:generate',
        ],
        'zmei.parser.stage3': [
            'zmei_flutter = zmei_gen_flutter.parsers.all_stage3:parsers',
        ],

        'zmei.templates': [
            'zmei_flutter = zmei_gen_flutter.templates',
        ]

    }
)
