# IE2-Triangle
Template code for the In-Class Exercise 2 on Unit Testing, an exercise that focuses on unit testing and
test effectiveness, using code coverage and mutation analysis.

# Installation
We advise you to create a virtual enviroment (python venv, conda) to install the packages.
Preferred version of python - **python3.8**. 
1. Run ```pip3 install -r requirements.txt.```
2. Test the setup by running 
  ```
   cd test_suit
   python3 -m test_triangle
   ```
3. Test the initial test suite by running the script: ```test.sh```
For more information on ```Pytest```, you can take a look at the homepage https://pypi.org/project/pytest/. 

Here are more details about ``unittest``: https://docs.python.org/3/library/unittest.html.



## Question

1. What are 2 best practices satisfied by the triangle project which make it easier to write the unit tests
and run them?

Ans: 

Best Practices Satisfied for Writing Unit Tests:

Modularity in Design: The Triangle class is modular, specifically providing the classify method and Type enum.

Input Validation: The classify method provides input validation with pre-condition checks.

Best Practices Satisfied for Running Unit Tests:

Initial Test Suite: The TriangleTests class provides an initial test suite. 

Documentation: The README file tells you how to build and run the project. 

Automation Scripts: There are shell scripts to run the coverage tool and the mutation analysis tool. 

2. For the isTriangle class with the initial test suite, what is the statement (a.k.a. line) coverage percentage? the decision (a.k.a.
branch) coverage percentage? the mutant detection rate (often called a mutation score)?

Ans: For most groups, the INITIAL TEST SUITE scores are: Statement coverage 65%. Decision coverage 51%, and Mutant detection rate : 23.1%.   Total generated mutants: 52, killed: 12 (23.1%) and survived: 40 (76.9%).

The mutation analysis tool, however, used a random seed. This could impact the above. For a small number of groups, the scores were different. Here is what we checked for them: 1) Based on the coverage analysis definitions, the statement coverage score is usually noticeably higher than the decision coverage score. Additionally given that the test suite had only 1 test case, the coverage score should not be near 90. 2) Based on the coverage versus mutation analysis definitions, the coverage scores are usually noticeably higher than the mutant detection rate. Additionally given the test case, it was very unlikely that the mutation detection rate was 0.

NOTE) The versions of python and the testing tools may have affected the above numbers. The statement coverage should be higher than the decision coverage. The decision coverage should be higher than the mutant detection rate.

3. Did your approach to writing unit tests differ between developing a coverage-adequate test suite and
developing a mutation-adequate test suite? Briefly explain why or why not.

Ans: Both approaches were similar in that they targeted specific parts of the original program (e.g., lines, branch, mutation). But for the mutation-adequate test suite, the approach needed to take into account the difference between the original program and the mutant. To kill a given mutant, you needed to design a test case where the same inputs led the original program to produce the expected output but that mutant did NOT produce the expected output.


4. Consider your mutation test suite and the triangle program. For any given program, why are some mutants not detectable?

Ans: 
For an undetectable mutant, it is behaviorally equivalent to the original program. For all possible test case inputs, the mutant and the original program produce the exact same outputs, meaning either both pass the test case or else both fail it. To kill a given mutant, you need to design a test case where the same inputs led the original program to produce the expected output but the mutant to NOT produce the expected output to kill that mutant. For the undetectable mutants, such inputs do not exist. Here are some common reasons for undetectable mutants.

-Equivalent Mutants
Equivalent mutants are mutants that, although syntactically different, are semantically equivalent to the original program. That is, they produce the same output for all possible inputs. For instance, one commonly generated mutant removed the @staticmethod annotation. This caused a warning to be reported. But it did not change the expected outputs.

-Redundant Code
If the mutated code section is not reachable, then no test case can detect it. This is often indicative of dead code in the program.

5. What changes in the code coverage percentages and mutant detection rate did you observe when deleting (or commenting out) all assertions?

Ans:

Code Coverage:

-Rate Unchanged: The code coverage percentages for `test_conditionCoverage.py` should remain the same. Code coverage measures which lines of code are executed, not whether they produce the expected output.

-Line Execution Continues: Even if assertions are commented out, the lines invoking methods like `Triangle.classify()` will still be executed. Therefore, these lines will still count as "covered" by the test suite.

-False Assurance: High code coverage could give a false sense of security. Even though metrics would indicate extensive testing, the absence of assertions would mean that the tests are not actually verifying the functionality of the code.


Mutant Detection Rate:

