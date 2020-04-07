---
layout: page
title: NumPy Methods and Operations
---

In this lesson, we will be working through various operations included in the NumPy library. 

Throughout this lesson, we will be assuming that the `import numpy as np` command has already been run. 


## The Array Used In This Lesson

For this lesson, I will be working with an array of length 4 created using `np.arange` in all of the examples. 

If you'd like to compare my array with the outputs used in this lesson, here is how I created and printed the array:

```python

arr = np.arange(4)

arr

```

The array values are below.

```python

array([0, 1, 2, 3])

```


## How To Perform Arithmetic In Python Using Number

NumPy makes it very easy to perform arithmetic with arrays. You can either perform arithmetic using the array and a single number, or you can perform arithmetic between two NumPy arrays.

We explore each of the major mathematical operations below.


### Addition

When adding a single number to a NumPy array, that number is added to each element in the array. An example is below:

```python

2 + arr

#Returns array([2, 3, 4, 5])

```

You can add two NumPy arrays using the `+` operator. The arrays are added on an element-by-element basis (meaning the first elements are added together, the second elements are added together, and so on). 

An example is below.

```python

arr + arr

#Returns array([0, 2, 4, 6])

```

Subtraction

Like addition, subtraction is performed on an element-by-element basis for NumPy arrays. You can find example for both a single number and another NumPy array below.

```python

arr - 10

#Returns array([-10,  -9,  -8,  -7])

arr - arr

#Returns array([0, 0, 0, 0])

```


### Multiplication

Multiplication is also performed on an element-by-element basis for both single numbers and NumPy arrays. 

Two examples are below.

```python

6 * arr

#Returns array([ 0,  6, 12, 18])

arr * arr

#Returns array([0, 1, 4, 9])

```


### Division

By this point, you're probably not surprised to learn that division performed on NumPy arrays is done on an element-by-element basis. An example of dividing `arr` by a single number is below:

```python

arr / 2

#Returns array([0. , 0.5, 1. , 1.5])

```

Division does have one notable exception compared to the other mathematical operations we have seen in this lesson.. Since we cannot divide by zero, doing so will cause the corresponding field to be populated by a `nan` value, which is Python shorthand for "Not A Number". Jupyter Notebook will also print a warning that looks like this:

```

RuntimeWarning: invalid value encountered in true_divide

```

An example of dividing by zero is with a NumPy array is shown below.

```python

arr / arr

#Returns array([nan,  1.,  1.,  1.])

```

We will learn how to deal with `nan` values in more detail later in this course. 


## Complex Operations in NumPy Arrays

Many operations cannot simply be performed by applying the normal syntax to a NumPy array. In this section, we will explore several mathematical operations that have built-in methods in the NumPy library.


### How To Calculate Square Roots Using NumPy

You can calculate the square root of every element in an array using the `np.sqrt` method:

```python

np.sqrt(arr)

#Returns array([0.        , 1.        , 1.41421356, 1.73205081])

```

Many other examples are below (note that you will not be tested on these, but it is still useful to see the capabilities of NumPy):

```

np.exp(arr)

#Returns e^element for every element in the array

np.sin(arr)

#Calculate the trigonometric sine of every value in the array

np.cos(arr)

#Calculate the trigonometric cosine of every value in the array

np.log(arr)

#Calculate the base-ten logarithm of every value in the array

```


## Moving On

In this lesson, we explored the various methods and operations available in the NumPy Python library. We will text your knowledge of these concepts in the practice problems presented next.
