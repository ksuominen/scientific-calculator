# Week 2

This week, I have created a basic version of the shunting yard algorithm. It should work with basic operators (+, -, *, /, ^) and parentheses. I have also created an algorithm for solving the reverse polish (or postfix) notation with those same operators. I've created unittests and documentation for the algorithms. I've created a very basic graphical ui.

The program has progressed nicely, in my opinion. Currently, the calculator can be used to calculate additions with singledigit numbers. However, when I improve the ui somewhat and create the function to parse the input, it should work with all the basic operators as well as parentheses. 

I've learned a lot this week. I understand how the algorithms work quite well now. I've also learned how to do unittests in Python and how to implement a basic graphical ui.

Next I'll write tests for calculator.py and for reverse polish raising errors, as well as integration tests for combining shunting yard and polish reverse algorithms. I'll create a function for parsing the input from list (so that multidigit numbers and floats can be used). After these I'll include some basic mathematical functions.

Time spent: approx. 8 hours
[Test coverage report](https://github.com/ksuominen/scientific-calculator/blob/master/documentation/Graph/coverage_report.png)