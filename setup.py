#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="nanpy",
      version="0.2",
      description="Use your Arduino board with Python",
      license="MIT",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="http://github.com/Octan/nanpy",
      packages = find_packages(),
      keywords= "arduino library prototype",
      zip_safe = True)
