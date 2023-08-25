# Testing document

### Running the tests

The tests can be run in project directory:
1. Open Poetry shell:
```
poetry shell
```

2. Run tests: 
```
pytest src
```

3. Exit Poetry shell:
```
exit
```
### Test coverage

The coverage report can be generated in project directory:
```
poetry run invoke coverage-report
```

The coverage report is saved as index.html file in htmlcov folder.

Unit testing coverage: 
![coverage report](https://github.com/ksuominen/scientific-calculator/blob/master/documentation/Graph/coverage_report.png)

The overall test coverage is 98%. In shunting yard and reverse polish there are a couple of partially tested functions. However, those missing parts are quite irrelevant, example: 

![example of partial testing](https://github.com/ksuominen/scientific-calculator/blob/master/documentation/Graph/example_from_coverage_report.png)

All the operators the calculator offers are covered, so no need to test with random input.

### Unit testing

algorithm_helpers_test.py: 
- Test that getting the precedence and associativity of operators works correctly. 
- Test that functions checking if a token is a number or if a token is an operator work correctly, as well as the function checking whether a function has one or two parameters. 

shunting_yard_test.py: 
- Test that invalid input raises ValueError (for example two many or two few brackets, invalid tokens, too many or too few operands etc.).
- Test that the function parses infix notation correctly to RPN. The correct answers I have calculated myself with help from different infix-postfix calculators found online (not all of them work correctly, thus I also tried to do these by hand).

reverse_polish_test.py:
- Test that invalid input raises ValueError (for example too few or too many operands). 
- Test that functions with one or two parameters work correctly. 
- Test that different kinds of operations work correctly. 

calculator_test.py:
- Test that updating the calculator's expression works, as well as getting the expression.
- Test that clearing the calculator's expression works.
- Test that deleting the last token from the calculator's expression works.
- Test that different operations and functions work correctly. 
- Test that the calculator parses floats and multidigit numbers correctly from the expression.
- Test that incorrect input raises ValueError.
- Test that Euler's number and pi work correctly.
- Test that the calculator saves the most recent result to Ans correctly.
- Test that saving the result to 'M' works correctly. 

### Manual testing

I have tested the calculator with different expressions, and compared the results with my CASIO fx-991ES calculator. They seem to produce similar results. 