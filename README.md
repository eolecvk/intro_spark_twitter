# Introduction to text mining with Spark

Objectives:

1. To learn about the Spark framework
2. To become familiar with the Databricks notebook environment
3. To implement text mining techniques
4. To work with social media data (tweets)


***************************************************************************************

**PLAN**


1. Overview of the relevant data objects and structures, [[link](https://github.com/eolecvk/intro_spark_twitter/blob/master/notebooks/data_overview.ipynb)]
    + Tweet object
    + JSON format
    + Spark DataFrame
    + Databricks table
    
2. Sourcing, [[link](https://github.com/eolecvk/intro_spark_twitter/blob/master/notebooks/data_sourcing.ipynb)]
    + (prior) Get Twitter data using the REST API
    + (prior) Aggregate tweet collection as a single JSON file
    + (prior) Upload the JSON source file to a Databricks table 
    + Create dataframe from Databricks table
    
3. Exploration, [[link](https://github.com/eolecvk/intro_spark_twitter/blob/master/notebooks/data_exploration.ipynb)]
   + Show dataframe, print schema
   + Basic sql queries
   + User tweet frequency bar graph
   + Count tweets containing a given keyword

4. Preparation, [[link]()]
   + tokenization (unigram, bigram, ...)
   + stop word removal
   + lemmatization (stemming, synonym expansion)

5. Analysis, SOON!!
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
