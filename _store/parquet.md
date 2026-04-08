---
aid: parquet
url: https://raw.githubusercontent.com/api-evangelist/parquet/refs/heads/main/apis.yml
apis:
- name: Apache Parquet Format Specification
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
- name: PyArrow Parquet Python API
  description: Python library for reading and writing Parquet files.
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
- name: Parquet Java API
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
- name: Parquet C++ API
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
- name: Parquet R API
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
- name: FastParquet Python API
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
name: Apache Parquet
tags:
- Apache
- Big Data
- Columnar Storage
- Data Format
- Parquet
type: Contract
image: https://parquet.apache.org/assets/img/parquet-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and tools for working with Apache Parquet columnar storage format.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

