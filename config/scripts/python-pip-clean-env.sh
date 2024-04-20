#!/bin/bash

source "$(dirname "$0")/tools.sh"
pretty_display " Cleaning virtual environment " "·"

num_packages=$(pip list | wc -l)

if [ "$num_packages" -gt 5 ]; then
  pip freeze | xargs pip uninstall -y
else
  pretty_display "The environment is already cleaned" " "
fi
