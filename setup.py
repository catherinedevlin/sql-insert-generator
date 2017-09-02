#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(catherinedevlin): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='sql_insert_generator',
    version='0.1.0',
    description="Helps create a SQINSERT statemeent with clarifying comments",
    long_description=readme + '\n\n' + history,
    author="Catherine Devlin",
    author_email='catherine.devlin@gmail.com',
    url='https://github.com/catherinedevlin/sql_insert_generator',
    packages=find_packages(include=['sql_insert_generator']),
    entry_points={
        'console_scripts': [
            'sql_insert_generator=sql_insert_generator.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="CC0 license",
    zip_safe=False,
    keywords='sql_insert_generator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
