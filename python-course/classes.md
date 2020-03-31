---
layout: page
title: Classes
---


In this last lesson of this course, we will explore Python classes, which provide a means of combining data and functionality.


## What Are Classes?

Classes are types of objects in Python. Classes allow you to create multiple occurences of the same class, which are called `instances`. Classes also can include methods similar to the methods that we have used already in this course. 

Although you may not have known it at the time, we have used many classes already in this course, including `int` - the integer class, and `str` - the string class. Creating customizable classes is very useful and will be explained throughout the rest of this lesson.

To create a new class, we use the keyword `class`. Class names are somewhat unique in Python because they are one of the only variable names that should not follow camelCase. Instead, class names should have their first letter capitalized.

After that, we name the class and place a colon before an indented block that specifies the class's attributes and methods.

In a very basic example, here is how we would create a class called `Person` which has an attribute called `age` that is given a default value of `0`:

```python

class Person:

	age = 0

```

Once a class is created, we can create `instances` of this class, which have their own variable values but inherit the methods from the parent class. The instance is created using a function called `__init__`. Note that since the `__init__` function is missing from the `Person` class that we created in the example above, there is actually no way for us to create a new instance of `Person`.

To fix this, let's add the `__init__` function to the `Person` class. By convention, `__init__` functions should always go at the start of class declarations, like this:

```python

class Person:

	def __init__ (self, age):

		self.age = age

```

You will likely be puzzled by the `self` variable contained in the block of code above. What is the `self` parameter? It is a reference to the current instance of the class and is used to access variables that belong to that instance of the class.

Note that, like many variables we have seen throughout this course, the `self` variable can be named whatever you like. The only restriction is that it must be the first argument that is passed into the `__init__` function. Here's an example of the same class that uses `x` instead of `self`:

```python

class Person:

	def __init__ (x, age):

		x.age = age

```

While `self` can be changed to whatever you like, the `self` keyword is generally considered a best practice and you should have a good reason before you use something other than `self`.

Another concept you should take away from the `Person` class is that while we simply wrote `age = 0` in our first draft of the class, we changed this to `self.age = age` in a later version. 

This is because age was actually passed into the `__init__` function as an argument, which means we must call `age` from `self` using the dot operator.

The only time you can write a normal variable declaration like `age = 0` within a class is when that variable is not passed in as part of the class's `__init__` function. 

Let's continue building out our `Person` class. Specifically, let's try and accomplish the following:



*   Track how many parking tickets the person has in a static variable called `parkingTickets` with an initial value of 0
*   Create a method called `giveParkingTicket()` that increases the value of the `parkingTickets` variable by 1

We'll use the `self` keyword moving forward. To recap, here's where our code left off:

```python

class Person:

	def __init__ (self, age):

		self.age = age

```

First, let's create the `parkingTickets` variable and assign it an initial value of 0 like this:

```python

class Person:

	def __init__ (self, age):

		self.age = age

	

parkingTickets = 0

```

Next, we'll need to create the `giveParkingTicket()` function. Like we did in our last lesson, let's start by creating a blank version of the function with a docstring:

```python

class Person:

	def __init__ (self, age):

		self.age = age

	

parkingTickets = 0

	

def giveParkingTicket(self):


    """This function increases the value of parkingTickets by 1"""	

```

Since `giveParkingTicket()` does not need to return anything (its simply modifying the value of an outside variable), we know that no `return` statement is necessary. Instead, we can simply increment the `parkingTickets` variable using the `+= 1` increment operators:

```python

class Person:

	def __init__ (self, age):

		self.age = age

	

parkingTickets = 0

	

def giveParkingTicket(self):


    """This function increases the value of parkingTickets by 1"""	


    parkingTickets += 1

```

And we're done! We now have a working class with a dynamic variable `age`, a static variable `parkingTickets`, and a function `giveParkingTickets()`. 

The next step is understanding how to create instances of this class. We can create instances of any class by using the class's name and assigning it to a variable, like this:

```python

me = Person(24)

```

Once your first `Person` instance is created, you can access its attributes (both static and dynamic) using the dot operator:

```python

print(me.age)

#Returns 24

print(me.parkingTickets)

#Returns 0

```

You can also use the dot operator to call methods:

```python

me.giveParkingTicket()

print(me.parkingTickets)

#Returns 1

```


## Moving On

Classes are the hardest topic discussed in this course. Understanding them is critical. Because of that, the practice problems lesson that we'll navigate to next is the longest sequence of practice problems in this course. Grab a cup of your favorite coffee and get to work!
