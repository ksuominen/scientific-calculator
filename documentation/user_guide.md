# User guide

### Installation

Prerequisites: Python version `3.11.3`, Poetry version `1.5.1`

1. In the project directory, install dependencies:
```
poetry install
```

2. Start application:
```
poetry run invoke start
```

### The GUI

![ui](https://github.com/ksuominen/scientific-calculator/blob/master/documentation/Graph/Graph_ui.png)

### Operators and functions the calculator provides 

- '.': dot, used in float numbers. Example: 1.23
- '+': addition. Example: 2+3 =5
- '-': subtraction. Example: 4-3 =1
- '×': multiplication. Example: 5×3 =15
- '÷': division. Example: 6÷0.5 =12.0
- '^': power. Example: 5^3 =125
- '√': square root. Example: √(4) =2.0
- '(-)': negation. Example: -(35) =35
- 'sin': sine function. The argument should be in radians. If it is in degrees, convert first to radians using rad(). Example: sin(π/6) = sin(rad(30)) = 0.5
- 'cos': cosine function. The argument should be in radians. If it is in degrees, convert first to radians using rad(). Example: cos(π/3) = cos(rad(60)) = 0.5
- 'tan': tangent function. The argument should be in radians. If it is in degrees, convert first to radians using rad(). Example: tan(π/4) tan(rad(45))= 1
- 'rad': converts degrees to radians. Example: rad(30) = π/6
- 'ln': natural logarithm (log base e). Example: ln(14) = 2.639057...
- 'log': logarithm (log base 10). Example: log(14) = 1.1461280...
- 'abs': absolute value. Example: abs(-(35)) = 35
- 'round': rounds the value to nearest integer.
- '!(x)': calculates the factorial of the number. Example: !(5) = 120
- 'min': chooses the minimum value of two options. Example: min(3,15) = 3
- 'max': chooses the maximum value of two options. Example: max(3,15) = 15
- ',': comma, used to separate the two options in min and max functions
- 'π': pi (3.14159265359......)
- 'e': Euler's number (2.7182818284......)
- '(' and ')': left and right parentheses, used in function calls and to indicate the order of calculation
- 'CE': clear (deletes the current expression)
- 'C': delete one (deletes the last token from the expression)
- 'Save': save the current result to 'M'. You need to calculate the result first with '='.
- 'M': use the saved result in a new expression. If no result is saved, the default value is 0.
- 'Ans': stores the result of the last expression. If no expression is yet calculated, the default value is 0.
- '=': equal to. Calculates the value of the expression.
