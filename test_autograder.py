import os, subprocess, re


statement_coverage = "test_statementCoverage.py"
condition_coverage = "test_conditionCoverage.py"
mutation_coverage =  "test_mutationAdequate.py"


# Compilation of files
statement_compilation = 'python -m py_compile ./test_suit/test_statementCoverage.py'
condition_compilation = 'python -m py_compile ./test_suit/test_conditionCoverage.py'
mutation_compilation = 'python -m py_compile ./test_suit/test_mutationAdequate.py'


proc = subprocess.run(statement_compilation, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if proc.returncode == 0:
    print("statement compiles")
 
 
proc = subprocess.run(condition_compilation, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if proc.returncode == 0:
    print("Condition Coverage Test Suite compiles")

proc = subprocess.run(mutation_compilation, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if proc.returncode == 0:
    print('mutation compiles')



statement_coverage_command = 'D:/Phd_2022/Spring23/TAcourse/in-class-exercise/ex2/python-testing/in-class2-python/triangle/statement_coverage.sh'
condition_coverage_command = 'D:/Phd_2022/Spring23/TAcourse/in-class-exercise/ex2/python-testing/in-class2-python/triangle/condition_coverage.sh'
mutation_coverage_command = 'D:/Phd_2022/Spring23/TAcourse/in-class-exercise/ex2/python-testing/in-class2-python/triangle/mutation.sh'

# # Statement Coverage
proc = subprocess.run(statement_coverage_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(proc)
actual_output = proc.stdout.decode('utf-8')
print("Actual",actual_output)
print(statement_coverage)
# Substring to search for statement_coverage
desired_line = None
for line in actual_output.splitlines():
    if statement_coverage in line:
        desired_line = line
        break

statement_coverage_match = re.search(r"(\d+(?:\.\d+)?)%", desired_line)
statement_coverage_rate = float(statement_coverage_match.group(1))
print(statement_coverage_rate)

if statement_coverage_rate < 0.8:
    print("Statement Coverage below 80%")
if statement_coverage_rate >= 0.8:
    print("Statement Coverage above 80%")



# Condition Coverage
proc = subprocess.run(['bash', condition_coverage_command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
actual_output = proc.stdout.decode('utf-8')

# Substring to search for condition_coverage

# Iterate over the lines and pick the line containing the substring
desired_line = None
for line in actual_output.splitlines():
    if condition_coverage in line:
        desired_line = line
        break

condition_coverage_match = re.search(r"(\d+(?:\.\d+)?)%", desired_line)
condition_coverage_rate = float(condition_coverage_match.group(1))
print(condition_coverage_rate)

if condition_coverage_rate < 0.8:
    print("Condition Coverage below 80%")
if condition_coverage_rate >= 0.8:
    print("Condition Coverage above 80%")


# Mutation Coverage

proc = subprocess.run(['bash', mutation_coverage_command], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
actual_output = proc.stdout.decode('utf-8')



# Substring to search for mutation_coverage

mutation_coverage_match = re.search(r"Mutation score.*?(\d+(?:\.\d+)?)%", actual_output)

mutation_coverage_rate = float(mutation_coverage_match.group(1)) / 100
print(mutation_coverage_rate)

if mutation_coverage_rate < 0.8:
    print("Mutation Coverage below 80%")
if mutation_coverage_rate >= 0.8:
    print("Mutation Coverage above 80%")
# if mutation_coverage >= 0.85:
#     print("Mutation Coverage above 85%")


# json_object = json.dumps(json_dictionary)

# with open('/autograder/results/results.json', 'w+') as f:
#     f.write(json_object)
