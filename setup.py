from __future__ import absolute_import, unicode_literals

from setuptools import setup, find_packages
from codecs import open
import os

here = os.path.dirname(__file__)
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vcrpy-unittest',
    version='0.1.7',
    description='Python unittest integration for vcr.py',
    long_description=long_description,
    url='https://github.com/agriffis/vcrpy-unittest',
    author='Aron Griffis',
    author_email='aron@scampersand.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='vcrpy vcr.py unittest testing mock http'.split(),
    packages=find_packages(exclude=['tests']),
    install_requires=['vcrpy'],
)
