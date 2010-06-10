# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
 
long_description = open('README.txt').read()
 
setup(
    name='django-taggit-autocomplete',
    version='0.1',
    description='Autocompletion for django-taggit',
    long_description=long_description,
    author='Jeremy Epstein',
    author_email='jazepstein@gmail.com',
    url='http://github.com/Jaza/django-taggit-autocomplete/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
) 
