---
layout: page
title: Pandas Series
---

In this lesson, we'll be exploring Series, which are a core component of the pandas library for Python programming.


## What Are Pandas Series?

Series are a special type of data structure available in the pandas Python library. Pandas Series are similar to NumPy arrays, except that we can give them a named or datetime index instead of just a numerical index.


## The Imports You'll Require To Work With Pandas Series

To work with pandas Series, you'll need to import both NumPy and pandas, as follows:

```python

import numpy as np

import pandas as pd

```

For the rest of this lecture, I will assume that both of those imports have been executed before running any code blocks.

## How To Create a Pandas Series

There are a number of different ways to create a pandas Series. We will explore all of them in this section. 

First, let's create a few starter variables - specifically, we'll create two lists, a NumPy array, and a dictionary.

```python

labels = ['a', 'b', 'c']

my_list = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {'a':10, 'b':20, 'c':30}

```

The easiest way to create a pandas Series is by passing a vanilla Python list into the `pd.Series()` method. We do this with the `my_list` variable below:

```python

pd.Series(my_list)

```

If you run this in your Jupyter Notebook, you will notice that the output is quite different than it is for a normal Python list:

```python

0    10

1    20

2    30

dtype: int64

```

The output shown above is clearly designed to present as two columns. The second column is the data from `my_list`. What is the first column?

One of the key advantages of using pandas Series over NumPy arrays is that they allow for labeling. As you might have guessed, that first column is a column of labels.

We can add labels to a pandas Series using the `index` argument like this:

```python

pd.Series(my_list, index=labels)

#Remember - we created the 'labels' list earlier in this lesson

```

The output of this code is below:

```

a    10

b    20

c    30

dtype: int64

```

Why would you want to use labels in a pandas Series? The main advantage is that it allows you to reference an element of the Series using its label instead of its numerical index. To be clear, once labels have been applied to a pandas Series, you can use _either_ its numerical index or its label.

An example of this is below.

```python

Series = pd.Series(my_list, index=labels)

Series[0]

#Returns 10

Series['a']

#Also returns 10

```

You might have noticed that the ability to reference an element of a Series using its label is similar to how we can reference the `value` of a `key`-`value` pair in a dictionary. Because of this similarity in how they function, you can also pass in a dictionary to create a pandas Series. We'll use the `d={'a': 10, 'b': 20, 'c': 30}` that we created earlier as an example:

```python

pd.Series(d)

```

This code's output it:

```

a    10

b    20

c    30

dtype: int64

```

It may not yet be clear why we have explored two new data structures (NumPy arrays and pandas Series) that are so similar. In the next section of this lesson, we'll explore the main advantage of pandas Series over numpy arrays.


## The Main Advantage of Pandas Series Over NumPy Arrays

While we didn't encounter it at the time, NumPy arrays are highly limited by one characteristic: every element of a NumPy array must be the same type of data structure. Said differently, NumPy array elements must be all string, or all integers, or all booleans - you get the point.

Pandas Series do not suffer from this limitation. In fact, pandas Series are _highly_ flexible. 

As an example, you can pass three of Python's built-in functions into a pandas Series without getting an error:

```python

pd.Series([sum, print, len])

```

Here's the output of that code:

```

0      &lt;built-in function sum>

1    &lt;built-in function print>

2      &lt;built-in function len>

dtype: object

```

To be clear, the example above is highly impractical and not something we would ever execute in practice. It is, however, an excellent example of the flexibility of the pandas Series data structure.


## Moving On

This concludes our discussion of pandas Series. After working through some practice problems in the next session, we will begin our discussion of pandas DataFrames, which are the most important data structure included in the pandas library.
