#!/bin/bash

# Bash script to install packages listed in the 'requirements.txt' file.

source "$(dirname "$0")/tools.sh"
pretty_display " Installing packages listed in the requirements file " "·"

pip install -r ../../requirements.txt
