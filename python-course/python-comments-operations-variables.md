---
layout: page
title: Python Comments, Operations, and Variables
---
In this lesson, we will be discussing the very basics of Python. Specifically, we will discuss comments, operations, and variables in the Python programming language.


## The Basics of Comments in Python (or any other language!)

In computer programming, comments are text included in your code that is not actually run by the computer. Comments exist to instruct _humans_;the rest of the code exists to instruct _computers_.

To start our course, I’ll explain how you can put comments in your code. Throughout the rest of this course, I will include comments after blocks of code to explain what the output of the course should be.


### Single-Line Comments in Python

Most programming languages (Python included) have slightly different syntax for single- and multi-line comments. The single-line comment operator in Python is the hash character ‘#’.

You can see an example of a single-line Python comment below:

```python

#This is a comment in Python

```

This means that the entire line that starts with ‘#’ will not be executed by the Python compiler or interpreter (which is fancy language that means this line will not run as part of the code). 


### Multi-Line Comments in Python

Multi-line comments in Python are initiated and completed using three quotes (can be single or double quotes):

```python

'''

This

is 

a

multi-

line

comment

in

Python

'''

```

This means that any code after the first “”” and before the second “”” will not be executed by the Python compiler or interpreter. 

Multi-line comments are often used at the beginning of function declarations to describe the purpose of a function. We have not yet explored functions in this course yet, but an example of a multi-line comment in a Python function is below:

```python

def my_function(name):


    '''


    This function prints the name passed in as an argument.


    '''


    print(name)

```

You may also sometimes see block comments, which serve to visibly chunk up your code into manageable blocks. Block comments start and end with a line of hash characters. An example is below:

```python

######################################################

#This is a block comment!

######################################################

```


## Basic Math Operations in Python

Now that we have a basic understanding of comments in the Python programming language, let’s continue by discussing basic math operations in Python.

Since Python is primarily used by scientists and other quantitatively-oriented programmers, these fundamental math operations are extremely extremely important. Let’s dig in!


### Addition

As you’d guess, you can add two numbers in Python using the ‘+’ character:

```python

2 + 2

#returns 4

```

You can chain multiple addition operators together, just as you can in conventional mathematics. An example is below:

```python

2 + 3 + 5

#returns 10

```


### Subtraction

Similar to addition, the subtraction operator in Python is exactly what your intuition would suggest. Subtraction is performed using the ‘-’ character in Python:

```python

2 - 1

#returns 1

```

Like addition, subtraction operations can be chained together. An example is below:

```python

10 - 2 - 3

#returns 5

```


### Multiplication

In Python, multiplication is performed using the asterisk, or *. An example is below:

```python

2 * 2

#returns 4

```

As with the other math operators, multiplication operations can be chained together. An example is below:

```python

2 * 3 * 4

#returns 12

```


### Division

Division is performed in Python using the forward slash ‘/’. For example, if you want to divide 6 by three, you’d do so using the following code:

```python

6 / 3

#returns 2

```

Division can also be chained together like the other operators we’ve discussed, but you’ll want to be careful that the order of operations is being executed as desired. If you’re worried about this, you can force a specific order of operations using brackets (which we explore later in this lesson). 


### Exponents

Exponents in Python are implemented with the double asterisk (**). As an example, 2 to the 4th power is calculated as follows:

```python

2**4

#returns 16

```


## Remainders

The [remainder](https://en.wikipedia.org/wiki/Modulo_operation) function is a lesser-known mathematical function defined as the polynomial "left over" after dividing one polynomial by another. As an example, the remainder of 18 divided by 4 is 2, because 16 divides evenly into 4 and 18 minus 16 is 2.

Dealing with remainders can be difficult on paper but is very easy in Python. You can calculate remainders using the ‘%’ character. An example is below:

```python

18%4

#returns 2

```


## Brackets

In Python, you can force your mathematical operations to execute in a certain order by using brackets. As an example, let’s say you had the following code:

```python

2 + 3 * 20

#Returns 62

```

This code will first execute the 3*20 (giving 60) and then add 2, which gives 62. If you wanted the addition to be implemented prior to the division, you’d wrap it brackets like this:

```python

(2 + 3) * 20

#returns 100

```

Note that round brackets, curly brackets, and square brackets are _not_ equivalent in Python. This code would not execute in the same manner as the previous example:

```python

[2 + 3] * 20

#WRONG - Don't Do This!
```

We’ll discuss how to properly use curly brackets and square brackets when we talk about data structures later in this course.


## A Note on Whitespace

In programming, all of the spaces (and tabs) included in your programming are called ‘whitespace’. I wanted to pause the lesson for a moment to discuss how whitespace impacts your code.

The short answer is that whitespace _doesn’t_ effect your code. To be specific, putting spaces between your math operations does not effect their meaning. A few examples:

```python

2**4

#returns 16

2 ** 4

#also returns 16

2+2

#returns 4

2          +          2

#also returns 4

``` 


## Variables in Python

In Python, we generally do not perform mathematical operations using numbers directly. We instead assign those numbers to variables and then manipulate the variables.

As an example, consider the following code:

```python

a = 1

b = 2

a + b 

#returns 3

```


### Variable Overwriting

Variable names are easily overwritten in Python (except in certain specific cases that we’ll discuss later). For example, if you executed the following code and printed the value in variable b, the value would be 4.

```python

b = 6

b = 4

#b returns 4

```


### Best Practices on Variable Naming

When creating variable names in Python, there are a few best practices that we should make sure to follow.

First, variable names cannot contain spaces. So you cannot name a variable ‘my name’. Instead, we use underscores - so the equivalent variable would be my_name.

Oftentimes, we don’t use underscores but instead practice a naming convention called “[camel case](https://en.wikipedia.org/wiki/Camel_case)” (sometimes stylized as camelCase). Camel case lists all of the word together without spaces, and capitalizes all of the first letters _except the first word_. 

Here are a few examples of camel case variable names:

```python

myVariableName

thisCourseIsFun

pythonIsTheBestLanguage

```


## Conclusion

In this lesson, we discussed comments, operations, and variables in the Python programming language. These are the very foundations of Python - you should make sure to have a firm grasp on them before proceeding further through this course. 
