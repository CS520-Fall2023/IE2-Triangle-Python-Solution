#!/bin/bash
# Change to the directory containing the Python script
## run decision/branch coverage
cd "./test_suit"
coverage run --branch test_decisionCoverage.py
coverage report -m --include="test_decisionCoverage.py"
coverage html -d decision_coverage_html
