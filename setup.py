#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Akudu
"""

import io
import os
from setuptools import setup

version = [i for i in open("akudu/__init__.py").readlines() if i.startswith("__version__")][0]
__version__ = ''
exec(version)

package_root = os.path.abspath(os.path.dirname(__file__))
readme_filename = os.path.join(package_root, "README.md")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
  name="akudu",
  version=__version__,
  keywords=['kudu', 'database', 'asyncio', 'bigdata', 'storage system'],
  description="Asyncio Client for Apache Kudu Database Engine (Storage System).",
  long_description=long_description,
  long_description_content_type='text/markdown',

  author="LovinJoy",
  author_email='technical-committee@lovinjoy.com',
  url="http://github.com/lovinjoy/akudu",
  license="MIT License",
  install_requires=[
      'protobuf>=3.20.0'
    ],
  packages=["akudu"],
  # packages = find_packages(),
  python_requires='>=3.8',
)
