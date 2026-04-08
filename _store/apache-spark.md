---
aid: apache-spark
url: https://raw.githubusercontent.com/api-evangelist/apache-spark/refs/heads/main/apis.yml
apis:
- name: Apache Spark REST API
  description: REST API for monitoring Spark applications, accessing cluster information, and managing Spark jobs through the Spark UI backend.
  image: https://spark.apache.org/images/spark-logo-trademark.png
  humanURL: https://spark.apache.org/docs/latest/monitoring.html
  baseURL: http://localhost:4040/api/v1
  tags:
  - Jobs
  - Metrics
  - Monitoring
  - Stages
  properties:
  - type: Documentation
    url: https://spark.apache.org/docs/latest/monitoring.html#rest-api
  - type: OpenAPI
    url: https://spark.apache.org/docs/latest/api/openapi/spark-api.yaml
  contact:
  - FN: Apache Spark Dev Mailing List
    email: dev@spark.apache.org
    url: https://spark.apache.org/community.html
- name: Spark SQL API
  description: Spark module for structured data processing with DataFrame and Dataset APIs. Provides SQL interface and supports various data sources.
  image: https://spark.apache.org/images/spark-logo-trademark.png
  humanURL: https://spark.apache.org/sql/
  baseURL: https://spark.apache.org/docs/latest/api/sql/
  tags:
  - Dataframes
  - Sql
  - Structured Data
  properties:
  - type: Documentation
    url: https://spark.apache.org/docs/latest/sql-programming-guide.html
  - type: API Reference (Scala)
    url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/sql/index.html
  - type: API Reference (Python)
    url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/index.html
  - type: API Reference (Java)
    url: https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/sql/package-summary.html
  - type: API Reference (R)
    url: https://spark.apache.org/docs/latest/api/R/reference/index.html
- name: Spark Streaming API
  description: Scalable, high-throughput, fault-tolerant stream processing of live data streams.
  image: https://spark.apache.org/images/spark-logo-trademark.png
  humanURL: https://spark.apache.org/streaming/
  baseURL: https://spark.apache.org/docs/latest/api/streaming/
  tags:
  - Data Processing
  - Real-Time
  - Streaming
  properties:
  - type: Documentation
    url: https://spark.apache.org/docs/latest/streaming-programming-guide.html
  - type: API Reference (Scala)
    url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/streaming/index.html
  - type: API Reference (Python)
    url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.streaming/index.html
- name: MLlib (Machine Learning Library)
  description: Spark's scalable machine learning library consisting of common learning algorithms and utilities, including classification, regression, clustering, and collaborative filtering.
  image: https://spark.apache.org/images/spark-logo-trademark.png
  humanURL: https://spark.apache.org/mllib/
  baseURL: https://spark.apache.org/docs/latest/api/mllib/
  tags:
  - Algorithms
  - Data Science
  - Machine Learning
  - Ml
  properties:
  - type: Documentation
    url: https://spark.apache.org/docs/latest/ml-guide.html
  - type: API Reference (Scala)
    url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/ml/index.html
  - type: API Reference (Python)
    url: https://spark.apache.org/docs/latest/api/python/reference/pyspark.ml.html
  - type: API Reference (Java)
    url: https://spark.apache.org/docs/latest/api/java/index.html?org/apache/spark/ml/package-summary.html
- name: GraphX API
  description: Spark API for graphs and graph-parallel computation with a collection of graph algorithms and builders.
  image: https://spark.apache.org/images/spark-logo-trademark.png
  humanURL: https://spark.apache.org/graphx/
  baseURL: https://spark.apache.org/docs/latest/api/graphx/
  tags:
  - Analytics
  - Graph Processing
  - Graphs
  properties:
  - type: Documentation
    url: https://spark.apache.org/docs/latest/graphx-programming-guide.html
  - type: API Reference (Scala)
    url: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/graphx/index.html
name: Apache Spark
tags:
- Analytics
- Apache
- Big Data
- Distributed Computing
- Machine Learning
- Streaming
type: Contract
image: https://spark.apache.org/images/spark-logo-trademark.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Spark is a unified analytics engine for large-scale data processing. It provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

