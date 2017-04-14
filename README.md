# Introduction to text mining with Spark

Objectives:

1. To learn about the Spark framework
2. To become familiar with the Databricks notebook environment
3. To implement text mining techniques
4. To work with social media data (tweets)


***************************************************************************************

**PLAN**


1. Overview of the relevant data objects and structures, [
[Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3923635548890252/3963252404083091/4930913221861820/latest.html)
]
    + Tweet object
    + JSON format
    + Spark DataFrame
    + Databricks table
    
2. Sourcing, [
[Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3923635548890252/3963252404083100/4930913221861820/latest.html)
]
    + Get Twitter data using the REST API (prior)
    + Aggregate tweet collection as a single JSON file (prior)
    + Upload the JSON source file to a Databricks table 
    + Create dataframe from Databricks table
    
3. Exploration, [
[Databricks](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3923635548890252/3963252404083096/4930913221861820/latest.html)]
   + Show dataframe, print schema
   + Basic sql queries
   + User tweet frequency bar graph
   + Count tweets containing a given keyword

4. Preparation, [
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
