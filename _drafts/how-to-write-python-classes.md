---
title: 'How To Write Python Classes: Code, Examples, & More'
date: 2020-04-18
author: Nick McCullum
layout: post
permalink: /how-to-write-python-classes/
---

Python is an object-oriented programming (OOP) language. 

OOP is methodology used by programmers that enables a system or program to be defined as a set of objects, which can be manipulated and controlled in a piece-by-piece manner. 

It is important for you to understand why object oriented languages are necessary in programming. When creating complex code, object-oriented programming allows you to re-use code, making it easy to maintain and scale. It also puts emphasis on objects, unlike procedure oriented programming languages that stress the importance of functions.

In this article, I am going to teach you how to write Python classes - which are special constructs that programmers use to keep things which are considered to be related together. 

## What is a Python Class Object?

For us to understand [Python classes](https://nickmccullum.com/python-course/classes/), you will first need to understand what an object is.

In Python, an object is an encapsulation of variables and functions into a single entity. The object functions act on the data stored within the object. An object is also referred to as an instance. And hence, instantiation is the word we use to refer to the process of creating an object.

A class object is created with the same name as the class.  We will see this in examples later in this article.

## What are Python Classes?

A _class_ is a code template used to create objects. On the other hand, objects are _instances_ of classes. 

An example could be helpful here. Consider a company that employs salespeople where one of these salespeople is named 'Nick'. 

If we needed to write this logic into a Python program, we would say that "Salesperson" is a _class_, while "Nick" is an _instance_ of "Salesperson". Each Salesperson instance has certain data associated with it (monthly sales, perhaps) and functions that it can perform (cold calling, as an example).

As you may have noticed, a class is different from a function in that it contains not just functions, but also data (stored in variables). These data variables are referred to as properties. The functions are referred to as methods. A Python class is a blueprint for creating objects. Methods are functions that are defined inside a given python class.

 

To understand what a class is, let's consider another example. You can think of a class as the design (or prototype) of a building. The design contains every detail about the building including material, size, and shape. Based on this description, the building is the object.

Given this blueprint, we can actually create many different buildings. Each building would be an _instance_ of the blueprint. These would have the same functions (or methods) within them (turn off the heat, perhaps), but would have different variables (location, as an example).


## How To Define Python Classes?

In Python, a class is created using the keyword _class, _followed by the name of your class, as follows:

class ClassName

 

Python classes are somewhat unique because their first letter is always capitalized. So we would use `ClassName`, not `class_name` or something similar.

Next, let's consider the generalized layout of a Python class:

class  ClassName:

#statement-1

.

.

#statement-N

 

As you can see, a Python class consists of a list of statements, indented like a loop or a function. We are going to see an example of these statements in a class later on in this article. 

We will be creating a class called 'Food' for the remainder of this article.

class Food

 

 


## Class Attributes in Python

As we continue, you will notice that you can create a class without any arguments. However, a class by itself without some functionality associated with it is of no use.

What you should know is that functionalities in Python classes are defined by setting _attributes._

These attributes are the ones that will then act as containers for _data_. As we mentioned earlier, data in a class are called _properties_.

Note that class attributes are attributes that are defined at the class level.  These attributes are owned by class itself and will be shared by all the instances of that class. 

Because they should have the same value for every instance. we define class attributes outside of the class methods. In general class attributes are are placed at the top, just below the class header.

To understand these terms well, let’s set some attributes in the class we had created, class Food.

class Food:

name= “pizza”

type= “snack”

 	 #name and type set as attributes of the class Food

** **

To summarize, class attributes are the same for all instances of the class, while class properties may differ between instances and can be modified by the class's methods.


## How To Instantiate Python Classes

Python classes can be assigned to variables. Assigning a class to a variable is what is called instantiation.

As I mentioned above, a class object is created with the same name as the class. 

Once you instantiate your class, you then assign it to a variable. In our case, we shall instantiate the class Food and assign it to a variable called `food`.

food=Food () 

# instantiate the class Food and assign it to variable food

** **


## Accessing Class Attributes

Instantiating a class allows us to access the attributes defined in that particular class.

To access the attributes inside a class, we use the dot operator `.`.

For instance, let us consider our example class `Food`. Recall that it has two attributes, `name` and `type`:

class Food:

name= “pizza”

type= “snack”

 

We are going to access the attribute name using the following syntax.

print (food.**name**)

#access the class attribute _name_ inside the class Food.

This will output the name of the food as shown below.

pizza

** **

Similarly, we can access the `type` attribute as follows:

print (food.**type**)

#access the class attribute name inside the class Food.

This will output the name of the food as shown below.

snack

** **

You should note that the class object not only allows us to access the attributes in that particular class, but also allows us to instantiate new objects of that class.** **


## Methods in Python Classes

We have already seen how to define a python class and how to set some attributes in our class. We have also seen how to instantiate a class as well as how to access an attribute inside the class.

We will now see how methods in a class are defined.


### How To Define Methods in a Python Class

Recall we said that a class contains two components: properties and methods.

In python classes, methods are functions that you define to access and/or modify the attributes.

It is important to note that once we define methods, we will always need to provide the first argument to the method with a _self_ keyword.

For instance, in our example class Food, which has two attributes _name _and _type,_ we can define one method, _change_type_. The defined method will take in an argument _new_type_ along with the key-word _self_, as shown in the following code block.

**class** Food:

name= “pizza”

**type**= “snack”

 	 def change_type(self, new_type)

 		#note that the first argument is self

 		self.**type**=new_type

 		#access class attribute _type_ with the self keyword

 

There is a lot to unpack here, so let’s discuss this example in a bit more detail.

You may have noticed the self-parameter in method definition inside the class. The self-parameter is a reference to the current instance of the class. 

It is important to note that whenever an object calls its function, the object itself is passed as the first argument. Therefore, the first argument of the function in class must be the object itself. This is conventionally called _self, _although you could name it whatever you want. 

The self-parameter is used to access variables that belong to the class. You should also note that you do not give a value for this parameter when you call the method. Instead, Python provides it.

Interestingly enough, if we have a method that takes no arguments, the requirement of the `self` parameter means that we still need to have one argument (`self`).

The following code block shows instantiation of example _class Food_ and changing of variable _type_ with the method _change_type_.

# instantiate the class

food = Food()

# print the current object type

print(food.type)    

**#**This will output “snack”

#change the type using the change_type method

food.change_type("meal")

**print**(food.**t**ype)      

#This will output “meal”

_ _


## The _init _ Method

To have an understanding of Python classes, you need to understand the built in _init_ method.


### What is an _init_method?

The _init_  method is found in all classes and is executed every time the class is initiated. The method is used to initialize the object’s state.

Let's use our example class to see how this is done.

 class Food:

 	name=pizza

type=snack

 

 	def _init_(self, **type**):

   		self.**type**=**type**

 

 	def change_**type**(self, new_type):

  		self.**type**= new_type

_ _

The `init` function in the above code block specifies that the `type` property is actually accepted as a variable upon the class's instantiation.


## Instance Attributes

In the following section, we shall learn how to create instance attributes in Python classes

We shall also learn how to provide values for the attributes in your class at runtime.


### Defining instant attributes

Instance properties belong to specific instances of a class. This means, if your class has two different instances, their instance attributes are usually different., unlike the class attributes. After you have mastered how to define attributes inside the init method, the next thing you should know is how to define separate attribute values for separate objects.

We are going to instantiate two of our variables in our example class _Food_.

This is done as shown in the below code block.

snack=Food (“snack”)

meal=Food (“meal”)

 

 print(**snack**.type)

#This will output “snack”

 print(**meal**.type)

#This will output “meal”

 


## Now, having learnt that, the next thing we shall learn is how to delete properties of an object in python classes.


## **How to Delete Object Properties in python classes**

To delete objects in a python class, you use the keyword _del_

For instance, in our class example, we can delete the _name_ property with the following syntax

**del** food.name


## **The Pass Statement in Python Classes**

As you learn python, you will realize that definitions of a class cannot be empty.  

However, if for any reason, you have a class definition that does not have content, you should put in the _pass_ statement to avoid the code getting an error. 

This is useful in the development stage when you know that you will need to create a class, but are not yet sure what its attributes, properties, or methods should be.

For instance, in our example class, if it did not have any content, we could do the following:

**Class** Food:

**pass**

 


## Python Class Inheritance

Python, being an object-oriented language, allows you to create another class by deriving it from an already existing class, instead of starting from scratch. This is referred to as class inheritance.

This is done by listing the parent class (the pre-existing class that you are deriving attributes from) in parentheses after the new class name.

Note that what the child class (the new class) inherits from the parent class are the attributes of the parent class.

These attributes are then used in the child class as if they were defined there.

 Interestingly, a child class can also override the properties (data) and methods (functions) from the parent class.

We are now going to see how a child class inherits from the parent class.


### The Syntax of Python Class Inheritance

We are going to use our example class (class Food), as the parent class.

 

class Food:

 	def __init__(self, new_type):

		self.type = new_type

   

  	def change_type(self):

		print(self.type**)**

** **

Now we will create the child class. To do this, we shall send the parent class (in this case, class Food) as a parameter when creating the child class.

Now let us create a child class (called `Lunch`).

**class Lunch(Food):**

**pass**

** **

Note the use of the statement pass in the child class.

 You should remember that we use the pass keyword when we do not want to add any other properties or methods to the class.

Now the _Lunch class_ has the same properties and methods as the _Food class_.

Despite the child class having no properties nor methods, we can use it to change the name of food by inheriting method change_type from the parent class (class Food).

This will be as follows:

class Food:

 	def __init__(self, new_type):

		self.type = new_type

   

  	def change_type(self):

		print(self.type**)**

** **

class Lunch(Food):

 	pass

 

x = Lunch("rice")

x.change_type()

** **

 


## Final Thoughts

In this article, I have taken you through a comprehensive lesson in Python classes.  We have learnt various aspects of Python classes from introduction to inheritance**. **If you'd like to work through some practice problems on Python classes, visit [this page.](https://nickmccullum.com/python-course/classes-practice-problems/)
