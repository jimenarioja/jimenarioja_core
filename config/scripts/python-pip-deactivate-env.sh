#!/bin/bash

# Bash script to deactivate a virtual environment.

source "$(dirname "$0")/tools.sh"
pretty_display " Deactivating a virtual environment " "·"

# Change directory to the specified directory where the virtual environment is located
cd $2
cd $1

# Deactivate the virtual environment
deactivate
