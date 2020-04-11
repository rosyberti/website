---
layout: page
title: NumPy Arrays
---

In this lesson, we will be learning about NumPy arrays.


## What Are NumPy Arrays?

NumPy arrays are the main way to store data using the NumPy library. They are similar to normal lists in Python, but have the advantage of being faster and having more built-in methods.

NumPy arrays are created by calling the `array()` method from the NumPy library. Within the method, you should pass in a list. 

An example of a basic NumPy array is shown below. Note that while I run the `import numpy as np` statement at the start of this code block, it will be excluded from the other code blocks in this lesson for brevity's sake. 

```python

import numpy as np

sample_list = [1, 2, 3]

np.array(sample_list)

```

The last line of that code block will result in an output that looks like this.

```python

array([1,2,3])

```

The `array()` wrapper indicates that this is no longer a normal Python list. Instead, it is a NumPy array.


## The Two Different Types of NumPy Arrays

There are two different types of NumPy arrays: vectors and matrices.

Vectors are one-dimensional NumPy arrays, and look like this:

```python

my_vector = np.array(['this', 'is', 'a', 'vector'])

```

Matrices are two-dimensional arrays and are created by passing a list of lists into the `np.array()` method. An example is below.

```python

my_matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

np.array(my_matrix)

```

You can also expand NumPy arrays to deal with three-, four-, five-, six- or higher-dimensional arrays, but they are rare and largely outside the scope of this course (after all, this is a course on Python programming, not linear algebra). 


## NumPy Arrays: Built-In Methods

NumPy arrays come with a number of useful built-in methods. We will spend the rest of this lesson discussing these methods in detail.


### How To Get A Range Of Numbers in Python Using NumPy

NumPy has a useful method called `arange` that takes in two numbers and gives you an array of integers that are greater than or equal to (`>=`) the first number and less than (`&lt;`) the second number.

An example of the `arange` method is below.

```python

np.arange(0,5)

#Returns array([0, 1, 2, 3, 4])

```

You can also include a third variable in the `arange` method that provides a step-size for the function to return. Passing in `2` as the third variable will return every 2nd number in the range, passing in `5` as the third variable will return every 5th number in the range, and so on.

An example of using the third variable in the `arange` method is below.

```python

np.arange(1,11,2)

#Returns array([1, 3, 5, 7, 9])

```

How To Generates Ones and Zeros in Python Using NumPy

While programming, you will from time to time need to create arrays of ones or zeros. NumPy has built-in methods that allow you to do either of these.

We can create arrays of zeros using NumPy's `zeros` method. You pass in the number of integers you'd like to create as the argument of the function. An example is below. 

```python

np.zeros(4)

#Returns array([0, 0, 0, 0])

```

You can also do something similar using three-dimensional arrays. For example, `np.zeros(5, 5)` creates a 5x5 matrix that contains all zeros.

We can create arrays of ones using a similar method named `ones`. An example is below.

```python

np.ones(5)

#Returns array([1, 1, 1, 1, 1])

```


### How To Evenly Divide A Range Of Numbers In Python Using NumPy

There are many situations in which you have a range of numbers and you would like to equally divide that range of numbers into intervals. NumPy's `linspace` method is designed to solve this problem. `linspace` takes in three arguments:



1. The start of the interval
2. The end of the interval
3. The number of subintervals that you'd like the interval to be divided into

An example of the `linspace` method is below.

```python

np.linspace(0, 1, 10)

#Returns array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

```


### How To Create An Identity Matrix In Python Using NumPy

Anyone who has studied linear algebra will be familiar with the concept of an 'identity matrix', which is a square matrix whose diagonal values are all `1`. NumPy has a built-in function that takes in one argument for building identity matrices. The function is `eye`.

Examples are below:

```python

np.eye(1)

#Returns a 1x1 identity matrix

np.eye(2) 

#Returns a 2x2 identity matrix

np.eye(50)

#Returns a 50x50 identity matrix

```


### How To Create Random Numbers in Python Using NumPy

NumPy has a number of methods built-in that allow you to create arrays of random numbers. Each of these methods starts with `random`. A few examples are below:

```python

np.random.rand(sample_size)

#Returns a sample of random numbers between 0 and 1.

#Sample size can either be one integer (for a one-dimensional array) or two integers separated by commas (for a two-dimensional array).

np.random.randn(sample_size)

#Returns a sample of random numbers between 0 and 1, following the normal distribution.

#Sample size can either be one integer (for a one-dimensional array) or two integers separated by commas (for a two-dimensional array).

np.random.randint(low, high, sample_size)

#Returns a sample of integers that are greater than or equal to 'low' and less than 'high'

```


### How To Reshape NumPy Arrays

It is very common to take an array with certain dimensions and transform that array into a different shape. For example, you might have a one-dimensional array with 10 elements and want to switch it to a 2x5 two-dimensional array.

An example is below:

```python

arr = np.array([0,1,2,3,4,5])

arr.reshape(2,3)

```

The output of this operation is:

```python

array([[0, 1, 2],

       [3, 4, 5]])

```

Note that in order to use the `reshape` method, the original array must have the same number of elements as the array that you're trying to reshape it into.

If you're curious about the current shape of a NumPy array, you can determine its shape using NumPy's `shape` attribute. Using our previous `arr` variable structure, an example of how to call the `shape` attribute is below:

```python

arr = np.array([0,1,2,3,4,5])

arr.shape

#Returns (6,) - note that there is no second element since it is a one-dimensional array

arr = arr.reshape(2,3)

arr.shape

#Returns (2,3) 

```

You can also combine the `reshape` method with the `shape` attribute on one line like this:

```python

arr.reshape(2,3).shape

#Returns (2,3)

```


### How To Find The Maximum and Minimum Value Of A NumPy Array

To conclude this lesson, let's learn about four useful methods for identifying the maximum and minimum values within a NumPy array. We'll be working with this array:

```python

simple_array = [1, 2, 3, 4]

```

We can use the `max` method to find the maximum value of a NumPy array. An example is below.

```python

simple_array.max()

#Returns 4

```

We can also use the `argmax` method to find the index of the maximum value within a NumPy array. This is useful for when you want to find the location of the maximum value but you do not necessarily care what its value is.

An example is below.

```python

simple_array.min()

#Returns 2

```

Similarly, we can use the `min` and `argmin` methods to find the value and index of the minimum value within a NumPy array.

```python

simple_array.argmin()

#Returns 0

```


## Moving On

In this lesson, we discussed various attributes and methods of NumPy arrays. We will follow up by working through some NumPy array practice problems in the next lesson.
