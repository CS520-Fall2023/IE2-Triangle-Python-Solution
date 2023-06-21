# Triangle
Example program for a software testing exercise that focuses on unit testing and
test effectiveness, using code coverage and mutation analysis.

# Required python packages
1. pip install -r requirements.txt. You may choose to create a virtual environment/conda environment. The python version should be 3.8>=. 
2. Test the setup by running 'python -m TriangleTest'
3. make sure to place "mut.py" in the test_suit folder.

If you encounter an error with "if self.isAlive():" from mutpy, do the following:
1. Open utils.py shown in the error message from the "mutpy" scripts
2. Go to the line "if self.isAlive():", shown in the error message
3. Make the following change: if self.isAlive(): becomes if self.is_alive():


# Testing
''mutation'': run './mutation.sh'
''line coverage'': run './statement_coverage.sh'
''branch coverage'': run ./condition_coverage.sh'


Optional details:

1. python.exe mut.py --target isTriangle --unit-test test_isTriangle -m --runner pytest
2. python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m --runner pytest 
3. python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m --report REPORT_FILE [generate report yaml file]
4. python.exe mut.py --target isTriangle --unit-test test_mutationAdequate -m --report-html mutation_report.html [generate html file]
5. python.exe mut.py --target isTriangle --unit-test test_mutationAdequate --mutation-number 43 [run only one mutation]

NB: python.exe command works for windows system. 

'coverage'
1. coverage run -m pytest test_statementCoverage.py
2. coverage html -d statement_html

'branch coverage'
1. coverage run --branch test_conditionCoverage.py
2. coverage html -d coverage_html




