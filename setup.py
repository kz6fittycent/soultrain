#!/usr/bin/env python3

from setuptools import setup

setup(
    name="soultrain",
    version="1.0.0",
    description="Make a mistake and get a reward...",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libsoultrain"],
    scripts=["soultrain"],
    package_data={"libsoultrain": ["data/*"]},
)
