---
layout: page
title: How to Import External Libraries in Python
---

Throughout this course, we will be working with two external libraries in Python:

*   [NumPy](https://numpy.org/)
*   [Pandas](https://pandas.pydata.org/)

To work with these external libraries, you'll need to import them first. This lesson will explain what a library is and demonstrate how you can import them into your Python applications.


## What is a Library?

A Python library is a collection of functions and methods that are created to let you complete common tasks without rewriting code. 

A few examples of common Python libraries (and their use cases) are below:



*   [Requests](https://requests.readthedocs.io/en/master/): Allows you to perform HTTP requests (to gather and send data across the Internet)
*   [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): For XML and HTML parsing, which means gathering specific data points from large, complex XML or HTML files
*   [SQLAlchemy](https://www.sqlalchemy.org/): A library for interacting with databases using the SQL programming language.
*   [Matplotlib](https://matplotlib.org/): A library for performing highly customizable data visualizations.
*   [SciPy](https://www.scipy.org/): A library with tools for performing algorithms and complex mathematical computations. 
*   [Scikit-learn](https://scikit-learn.org/stable/): Machine learning and data mining.
*   [Tensorflow](https://www.tensorflow.org/): Machine learning and deep learning.

Many of these Python libraries are 'open source'. This means that the source code is hosted in a public repository and anyone can suggest improvements to it. 

The open source software community is vibrant, and encourages people who use these open source tools to contribute back and improve them over time. Some large corporations have even developed programming libraries internally and then open-sourced them later so that they could benefit from these public contributions. Facebook's open source user interface library React.js is probably the best example of this. 

In this course, the two libraries that we will be spending the most time in are NumPy and Pandas. We will explore how to import each library in the following sections. 


## How To Import the NumPy Library

Python library imports are always initialized using the `import` keyword. That `import` keyword is then followed by the name of the library being imported. 

For example, the NumPy library can be imported like this:

```python

import numpy

```

While this is _one_ way that we could import the NumPy library, there are better options. We often import Python libraries using an _alias_, which is a shorthand name that we will use to refer to the library at a later date. 

Each Python library typically has a specific alias that is widely accepted among the developer community. For example, it is considered a best practice to use the `np` alias to import numpy, like this:

```python

import numpy as np

```

Now that NumPy has been imported into our application, what does this allow us to do?


## How To Import The Pandas Library

Just like the NumPy library is typically referred to by the alias `np`, the pandas library is typically referred to by the alias `pd`. 

Because of this, the pandas libary is usually imported like this:

```python

import pandas as pd

```

It is very common to see both NumPy and pandas imported into the same script. We will explore how to do this in the next section. 


## Importing Multiple Libraries

It is possible (and very common) to import multiple libraries into a Python script. There are two ways to do this.

The first is a multi-line import, which is probably exactly what you expect it to be:

```python

import numpy as np

import pandas as pd

```

The second way to import multiple libraries into a Python script is by using a single-line import, which involves separating each import by a comma like this:

```python

import numpy as np, import pandas as pd

```

Using single-line or multi-line imports is a matter of taste. I prefer mutli-line imports myself. 

Why?

Because in large, complex applications that have many external dependencies, your single-line import is likely to become sufficiently long to move off the screen. See below for an example. 

```python

import numpy as np, import pandas as pd, import psycopg2, import requests, import bs4, import scikit-learn, import json

```


## Moving On

You now understand how to import libraries and use their functions. In the next lesson, we will begin taking a closer look at the NumPy library in Python. 
