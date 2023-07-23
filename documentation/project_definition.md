# Project definition

The aim of this project is to produce a scientific calculator that can be used to calculate the values of mathematical expressions containing for example numbers, variables, basic arithmetic operations, and functions. The result can be stored in a variable. The project is implemented using Python. The language of documentation is English.  My study program is tietojenkäsittelytieteen kandiohjelma (TKT).

### Algorithms and data structures

Shunting yard algorithm parses a mathematical expression and produces a Reverse Polish Notation (RPN) string. Shunting yard algorithm utilizes a list for input tokens, a stack for operators, and a queue for the output. From RPN a result is calculated using reverse polish procedure, which utilizes a stack for storing the operands.

### Input and output

Input is a mathematical expression presented as a list of tokens, and output is the result of solving the expression.

### References

- https://en.wikipedia.org/wiki/Shunting_yard_algorithm
- https://en.wikipedia.org/wiki/Reverse_Polish_notation
- https://brilliant.org/wiki/shunting-yard-algorithm/