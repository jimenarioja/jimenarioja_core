.PHONY: help
help:						## Show the help.
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep


.PHONY: build
build:						## Build Project.
	echo "Upgrade pip"
	pip install --upgrade pip
	echo "Install build project"
	pip install --upgrade build
	echo "Build project"
	python -m build
	echo "Install jimena-core package [local]"
	pip install ./dist/jimena-core-0.0.1.tar.gz

.PHONY: reset-env install-packages

python-pip-reset-env:
	shell_script infra/scripts/python-pip-reset-env.sh
