---
layout: page
title: How To Join DataFrames in Pandas
---

In this lesson, you will learn how to join pandas DataFrames.


## The DataFrames We Will Be Using In This Lesson

We will be using the following two DataFrames in this lesson:

```python

leftDataFrame = pd.DataFrame({  'A': ['A0', 'A1', 'A2', 'A3'],

                                'B': ['B0', 'B1', 'B2', 'B3']},

                                index =['K0', 'K1', 'K2', 'K3'])

   

rightDataFrame = pd.DataFrame({ 'C': ['C0', 'C1', 'C2', 'C3'],

                                'D': ['D0', 'D1', 'D2', 'D3']},

                                index = ['K0', 'K1', 'K2', 'K3'])  

```

If these look familiar, it's because they are! These are the nearly the same DataFrames as we used when learning how to merge pandas DataFrames. A key difference is that instead of the `key` column being its own column, it is now the index of the DataFrame. You can think of these DataFrames as being those from the last lesson after executing `.set_index(key)`.


## How To Join Pandas DataFrames

Joining pandas DataFrames is very similar to merging pandas DataFrames except that the keys on which you'd like to combine are in the index instead of contained within a column.

To join these two DataFrames, we can use the following code:

```python

leftDataFrame.join(rightDataFrame)

```


## Moving On

That concludes our (very) brief discussion of how to join pandas DataFrames. We'll work through a few examples before discussing other common operations from the pandas Python library.
