# Introduction to text analysis with PySpark using Twitter data

Objective:
_Using the Spark Python API (PySpark) in a Databricks notebook environment to perform some basic text mining._

***************************************************************************************

**PLAN**


1. Data overview
    + Tweet object
    + JSON format
    + Spark DataFrame
    + Databricks table
    
2. Data sourcing
    + (prior) Get Twitter data using the REST API
    + (prior) Aggregate tweet collection as a single JSON file
    + (prior) Upload the JSON source file to a Databricks table 
    + Create dataframe from Databricks table
    
3. Data exploration
   + Show dataframe, print schema
   + Basic sql queries
   + User tweet frequency bar graph
   + Count tweets containing a given keyword

4. Text preprocessing
   + tokenization (unigram, bigram, ...)
   + stop word removal
   + lemmatization (stemming, synonym expansion)

5. Text analysis
   + Clustering?

***************************************************************************************
**Doc & programming guides**
+ [PySpark doc](https://spark.apache.org/docs/latest/api/python/)
+ [Spark SQL programming guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
+ [Databricks doc](https://docs.databricks.com/)
+ [Twitter API overview](https://dev.twitter.com/overview/api)

**Tutorials**
+ [Databricks workshop doc](http://training.databricks.com/workshop/sparkcamp.pdf)
+ [Scala crash course](https://lintool.github.io/SparkTutorial/slides/day1_Scala_crash_course.pdf)

***************************************************************************************
