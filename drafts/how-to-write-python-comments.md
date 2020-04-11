For programmers, it is important that your code is easily understood by outside users. 

While professionals might not find it difficult to understand, for someone who is trying to learn Python, including comments in the code can be very helpful. 

I have seen many bad practices within Python comments over the years. 

In this article, I will explain the best way to write Python comments for developers in 2020 (and beyond!).


## What Are Python Comments?

Comments can be understood as lines of code that allow a layman to read and understand the code. 

These lines are skipped by the compilers and interpreters when the code is executed. Said differently, code instructs computers, while comments instruct humans. 

There are many reasons why developers include comments in their code.

Depending on the length of the program or the purpose of it, comments can be used to make notes for a reader or yourself. Sometimes they are also used to help another programmer understand your code.

It is always a good idea to include comments in your code when writing new code or updating an old one because you might forget your thought process later on.


## Understanding the Syntax

Python comments start with a hash sign `#` and a white space character. Anything that is written after that until the end of the line counted as a comment.

For instance:


```python
# this is a comment
```


Comments do not appear on the screen when you run a program because they do not execute. They appear in the source code for humans to get a better understanding of it. The computer, however, does not execute it.

Have a look at the code below.


```python
print ("This will show on the screen") # This will not run
```


When the above code is executed, you will see the output as `This will show on the screen.` Everything else will be ignored. 

You can make comments anywhere in the code followed by a hash mark. However, it is suggested that comments must be made at the same indent as the code it is commenting on.


## A Simple Use of Python Comments in the “Hello World” Program

The first program you ever make when learning a new language is “Hello, World!”. Here’s how you write the code for it in Python along with comments.


```python
# Print "Hello, World!" to console
print ("Hello, World!")
```


 

Let us look at another example. Consider a _for_ loop in Python that iterates over a list of items. To elaborate it in the code, you may write the following:


```python
# Define fruits variable as a list of strings
fruits = ['apple', 'mango', 'banana', 'grapes', 'strawberry', 'orange']
# To print each item in the list
for fruit in fruits:
     print(fruit)
```



## Python Multiline Comments

The above examples were for the single-line comments. There will also be times when you will need to include longer Python comments that cover multiple lines. These are called multiline comments.

Unlike C or Java, there is no syntax to write multiline comments in Python:


```python
# If you do this in Python
it will raise a Syntax error

```


However, all is not lost. While there is no native multiline commenting functionality in Python, there are two ways of doing it.

The first method is to simply press the Enter key after each line and add hashmark at the beginning of the new line:


```
# This is a good example of
# how you can include a multiline
# comment in your Python code
```


 Because each line beginning with a hash mark is ignored by the program, this is perhaps the most logical way to include multiline comments in your code. However, it is not the method that I use.

There is another thing you can do to write comments that go on for multiple lines. You can wrap your entire comment inside a set of triple quotes as shown below:


```python
"""
If you hate to type so many hash
marks at the beginning of each line,
you can just wrap it in triple quotes
like this instead
"""
```


For anyone that has familiarity with Java programming, this is very similar to comments in Java. However, you must know that it, technically, is not a comment. 

Instead, multiline comments created with the `"""` operator are strings that are not assigned to any variable and therefore, it is not called or referenced in the program when you use it. It does not appear in the bytecode and functions effectively as a comment.

At the same time, you need to be careful where you place them in your program. You might turn them into docstrings if placed incorrectly as shown in the example below:


```python
def my_function():
    """Demonstrate docstrings"""
    return None


print "Using __doc__:"
print my_function.__doc__
```


The output, in this case, will be:


```
Using __doc__:
Demonstrate docstrings
```

This is because using triple double quotes below class, method, or function declaration leads to a docstring declaration. Docstrings are used to associate documentation with Python modules, functions, classes, and methods.

Choosing between the `#` character and the `"""` character when creating multi-line strings can be confusing. I have one recommendation: if you are doubtful, just put a hash mark before the beginning of each comment line.


## Why Write Python Comments?

Commenting happens to be a significant part of any large Python application. 

Now that you know how to write simple and complex comments while keeping them separate from docstrings, I wanted to discuss when and why to use them.


###  **Understanding Your Own Code**

Programmers forget what their code does all the time, especially when codes are long, and deadlines are tight. This can make you completely lost and get you stuck in the middle of all the mess.

There may be times when you did not name your variables properly because you were in a rush. I run into this problem regularly, especially when I'm in the development stage of a new project.

Not including any Python comments to tell you "what is what" or "what does what" can be a nightmare. Completing the code and going back to comment on it never really works because, by the time you are done developing, you may forget most of what is to be placed where and you are tired.

Therefore, to make sure that your code is understood by you at any point in the future, the best way is to comment as you go.


### 
    Helping Others Understand your Code

Imagine working on a code that turns out to be more than 20,000 lines and you have to collaborate with other developers to complete it. Now, for the new developers to understand what has already been written and start working, comments will prove to be very important. 

They can skim through your code and use comments to understand what you have written and how it works. It can also help in a smooth transition if you need to hand over the project to another developer completely.


### What NOT to do When Writing Python Comments?

While there is no limitation to how you write comments, there are some practices that must be avoided at all costs to make your code easy to understand while not wasting much of your time writing them. (Because in the end, comments are not part of the actual program.)


### 
    **Do Not Repeat Yourself**

The main function of comments is to explain something that is not obvious. There are functions that are self-explanatory and you must refrain from including comments in such places. 

I am guilty of wanting to over-comment my code on some occasions. Because of this, I think a blatant example is helpful for understanding when you should not include comments in your code:


```python
return a # Returns a
```


It is very clear in the above line of code that `a `is returned. Stating the same thing in the comment makes it redundant and wastes the time of the programmer as well as the reader. It also makes the code less readable.

If while writing the code, you write some comments for your own help, make sure you go back and delete them when code is running properly.


### 
    Stay Away From Smelly Comments

Smelly comments are defined as comments that hint at a deeper problem with the code. Comments are supposed to support your code and not explain it. Said differently, smelly comments are those that explain _how_ your code works, instead of _why _it is performing a certain task.

Why are smelly comments bad? An unnecessary explanation of the code signifies that it is trying to mask any underlying issue and there are good chances that code is written poorly. No amount of commenting can fix that and it will only make the code either buggy or bulky.


### 
    Avoid Rude Comments

When working with other developers, you might need to rewrite the code and make changes to correct it. While doing so, here is what you must not do:


```python
# Put this here to fix Mike's really stupid error - what an idiot...
```


While this might be humorous when you're in the development stage, such comments can accidentally be left in the code and shipped as such to production. This will look really, really bad on your part and create problems for and within your organization.


## Header Comments in Python

Python files usually starts with a few lines of comments that state the information about the project, details about the programmer, software license used for the code, and the purpose behind creating the file. 

Below is an example of what that might look like.


```python
# -----------------------------------------------------------
# demonstrates how to run a program
#
# (C) 2020 Nick McCullum, Brunswick, Canada
# Released under Public License ABC
# email nicholasmccullum@gmail.com
# -----------------------------------------------------------
```


In larger organizations, this is helpful because it demonstrates who should be contacted if a code file begins to malfunction.


## The Bottom Line

Writing comments is not and should not be a tedious task. 

It helps the programmers and non-technical people understand the code. Even if you visit your code at a later date, you will not feel lost. 

In this article, we demonstrated how to write Python comments properly.

If you're interested in more articles that will show you how to become a better software developer, please feel free to join my mailing list below:
