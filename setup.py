#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
import os.path
import re

me = "Morten Grunnet Buhl"

def read(fname):
    with open(fname) as fd:
        return fd.read()

def path(path):
    if isinstance(path, list):
        path = os.path.join(*path)
    return os.path.realpath(os.path.join(os.path.dirname(__file__), path))

def version():
    pattern = "__version__\s?=\s?.([0-9.]+)."
    version, = re.findall(pattern, read(path(["di","__init__.py"])))
    return version

def email(me):
    return "{}@{}.{}".format("".join([s[0].lower() for s in me.split(" ")]), "arendal", "dk")


setup(
    name="python-di",
    version=version(),
    description="di - A Python dependency injection module",
    long_description=read(path("README.rst")),
    url="https:github.com/buhl/python-di",
    author=me,
    author_email=email(me),
    license="BSD-2",
    packages=["di"],
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License :: BSD-2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only'
    ]
)
