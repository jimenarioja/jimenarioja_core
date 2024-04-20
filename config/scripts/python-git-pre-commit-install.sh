#!/bin/bash

source "$(dirname "$0")/tools.sh"
pretty_display " Running pre-commit - Install ... " "·"

pip install pre-commit==2.20.0
pre-commit install && pre-commit install --hook-type pre-push
