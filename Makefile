
SHELL := /bin/bash

.SILENT: build clean devenv
.IGNORE: clean
.ONESHELL:

BLUE:=\033[0;34m
RED:=\033[0;31m
NC:=\033[0m # No Color
BOLD:=$(tput bold)
NORM:=$(tput sgr0)

# the location of this file.
DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# build the package from the source
build: devenv
	. venv/bin/activate;
		python -m build;
		twine check --strict dist/*

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf src/uplevel.egg-info/
	rm -rf venv/
	rm -rf `find . -type d -name __pycache__`

devenv:
	if [ ! -d "$(DIR)/venv" ]; then
		echo "Creating venv";
		python -m venv venv/;
	fi
	@if ! venv/bin/python -c "import uplevel" 2>/dev/null; then
		echo "Installing uplevel in editable mode";
		. venv/bin/activate;
		pip install --upgrade -e .[dev];
	fi

publish: build
	echo "uploading build to PyPI"
	. venv/bin/activate;
		twine upload ./dist/*
