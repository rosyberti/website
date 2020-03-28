---
layout: page
title: Strings and String Operations
---

In the last lesson, we had our first exposure to comments, operations, and variables in Python. We're going to continue our discussion of Python fundamentals by exploring strings and the operations you can perform on them.


## What Are Strings?

In our last lesson, we were working exclusively with integers - numbers that have no decimals associated with them. Integers are an example of a _data structure_ in Python, and so are strings. We will discuss many other data structures outside of strings and integers later in this course.

While integers were numbers, strings are sequences of characters. Strings are identified by being wrapped in either single- or double-quotes.

The following variables are each examples of strings in Python:

```python

string = 'string'

another_string = "I am another string"

yetAnotherString = 'This is another string!!! Yeehaw!'

```


## Single-Quotes vs. Double-Quotes

Single-quotes and double-quotes serve _exactly_ the same purpose in Python. The only caveat is you must be consistent: single-quotes can only be used with single-quotes and double-quotes can only be used with double-quotes. 

Said another way, you can't do this:

```python

possible_string = "Do you think this will work?'

#returns error

```

This string returns an error because it starts with a double-quote but ends with a single-quote.

There's only one case where you must be careful whether to use single-quotes or double-quotes: when the string itself contains one of those characters. To see why, consider the following code block:

```python

mrRogersQuote = 'It's a beautiful day in the neighborhood!'

#Returns error

```

This code returns an error because the first single-quote starts a string that is ended by the single-quote in "it's". The interpreter does not know what do with the text after the second single-quote, so it throws an error.

There are two solutions to this problem.

The first solution is to use double-quotes for the string:

```python

mrRogersQuote = "It's a beautiful day in the neighborhood!"

```

The second solution is to use what is called an 'escape character', which in Python is coded to the backslash '\\'. The escape character allows you to include characters in a string that otherwise have special meaning (like single-quotes and double-quotes).

In other words, the backslash allows you to include a single-quote in a string that is wrapped in single-quotes, like this:

```python

mrRogersQuote = 'It\'s a beautiful day in the neighborhood!'

```

In this specific case, it definitely makes more sense to just wrap the string in double-quotes because it makes the code more readable. 


## Multi-Line Strings 

The string syntax that we have explored so far in this lesson _only works for single-line strings_. Fortunately, the syntax for multi-line strings is similar - and, interestingly enough, we've already discussed it in this course!

The multi-line comments that we explored previously were actually just multi-line strings included in the codebase. The strings aren't used for anything, so they're functionally equivalent to comments. 

In case you've forgotten, we created these multi-line comments (now multi-line strings) using triple-quotes, like this:

```python

multiLineString = '''

This

is

a

multi

line

string

'''

```

Moving forward, please note that all of the concepts and operations we discuss can be applied to multi-line strings, although I will primarily be using single-line strings for brevity's sake. 


## Whitespace in Strings

Strings are very different from normal Python code because whitespace matters. Because of this, the following two pieces of code are not equivalent:

```python

string1 = "this is a string"

string2 = "this  is  a  string"

```

String whitespace is a common source of errors for computer programmers, so keep this distinction in mind as we continue through this lesson.


## String Concatenation

Concatenation means adding one string to the end of another string. As an example, concatenating the strings "Python" and "Course" would give "PythonCourse" (notice how the lack of whitespace is reflected in the concatenation).

String concatenation in Python is performed using the '+' character. An example is below:

```python

str1 = 'Hello'

str2 = "World"

str1 + str2 

#returns 'HelloWorld'

```

Again, notice how the lack of whitespace is reflected in the code block above. One other observation is that even though the two strings being concatenated together used different quotes (single-quotes and double-quotes), they were still able to be concatenated together. This demonstrates how single-quotes and double-quotes are equivalent in Python.

Like integer addition discussed earlier in this course, you can chain together string concatenation as long as you'd like. This is actually an easy way to add spaces between words when the necessary whitespace isn't included in the variables themselves. After all, very few people want to concatenate words with no spaces, like 'HelloWord'.

The following code fixes the whitespace problem from the previous code block:

```python

str1 = "Hello"

str2 = "World"

str1 + " " + str2 

#returns 'Hello World'

```

If you need to repeat a string many times, you can do so using the '*' character and an integer. It is analogous to multiplication on normal numbers - the string will repeat once for each integer that you multiply it by. An example:

```python

str = 'Are we there yet? '

str * 3

#returns 'Are we there yet? Are we there yet? Are we there yet? '

```


## String Interpolation

String interpolation is the process of substituting variables into a string. It allows you to inject variables (which change over time) into a string that otherwise remains constant.

An analogy would be if you wrote the sentence "Today's date is X", and you wanted X to update each day with the correct string. 

There are two main ways to perform string interpolation in Python. I'll discuss each in this lesson.


### String Interpolation Using the '+' Operator

