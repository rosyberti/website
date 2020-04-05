---
layout: page
title: Functions
---

In this lesson, we will explore functions, which are one of the most important elements of a fully-fledged Python application.


## What Are Functions?

A function is a chunk of code that takes an input, performs computations, and produces an output. Functions can do anything from basic mathematics to create useful documents for non-technical users (like PDFs or Microsoft Word documents).

Functions are always defined with the `def` keyword. It is a best practice to place a `docstring` in each Python function, which is a multi-line comment that describes what the function does. 

After the `def` keyword is used to create the function's action, the function's name is written followed by round brackets. 

Any inputs required for the function (called `arguments`) are passed into these round brackets. After that, the computations performed by the function are indented (similar to the indents used by `if` statements and `for` and `while` loops. 

Functions can return an output, but they do not have to. Functions that do have an output specify that output using the `return`. Functions that do not have an explicit `return` statement will return `None`. 

It might be puzzling why you would want to create a Python function that has no output. There are many cases - oftentimes, functions that have no output are designed to interact with something outside the program itself. Examples include making modifications to an outside database, sending an email, or querying a website. 

You've just done plenty of reading about functions, but you haven't actually seen one yet! The time is now. You can see an example of a function that prints an inputted string 5 times below:

```python

def new_function(string):

	"""The docstring goes here"""

	print(string)

	print(string)

	print(string)

	print(string)

	print(string)

```

Functions can contain any type of code that we've discussed already in this course. Because of this, a much more efficient way to write the function above would be to wrap it in a `while` loop, like this:

```python

def new_function(string):

	"""The docstring goes here"""

	i = 0

	while (i < 5):

		print(string)

		i += 1

```

Note that the actions performed within the function's `while` loop are indented _twice_  - once for the `while` loop and once for the function. This double indenting makes it easy to create bugs in your code, so please be diligent about indenting your code appropriately whenever you include a loop within a function. 


## Function Docstrings

All functions should have a docstring, which is an embedded string within the function that describes its purpose and functionality. 

Docstrings are created at the start of the function and wrapped in triple-quotes. To provide another example, here's how you could create a docstring within a function called `this_function`:

```python

def this_function():

	"""This function serves to demonstrates how docstrings work."""

	return 'Docstrings are awesome!'

```

Docstrings are designed to be extremely useful for outside users of your code. Because of this, there is an embedded method that allows you to easily print your docstring at a later date. Simply use the `__doc__` method to print out the docstring of a function.

An example of this is below:

```python

def multiplyByFive(integer):

	"""This function takes in an integer and multiplies it by 5."""

	return integer*5

print(multiplyByFive.__doc__)

#Returns 'This function takes in an integer and multiplies it by 5.'

```

This `__doc__` method can be used even when you haven't created the function yourself. To test this out, try typing the following commands into your Jupyter Notebook:

```python

print.__doc__

sum.__doc__

len.__doc__

```

We haven't seen leading underscores (meaning underscores at the beginning of words) in variable or function names yet in this course. They are used to indicate that a variable or function is primarily intended for internal use by the programmer who created them.

We've covered the basics of functions so far in this lesson. Given their complexity, the best way to learn functions is by practicing examples of increasing difficulty. We will work through 3 more examples together to conclude this lesson. 


## Function Example #1: How To Calculate The Length of a String in Python

In this course, we have used the `len()` function to calculate the length of strings and lists. We will now build a function from scratch called `myLen()` that has the same functionality.

To start, initialize the function with the `def` keyword with the argument `item` and create the docstring:

```python

def myLen(item):

	"""Docstring"""

```

Noticed how I filled the docstring with the placeholder word `Docstring`. That's because I want this docstring to match the docstring of the normal `len()` function. To find the docstring of `len()`, type `len.__doc__` into your Jupyter Notebook. You will get the following output:

```

'Return the number of items in a container.'

```

Let's place this docstring into our `myLen()` function:

```python

def myLen(item):

	"""Return the number of items in a container."""

```

**Before reading further, please attempt to fill in the rest of the function yourself! Think about the logic necessary to complete the desired task and map it out on paper if necessary. If you're stuck, keep reading for a more detailed walkthrough.**

Ok, let's keep going! The easiest way to calculate the length of a string or list is to loop through each item in the string or list, and add `1` to a specified variable each time the loop is completed. Specifically, the loop should look something like this:

```python

length = 0

for i in item:

	length += 1

```

Placing a `return` statement after that loop is all we need to complete the function!

```python

def myLen(item):

	"""Return the number of items in a container."""


	length = 0


	for i in str:


		length += 1


	return length

```


## Function Example #2: How To Reverse A String In Python

Let's start by creating a function template called `stringReverser` that takes in a string and returns a reversed version of that string (where the last character becomes the first character, and so on). We'll place some useful text within the docstring as well. Here's what this should look like:

```python

def stringReverser(string):

	"""This function reverses a string."""

```

We also know that the output of this function will be a reversed string, so we can add an empty string `reversedString` at the start of the function and `return reversedString` as the `return` statement:

```python

def stringReverser(string):

	"""This function reverses a string."""

	reversedString = ""

	return reversedString

```

**Before reading further, please attempt to fill in the rest of the function yourself! Think about the logic necessary to complete the desired task and map it out on paper if necessary. If you're stuck, keep reading for a more detailed walkthrough.**

We'll again approach this using a loop, but instead of loop from the start of the string until the end of the string, we'll loop from the end of the string to the start. 

We'll need to assign our increment operator an initial value of `len(string) - 1` (the `- 1` is required because Python is zero-indexed, remember) and instead of increasing the increment operator with each loop iteration, we will need to decrease its value with each loop iteration. We can decrease its value with each loop iteration using the `decrement operator`, which is specified by `-=` in Python.

Here's what this would look like in practice:

```python

i = len(string) - 1

while i >= 0:

	reversedString = reversedString + string[i]

	i -= 1

```

Placing this loop inside our function completes it:

```python

def stringReverser(string):

	"""This function reverses a string."""

	reversedString = ""

	i = len(string) - 1


	while i >= 0:


		reversedString = reversedString + string[i]


		i -= 1

	return reversedString

```


## Function Example #3: How To Calculate Absolute Value in Python

Next, we will build a function that calculates absolute value. For those unfamiliar with absolute value, it is a mathematical concept that removes any concept of positive or negative. In other words, the absolute value of all numbers is positive. 

Let's start by creating a blank function with a docstring, as before:

```python

def absoluteValue(number):

	"""This function takes in a number and returns its absolute value."""

```

We also know that we will be returning the number after some possible modifications to it, so we can include our `return` statement:

```python

def absoluteValue(number):

	"""This function takes in a number and returns its absolute value."""

	return number

```

**Before reading further, please attempt to fill in the rest of the function yourself! Think about the logic necessary to complete the desired task and map it out on paper if necessary. If you're stuck, keep reading for a more detailed walkthrough.**

Calculating absolute value is usually done through an `if` statement:

```python

if(number < 0)

	number = -number

```

Placing this `if` statement within the function completes the problem:

```python

def absoluteValue(number):

	"""This function takes in a number and returns its absolute value."""

	if(number < 0)

		number = -number

	return number

```


## Moving On

This lesson provided a basic introduction to Python functions. 

I fully recognize that functions are the hardest topic covered so far in this course, so do not worry if you had a difficult time understanding them right away. In the next lesson, you will be exposed to plenty of practice problems (and solutions) that will make you a function master before you know it!