-Decrease to Zero: With the assertions commented out, the tests will not kill any mutants, as there is no comparison being made between expected and actual output.

-False Negatives: All mutants will survive, suggesting that the code under test is of low quality, even though this might not be the case.

6. Create a definition of “test case redundancy” based on code coverage or mutation analysis. Given your definition of test case redundancy, are some of the test cases in your test suites redundant? Given your definition of test case redundancy, would you remove redundant test cases? Briefly explain why or why not.

Ans:

Here are two examples of Test Case Redundancy Definitions

- Code Coverage: A test is "redundant" if it doesn't cover any new lines or conditions.
  
- Mutation Analysis: A test is "redundant" if it kills no new mutants.

Redundancy in the test suites

- Code Coverage: 100% doesn't imply no redundancy. Need line-by-line analysis.
  
- Mutation Analysis: If multiple tests kill the same mutants, they may be redundant.

Should Redundant Tests be Removed?

- Pros: Simplifies suite, reduces runtime.
  
- Cons: May reduce robustness and lose nuance.

- Recommendation: Remove cautiously, consider objectives and criticality.

Each "redundant" test should be individually examined before removal.

NOTE) Other definitions are acceptable.


7. How many decision points did you find for the Control flow graph for scalene triangle, equilateral triangle, and isosceles triangle? Identify and note by type of decision points (e.g, side equality, side lengths. ) Did these findings help you to create a better test suite?

Ans: 

### Decision points for normative paths(scalene, isosceles and equilateral triangle)

**Scalene Triangle**:

- Node 10: Checks if ```trian == 0```, which would indicate a Scalene triangle if the triangle inequalities are satisfied.

- Node 11: Checks the triangle inequalities 
a+b>c, a+c>b, and b+c>a.

So, for Scalene triangles, you would primarily look at Nodes 10 and 11. Node 1 (which checks if any of the sides are less than or equal to zero) is a general check for validity and applies to all types of triangles, not just Scalene. Node 4, 6, and 8 are checking for the relationships among the three sides.

**Isosceles and Equilateral Triangle**

- Node 14: Checks if trian > 3, which would indicate an Equilateral triangle.

- Nodes 16, 18, and 20: These nodes check various conditions to determine if the triangle is Isosceles based on the value of trian.

For Isosceles and Equilateral triangles, the primary decision points are Nodes 14, 16, 18, and 20.

It's worth noting that Node 1, which checks for non-positive side lengths, and Node 11, which checks for violations of the triangle inequality, are general checks that apply to all types of triangles. Node 4, 6, and 8 are checking for the relationships among the three sides.

Summary:

Scalene: Nodes 10 and 11

Isosceles: Nodes 16,18 and 20

Equilateral: Node 14

The decision points help to create test cases addressing each branch or condition and ensures overall coverage. The required conditions are highlighted by the decision points for each triangle and also helps to identify potential edge cases or boundary conditions, like very small or large side lengths. These findings help in creating specific test cases. 


### Decision points of exception paths (Invalid sides and Triangle Inequality)


- Node 1: This node checks whether any of the sides 
a,b,c are less than or equal to zero. If any of these conditions are true, the function returns INVALID.

- Node 11: This node is where the triangle inequality conditions are checked. Specifically, it verifies whether a+b≤c, a+c≤b, or b+c≤a. If any of these conditions hold, the function returns INVALID. Node 4, 6, and 8 are checking for the relationships among the three sides.

- Node 20: This node appears to serve as a "catch-all" for any cases that somehow manage to bypass the earlier checks without being classified as any of the valid triangle types (Scalene, Isosceles, or Equilateral). In such cases, the function returns INVALID. Node 4, 6, and 8 are checking for the relationships among the three sides.

Node 1 and Node 11 are designed to catch scenarios where the given side lengths cannot form a valid triangle, either because they are non-positive (Node 1) or because they violate the triangle inequality theorem (Node 11). Node 20 acts as a fail-safe, ensuring that the function does not return an undefined or incorrect classification. It's a good practice to have such a catch-all condition to handle unexpected inputs or states that might not be caught by the primary logic.

So, we have three main decision points related to exception cases:

Node 1: Checks for non-positive side lengths.

Node 11: Checks for violations of the triangle inequality theorem.

Node 20: Acts as a fail-safe for unclassified or unexpected cases, returning INVALID.


   To address these exception cases when creating a test suite:
   - Test with one or more sides having a non-positive value (e.g., 0, -1).
   - Test with sides that violate the triangle inequality theorem (e.g., sides 1, 2, and 4).




