#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    import multiprocessing  # NOQA
except:
    pass

tests_require = [
    'Django',
    'celery',
    'django-nose>=1.0',
    'mock>=0.8.0',
]

setup(
    name='django-modeldict',
    version='1.5.0',
    author='DISQUS',
    author_email='opensource@repleo.nl',
    url='http://github.com/bjarnoldus/django-modeldict/',
    description='Stores a model as a dictionary',
    packages=find_packages(),
    zip_safe=False,
    tests_require=tests_require,
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
