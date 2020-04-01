---
layout: page
title: Data Structures: Sets
---

To continue our discussion of data structures, we're going to discuss sets. 


## What is a Set?

A set is an unordered collection of _unique_ elements that is mutable. Let's examine each word from that sentence carefully:



*   **Unordered:** the elements in a set have no order
*   **Unique:** there can be no duplicate elements in a set
*   **Mutable:** sets can be modified after their creation. 

Python sets are created using curly brackets, like dictionaries. They are recognize as being distinct from dictionaries because they contain normal items and not key-value pairs:

```python

my_first_set = {'a', 'b', 'c'}

```


## The Mutability of Sets

While sets are mutable, their mutability is constrained by the fact that sets are unordered. This means that we cannot change a specific element within a set because we cannot access them from their index (like we could with lists).

There is plenty of jargon in that paragraph, so let's unpack it with an example. Consider a list and a set that both contain the same elements:

```python

my_list = [1, 2, 3]

my_set ={1, 2, 3}

```

We can change the first element of the list by accessing it by its index:

```python

my_list[0] = 7

my_list			#This line will print the modified list

#Returns [7, 2, 3]

```

We cannot take the same approach with sets:

```python

my_set[0] = 7

#Returns error

```

Instead, sets must be modified using set methods.


## Set Methods

Like the other data structures in this course, sets have a number of useful built-in methods. We will discuss some of the most important set methods to conclude this lesson.


### How To Calculate The Length Of A Set

We can calculate the length of a set in the same way that we calculate the length of a string, list, or dictionary: by using the `len()` function. An example is below:

```python

set = {1, 2, 3}

len(set)

#Returns 3

```

### How To Add An Item To A Set

You can add items to sets in Python using the `add()` method. You simply pass in the item to be added in the brackets. An example is below:

```python

ingredients = {'pepperoni', 'mushroom', 'bacon'}

ingredients.add('cheese')

ingredients		#This prints the modified set

#Returns {'bacon', 'cheese', 'mushroom', 'pepperoni'}

```

Notice how the output of that code does not match the order in which the elements were created? That's because sets are unordered!

### How To Remove An Item From A Set 

There are two ways to remove an item from a set. Both methods can be useful depending on the task you're trying to accomplish.

The first method to remove an item from a set is `remove()`. You can use this function as follows:

```python

my_set = {'alpha', 'omega', 'charlie'}

my_set.remove('alpha')

my_set

#Returns {'charlie', 'omega'}

```

The second method to remove an item from a set is `discard()`. You can use this function as follows:

```python

setList = {"Don't Stop Believin'", "Open Arms", "Faithfully", "Stone in Love"}

setList.discard("Faithfully")

setList

#Returns {"Don't Stop Believin'", 'Open Arms', 'Stone in Love'}

```

What is the difference between the `remove()` method and the `discard()` method? If the item being remove does not exist, then `remove()` will raise an error while `discard()` will not raise an error. 

For example:

```python

countryArtists = {'Dean Brody', 'Jason Aldean', 'Kenny Chesney'}

countryArtists.remove('Justin Bieber')

#Returns KeyError: 'Justin Bieber'

```

If you tried something similar using the `discard()` function, then no error would be returned:

```python

goodBands = {'Journey', 'Foreigner', 'The Beatles', 'Boston'}

goodBands.discard('Zac Brown Band')

#Returns nothing

```


## Moving On

Sets are the last data structure that we will be discussing in this course. In our next lesson, we will work through several practice problems on sets to solidify your understanding of this data structure. 
