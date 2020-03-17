---
title: 'How I Taught Myself to Code in 6 Months (and How You Can Too)'
date: 2020-03-17
author: Nick McCullum
layout: post
permalink: /learn-to-code/
---


Over the last six months, I’ve been on an unbelievably fun journey teaching myself how to code. I wrote this article to share my journey.

To be clear, it has not been easy. With that said, learning to code is simpler than ever because of the vast swath of free resources available on the Internet.

In this article, I’ll outline my journing from knowing next-to-nothing about software to being a productive software engineer in a real company. Be sure to read to the end, where I provide tips to a novice developer starting today.


## What Does It Mean to “Learn to Code”

Before discussing my journey, I considered it important to provide some context on what I mean when I say that I ‘know how to code’.

Like any field, there is huge variance in the knowledge base of its practitioners. I am still decades away from being an expert in software engineering. When I say “I know how to code,” here’s a rough description of what that means:



1. I have an understanding of version control systems like git and use a remote git tool (like GitHub) on a regular basis
2. I have a high-level understanding of how the front- and back-end work and a deep understanding of one 
3. I have a programming language of choice (for me, Python) and can build performant applications using that language; within the language, I have understanding of the major libraries and frameworks (for Python, the main contenders would be NumPy, Pandas, SciPy, and Django)
4. I have enough understanding of a cloud computing provider (like Amazon Web Services) to deploy and monitor a large application

With that out of the way, let’s begin discussing how I taught myself how to code.


## Step 0: My Background

Like most twenty-somethings that work in finance or technology, I had some background in software prior to teaching myself how to code. I wanted to start by providing the brief education I had on software before embarking on this journey. 

My previous education included only two exposures to building software:



*   In college (circa 2015), I took one course on introductory Java programming
*   I started (but soon quit) the freeCodeCamp curriculum, also in 2015

Speaking of freeCodeCamp...


## Step 1: freeCodeCamp

