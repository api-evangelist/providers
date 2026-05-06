---
aid: parquet
name: Apache Parquet
description: APIs and tools for working with Apache Parquet, the open source columnar storage format for efficient analytics workloads. This index covers the format specification along with the major language implementations.
type: Index
position: Producer
access: Open Source
image: https://parquet.apache.org/assets/img/parquet-logo.png
tags:
  - Apache
  - Big Data
  - Columnar Storage
  - Data Format
  - Parquet
created: '2024-01-01'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/parquet/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: parquet:format-specification
    name: Apache Parquet Format Specification
    description: The core specification for the Parquet columnar storage format.
    image: https://parquet.apache.org/assets/img/parquet-logo.png
    humanURL: https://parquet.apache.org/docs/
    baseURL: https://github.com/apache/parquet-format
    tags:
      - Format
      - Schema
      - Specification
    properties:
      - type: Documentation
        url: https://parquet.apache.org/docs/file-format/
      - type: GitHub Repository
        url: https://github.com/apache/parquet-format
      - type: Thrift Definition
        url: https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift
  - aid: parquet:pyarrow
    name: PyArrow Parquet Python API
    description: Python library for reading and writing Parquet files, distributed as part of Apache Arrow.
    humanURL: https://arrow.apache.org/docs/python/parquet.html
    baseURL: https://pypi.org/project/pyarrow/
    tags:
      - Library
      - Python
      - Read
      - Write
    properties:
      - type: Documentation
        url: https://arrow.apache.org/docs/python/parquet.html
      - type: PyPI Package
        url: https://pypi.org/project/pyarrow/
      - type: GitHub Repository
        url: https://github.com/apache/arrow
      - type: API Reference
        url: https://arrow.apache.org/docs/python/api/formats.html
  - aid: parquet:java
    name: Parquet Java API
    description: Java implementation for reading and writing Parquet files.
    humanURL: https://github.com/apache/parquet-java
    baseURL: https://search.maven.org/search?q=g:org.apache.parquet
    tags:
      - Hadoop
      - Java
      - Library
    properties:
      - type: Documentation
        url: https://github.com/apache/parquet-java/blob/master/README.md
      - type: GitHub Repository
        url: https://github.com/apache/parquet-java
      - type: Maven Repository
        url: https://search.maven.org/search?q=g:org.apache.parquet
      - type: JavaDoc
        url: https://www.javadoc.io/doc/org.apache.parquet/parquet-hadoop
  - aid: parquet:cpp
    name: Parquet C++ API
    description: C++ implementation as part of Apache Arrow.
    humanURL: https://arrow.apache.org/docs/cpp/parquet.html
    baseURL: https://github.com/apache/arrow/tree/main/cpp
    tags:
      - Cpp
      - Library
      - Performance
    properties:
      - type: Documentation
        url: https://arrow.apache.org/docs/cpp/parquet.html
      - type: GitHub Repository
        url: https://github.com/apache/arrow
      - type: API Reference
        url: https://arrow.apache.org/docs/cpp/api/parquet.html
  - aid: parquet:r
    name: Parquet R API
    description: R package for reading and writing Parquet files via Apache Arrow.
    humanURL: https://arrow.apache.org/docs/r/
    baseURL: https://cran.r-project.org/package=arrow
    tags:
      - Data Analysis
      - Library
      - R
    properties:
      - type: Documentation
        url: https://arrow.apache.org/docs/r/articles/parquet.html
      - type: CRAN Package
        url: https://cran.r-project.org/package=arrow
      - type: GitHub Repository
        url: https://github.com/apache/arrow/tree/main/r
  - aid: parquet:fastparquet
    name: FastParquet Python API
    description: Alternative Python implementation for Parquet files.
    humanURL: https://fastparquet.readthedocs.io/
    baseURL: https://pypi.org/project/fastparquet/
    tags:
      - Alternative
      - Library
      - Python
    properties:
      - type: Documentation
        url: https://fastparquet.readthedocs.io/en/latest/
      - type: PyPI Package
        url: https://pypi.org/project/fastparquet/
      - type: GitHub Repository
        url: https://github.com/dask/fastparquet
maintainers:
  - FN: Apache Software Foundation
    email: dev@parquet.apache.org
    url: https://parquet.apache.org
common:
  - type: Mailing Lists
    url: https://parquet.apache.org/community/
  - type: Issue Tracker
    url: https://issues.apache.org/jira/projects/PARQUET
  - type: Blog
    url: https://parquet.apache.org/blog/
  - type: License
    url: https://github.com/apache/parquet-format/blob/master/LICENSE
---
