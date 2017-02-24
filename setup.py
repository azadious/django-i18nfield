from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


setup(
    name='django-i18nfield',
    version='0.0.0',
    description='Store internationalized strings in Django models',
    long_description=long_description,
    url='https://github.com/raphaelm/django-i18nfield',
    author='Raphael Michel',
    author_email='mail@raphaelmichel.de',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django :: 1.10'
    ],

    keywords='i18n strings database models',
    install_requires=[
    ],

    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
)
