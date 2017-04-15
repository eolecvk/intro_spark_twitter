# Introduction to text mining with Spark

Objectives:

1. To learn about the Spark framework
2. To become familiar with the Databricks notebook environment
3. To implement text mining techniques
4. To work with social media data (tweets)


***************************************************************************************

**PLAN**


1. Overview of the relevant data objects and structures, [
[Git](https://github.com/eolecvk/intro_spark_twitter/blob/master/notebooks/data_overview.ipynb) |
[Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3923635548890252/3963252404083091/4930913221861820/latest.html)
]
    + Tweet object
    + JSON format
    + Spark DataFrame
    + Databricks table
    
2. Sourcing, [
[Git](https://github.com/eolecvk/intro_spark_twitter/blob/master/notebooks/data_sourcing.ipynb) | 
[Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3923635548890252/3963252404083100/4930913221861820/latest.html)
]

    + Define relevant search parameter or make a random search.
    + Get tweets using the [REST API](https://dev.twitter.com/rest/public)(prior)
    + Aggregate tweets to this [single JSON source file](https://github.com/eolecvk/intro_spark_twitter/blob/master/data/tweets.json) with [this script](https://github.com/eolecvk/intro_spark_twitter/blob/master/utils/json_aggregator.py)) (prior)
    + _Export to S3_
    + Upload the JSON source file to a Databricks table 
    + Create dataframe from Databricks table
    
3. Exploration, [
[Git](https://github.com/eolecvk/intro_spark_twitter/blob/master/notebooks/data_exploration.ipynb) | 
[Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3923635548890252/3963252404083096/4930913221861820/latest.html)]
   + Show dataframe, print schema
   + Basic sql queries
   + User tweet frequency bar graph
   + Count tweets containing a given keyword

4. Preparation, [
[Git](https://github.com/eolecvk/intro_spark_twitter/blob/master/notebooks/data_preparation.ipynb) | 
[Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3923635548890252/1357850364289680/4930913221861820/latest.html)
]
   + tokenization
   + stop word removal
   + Stemming
   + N-Grams

5. Analysis (available soon!)
   + Principal Component Analysis
   + Cluster analysis
   + ..


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
