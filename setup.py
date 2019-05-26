import os
from glob import glob

from setuptools import setup, find_packages


def find_package_data(*allowed_extensions):
    package_data = {}

    for ext in allowed_extensions:
        for file in glob(f'**/*.{ext}', recursive=True):
            pos = -1
            parts = file.split('/')
            while True:
                prefix = '/'.join(parts[0:pos])
                package = '.'.join(parts[0:pos])
                data_file = '/'.join(parts[pos:])

                if prefix == '':
                    break

                if os.path.exists(os.path.join(prefix, '__init__.py')):
                    break

                pos -= 1

            if prefix != '':
                if package not in package_data:
                    package_data[package] = []

                package_data[package].append(data_file)

    return package_data


setup(
        name='zmei-gen-flutter',
    version='0.1.3',
    packages=find_packages(),
    url='',
    license='GPLv3',
    author='Alex Rudakov',
    author_email='ribozz@gmail.com',
    description='FLutter generator for Zmei',
    long_description='',

    package_data=find_package_data('g4', 'tpl', 'html'),

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
