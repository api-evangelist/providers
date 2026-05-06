---
aid: apache-spark
name: Apache Spark
description: Apache Spark is a unified analytics engine for large-scale data processing. It provides high-level APIs in Java, Scala, Python, and R, and an optimized engine that supports general execution graphs. Spark offers a comprehensive suite of APIs for batch processing, SQL queries, streaming analytics, machine learning, and graph computation, governed by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://spark.apache.org/images/spark-logo-trademark.png
tags:
  - Analytics
  - Big Data
  - Distributed Computing
  - Machine Learning
  - Open Source
  - Streaming
created: '2024-01-01'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-spark/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-spark:apache-spark-rest-api
    name: Apache Spark REST API
    description: REST API for monitoring Spark applications, accessing cluster information, and managing Spark jobs through the Spark UI backend. Exposes endpoints for applications, jobs, stages, tasks, storage, environment, executors, and streaming statistics on port 4040 (or 18080 for Spark History Server).
    humanURL: https://spark.apache.org/docs/latest/monitoring.html#rest-api
    tags:
      - Jobs
      - Metrics
      - Monitoring
      - Stages
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/monitoring.html#rest-api
  - aid: apache-spark:apache-spark-sql-api
    name: Apache Spark SQL API
    description: Spark module for structured data processing with DataFrame and Dataset APIs. Provides a SQL interface and supports various data sources including Parquet, ORC, JSON, CSV, JDBC, Hive, and Delta Lake. The Spark SQL API supports Scala, Python, Java, and R bindings.
    humanURL: https://spark.apache.org/docs/latest/sql-programming-guide.html
    tags:
      - DataFrames
      - SQL
      - Structured Data
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/sql-programming-guide.html
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html
        title: Scala API Reference
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html
        title: Python API Reference
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/sql/package-summary.html
        title: Java API Reference
  - aid: apache-spark:apache-spark-streaming-api
    name: Apache Spark Streaming API
    description: Scalable, high-throughput, fault-tolerant stream processing of live data streams. Supports Structured Streaming (the newer DStream-based API) with exactly-once semantics, continuous processing mode, and integration with Kafka, Kinesis, HDFS, and other sources.
    humanURL: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
    tags:
      - Data Processing
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html
        title: Scala Streaming API
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.streaming/index.html
        title: Python Streaming API
  - aid: apache-spark:apache-spark-mllib-api
    name: Apache Spark MLlib API
    description: Spark's scalable machine learning library consisting of common learning algorithms and utilities, including classification, regression, clustering, collaborative filtering, dimensionality reduction, and feature engineering. Supports pipeline-based ML workflows through the spark.ml package.
    humanURL: https://spark.apache.org/docs/latest/ml-guide.html
    tags:
      - Algorithms
      - Data Science
      - Machine Learning
      - ML
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/ml-guide.html
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html
        title: Scala MLlib API
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html
        title: Python MLlib API
  - aid: apache-spark:apache-spark-graphx-api
    name: Apache Spark GraphX API
    description: Spark API for graphs and graph-parallel computation with a collection of graph algorithms and builders, including PageRank, Connected Components, Triangle Counting, and shortest paths.
    humanURL: https://spark.apache.org/docs/latest/graphx-programming-guide.html
    tags:
      - Analytics
      - Graph Processing
      - Graphs
    properties:
      - type: Documentation
        url: https://spark.apache.org/docs/latest/graphx-programming-guide.html
      - type: SDK
        url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html
        title: Scala GraphX API
common:
  - type: GitHubRepository
    url: https://github.com/apache/spark
  - type: Portal
    url: https://spark.apache.org/
  - type: Documentation
    url: https://spark.apache.org/docs/latest/
  - type: GettingStarted
    url: https://spark.apache.org/docs/latest/quick-start.html
  - type: Blog
    url: https://spark.apache.org/news/
  - type: Support
    url: https://spark.apache.org/community.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/apache-spark
  - type: SDK
    url: https://pypi.org/project/pyspark/
    title: PySpark (Python)
  - type: SDK
    url: https://search.maven.org/search?q=g:org.apache.spark
    title: Maven (Scala/Java)
  - type: Features
    data:
      - name: Unified Analytics Engine
        description: Single engine for batch, streaming, SQL, ML, and graph processing workloads.
      - name: Lazy Evaluation and DAG Execution
        description: Optimized execution plans with Catalyst optimizer and DAG scheduling.
      - name: In-Memory Processing
        description: Up to 100x faster than Hadoop MapReduce for iterative algorithms via in-memory caching.
      - name: Structured Streaming
        description: Unified streaming and batch processing with exactly-once semantics and Kafka integration.
      - name: Multi-Language Support
        description: High-level APIs in Scala, Java, Python (PySpark), and R (SparkR).
      - name: Delta Lake Integration
        description: ACID transactions, schema evolution, and time travel for data lakes.
      - name: Kubernetes Native
        description: Native Kubernetes scheduling for cloud-native deployment of Spark workloads.
  - type: UseCases
    data:
      - name: Large-Scale ETL
        description: Extract, transform, and load petabytes of data across distributed clusters.
      - name: Real-Time Analytics
        description: Streaming analytics on live event data with sub-second latency.
      - name: Machine Learning Pipelines
        description: Distributed ML training and feature engineering at scale with MLlib.
      - name: Data Lake Processing
        description: Query and transform data stored in cloud object stores and HDFS.
      - name: Interactive SQL Analytics
        description: Interactive SQL queries on structured and semi-structured data at scale.
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: HDFS storage, YARN cluster manager, and Hadoop ecosystem integration.
      - name: Apache Kafka
        description: Structured Streaming source and sink for real-time event processing.
      - name: Delta Lake
        description: Open-source storage layer with ACID transactions for data lakes.
      - name: Apache Iceberg
        description: Open table format for huge analytic datasets on cloud storage.
      - name: Apache Hive
        description: Hive metastore integration for table catalog and metadata management.
      - name: Kubernetes
        description: Native Kubernetes scheduling for cloud-native Spark deployments.
      - name: Apache Airflow
        description: Workflow orchestration for scheduling and managing Spark jobs.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
