#!/usr/bin/env python3

import setuptools
import x9k3

with open("README.md", "r") as fh:
    readme = fh.read()

setuptools.setup(
    name="x9k3",
    version=x9k3.version(),
    author="Adrian of Doom",
    author_email="spam@iodisco.com",
    description="A SCTE-35 Aware HLS Segmenter",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/superkabuki/x9k3",
    py_modules=["x9k3"],
    scripts=["bin/x9k3"],
    platforms="all",
    install_requires=[
        "threefive >= 3.0.53",
        "m3ufu >= 0.0.91",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    python_requires=">=3.6",
)
