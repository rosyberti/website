---
layout: page
title: The 3 Interfaces of Matplotlib
---

In this lesson, we will briefly discuss the 3 different interfaces available to matplotlib users and explain why they are a common source of confusion for new users to the visualization library.


## The 3 Interfaces of Matplotlib

Matplotlib has three different interfaces:



*   Pylab - which is deprecated
*   Pyplot - which we used to quickly create a chart in the last lesson
*   An Object-Oriented API


## Pylab

Pylab was created by matplotlib's creator, [John D. Hunter](https://en.wikipedia.org/wiki/John_D._Hunter), as a very close approximation to the MATLAB programming language. Pylab made it very easy for MATLAB practitioners to switch to Python for visualizations.

The main problem with Pylab is that it imports everything into the global namespace. This means that it could create clashes between variables declared in functions or classes. 


## Pyplot

Pyplot was created to fix the problems associated with the Pylab interface. Namely, pyplot used namespaced code, which prevents clashes between global and local variables. 

Pyplot is definitely the most popular matplotlib interface used today. The majority of practitioners and educators will use pyplot as their method for interacting with the matplotlib visualization library.

Pyplot does break down when you need very specific modifications to your data visualizations. This is where the object-oriented API comes in.


## Object-Oriented API

Matplotlib's object-oriented API is designed for users who want total control over their data visualizations. 

However, it does come with some downsides. It is very syntactically heavy, which means you might need to write numerous lines of code to create simple visualizations.


## Why The 3 Interfaces Can Cause Confusion

As I mentioned in the introduction to this lesson, the 3 interfaces of matplotlib commonly cause confusion among beginner matplotlib practitioners.

Why is this?

It is because since there are 3 interfaces, this means that there are (at least) three different ways of creating each chart. When people are learning matplotlib, they will often Google search for similar examples (as they should!) - but this usually results in them reading about many different ways of solving the same problem, which is confusing.


## Moving On

In this lesson, we briefly explored each of the 3 major interfaces available in matplotilb. Do not worry if some of the nomenclature or terminology discussed in this lesson was unfamiliar to you. 

The goal of this lesson was to simply make you aware that matlpotlib has 3 different interfaces, and that because of this you may encounter many different ways to solve the same data visualization problem in the future. Moving forward, we will be using the `pyplot` module for the remainder of this course. 
