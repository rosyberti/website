---
layout: page
title: Loops
---

In the last lesson of this course, we discussed logical operators and if statements, which are the smallest building blocks of real-world Python applications.

We will discuss the two larger building blocks of applications over the next two lessons: loops and classes.

First, let's talk about loops.


## What Are Loops?

In computer programming, loops are reusable blocks of code that execute based on some outside criterion. They are similar to if statements but can be executed multiple times.

There are multiple types of loops. The first type of loop that we will talk about is the `for` loop.


## The `For` Loop

The `for` loop exists to perform some operations _for_ every element in some outside data structure. In this lesson, that outside data structure will generally be a list, but you can also loop over tuples, sets, and other data structures.

The general structure of a `for` loop looks like this:

```python

for x in list:

	action

```

Let's break this down:

	



*   `x` is simply a placeholder variable name. Many novice Python programmers get confused about what `x` is, so let me be clear: `x` can be WHATEVER you want! We'll explore this more later.
*   `list`: this is the outside data structure that we are looping over.
*   `action`: this is the code that you want to run every time the loop is executed.

Here is an example of a real `for` loop:

```python

canadianPrimeMinisters =[

                        'Justin Trudeau',

                        'Stephen Harper',

                        'Paul Martin',

                        'Jean Chretien',

                        'Kim Campbell',

                        'Brian Mulroney'

                        ]

for primeMinister in canadianPrimeMinisters:

    print(primeMinister)

```

Here's the output of that loop:

```python

Justin Trudeau

Stephen Harper

Paul Martin

Jean Chrétien

Kim Campbell

Brian Mulroney

```

Remember when I said that `x` can be whatever you want? In this loop, `primeMinister` is the equivalent of `x`. Since you can name that variable whatever you'd like, each of these `for` loops are _exactly the same:_

```python

for x in canadianPrimeMinisters:

    print(x)

for smellyCat in canadianPrimeMinisters:

    print(smellyCat)

for cliffordTheDog in canadianPrimeMinisters:

    print(cliffordTheDog)

```

For obvious reasons, it is ideal to make `x` something that is easy for outside software engineers to understand. In this case `primeMinister` was likely the best choice. With that said, it is important to understand that you have complete flexibility over how to name that variable, and its name does not impact how the code runs whatsoever. 


## The `While` Loop

The `while` loop exists to continue running _while_ some outside condition continues to be satisfied. 

While loops have the following general syntax:

```python

while(condition):

	action

```

As you might have guessed, `while` loops present a bit of a problem. It is possible to create a `while` loop that runs indefinitely. This is called an infinite loop and is a common source of problems in software development. 

Here is an example of an infinite loop:

```python

bool = True

while(bool):

	print("This is an infinite loop, and this will print A LOT.")

```

To prevent this, we typically introduce _increment variables_ before a `while loop` and increase the increment variable each time the loop is completed. Increment variables are often given the variable names `i`, `j`, or `k`. 

Increment variables are increased with each repetition of the loop using increment operators, which increase the value of a variable by 1. The increment operator is denoted by `+= 1` in Python. 

Here is an example of an increment operator in Python:

```python

i = 1

i += 1

i 		#To print its new value

#Returns 2

```

Here is an example of a while loop that appropriately uses an increment variable:

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

Increment variables are very important for avoiding infinite loops in Python. Please make sure to use them wisely before getting stuck in a dreaded infinite loop!


## The Relationship Between For Loops and While Loops

Although `for` loop and `while` loops seem quite different on the surface, it is actually common to see situations where `for` loops and `while` loops can both adequately solve a problem.

For example, imagine that you have a list of ingredients for a pizza and you want to loop through the ingredients and print them out.

Here is how you could solve this problem using a `for` loop:

```python

ingredientList = ['mushrooms', 'bacon', 'green peppers', 'pepperoni', 'cheese']

for ingredient in ingredientList:

	print(ingredient)

```

Here is how you could solve this problem using a `while` loop: 

```python

ingredientList = ['mushrooms', 'bacon', 'green peppers', 'pepperoni', 'cheese']

i = 0

while i < len(ingredientList):

    print(ingredientList[i])

    i += 1

```

In another example, imagine that you have a list of students in a class, and you want to ask them if they are present.

Here is how you could solve this problem using a `for` loop:

```python

students = ['Nick', 'John', 'Joe']

for student in students:

	print(f'Is {student} here?')

```

Here is how you could solve this problem using a `while` loop:

```python

students = ['Nick', 'John', 'Joe']

i = 0 

while i < len(students):

	print(f'Is {students[i]} here?')

	i += 1

```

As you can see, it is fairly straightforward to relate `for` loops to `while` loops. Make sure that you understand the relationship between `for` loops and `while` loops, as there will be numerous questions on this topic in this lesson's associated practice problems. 


## Moving On

In this lesson, we explored `for` loops and `while` loops, which are fundamental building blocks to any Python program. We'll round out your understanding of these topics in the next lesson by creating many loops from scratch in our practice problems. 
