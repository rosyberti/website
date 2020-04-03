---
layout: page
title: Data Structures - Lists
---

So far in this course, we have examined integers and strings as examples of data structures (although we may not have specifically referred to them by that name). In this lesson, we will explore another data structure called _lists_ - which are arguably one of the most important data structures in the Python programming language. 


## What Are Lists

Lists are ordered sequences of elements that themselves contain other elements. If you’ve worked with other programming languages before, lists are similar to arrays in certain other languages (JavaScript is one example).

Lists are recognizable because they are created with square brackets. The elements within a list are separated by commas. You can see your first example of a list below:

```python

myList = [0, 1, 2, 3]

```

The elements within a list can be accessed by passing in the element's index using square brackets. Remember, Python is zero-indexed, so the first element is accessed by index 0, the second element is accessed by index 1, and so on.

An example of this is shown below:

```python

anotherList = ['alpha', 'beta', 'charlie']

anotherList[0]

#Returns 'alpha'

anotherList[1]

#Returns 'beta'

anotherList[2]

#Returns 'charlie'

```


## List Mutability

In programming, data structures are divided into two categories:



*   **Mutable Data Structures:** those that can be modified after creation
*   **Immutable Data Structures:** those that cannot be modified after creation. 

Lists are mutable, which means you can change them on demand. As an example, consider the following code:

```python

yet_another_list = [10, 9, 8, 7]

yet_another_list = [1, 2, 3]

yet_another_list #This line prints out the current data stored in that variable name

#Returns [1, 2, 3]

```

List mutability and indexing can be combined together to change a single element within a list, which is extremely useful. 

To change the first element of a list, you'd write the following code:

```python

thisList = ['Canada', 'United States', 'Germany']

thisList[1] = 'US'

thisList

#Returns ['Canada', 'US', 'Germany']

```


## List Elements and Nested Lists

Unlike the other two data structures that we have seen so far - integers and strings - lists contain other elements, which causes them to have unique properties. 

First of all, lists do not need to contain all of the same data types within them. Lists to not need to contain only integers or only strings, as an example.

Instead, lists can contain a variety of different element types: 

```python

listOfDifferentElements = ['Nick', 24]

```

More generally, lists can be contained within other lists - and this trend can continue on indefinitely. A list contained within another list is called a nested list. Some of the most unreadable code I have ever encountered has contained many levels of nested lists. 

An example of a nested list with 1 layer is shown below:

```python

nestedList = [1, [2, 3], 4]

```

An example of a nested list with 3 layers is shown below:

```python

complexNestedList = [1, [2, [3,4]]]

```

As you can imagine, nested lists can quickly become extremely complex when you start to involve multiple layers. Their readability can be improved by spreading them out on different lines, like this:

```python

complexNestedList = [1, 


            [2, 


                [3,4]


                ]


            ]

```


## List Methods

We'll now explore some of the most important methods that can be applied to lists before concluding this lesson.


### How To Calculate The Length Of A List

We calculate the length of a list in the same way that we calculated the length of a string in our last lesson:

```python

duplicatedNestedList = [1, 'One', [1, 'One']]

len(duplicatedNestedList)

#Returns 3

```

Notice that even though the `duplicatedNestedList` list contains a nested list, its length is still 3 because the nested list only counts as one element. 


### How To Calculate The Sum Of A List

Calculating the sum of a list (assuming the list contains only numbers and no other data types) is very easy. We simply use the `sum()` function:

```python

listToSum = [10, 5, 50]

sum(listToSum)

#Returns 65

```

For obvious reasons, this function does not work if there is a string (or any other non-number data structure that we'll explore later in this course) contained in the list. 

```python

listThatCannotBeSummed = [1, 'two', 3]

sum(listThatCannotBeSummed)

#Returns error

```


### How To Identify The Minimum and Maximum Values in a List

Finding the smallest and largest values in a list of numbers can be easily done using the `min()` and `max()` functions. Examples of each function are below:

```python
list1 = [5, 6, 7]
min(list1)
#Returns 5
```

```python
list2 = [10, 15, 25]
max(list2)
#Returns 25
```

### How To Append An Element To The End Of A List

There are many situations in which you will want to add an element to the end of a list. This operation is performed using the `.append()` method. An example is below:

```python

initialList = [5, 6, 7]

initialList.append(8)

initialList

#Returns [5, 6, 7, 8]

```


### How To Concatenate Lists

The last list method that we'll discuss will allow us to add one list to the end of another. This is similar to string concatenation that we discussed earlier in this course. The method of choice for this problem is `.extend()`.

An example is below:

```python

list1 = [1, 2, 3]

list2 = [4, 5, 6]

list1.extend(list2)

list1

#Returns [1, 2, 3, 4, 5, 6]

```

## Moving On

In this lesson, we explored lists - one of the most important data structures in Python. In the next lesson of this course, we will work through practice problems related to lists to solidify the information presented in this lesson. 
