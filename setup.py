#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('CHANGES.rst').read().replace('.. :changelog:', '')

requirements = [

]

test_requirements = [
    'mock',
]

setup(
    name='bighelp',
    version='0.1.0',
    description="This is a bighelp for everybody who's using the python interactive mode.",
    long_description=readme + '\n\n' + history,
    author='Gregor Müllegger',
    author_email='gregor@muellegger.de',
    url='https://github.com/gregmuellegger/bighelp',
    packages=[
        'bighelp',
    ],
    package_dir={'bighelp':
                 'bighelp'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='bighelp',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
