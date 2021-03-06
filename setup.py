#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# VoR-CV

# The MIT License
#
# Copyright (c) 2010,2015 Jeremie DECOCK (http://www.jdhp.org)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

import sys

from vorcv import __version__ as VERSION

# See :  http://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'Intended Audience :: Education',
               'Intended Audience :: End Users/Desktop',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT License',
               'Natural Language :: English',
               'Operating System :: OS Independent',
               'Programming Language :: Python :: 3.4',
               'Topic :: Multimedia :: Video',
               'Topic :: Multimedia :: Video :: Capture',
               'Topic :: Scientific/Engineering :: Image Recognition',
               'Topic :: Scientific/Engineering :: Artificial Intelligence']


KEYWORDS = 'opencv image recognition robotics'


# You can either specify manually the list of packages to include in the
# distribution or use "setuptools.find_packages()" to include them
# automatically with a recursive search (from the root directory of the
# project).
#PACKAGES = find_packages()
PACKAGES = ['vorcv']


# The following list contains all dependencies that Python will try to
# install with this project
INSTALL_REQUIRES = ['numpy']
#INSTALL_REQUIRES = []


SCRIPTS = ["scripts/vorcv-demo",
           "scripts/vorcv-circle-detection-calibration"]


# Entry point can be used to create plugins or to automatically generate
# system commands to call specific functions.
# Syntax: "name_of_the_command_to_make = package.module:function".
ENTRY_POINTS = {}
#ENTRY_POINTS = {
#  'console_scripts': [
#      'vorcv-demo = vorcv.demo:main',
#  ],
#}


README_FILE = 'README.rst'

def get_long_description():
    with open(README_FILE, 'r') as fd:
        desc = fd.read()
    return desc


setup(author='Jeremie DECOCK',
      author_email='jd.jdhp@gmail.com',
      maintainer='Jeremie DECOCK',
      maintainer_email='jd.jdhp@gmail.com',

      name='pyvorcv',
      description="The PyVoR-CV project, a computer vision library made for some VoRobotics projects (VoR11, VoR12, ...).",
      long_description=get_long_description(),
      url='http://www.jdhp.org/',
      download_url='http://www.jdhp.org/',# Where the package can be downloaded

      classifiers=CLASSIFIERS,
      #license='MIT',            # Useless if license is already in CLASSIFIERS
      keywords=KEYWORDS,

      packages=PACKAGES,
      include_package_data=True, # Use the MANIFEST.in file

      install_requires=INSTALL_REQUIRES,
      #platforms=['Linux'],
      #requires=['pyserial'],

      scripts=SCRIPTS,
      entry_points=ENTRY_POINTS,

      version=VERSION)
