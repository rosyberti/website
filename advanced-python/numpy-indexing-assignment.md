---
layout: page
title: NumPy Indexing and Assignment
---

In this lesson, we will explore indexing and assignment in NumPy arrays.


## The Array I'll Be Using In This Lesson

As before, I will be using a specific array through this lesson. This time it will be generated using the `np.random.rand` method. Here's how I generated the array:

```python

arr = np.random.rand(5)

```

Here is the actual array:

```

array([0.69292946, 0.9365295 , 0.65682359, 0.72770856, 0.83268616])

```

To make this array easier to look at, I will round every element of the array to 2 decimal places using NumPy's `round` method:

```python

arr = np.round(arr, 2)

```

Here's the new array:

```

array([0.69, 0.94, 0.66, 0.73, 0.83])

```


## How To Return A Specific Element From A NumPy Array

We can select (and return) a specific element from a NumPy array in the same way that we could using a normal Python list: using square brackets. 

An example is below:

```python

arr[0]

#Returns 0.69

```

We can also reference multiple elements of a NumPy array using the colon operator. For example, the index `[2:]` selects every element from index 2 onwards. The index `[:3]` selects every element up to and excluding index 3. The index `[2:4]` returns every element from index 2 to index 4, excluding index 4. The higher endpoint is always excluded.

A few example of indexing using the colon operator are below.

```python

arr[:]

#Returns the entire array: array([0.69, 0.94, 0.66, 0.73, 0.83])

arr[1:]

#Returns array([0.94, 0.66, 0.73, 0.83])

arr[1:4] 

#Returns array([0.94, 0.66, 0.73])

```


## Element Assignment in NumPy Arrays

We can assign new values to an element of a NumPy array using the `=` operator, just like regular python lists. A few examples are below (note that this is all one code block, which means that the element assignments are carried forward from step to step).

```python

array([0.12, 0.94, 0.66, 0.73, 0.83])

arr

#Returns array([0.12, 0.94, 0.66, 0.73, 0.83])

arr[:] = 0

arr

#Returns array([0., 0., 0., 0., 0.])


```
<p style="text-align: right">
In [ ]:
</p>
```


arr[2:5] = 0.5

arr

#Returns array([0. , 0. , 0.5, 0.5, 0.5])

```


## Array Referencing in NumPy

NumPy makes use of a concept called 'array referencing' which is a very common source of confusion for people that are new to the library. 

To understand array referencing, lets first consider an example:

```python

new_array = np.array([6, 7, 8, 9])

second_new_array = new_array[0:2]

second_new_array

#Returns array([6, 7])


```
<p style="text-align: right">
In [ ]:
</p>
```


second_new_array[1] = 4

second_new_array 

#Returns array([6, 4]), as expected

new_array 

#Returns array([6, 4, 8, 9]) 

#which is DIFFERENT from its original value of array([6, 7, 8, 9])

#What the heck?

```

As you can see, modifying `second_new_array` also changed the value of `new_array`.

Why is this?

By default, NumPy does not create a copy of an array when you reference the original array variable using the `=` assignment operator. Instead, it simply points the new variable to the old variable, which allows the second variable to make modification to the original variable - even if this is not your intention.

This may seem bizarre, but it does have a logical explanation. The purpose of array referencing is to conserve computing power. When working with large data sets, you would quickly run out of RAM if you created a new array every time you wanted to work with a slice of the array.

Fortunately, there is a workaround to array referencing. You can use the `copy` method to explicitly copy a NumPy array.

An example of this is below.

```python

array_to_copy = np.array([1, 2, 3])

copied_array = array_to_copy.copy()

array_to_copy

#Returns array([1, 2, 3])

copied_array

#Returns array([1, 2, 3])

```

As you can see below, making modifications to the copied array does not alter the original.

```python

copied_array[0] = 9

copied_array

#Returns array([9, 2, 3])

array_to_copy

#Returns array([1, 2, 3])

```

So far in the lesson, we have only explored how to reference one-dimensional NumPy arrays. We will explore the indexing 

## Indexing Two-Dimensional NumPy Arrays

To start, let's create a two-dimensional NumPy array named `mat`:

```python

mat = np.array([[5, 10, 15],[20, 25, 30],[35, 40, 45]])

mat

"""

Returns:

array([[ 5, 10, 15],

       [20, 25, 30],

       [35, 40, 45]])

"""

```

There are two ways to index a two-dimensional NumPy array:



*   `mat[row, col]`
*   `mat[row][col]`

I personally prefer to index using the `mat[row][col]` nomenclature because it is easier to visualize in a step-by-step fashion. For example:

```python

#First, let's get the first row:

mat[0]

#Next, let's get the last element of the first row:

mat[0][-1]

```

You can also generate sub-matrices from a two-dimensional NumPy array using this notation:

```python

mat[1:][:2]

"""

Returns:

array([[20, 25, 30],

       [35, 40, 45]])

"""

```

Array referencing also applies to two-dimensional arrays in NumPy, so be sure to use the `copy` method if you want to avoid inadvertently modifying an original array after saving a slice of it into a new variable name.


## Conditional Selection Using NumPy Arrays

NumPy arrays support a feature called `conditional selection`, which allows you to generate a new array of boolean values that state whether each element within the array satisfies a particular `if` statement. 

An example of this is below (I also re-created our original `arr` variable since its been awhile since we've seen it):

```python

arr = np.array([0.69, 0.94, 0.66, 0.73, 0.83])

arr > 0.7

#Returns array([False,  True, False,  True,  True])

```

You can also generate a new array of values that satisfy this condition by passing the condition into the square brackets (just like we do for indexing).

An example of this is below:

```python

arr[arr > 0.7]

#Returns array([0.94, 0.73, 0.83])

```

Conditional selection can become significantly more complex than this. We will explore more examples in this section's associated practice problems.


## Moving On

In this lesson, we explored NumPy array indexing and assignment in thorough detail. We will solidify your knowledge of these concepts further by working through a batch of practice problems in the next section.
