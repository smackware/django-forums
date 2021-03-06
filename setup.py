import os
from setuptools import setup, find_packages

import forums


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-forums',
    version=forums.__version__,
    description='Small standalone django forums application',
    long_description=read('README.md'),
    license='MIT License',
    author='byteweaver',
    author_email='contact@byteweaver.net',
    url='https://github.com/byteweaver/django-forums',
    packages=find_packages(),
    install_requires=[
        'django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='forums.tests',
)
