---
layout: page
title: Logical Operators and If Statements
---

We just finished a thorough overview of the major data structures in Python, including:

*   Integers
*   Strings
*   Lists
*   Tuples
*   Dictionaries
*   and Sets

However, all of the data structure knowledge in the world is not enough to build real-world applications. There is a common saying in computer programming:

_"Data Structures + Algorithms = Applications"_

In this lesson, we'll begin learning about logical operators, which are the backbone of the algorithms you'll need to build full applications later in your career. 

This will be one of the longest lessons in this course, but it is also one of the most important, so please make sure you understand these concepts thoroughly before proceeding. 


## A Quick Review of Booleans

I briefly introduced the concept of boolean variables in an earlier lesson of this course. Understanding boolean variables is extremely important for learning the content of this lesson, so a quick review is merited.

Boolean variables are a special data structure that can only be assigned two values: `True` or `False`. The values are not wrapped in quotes, and the first letter must be capitalized. 

Examples of each boolean variable value are below:

```python

trueBool = True

falseBool = False

```

Throughout this lesson, we will see how boolean variables can be used to control whether or not a block of code is executed. 

We need to understand how to generate boolean variables first. Let's cover that next.


## Equality Operators

As you might imagine by the nature of boolean variables, they are used to represent whether a certain statement is true or not. The most basic form of these statements is an equality statement:  are two things equal to one another?

Python has a built-in way to check this statement for two variables. It is called the equality operator and is represented by `==`. The equality operator returns `True` if two variables are equal and `False` if they are not equal.

Here are five examples of the equality operator in action:

```python

'Nick' == 'Not Nick'

#Returns False

"Nick" == 'Nick'

#Returns True

a = 1

b = 2

a == b

#Returns False

a + 1 == b

#Returns True

boolean_variable = True

boolean_variable == False

#Returns False

```

Please make sure to understand all of these examples before proceeding. Specifically, be sure to understand the difference between `=`, the assignment operator, and `==`, the equality operator. 


## Inequality Operators

The inequality operator is the opposite of the equality operator. It tests whether two variables are _not_ equal to each other. The inequality operator is represented by `!=` in Python.

Five examples of the inequality operator are listed below:

```python

trueBoolean = True

falseBoolean = False

trueBoolean != falseBoolean

#Returns True

trueBoolean != True

#Returns False

falseBoolean != False

#Returns False

1 != two

#Returns True

'String' != 'string'

#Returns True (notice the difference in capitalization on the 's')

```

Given that the equality operator and the inequality operator are polar opposites of one another, you might be wondering if there is any way to relate the two. There is, and it is called the 'not' operator. 


## Chaining Equality Operators Together

You can easily chain together equality and inequality variables in Python. Here is an example, which tests for whether someone is over 65, likes to dance, and has grey hair:

```python

isOver65 = True
likesToDance = True
hasGreyHair = False

True == isOver65 == likesToDance == hasGreyHair
#Returns False

```


## The 'Not' Operator

The word 'not' is a special keyword in Python that modifies the value of a boolean variable. Specifically, it changes `True` values to `False` and `False` values to `True`.

Two examples are below:

```python

isNickCool = True

not isNickCool

#Returns False

```


## Storing Equality Tests in Variables

Testing for equality or inequality is useful, but it becomes significantly more useful when you start to store the outputs of these tests in variables. You can do this using the assignment operator `=` that we have been relying on throughout this course. Let's peruse three examples to understand this properly.

As you can tell, I find it useful to write my boolean variable names as quasi-questions so that I can easily remember the statement that they're store a `True` or `False` value for. Variable names like `isNickCool` or `hasGreyHair` allow us to easily recognize what statement they're representing. 

Here are a few examples of storing equality tests in variables:

```python
int1 = 1
int2 = 2
areTheIntegersEqual = int1 == int2

myName = 'Nick'
myFriendsName = 'Levi'
doWeHaveTheSameName = myName == myFriendsName
```

So far, we have discussed how to test for equality and inequality, and how to store those tests' outputs in variables. We have also explored how to change the value of a boolean variable using the 'not' operator. 


## The `and` and `or` Operators

It is often useful to be able to test boolean logic in an all-or-nothing fashion. More specifically, we often would like to return `True` if all conditions are met and `False` if one or more conditions are not met. 

The `and` operator is the best way to do this. An example of the `and` operator is below:

```python

True and True and True

#Returns True

 \
True and False and True

#Returns False

```

Having a more realistic example is helpful for understanding how the `and` operator is used in practice:

```python

sunnyDay = True

rainyDay = False

sunnyDay and rainyDay

#Returns False

```

