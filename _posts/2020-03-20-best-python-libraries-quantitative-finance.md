---
title: 'The 5 Best Python Libraries for Quantiative Finance'
date: 2020-03-16
author: Nick McCullum
layout: post
permalink: /best-python-libraries-quantiative-finance/
---

Python is arguably the most widely-used programming language in the world of quantitative finance. Investors, asset managers, and investment bankers use Python for tasks ranging from security selection to portfolio rebalancing to high-frequency trading.

With that said, programmers themselves do not need to write all of the code to perform these tasks. A number of Python libraries make it both easier and faster to get started writing mission-critical applications for your business.

This article explores the 5 most important Python libraries for quantitative finance today.
<!--more-->
## Python Library #1: NumPy
![NumPy](https://raw.githubusercontent.com/nicholasmccullum/nicholasmccullum.github.io/master/images/numpy.svg?sanitize=true)

NumPy (pronounced "Numb Pie") is arguably the most important library for quantitative finance.

The library's main capability is the creation and manipulation of multi-dimensional data types like array and matrices.

NumPy also includes built-in high-level mathematical functions for performing operations on these data types (as well as similar functions that operate on integers and floating-point numbers).

Numeric - the earliest predecessor to NumPy - was created by Jim Hugunin with contributions by many other developers. The earliest true version of NumPy was created by Travis Oliphant by combining features from the aforementioned Numeric with another library named Numarray.

To install NumPy at the command line using the pip package manager, use the following command:

`pip install numpy`

To import NumPy into a Python program, the default convention is to use the following command:

`import numpy as np`

NumPy functions can later be called using the dot operator on the np variable.

## Python Library #2: Pandas

![Pandas](https://raw.githubusercontent.com/nicholasmccullum/nicholasmccullum.github.io/master/images/pandas.svg?sanitize=true)

Pandas goes hand-in-hand with NumPy as one of the most widely-used libraries in quantitative finance. In fact, pandas (whose first letter is not normally capitalized) is so intertwined with NumPy that installing pandas will automatically install NumPy along with it. Because of this, it is actually somewhat rare so see a NumPy import in a Python program because it's automatically included with a pandas import.

The pandas library derives its name from 'panel data'. As its name suggests, the two main purposes of the pandas library are:

1. The creation and manipulation of numerical tables
2. The creation and manipulation of time series data

To install pandas at the command line using the pip package manager, use the following command:

`pip install pandas`

To import pandas into a Python program, the default convention is to use the following command:

`import pandas as pd`

Pandas functions can later be called using the dot operator on the "pd" variable.

## Python Library #3: SciPy

![SciPy](https://raw.githubusercontent.com/nicholasmccullum/nicholasmccullum.github.io/master/images/scipy.svg?sanitize=true)

SciPy (pronounced "Sigh Pie") is a Python library that was originally designed for scientific and technical computing. The library contains many advanced functions that are not naturally included in either NumPy or pandas, including:

- Optimization functions
- Linear algebra functions
- Integration
- Interpolation (linear and otherwise)
- Image processing
- Signal processing
- Ordinary differential equation solvers
- Partial differential equation solvers
- and other special functions.

Like pandas, SciPy is part of the NumPy stack and relies heavily on the NumPy array data type. In fact, the two libraries are so closely related that the NumPy stack is sometimes referred to as the SciPy stack.

To install SciPy at the command line using the pip package manager, use the following command:

`pip install scipy`

To import SciPy into a Python program, use the following line of code:

`import scipy`

You may also want to just import the stats module from SciPy. I find this quite useful for a number of my projects. If this is the case, use the following command:

`from scipy import stats`

## Python Library #4: XlsxWriter

![Excel](https://raw.githubusercontent.com/nicholasmccullum/nicholasmccullum.github.io/master/images/excel.svg?sanitize=true)

The first three libraries discussed in this article helped us better manipulate data. The last two libraries discussed in this article will help us present data for outside users.

The first is XlsxWriter, which contains a number of functions and object types to help export data into beautifully-formatted .xlsx files. This package is great for creating resources for non-technical users who are not capable of working with Python scripts.

To install XlsxWriter at the command line using the pip package manager, use the following command:

`pip install xlsxwriter`

To import XlsxWriter into a Python script, use the following line of code:

`import xlsxwriter`

## Python Library #5: MatplotLib

![NumPy](https://raw.githubusercontent.com/nicholasmccullum/nicholasmccullum.github.io/master/images/matplotlib.svg?sanitize=true)

Matplotlib is the most popular library for the presentation of two-dimensional data in Python. Matplotlib has the capability of publishing a variety of charts in both hardcopy formats and interactive environments across platforms.

You can install matplotlib at the command line using the pip package manager using the following command:

`pip install matplotlib`

In your Python application, you can import matplotlib using the following command:

`import matplotlib.pyplot as plt`

While this is a bit different than some of the other import commands that we have seen in this article, this is because we are only importing one module of matplotlib (pyplot).

To be more specific, we specify the exact module we'd like to import using the ".pyplot" suffix, and then label that module as "plt" for when we reference it later in the Python program.

## Final Thoughts
It is hard to overstate how useful the Python programming language can be for quantitative finance practitioners today.

With that said, investors do not need to write all of their code themselves. There are a number of Python libraries available today that make it easy to get started building applications for quantitative finance. Five of the most important were discussed in this article:

- NumPy
- Pandas
- SciPy
- XlsxWriter
- Matplotlib

Use these libraries as you proceed through your quantiative finance career for a more productive and less stressful development experience.
