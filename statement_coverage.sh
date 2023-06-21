#!/bin/sh
# Change to the directory containing the Python script
cd "./test_suit"
coverage run -m pytest test_statementCoverage.py
# coverage json -m --include="test_statementCoverage.py" --pretty-print -o 'coverage.json'
coverage report -m --include="test_statementCoverage.py"
coverage html 
