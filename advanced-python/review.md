---
layout: page
title: A Review From Introduction To Python
---

This course is designed as a natural followup to my Introduction to Python course. In other words, you should be able to finish that course and start this course without any hiccups.

There are bound to be students who take this course who did not come from Introduction to Python. Because of that, I wanted to start this course with a rapid-fire review of the topics covered in my beginner course. It would be wise to review any topics in this lesson that you're unfamiliar with before proceeding through the rest of the course. 


## How To Install Anaconda

This course will use the Anaconda distribution of Python for all of its programming. Specifically, we will be working within Jupyter Notebooks. 

If you do not already have Anaconda installed on your computer, please [visit this page for a step-by-step tutorial.](https://nickmccullum.com/python-course/how-to-install-anaconda/)

## Comments, Operations, and Variables

Comments are created in Python using the `#` character:

```python

#This is a comment in Python

```

Multi-line comments are created using triple-quotes:

```python

"""

This

is 

a

multi-

line

comment

in

Python

"""

```

Variables are assigned in Python using the `=` operator. Two examples are below:

```python

var1 = 1

var2 = 3

```

Boolean variables are a special type of variable that can only store two values: `True` and `False`.

Once variables are created, you can perform operations with them:

```python

a = 3

b = 7

a + b 

#Returns 10

```


## Strings and String Methods

Strings are sequences of characters in Python. Strings are created by wrapping text in either single quotes (`'`) or double quotes (`"`).

Strings can be concatenated using  the `+` operator:

```python

first_word = 'Hello'

space = " "

second_word = 'World'

first_word + space + second_word

#Returns 'Hello World'

```

Variables can be interpolated into a string by placing an `f` outside the first quote and placing the variable name in curly brackets:

```python

sales = 400

f"Our sales so far this month are {sales}!"

#Returns "Our sales so far this month are 400!"

```

You can use various functions and methods to modify strings or learn more about them:



*   `len(string)`: Calculate the length of a string
*   `string.upper()`: Transforms a string into all uppercase letters
*   `string.lower()`: Transforms a string into all lowercase letters
*   `string.replace(old, new)`: Replaces an old character in a string with a new character


## Lists

Lists are ordered sequences of elements. Lists are created with square brackets:

```python

myList = [0, 1, 2, 3]

```

Specific items of a list can be accessed or modified using square brackets:

```python

theList = ['one', 'two', 'three']

theList[0]

#Returns 'one'

theList[0] = 1

theList[1]

#Returns 1

```

Here are some important functions and methods that can be performed on lists:



*   `len(list)`: Calculate the length of a list.
*   `sum(list)`: Calculate the sum of all the elements in a list.
*   `min(list)`: Identify the minimum value from a list.
*   `max(list)`: Identify the maximum value from a list.
*   `list.append(element)`: Append a new element to the end of an existing list.
*   `list1.extend(list2)`: Add all of the elements of list2 to the end of list1.


## Tuples

Tuples are ordered sequences of elements, just like lists. However, tuples cannot be modified after their creation. Tuples are called `immutable` because of this. 

Tuples are created with round brackets:

```python

a_tuple = (1, 2, 3)

```

While tuples cannot be modified, it is possible to overwrite them entirely:

```python

the_tuple =(1, 2, 3)

the_tuple =(4, 5, 6)

print(the_tuple)

#Returns (4, 5, 6)

```

Here are some important functions and methods that can be performed on tuples:



*   `tuple.count(element)`: Counts the number of times `element` appears in `tuple`.
*   `tuple.index(element)`: Returns the index of `element` in `tuple`.


## Dictionaries

Dictionaries are unordered collections of key-value pairs. Dictionaries are creation with curly brackets:

```python

countryPopulations = {

    'China': 1433783686,

    'India': 1366417754,

    'United States': 32906491

}

```

You can pass a key from a dictionary's key-value pair into the dictionary's square brackets to return the value. An example is below:

```python

simpleDict = {'key': 'value'}

simpleDict['key']

#Returns 'value'

```

Here are some important functions and methods that can be performed on dictionaries:



*   `dictionary.keys()`: Returns a list of the keys from the dictionary. Ideally, you will wrap this method in a `list()` function.
*   `dictionary.values()`: Returns a list of the values from the dictionary. Ideally, you will wrap this method in a `list()` function.
*   `dictionary.clear()`: Clears all of the key-value pairs out of a dictionary.
*   `dictionary.pop(key)`: Removes the key-value pair whose key is `key` from the dictionary.


## Sets

Sets are unordered collections of unique elements. They are wrapped in curly brackets (similar to dictionaries, except their elements are not key-value pairs):

```python

The_set = {1, 2, 3}

```

Here are some important functions and methods that can be performed on sets:



*   `len(set)`: Calculates the length of a set.
*   `set.add(element)`: Adds `element` to `set`.
*   `set.remove(element)`: Removes `element` from `set`. Raises an error if `element` is not in `set`.
*   `set.discard(element)`: Removes `element` from `set`. Does not raise an error if `element` is not in `set`.


## Logical Operators and If Statements

You can test equality between two variables in Python using the `==` operator:

```python

var1 = 'Yes.'

var2 = 'No.'

var3 = 'Yes.'

var1 == var2

#Returns False

var1 == var3

#Returns True

```

The inequality operators `!=` tests for inequality:

```python

var1 != var2

#Returns True

```

The `and` and `or` operators allow us to test whether everything is `True` (for the `and` operator) or whether everything is `False` (for the `or` operator):

```python

True `and` True `and` True

_#Returns True_

True `and` False `and` True

_#Returns False_

_True `or` False_

_#Returns True_

_False `or` False_

_#Returns False_

```

Python also has four comparison operators that allow us to compare the values of numerical variables:

```python

>

#Greater than

<

#Less Than

>=

#Greater than or equal to

<=

#Less than or equal to

```

Python's `if` statements allow us to execute code based on the value of an outside variable or statement. They have the following appearance:

```python

if(statement):

	action

```

Here is an example of three `if` statements that print different text depending on a person's `age`:

```python

age = 20

if(age < 20):

	print("You are less than 20 years old!")

if(age == 20):

	print("You are exactly 20 years old!")

if(age > 20):

	print("You are more than 20 years old!")

````

We can also use `elif` and `else` statements ,which is considered more readable. 

```python

age = 20

if(age < 20):

	print("You are less than 20 years old!")

elif(age == 20):

	print("You are exactly 20 years old!")

else:

	print("You are more than 20 years old!")

````


## Loops

Python's `for` loops allow us to perform an operation for every element in an outside data structure. An example of a `for` loop is below:

```python

canadianPrimeMinisters =[

                        'Justin Trudeau',

                        'Stephen Harper',

                        'Paul Martin',

                        'Jean Chrétien',

                        'Kim Campbell',

                        'Brian Mulroney'

                        ]

for primeMinister in canadianPrimeMinisters:

    print(primeMinister)

```

Python's `while` loops allow us to continue executing a block of code as long as a certain statement evaluates to `True`. When using `while` loops, you must be careful not to create an infinite loop. 

An example of a `while` loop is below:

```python

numberString = ""

#Note - this is an empty string that we will be adding characters to in each iteration of the loop. 

#When you're modifying an outside data structure in a loop, 

# that data structure must be created outside the loop before the loop begins.

i = 0

while(i <= 10):

	numberString = numberString + str(i)

	#The line above adds each number to the string. 

	#The str() operator transforms the integer into a string. 

	#Without the str() operator, this concatenation would not be possible.

	

	i += 1

	#The line above increases the value of the increment variable.

	

print(numberString)

#Returns '012345678910' (which is a string, not an integer)

```

It is important to understand that for every `for` loop, there is an equivalent `while` loop. The opposite is also true: for every `while` loop, there is an equivalent `for` loop. As an example, the following two loops have identical functionality:

```python

students = ['Nick', 'John', 'Joe']

for student in students:

	print(f'Is {student} here?')

i = 0 

while i < len(students):

	print(f'Is {students[i]} here?')

	i += 1

```


## Functions

A function is a chunk of code that takes an input, performs computations, and produces an output. Functions are always defined with the `def` keyword and contain a `docstring`, which is a multi-line comment that describes the purpose and functionality of the function.

An example of a function is below:

```python

def new_function(string):

	"""The docstring goes here"""

	i = 0

	while (i < 5):

		print(string)

		i += 1

```


## Classes

Classes are types of objects in Python. Classes allow you to create multiple occurences of the same class, which are called `instances`. Classes also can include methods that allow you to perform operations on specific instances of the class.

To create a new class, we use the keyword class. Class names are somewhat unique in Python because they are one of the only variable names that should not follow camelCase. Instead, class names should have their first letter capitalized. Classes are defined with an `init` method, which specifies their dynamic variables. 

An example of a class called `Person` with a dynamic variable called `age` and a static variable called `parkingTickets` is below. The class also has a method called `giveParkingTicket` that increases the value of the `parkingTickets` variable by 1.

```python

class Person:

	def __init__ (self, age):

		self.age = age

	

	parkingTickets = 0

	

	def giveParkingTicket(self):

    		"""This function increases the value of parkingTickets by 1"""	

    		parkingTickets += 1

```


## Moving On

This lesson provided a rapid-fire review of the material from my Introduction to Python course. If everything in this lesson made sense to you, then you are ready to proceed to the next lesson, which will teach you how to import external libraries into a Python program.
