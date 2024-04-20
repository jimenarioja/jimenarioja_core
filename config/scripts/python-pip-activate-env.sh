#!/bin/bash

source "$(dirname "$0")/tools.sh"
pretty_display " Activating virtual environment " "·"

# Bash script to activate a virtual environment.

# Change directory to the specified directory where the virtual environment is located
cd $2
cd $1

# Activate the virtual environment
source ./Scripts/activate
