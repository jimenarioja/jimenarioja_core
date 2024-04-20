#!/bin/bash

source "$(dirname "$0")/tools.sh"
pretty_display " Reset virtual environment " "="

sh python-pip-clean-env.sh
sh python-pip-install-packages.sh
sh python-git-pre-commit-install.sh
sh python-pip-verify-env.sh
