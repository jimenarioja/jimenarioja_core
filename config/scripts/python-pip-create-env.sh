#!/bin/bash

# Bash script to create a virtual environment.

# The script expects two arguments:
# $1: Name of the virtual environment
# $2: Path to the directory where the virtual environment will be created
source "$(dirname "$0")/tools.sh"
pretty_display " Creating a virtual environment " "·"

echo Create a environment - $1

# Access the specified directory
cd $2

# Remove the existing virtual environment, if any
rm -Rf $1

# Install or upgrade pip
python -m pip install --upgrade pip

# Check if virtualenv is installed, if not, install it
$ python -c "import virtualenv" 2>/dev/null || pip install virtualenv

# Create the virtual environment
virtualenv "$1"