In a slightly different scenario, it can be useful to return `True` if even a single value is true, and return `False` only if all values are false. The `or` operator allows us to do this. 

An example of the `or` operator is below: 

```python

True or False

#Returns True

False or False

#Returns False

```

Again, a more realistic example is helpful:

```python

sunnyDay = True

rainyDay = False

sunnyDay or rainyDay

#Returns True

```

Comparison Operators

While the equality and inequality operators were used earlier in this lesson to test the equality (or lack thereof) of two variables, the comparison operators are used to _compare_ values.

There are four comparison operators in Python, and their syntax mimics their mathematical counterparts:

```python

>

&lt;

>=

&lt;=

```

Examples of how to use these comparison operators are demonstrated below:

```python

1 &lt; 2

#Returns True

2 &lt; 1

#Returns False

1 > 0

#Returns True

0 > 1

#Returns False

1 &lt;= 2

#Returns True

3 &lt;= 2 

#Returns False

3 &lt;= 3 

#Returns True

3 >= 3

#Returns True

3 >=  2

#Returns True

2 >=  3

#Returns False

```

We have spent a great deal of time in this lesson learning various logical operators. In the next section, we will learn how to use

If Statements

'If statements' are used in computer programming to control whether or not a block of code is executed depending on some outside condition. In Python, if statements are controlled by boolean variables.

If statements have the following general syntax in Python:

```

if(statement):

	action

```

Let's break this down:



*   **Statement**: this is a boolean condition that controls whether or not the code in the if statement will run
*   **Action**: this is the code that will run if the 'statement' is `True`. The indent before this action is key - without the indent after the if statement's colon, the code will not compile correctly and will throw an error. 

Let's consider a real example of an if statement in action:

```python

age = 20

if(age &lt; 20):

	print("You are less than 20 years old!")

if(age == 20):

	print("You are exactly 20 years old!")

if(age > 20):

	print("You are more than 20 years old!")

```

If statements can also be used to modify other variables. 

For example, consider an hourly working being paid $25/hour who gets 2x overtime for all hours above 40 hours per week. This section of if statements calculates his weekly compensation after accounting for his overtime pay:

```python

totalHours = 37

hourlyPay = 25

if(totalHours &lt; 40):

	weeklyPay = totalHours * hourlyPay

if(totalHours >= 40):

	weeklyPay = 40 * hourlyPay + (totalHours - 40) * 

```


## ElseIf and Else Statements

As we saw in the last section, you can pair together multiple if statements to account for different scenarios. In this section, we will discuss a better, more readable way of using different logic scenarios: if else statements.

If else statements are another way to run conditional code that is considered more readable than chained if statements. If else statements have the following appearance:

```python

if(statement)

	action

else:

	different action

```

An example of this logic is below:

You can also use `elif` statements to test multiple conditions before executing the catch-all code held within the `else` block. `Elif` stands for 'else if', and is executed as follows:

```python

if(statement1)

	action1

elif(statement2):

action2

else:

	action3

```

There is no limit to how many `elseif` statements can be in one statement. For example, consider the following code:

```python

items = 7

if(items == 0):

    print('There are no items in your shopping cart.')

elif (items == 1):

    print('There is 1 item in your shopping cart.')

elif (items == 2):

    print('There are 2 items in your shopping cart.')

elif (items == 3):

    print('There are 3 items in your shopping cart.')

elif (items == 4):

    print('There are 4 items in your shopping cart.')

elif (items == 5):

    print('There are 5 items in your shopping cart.')

elif (items == 6):

    print('There are 6 items in your shopping cart.')

elif (items == 7):

    print('There are 7 items in your shopping cart.')

elif (items == 8):

    print('There are 8 items in your shopping cart.')

elif (items == 9):

    print('There are 9 items in your shopping cart.')

elif (items == 10):

    print('There are 10 items in your shopping cart.')

else:

    print(f'There are too many items to count in your shopping cart!')

```

**Important Note:** The code above is for illustation's purpose only. The best way to solve the shopping cart item would be to use the f string interpolation that we learned earlier in this course, like this:

```python

items = 20

if(items == 0):

    print('There are no items in your shopping cart.')

elif (items == 1):

    print('There is 1 item in your shopping cart.')

else:

    print(f'There are {items} items in your shopping cart!')

#Returns 'There are 20 items in your shopping cart!'

```


## Moving On

This lesson provided a detailed explanation of logical operators and if statements in Python.

This is unquestionably the hardest topic we've covered yet in this course. To make sure you understand it fully, the next lesson of this course will work through numerous practice problems to help you solidify your knowledge of these fundamental concepts. 
