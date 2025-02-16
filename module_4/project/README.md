
# Module 4 -  Final Project Specifications

## Introduction

In this lesson, we'll review all the guidelines and specifications for the final project for Module 4.

## Objectives

* Understand all required aspects of the Final Project for Module 4
* Understand all required deliverables
* Understand what constitutes a successful project

### Final Project Summary

Another module down--you're absolutely crushing it! For this project, you'll get to flex your **_Regression & Time-Series_** muscles!

<img src='https://raw.githubusercontent.com/learn-co-curriculum/dsc-mod-4-project/master/images/timegif.gif'>

For this module's final project, we're going to put your new found **Regression & Time Series Analysis_** skills to the test.

### The Project

For this project, you will be acting as a consultant for a fictional firm. As a part of your data exploration, come up with a driving question based on this data.  For example, if you were given a data set of housing price data for a given city, a driving question might be:

> what are the top 5 best zipcodes for us to invest in?


## The Deliverables

The goal of this project is to have you complete a very common real-world task in regard to Regression and Time-Series Modeling. However, real world problems often come with a significant degree of ambiguity, which requires you to use your knowledge of statistics and data science to think critically about and answer.

In short, to pass this project, demonstrating the quality and thoughtfulness of your overall recommendation is at least as important as successfully building your models!

In order to successfully complete this project, you must have:

* A well-documented **_Jupyter Notebook_** containing any code you've written for this project.
* An **_'Executive Summary' PowerPoint Presentation_** that explains your rationale and methodology for determining the best zipcodes for investment.


### Jupyter Notebook Must-Haves

1. You must source & clean your data.  All boring stuff should be pushed to a .py file that is imported.  A single data set (albeit possibly from multiple sources) should be able to support all of the following requirements.
2. You must do one each of a linear regression, a logistic regression, and a time-series analysis (to included, at a minimum, a calculation of trend and seasonality).
3. In either your linear or logistic regression, use $R^2$ and AIC/BIC to determine the best of two models
4. Visualizations to support each of your models built

#### Organization/Code Cleanliness

The notebook should be well organized, easy to follow, and code is modularized and commented where appropriate.

* Level Up: The notebook contains well-formatted, professional looking markdown cells explaining any substantial code. All functions have docstrings that act as professional-quality documentation.
* The notebook is written to technical audiences with a way to both understand your approach and reproduce your results. The target audience for this deliverable is other data scientists looking to validate your findings.
* Data visualizations you create should be clearly labeled and contextualized--that is, they fit with the surrounding code or problems you're trying to solve. No dropping data visualizations randomly around your notebook without any context!

#### Findings

Your notebook should briefly mention the metrics you have defined as "best", so that any readers understand what technical metrics you are trying to optimize. You do **not** need to explain or defend your your choices in the notebook--the blog post and executive summary presentation are both better suited to that sort of content. However, the notebook should provide enough context about your definition for "best investment" so that they understand what the code you are writing is trying to solve.

#### Visualizations

Regression & Time-Series Analysis are areas of data science that lend themselves well to intuitive data visualizations. **_Any findings worth mentioning in this problem are probably also worth visualizing_**. Your notebook should make use of data visualizations as appropriate to make your findings obvious to any readers.

Also, remember that if a visualization is worth creating, then it's also worth taking the extra few minutes to make sure that it is easily understandable and well-formatted. When creating visualizations, make sure that they have:

* A title
* Clearly labeled X and Y axes, with appropriate scale for each
* A legend, when necessary
* No overlapping text that makes it hard to read
* An intelligent use of color--multiple lines should have different colors and/or symbols to make them easily differentiable to the eye
* An appropriate amount of information--avoid creating graphs that are "too busy"--for instance, don't create a line graph with 25 different lines on it

<center><img src='images/bad-graph-1.png' height=100% width=100%>
There's just too much going on in this graph for it to be readable--don't make the same mistake! (<a href='http://genywealth.com/wp-content/uploads/2010/03/line-graph.php_.png'>Source</a>)</center>

### Executive Summary Must-Haves

Your presentation should:

Contain between 5-10 professional quality slides detailing:

* A high-level overview of your methodology and findings, including the 5 zipcodes you recommend investing in
* A brief explanation of what metrics you defined as "best" in order complete this project

As always, this presentation should also:

* Take no more than 5 minutes to present
* Avoid technical jargon and explain results in a clear, actionable way for non-technical audiences.
