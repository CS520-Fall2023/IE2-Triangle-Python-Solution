# IE2-Triangle
Template code for the In-Class Exercise 2 on Unit Testing, an exercise that focuses on unit testing and
test effectiveness, using code coverage and mutation analysis.

# Installation
1. Run ```pip3 install -r requirements.txt.```
2. Test the setup by running 
  ```
   cd test_suit
   python -m test_isTriangle
   ```
For more information on ```Pytest```, you can take a look at the homepage https://pypi.org/project/pytest/. 



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

2. For the initial test suite, what is the statement (a.k.a. line) coverage percentage? the condition (a.k.a.
branch) coverage percentage? the mutant detection rate?

Ans: Initial Test scores: Statement coverage 65%. Condition coverage 51%, and Mutation score : 0%.   Total generated mutants: 52, killed: 0 (0%) and survived: 52 (100%).

3. Did your approach to writing unit tests differ between developing a coverage-adequate test suite and
developing a mutation-adequate test suite? Briefly explain why or why not.

Ans: Both approaches were similar in that they targeted specific parts of the original program (e.g., lines, branch, mutation). But for the mutation-adequate test suite, the approach needed to take into account the difference between the original program and the mutant. To kill a given mutant, you needed to design a test case where the same inputs led the original program to produce the expected output but that mutant do NOT produce the expected output.


4. Consider your mutation test suite and the triangle program. For any given program, why are some mutants not detectable?

Ans: 
For an undetectable mutant, it is behaviorally equivalent to the original program. For all possible test case inputs, the mutant and the original program produce the exact same outputs so either both pass the test case or else both fail it. To kill a given mutant, you need to design a test case where the same inputs led the original program to produce the expected output but the mutant to NOT produce the expected output to kill that mutant. For the undetectable mutants, such inputs do not exist. Here are some common reasons for undetectable mutants.

-Equivalent Mutants
Equivalent mutants are mutants that, although syntactically different, are semantically equivalent to the original program. That is, they produce the same output for all possible inputs. 

-Redundant Code
If the mutated code section is not reachable, then no test case can detect it. This is often indicative of dead code in the program.


-Example from Our Case
Consider the following undetected mutant in the mutation_output log:
```diff
-  if (a <= 0 or b <= 0 or c <= 0):
+  if (a <= 0 and b <= 0 and c <= 0):
```
This mutant is difficult to detect because it changes the behavior of the code only when all sides are less than or equal to zero. The existing tests don't cover this particular scenario. However, it's arguable whether this is an important case to consider; in most real-world contexts, a triangle with all sides <= 0 is clearly invalid, and the program would still return `INVALID` for any such input.


5. What changes in the code coverage percentages and mutant detection rate did you observe when deleting (or commenting out) all assertions?

Ans:

Code Coverage:

-Rate Unchanged: The code coverage percentages for `test_conditionCoverage.py` should remain the same. Code coverage measures which lines of code are executed, not whether they produce the correct output.

-Line Execution Continues: Even if assertions are commented out, the lines invoking methods like `Triangle.classify()` will still be executed. Therefore, these lines will still count as "covered" by the test suite.

-False Assurance: High code coverage could give a false sense of security. Even though metrics would indicate extensive testing, the absence of assertions would mean that the tests are not actually verifying the functionality of the code.


Mutant Detection Rate:

-Decrease to Zero: With the assertions commented out, the tests will not kill any mutants, as there is no comparison being made between expected and actual output.

-False Negatives: All mutants will survive, suggesting that the code under test is of low quality, even though this might not be the case.

6. Create a definition of “test case redundancy” based on code coverage or mutation analysis. Given your definition of test case redundancy, are some of the test cases in your test suites redundant? Given your definition of test case redundancy, would you remove redundant test cases? Briefly explain why or why not.

Ans:

Test Case Redundancy Definition

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


7. How many decision points did you find for the Control flow graph for scalene triangle, equilateral triangle, and isosceles triangle? Identify and note by type of decision points (e.g, side equality, side lengths. ) Did these findings help you to create a better test suite?

Ans: 

   Scalene Triangle:
   Decision Points: 6 (Three for side lengths, and three for side equality)

   Equilateral Triangle:
   Decision Points: 5 (Three for side lengths, and two for side equality)

   Isosceles Triangle:
   Decision Points: 5 (Three for side lengths, and two for side equality)

The decision points help to create test cases addressing each branch or condition and ensures overall coverage. The required conditions are highlighted by the decision points for each triangle and also helps to identify potential edge cases or boundary conditions, like very small or large side lengths. These findings help in creating specific test cases. 

   Invalid Sides
   Decision Points for Invalid Sides: 3 (One for each side's length)

   Triangle Inequality
   Decision Points for Triangle Inequality: 3 (One for each inequality condition)

   To address these exception cases when creating a test suite:
   - Test with one or more sides having a non-positive value (e.g., 0, -1).
   - Test with sides that violate the triangle inequality theorem (e.g., sides 1, 2, and 4).




