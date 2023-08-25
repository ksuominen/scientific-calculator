# Implementation

A scientific calculator to calculate mathematical expressions using Python. The calculator uses shunting yard algorithm to parse the mathematical expression that is in infix notation. The algorithm produces a Reverse Polish Notation string, which is then evaluated to produce the final result. 

### Shunting yard algorithm

Shunting  yard algorithm parses a mathematical expression presented in infix notation. It produces a Reverse Polish Notation (or postfix) string. Shunting yard algorithm utilizes a stack for processing operators, parentheses, and functions. The input is read one token at a time. If it is a number or a dot, it is added straight to output. If it is a function, it is pushed to stack. If it is an operator, with certain conditions operators from stack are popped to output (see Wikipedia article for closer details), and the operator is pushed to stack. If the token is a comma (used for min and max functions in my calculator), tokens from stack are popped to output until a left parenthesis is encountered. A left parenthesis is pushed straight to stack. With a right parenthesis, tokens from stack are popped to output until a left parenthesis is encountered. The parentheses are discarded, they are not added to output. If there is a function at the top of the stack, it is also popped to output. When the input is empty, the rest of the stack is added to output.

The time complexity of the algorithm is O(n). Each token is read once from the input notation. Each number is added straight to output. Each parenthesis, operator, and function is pushed and popped to stack once. Thus there is a constant (low) number of operations performed per token and the time complexity is therefore O(n). Also the space complexity is O(n), since there is a need for a list for input tokens, a second list for output tokens, and a stack for operators, functions, and parentheses. 

### Reverse Polish Notation and Reverse Polish process

Reverse Polish Notation (RPN) is a mathematical notation where the operators follow the operands. For example, if the "common" infix notation would be '3+4', in RPN it would be '34+'. 

From RPN a result is calculated using reverse polish procedure, which utilizes a stack for storing the operands. The input is read one token at a time. If the token is a number, it is pushed to the stack. If the token is an operator, a required amount of operands are popped from the stack, the operation is performed, and the result is pushed back to the stack. When the tokens are finished, there should be only one number left in the stack, e.g. the result. 

### UI

The UI is a crude graphical UI created with Tkinter. The design is very basic with for example default colors. 
![ui](https://github.com/ksuominen/scientific-calculator/blob/master/documentation/Graph/Graph_ui.png)

### Shortcomings and suggestions for improvement

- The ui design is not the prettiest.
- The syntax for factorial is not the conventional one, e.g. x! (instead is !(x)).
- sin, cos and tan functions take the input as radians. Would be great to have some kind of switch to choose, whether one wants to use radians or degrees. Now one has to use the rad function to convert degrees to radians.
- If the expression is long, the whole of it doesn't show in the label field, and one cannot scroll backwards either, so difficult to check for syntax errors.
- In case of syntax error, the calculator could keep the expression and the user could be able to correct the mistake. Now one needs to rewrite the whole expression in case of mistake.
- It would be great, if the application could autoclose all the parentheses when pressing '='.
- Maybe the app could show what  caused the syntax error instead of just saying syntax error? I chose to do it this way, since my Casio scientifix calculator just says error.

### References

- https://en.wikipedia.org/wiki/Shunting_yard_algorithm
- https://en.wikipedia.org/wiki/Reverse_Polish_notation
- https://brilliant.org/wiki/shunting-yard-algorithm/