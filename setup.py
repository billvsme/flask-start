'''
Flask-Start
-----------

Quick start flask project and app tool like django.

Links
```
* `development version <https://github.com/billvsme/flask-start>`_
'''
from setuptools import setup


setup(
    name='Flask-Start',
    version='1.0-dev',
    license='MIT',
    author='billvsme',
    author_email='994171686@qq.com',
    description='Quick start flask project and app tool like django',
    long_description=__doc__,
    scripts=['flask-start.py'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
