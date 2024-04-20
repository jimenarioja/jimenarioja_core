"""
Packaging Python Projects
Documentation: https://packaging.python.org/tutorials/packaging-projects/
"""

import setuptools

from jimena.core.components.tools.constants import (
    PROJECT_NAME,
    PROJECT_VERSION,
    AUTHOR,
    AUTHOR_EMAIL,
    DESCRIPTION,
    LONG_DESCRIPTION_CONTENT_TYPE,
    URL,
    PYTHON_REQUIRES,
    REQUIREMENTS_FILE,
)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
    url=URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Development Status :: 1 - Planning",
    ],
    install_requires=[i.strip() for i in open(REQUIREMENTS_FILE).readlines()],
    python_requires=PYTHON_REQUIRES,
)
