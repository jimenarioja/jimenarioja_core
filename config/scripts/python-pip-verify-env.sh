#!/bin/bash

# This script checks if all the packages specified in the 'requirements.txt' file are installed.
# It is expected that the 'requirements.txt' file contains a list of Python packages with their versions.
# If a package is not installed, the script will display a warning message and exit with a non-zero exit code.
# If all packages are installed, the script will display a message indicating that all specified packages are installed.

# Set the path to the requirements file

source "$(dirname "$0")/tools.sh"
pretty_display " Verifying the packages installed " "·"

requirements="requirements.txt"

# Access the specified directory
cd $2

# Iterate over each line in the requirements file
while IFS= read -r line; do
    # Filter name of package
    package_name=$(echo "$line" | awk -F'==' '{print $1}')

    # Check if the package is already installed
    if ! pip show "$package_name" >/dev/null 2>&1; then
        pretty_display "The package $package_name isn't installed." " "
        exit 1
    fi
done < "$requirements"

pretty_display "All the specified packages en $requirements are installed." " "