The first way to perform string interpolation is by simply chaining together string concatenation using the '+' operator. An example is below. 

```python

firstName = 'Nick'

lastName = 'McCullum'

'My name is ' + firstName + ' ' + lastName

#Returns 'My name is Nick McCullum

```

I would not recommend this method in general because it is considered to be a poor practice among the Python community, since the code is a bit harder to read. 

To be clear, the example I provided wasn't _impossible_ to read, but the readability of chained concatenation gets worse and worse the more variables you have. It also becomes harder to read if there are any '+' characters in the strings themselves.

The next section introduces a better alternative.


### String Interpolation Using F-Strings

The best method for string interpolation in Python 3 is using f-strings. This method involves placing an 'f' before the first quote, and then interpolating the variables inside curly brackets. 

```python

firstName = 'Barack'

lastName = 'Obama'

f'The 44th President of the United States was {firstName} {lastName}'

#Returns 'The 44th President of the United States was Barack Obama'

```

This method is a bit more difficult, so multiple examples are warranted. Here is one more:

```python

topping1 = 'pepperoni'

topping2 = 'mushrooms'

topping3 = 'bacon'

pizzaType = 'Canadian'

f'Your {pizzaType} will have {topping1}, {topping2} and {topping3} on it.'

#Returns 'Your Canadian will have pepperoni, mushrooms and bacon on it.'

```

And another:

```python

carModel = 'Ford F-150'

feature1 = 'heated seats'

feature2 = 'air conditioning'

f'Your {carModel} with {feature1} and {feature2} is waiting for you on the lot!'

#Returns 'Your Ford F-150 with heated seats and air conditioning is waiting for you on the lot!'

```


## Other Methods of String Interpolation

While I discussed two methods of string interpolation in this lesson, there are others. They generally make use of the '%' character or the .format() function and have been carried forward from older versions of Python. While you may encounter these older methods in legacy programs, it is best to use f strings for all new code that you write moving forward. 


## Other String Operations

Over the course of your programming career, you will likely discover problems that require you to transform strings in other ways. To wrap up this lesson, I wanted to provide an overview of some of the most common string operations.


### Accessing A Specific Character of a String

There are many situations in which you will need to access a specific character of a string. You can do so using square brackets, like this:

```python

vicePresident = 'Joe Biden'

vicePresident[0]

#Returns 'J'

```

Note that all data structures in Python are 'zero-indexed', which means that the first item in a data structure has index 0, the second item has index 1, and so on. This is not intuitive to beginner programmers and can result in 'off-by-one errors', often abbreviated OBOE.

If you are unsure of how long a string is but you want to access its last character, you can use index -1:

```python

pokemonGuy = 'Ash Ketchum'

pokemonGuy[-1]

#Returns 'm'

```

Similarly, the second-last character can be accessed using index -2:

```python

amazonFounder = 'Jeff Bezos'

amazonFounder[-2]

#Returns 'o'

```

This pattern can be repeated for any character in the string. 


### How To Determine String Length

Determining a string length is one of the most common string operations. You can calculate a string's length using the len() function:

```python

country = 'Canada'

len(country)

#Returns 6

```

Since Python is zero-indexed, the last character always has index of `len(string)-1`. For example, the last index of the string 'four' is 3 - the length of the string, 4, minus 1.


### How To Transform A String to Uppercase or Lowercase

Another common operation you'll need is transforming a string to uppercase or lowercase. These actions can be performed using either the `.upper()` or `.lower()` methods. 

We have not discussed methods in much detail yet, but they are quite simple: to invoke a method, you must simply take it (along with a period) to the end of the variable you're working with. An example for both the `.upper()` and `.lower()` methods are below:

```python

whispering = 'shhhh'

whispering.upper()

#Returns 'SHHHH'

```

```python

email = 'IDoNotUnderstandThatEmailsAreNotCapitalSensitive@gmail.com'

email.lower()

#Returns 'idonotunderstandthatemailsarenotcapitalsensitive@gmail.com'

```

### How To Replace A Character in a String

The last string operation we'll discuss is the `.replace()` method, which is used to replace a character in a string. This method has two required arguments: the character to be replaced, and the character you'd like it to be replaced with.

An easy way to represent this is as follows:

```python

string.replace(old,new)

```

An example of this method is below:

```python

example = 'This is a string'

example.replace('i','!')

#Returns 'Th!s !s a str!ng'

```

There is an optional third argument in the `.replace()` method that specifies the number of times you'd like to replace the character. For example, if you'd like to replace only the first 'i' from the last code block, you'd write the following code:

```python

example = 'This is a string'

example.replace('i','!',1)

#Returns 'Th!s is a string'

```


## Moving On

This article discussed strings and the various ways you can manipulate them in Python. Strings are one of the most important data structures in Python - we'll explore other data structures in the next lesson of the course.
