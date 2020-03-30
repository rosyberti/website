---
layout: page
title: Tuples and Tuple Methods
---

In the last lesson of this course, we discussed lists, which are arguably the most important data structure in the Python programming language. In this lesson we'll discuss tuples, which are similar to lists but with one important difference. 


## What Are Tuples?

Tuples are ordered sequences of elements - just like lists. The difference between lists and tuples is that lists are mutable and tuples are immutable. 

As a reminder, 'mutability' refers to whether a data structure can be modified after its creation. 

A mutable data structure can be modified while an immutable data structure cannot be modified. Said differently, you can modify lists after their creation but you cannot modify tuples after their creation.

Tuples are characterized by round brackets (instead of square brackets like lists):

```python

my_tuple = ('this', 'is', 'a', 'tuple')

```

Like lists, tuples do not necessarily need to contain all of the same data types within them. For example, this is a perfectly valid tuple:

```python

anotherTuple = (['this', 'is', 'a', 'nested', 'list'], 1, 'string', ('nested', 'tuple'))

```

Since tuples are immutable, you cannot modify the items within the tuple. For example, if you tried to run this code:

```python

my_tuple = (1, 2, 3)

my_tuple[0] = 2

```

Then you would receive this error message:

```

TypeError: 'tuple' object does not support item assignment

```

If you desperately need to change the value of a tuple, there is a workaround. Tuples do not allow for item assignment but you can overwrite the entire tuple in a pinch. 

An example is helpful in understanding this. Take, for instance, the `my_tuple` tuple from the last code block. If you wanted to change its first entry to 2 (like we were trying to do in the item assignment), you could do so by doing this:

```python

my_tuple = (1, 2, 3)

my_tuple = (2, 2, 3)

my_tuple

#Returns (2, 2, 3)

```

It is important to note that this is generally considered a bad practice. If you expect that you'll need to overwrite items within your tuple, it is better to use a list instead. 


## Tuple Methods

Like lists, tuples have a number of built-in methods that you can use to perform operations on them. We will discuss two in this lesson.


### The Tuple `count()` Method

The `count()` method allows us to return the number of times a specified value occurs in a tuple. An example is below: 

```python

dietLog = ('Pizza', 'Omelette', 'Pizza', 'Steaks', 'Barbecue', 'Pizza')

dietLog.count('Omelette')

#Returns 1

dietLog.count('Pizza')

#Returns 3

```


### The Tuple `index()` Method

The tuple `index()` method searches the tuple for a specified value and returns the position of where it was found. An example is below:

```python

countryTuple = ('Canada', 'United Kingdom', 'China', 'Mexico', 'Switzerland')

countryTuple.index('China')

#Returns 2

```

Caution must be used when using the `index()` method. It only returns the index of the _first_occurence. To see how this could cause problems, consider this example:

```python

secondCountryTuple = ('Canada', 'United Kingdom', 'China', 'Mexico', 'Switzerland', 'China')

secondCountryTuple.index('China')

#Returns 2, even though there is another matching entry at index 5

```


## Moving On

In this lesson, we discussed the tuples data structure as well as two important tuple methods. The next lesson of this course will present some practice problems to solidify your understand of tuples as a data structure in Python.