Because of my previous exposure, the first resource I used to learn to code is [freeCodeCamp](https://www.freecodecamp.org/) - a free online challenge-based tool for learning frontend software development. 

I have followed freeCodeCamp for many years after originally starting its curriculum back in college. Ever since, I have been on Quincy Larson’s (the founder) mailing list for freeCodeCamp and have been amazed at the progress of non-profit over time.

I eventually completed the basic curriculum of freeCodeCamp, which involved completed the first two certifications:



1. Responsive Web Design Certification
2. JavaScript Algorithms and Data Structures Certification

I did not see much value in learning additional frontend skills because I knew I wanted to work backend software infrastructure. However, I was not sure the best way to proceed along my educational journey. 

I began listening to the freeCodeCamp podcast while working through the curriculum. In doing so, I heard Quincy mention a course called ‘JavaScript 30’, which was the next destination on my software education journey.


## Step 2: JavaScript 30

JavaScript 30 is a free 30-day programming course taught by [Wes Bos](https://wesbos.com/) that guides you through building 30 real programs in 30 days. 

Wes is an excellent teacher. His knowledge of the front end software landscape never fails to impress me. Moreover, his courses are very affordable. He teaches the following free courses:



*   [Command Line Power User](https://commandlinepoweruser.com/)
*   [Learn Redux](https://learnredux.com/)
*   [What The FlexBox?!](https://flexbox.io/)
*   [CSS Grid](https://cssgrid.io/)
*   [Mastering Markdown](https://masteringmarkdown.com/)

He also has a few paid courses, like [React for Beginners](https://reactforbeginners.com/) and [Beginner JavaScript](https://beginnerjavascript.com/).

I basically followed the JavaScript 30 curriculum exactly as prescribed, but with one small change: I made sure to turn the JavaScript 30 projects into real websites whenever possible. 

You can see a few examples of these websites below:



*   [Canadian Cities By Population](http://canadiancitiesbypopulation.com/)
*   [U.S. Cities By Population](http://uscitiesbypopulation.com/)
*   [My Robo Voice](http://myrobovoice.com/)
*   [Minimalist Clock](http://minimalistclock.com/)
*   [Online Drum Kit](http://onlinedrumkit.com/)

I generally used Amazon Web Services (AWS) Route 53 combined with GitHub Pages to host these websites. For Route 53, you have to pay the upfront cost of purchasing the domain name and then $0.50/domain thereafter. GitHub Pages is available for free. Altogether, I learned _a ton _from pushing these to the Internet - and for very little cost. 

With that said, building these websites was not the end goal. I wanted to build fully-fledged web applications that interacted with a database on the backend. For that, I turned to a different course provider.


## Step 3: Udemy

The main problem with freeCodeCamp and Wes Bos’ JavaScript 30 course was that they were entirely focused on front end web development. Note that this isn’t a “real” problem; instead, it was a mismatch between what I was learning and what I needed to learn. 

After talking to a good friend who works in software, we concluded that I needed to learn Python and SQL. The first Udemy course that I took was Jose Portilla’s [Python for Financial Analysis and Algorithmic Trading](https://www.udemy.com/course/python-for-finance-and-trading-algorithms/). This course formed the core set of knowledge that I use today, including:



1. Working with the major data types like integers, dictionaries, lists, and strings.
2. Downloading and operating the Anaconda distribution of Python, marketed as “The World’s Most Popular Data Science Platform”
3. Installing and working with important Python libraries like NumPy, Pandas, and SciPy

After that, there were other important skills that I needed to truly develop software from scratch. Wes Bos’ free course [Command Line Power User](https://commandlinepoweruser.com/) taught me how to make smart use of the terminal. I also benefited tremendously from the following three courses: 



1. [GitHub Ultimate: Master Git and GitHub - Beginner to Expert](https://www.udemy.com/course/github-ultimate/)
2. [Shell Scripting: Discover How To Automate Command Line Tasks](https://www.udemy.com/course/shell-scripting-linux/)
3. [Vim Masterclass](https://www.udemy.com/course/vim-commands-cheat-sheet/)

In addition to these courses, I also enrolled in a half-dozen other Udemy courses, but finished barely any of them.

A quick note on cost - I am fortunate to have an employer who believes in the power of continuing education and purchased these courses on my behalf. While you might not think that your employer would do the same, I’d encourage you to ask. At best, you’ll get the courses for free; at worst, you’ll be declined - but their perception of you will improve because they’ll notice you trying to expand your skill set at your own discretion. 


## Step 4: Build Your First Real Project

After a ton of coursework, I believed I was ready to start building a real-world project. At my employer, we had a complicated task that was ready for automating. 

Here’s the gist of the project.

On our website, we had a number of Excel spreadsheets full of financial data for groups of publicly-traded equities. These were free for download in exchange for joining our mailing list - a “content upgrade”, as the marketing folks call it. 

At the time I decided to automate this task, one of my colleagues was manually updating these spreadsheets once per month. This involved exporting the necessary financial data from [YCharts](https://ycharts.com/), formatting the Excel spreadsheet, and uploading the documents to [Wordpress](https://wordpress.com/). 

This doesn’t sound that horrible until you scale it up. We were updating many dozens of these databases each month, spends dozens of hours on a mundane task.

The steps I used to automate this task were as follows:



1. **Find a data source:** I used [IEX Cloud](https://iexcloud.io/), an affordable provider of stock market data.
2. **Import the data:** I pinged the IEX Cloud API using [Python’s requests library](https://requests.readthedocs.io/en/master/) and stored it in a [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html).
3. **Manipulate the data:** I used many of Python’s and Pandas’ built in functions for this.
4. **Save the data as an .xlsx file:** I used the [XlsxWriter library for Python](https://xlsxwriter.readthedocs.io/)
5. **Push the data to a centralized location for customers to download:** I stored the data in an [AWS S3](https://aws.amazon.com/s3/) bucket


## Step 5: Fill Out Your Knowledge Gaps

After building and deploying my first real software tool, I noticed that there were many steps of the software development lifecycle that I didn’t fully understand. To finish off this article, I thought I’d briefly discuss them one-by-one.



*   **Tooling & Text Editors:** I bounced around between six different text editors while I was learning to code: Atom, PyCharm, JupyterLab (if you count that), Sublime Text, VS Code, and Vim. I now use Vim for almost all my development. I would recommend really focusing on becoming proficient with one text editor frmo the very beginning. 
*   **Dependency Management:** I now use Python’s pip package manager to manage dependencies. I also use [virtualenv](https://virtualenv.pypa.io/en/latest/) to manage my virtual environments, and send them to other developers using a requirements.txt file. It’s important to start doing this from the very beginning or you will experience negative side effects when switching from project to project later on.
*   **Version Control and Source Code Management: **A productive software engineer is identifiable by the contributions shown on their GitHub profile. This is because mature engineers push their code early and often, so that they can catch (and fix) smaller bugs frequently. I would recommend becoming familiar with command line git at the start of your software education journey. 
*   **Profiling:** In software engineering, ‘profiling’ is the act of running code and measuring how long it takes to complete. Profiling breaks down a script by listing its specific components and how long they take in total. Without a knowledge of profiling, it is difficult (if not impossible) to write performant code ready for modern-day applications. You can learn more about how to profile Python code [here](https://docs.python.org/2/library/profile.html).


## Tips for the Novice Developer

In this article, I have outlined my journey to becoming a productive software engineer. Like most people who are self-educated on a topic, the path I took was highly suboptimal. I’d like to close this article by describing _the path I’d wish I’d taken _instead.

If I were re-learning how to write software today, I would skip all the non-essential steps (which, in general, were omitted from this article) and follow these steps:



1. Create a GitHub account
2. Familiarize myself with how to use git at the command line
3. Work through the first few sections of freeCodeCamp to familiarize myself with the basics of HTML, CSS, and JavaScript for frontend development
4. Take Jose Portilla’s Python for Financial Analysis and Algorithmic Trading
5. START BUILDING REAL PROJECTS

The last point is of paramount importance. Unsurprisingly, the best way to get good at building software is by building software. It is impossible to understand the intricacies of software engineering without immersive yourself in complex, real-world problems. 


## Final Thoughts

After a wild six months, I now have enough rudimentary knowledge to be producing production-level code on a daily basis. It has been transformative for my career, my growth, and my life. 

If you are starting your software development journey today and have any questions (or need advice!), please feel free to [email me](mailto:nicholasmccullum@gmail.com). I would love to help you in any way possible. 


<!-- Docs to Markdown version 1.0β19 -->
