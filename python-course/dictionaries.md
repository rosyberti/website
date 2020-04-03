---
layout: page
title: Data Structures - Dictionaries
---

In this lesson, we will continue our discussion of Python data structures by discussing dictionaries.


## What Is A Dictionary?

To understand dictionaries, you must first understand the concept of a key-value pair. 

A key-value pair is simply two paired values, one of which is designated as the 'key' and one of which is designated as the 'pair'. The key always comes first in a key-value pair, and the value comes second. Key-value pairs are separated by colons, like this:

```python

'key':'value'

```

A dictionary is a data structure that contains an unordered collection of key-value pairs. Dictionaries are wrapped in curly brackets:

```python

myFirstDictionary = { 'key1': 'value1', 'key2': 'value2'	}

```

Dictionaries in Python are similar to real-world language dictionaries. In that analogy, the word is the key and the definition of that word is the value.

For long dictionaries, it is common practice to have only one key-value pair per line. This is an example:

```python

presidentDictionary = {

			42: 'Bill Clinton',

			43: 'George W. Bush',

			44: 'Barack Obama',

			45: 'Donald Trump'

			}

```

Like lists, we can modify specific elements of a dictionary by passing in its key (the analogy to an index in a list). An example is below (note that the last digit of the United States value was left out, causing it to be off by 10x - this code serves to correct that error):

```python

countryPopulations = {

    'China': 1433783686,

    'India': 1366417754,

    'United States': 32906491

}

countryPopulations['United States'] = 329064917

countryPopulations		#This line will print out the modified dictionary

#Returns {'China': 1433783686, 'India': 1366417754, 'United States': 329064917}

```

Dictionaries are like lists and tuples in that they can contain any type of data structure and still be valid. For example, this is a perfectly valid dictionary:

```python

complicatedDict = {

			('my, tuple'): 'This is the key for my tuple!',

			'Second Key': [2, 3, 4, 5]

			}

```


## Calling Values From A Dictionary

The most important functionality that dictionaries have in Python is the ability to pass in a key and have the value returns. This is done using square brackets, just like when we were returning items out of lists earlier in this course.

To see this work in practice, let's use the `presidentDictionary` from earlier in this lesson:

```python

presidentDictionary = {

			42: 'Bill Clinton',

			43: 'George W. Bush',

			44: 'Barack Obama',

			45: 'Donald Trump'

			}

presidentDictionary[42]

#Returns 'Bill Clinton'

presidentDictionary[43]

#Returns 'George W. Bush'

presidentDictionary[44]

#Returns 'Barack Obama'

presidentDictionary[45]

#Returns 'Donald Trump'

```

As you can see, dictionaries can be extremely useful when you have datasets with some sort of index (the key of the key-value pair). Knowing the key can quickly allow you to access the value of the key-value pair. 


## Dictionary Methods

This section will discuss the most important dictionaries methods that you'll need to understand as a Python programmer. 


### How To Get A List Of The Keys In A Dictionary In Python

From time to time, it is very useful to have a list containing all of the keys from a dictionary in Python. The `.keys()` method allows us to generate such a list:

```python

workDays = {

    'Monday': True,

    'Tuesday': True,

    'Wednesday': True,

    'Thursday': True,

    'Friday': True,

    'Saturday': False,

    'Sunday': False

}

workDays.keys()

#Returns dict_keys(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

```

Note that the `keys()` method returns a `dict_keys()` object, not a true list. You can easily fix this by wrapping the `dict_keys()` object in a `list()` function like this:

```python

list(workDays.keys())

#Returns ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

```


### How To Get A List Of The Value In A Dictionary In Python

The `values()` method allows you to easily create a list of all of the values in a Python dictionary. As an example, let's again use the workDays dictionary:

```python

workDays = {

    'Monday': True,

    'Tuesday': True,

    'Wednesday': True,

    'Thursday': True,

    'Friday': True,

    'Saturday': False,

    'Sunday': False

}

workDays.values()

#Returns dict_values([True, True, True, True, True, False, False])

```

Just like last time, this returns a special `dict_values()` object which can be transformed into a normal list using the `list()` function, like this:

```python

list(workDays.values())

#Returns [True, True, True, True, True, False, False]

```


### How To Remove All Elements From A Dictionary In Python

You can remove all the elements from a dictionary (where each element is a key-value pair) using the `clear()` method:

```python

numberDict = {

    1: 2,

    3: 4,

    5: 6

}

numberDict.clear()

numberDict		#to make it print

#Returns {}, an empty dictionary

```


### How To Remove A Key-Value Pair From A Dictionary In Python

It is much more common to want to remove a specific key-value pair from a dictionary, rather than clearing the entire data structure. This is done using the `pop()` method. An example is below:

```python

cityPopulation = {

    'NYC': 8623000,

    'Houston': 2313000,

    'San Fransisco': 884000

}

cityPopulation.pop('NYC')

cityPopulation		#This line is to print out the final dictionary

#Returns {'Houston': 2313000, 'San Fransisco': 884000}

```


## Moving On

In this lesson, we discussed dictionaries and the methods you can call against them. The next lesson will provide some dictionary practice problems to help you understand this further. 

