---
aid: pyspark
name: Apache PySpark
description: Python API for Apache Spark - A unified analytics engine for large-scale data processing supporting batch processing, streaming, machine learning, and graph computing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Big Data
  - Data Processing
  - Distributed Computing
  - Machine Learning
  - Python
  - Streaming
url: https://raw.githubusercontent.com/api-evangelist/pyspark/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: pyspark:pyspark-core-api
    name: PySpark Core API
    description: Core Spark functionality including RDDs, SparkContext, and basic operations.
    humanURL: https://spark.apache.org/docs/latest/api/python/reference/pyspark.html
    tags:
      - RDD
      - Spark Context
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.html
      - type: APIReference
        url: https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.SparkContext.html
  - aid: pyspark:pyspark-sql
    name: PySpark SQL
    description: Structured data processing with DataFrame and SQL operations.
    humanURL: https://spark.apache.org/docs/latest/sql-programming-guide.html
    tags:
      - DataFrame
      - SQL
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html
      - type: GettingStarted
        url: https://spark.apache.org/docs/latest/sql-getting-started.html
  - aid: pyspark:pyspark-streaming
    name: PySpark Streaming
    description: Real-time stream processing capabilities using DStreams and Structured Streaming.
    humanURL: https://spark.apache.org/docs/latest/streaming-programming-guide.html
    tags:
      - Streaming
      - Real-Time
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.streaming/index.html
      - type: ProgrammingGuide
        url: https://spark.apache.org/docs/latest/streaming-programming-guide.html
  - aid: pyspark:pyspark-mllib
    name: PySpark MLlib
    description: Machine learning library with scalable algorithms for classification, regression, clustering, and more.
    humanURL: https://spark.apache.org/docs/latest/ml-guide.html
    tags:
      - Machine Learning
      - MLlib
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html
      - type: MLGuide
        url: https://spark.apache.org/docs/latest/ml-guide.html
  - aid: pyspark:pyspark-ml
    name: PySpark ML (DataFrame-based)
    description: DataFrame-based machine learning API with pipelines and feature transformers.
    humanURL: https://spark.apache.org/docs/latest/ml-pipeline.html
    tags:
      - Machine Learning
      - Pipeline
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html
      - type: PipelineGuide
        url: https://spark.apache.org/docs/latest/ml-pipeline.html
common:
  - type: Website
    url: https://spark.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache/spark
  - type: GettingStarted
    url: https://spark.apache.org/docs/latest/api/python/getting_started/install.html
  - type: QuickStart
    url: https://spark.apache.org/docs/latest/quick-start.html
  - type: Downloads
    url: https://spark.apache.org/downloads.html
  - type: Community
    url: https://spark.apache.org/community.html
  - type: IssueTracker
    url: https://issues.apache.org/jira/projects/SPARK
  - type: ReleaseNotes
    url: https://spark.apache.org/releases/
  - type: Security
    url: https://spark.apache.org/security.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
