---
layout: page
title: Remote Data Input in Pandas
---

In the  last lesson of this course, we learned how to import data from `.csv`, `.json`, and `.xlsx` files that were saved on our local computer. We will follow up by showing you how you can import files without actually saving them to your local machine first. This is called `remote importing`.


## What Is Remote Importing and Why Is It Useful?

Remote importing means bringing a file into your Python script without having that file saved on your computer.

On the surface, it may not seem clear why we might want to engage in remote importing. However, it can be very useful.

The reason why remote importing is useful is because, by definition, it means the Python script will continue to function even if the file being imported is not saved on your computer. This means I can send my code to colleagues or friends and it will still function properly.

Throughout the rest of this lesson, I will demonstrate how to perform remote imports for `.csv`, `.json`, and `.xlsx` files.


## How To Import Remote `.csv` Files

First, navigate to this course's [GitHub Repository](https://github.com/nicholasmccullum/advanced-python/). Open up the `stock_prices` folder. Click on the file `stock_prices.csv` and then click the button for the `Raw` file, as shown below.

![Raw GitHub File Example]({{ site.baseurl }}/images/advanced-python/pandas-remote-data/raw-github-file.png)

This will take you to a new page that has the data from the `.csv` file contained within `stock_prices.csv`. 

To import this remote file into your into your Python script, you must first copy its URL to your clipboard. You can do this by either (1) highlighting the entire URL, right-clicking the selected text, and clicking `copy`, or (2) highlighting the entire URL and typing CTRL+C on your keyboard.

The URL will look like this:

```

[https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv](https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv)

```

You can pass this URL into the `read_csv` method to import the dataset into a pandas DataFrame without saving the dataset to your computer first:

```python

pd.read_csv('[https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv](https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.csv)')

```


## How To Import Remote `.json` Files

We can import remote `.json` files in a similar fashion to `.csv` files. 

First, grab the raw URL from GitHub. It will look like this:

```

[https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.json](https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.json)

```

Next, pass this URL into the `read_json` method like this:

```python

pd.read_json('[https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.json](https://raw.githubusercontent.com/nicholasmccullum/advanced-python/master/stock_prices/stock_prices.json)')

```


## How To Import Remote `.xlsx` Files

We can import remote `.xlsx` files in a similar fashion to `.csv` and `.json` files. Note that you will need to click in a slightly different place on the GitHub interface. Specifically, you'll need to right-click 'View Raw' and select 'Copy Link Address,' as shown below.

![Raw GitHub File Example]({{ site.baseurl }}/images/advanced-python/pandas-remote-data/raw-excel-file.png)

The raw URL will look like this:

```python

https://github.com/nicholasmccullum/advanced-python/blob/master/stock_prices/stock_prices.xlsx?raw=true

```

Then, pass this URL into the `read_excel` method, like this:

```python

pd.read_excel('https://github.com/nicholasmccullum/advanced-python/blob/master/stock_prices/stock_prices.xlsx?raw=true')

```


## The Downsides to Remote Importing

Remote importing means that you do not need to first save the file being imported onto your local computer, which is an unquestionable benefit.

However, remote importing also has two downsides:



1. You must have an Internet connection to perform remote imports
2. Pinging the URL to retrieve the dataset is fairly time-consuming, which means that performing remote imports will slow the speed of your Python code


## Moving On

In this lesson, we learned how to perform remote dataset imports using pandas. While remote imports have the benefit of allowing you to operate your code without saving your datasets to your local computer, they also have two important disadvantages that you should keep in mind:



3. You must have an Internet connection to perform remote imports.
4. Pinging the URL to retrieve the dataset is fairly time-consuming, which means that performing remote imports will slow the speed of your Python code.
