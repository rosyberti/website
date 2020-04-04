---
layout: page
title: How To Merge DataFrames in Pandas
---

In this lesson, we'll learn how to merge pandas DataFrames.


## The DataFrames We Will Be Using In This Lesson

In this lesson, we will be using the following two pandas DataFrames:

```python

import pandas as pd

leftDataFrame = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],

                     'A': ['A0', 'A1', 'A2', 'A3'],

                     'B': ['B0', 'B1', 'B2', 'B3']})

   

rightDataFrame = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],

                          'C': ['C0', 'C1', 'C2', 'C3'],

                          'D': ['D0', 'D1', 'D2', 'D3']})    

```

The columns `A`, `B`, `C`, and `D` have real data in them, while the column `key` has a key that is common among both DataFrames. To `merge` two DataFrames means to connect them along one column that they both have in common.


## How To Merge Pandas DataFrames

You can merge two pandas DataFrames along a common column using the `merge` columns. For anyone that is familiar with the SQL programming language, this is very similar to performing an `inner join` in SQL.

Do not worry if you are unfamiliar with SQL, because `merge` syntax is actually very straightforward. It looks like this:

```python

pd.merge(leftDataFrame, rightDataFrame, how='inner', on='key')

```

Let's break down the four arguments we passed into the `merge` method:



1. `leftDataFrame`: This is the DataFrame that we'd like to merge on the left.
2. `rightDataFrame`: This is the DataFrame that we'd like to merge on the right.
3. `how=inner`: This is the type of merge that the operation is performing. There are multiple types of merges, but we will only be covering inner merges in this course.
4. `on='key': This is the column that you'd like to perform the merge on. Since `key` was the only column in common between the two DatAFrames, it was the only option that we could use to perform the merge.


## Moving On

This concludes our brief discussion of how to perform merges using pandas DataFrames. We'll work through some practice problems before learning about joins, which are similar to merges but have slightly different syntax and functionality.
