#!/usr/bin/env bash
# Complete Test suite for GeoMath library

PYTHONPATH=. coverage run test.py

coverage xml -o coverage.xml
coverage html -d coverage

rm -f pep8.log pyflakes.log

nosetests --with-xcoverage --with-xunit

pep8 --max-line-length=120 geomath > pep8.log || true
pyflakes geomath > pyflakes.log || true
