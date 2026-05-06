---
aid: apache-pig
name: Apache Pig
description: Apache Pig is a platform for analyzing large data sets that provides a high-level language (Pig Latin) for expressing data analysis programs. It compiles Pig Latin programs into MapReduce/Tez jobs and runs them on Hadoop clusters.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Big Data
  - Data Analysis
  - ETL
  - Hadoop
  - Scripting
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-pig/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-pig:apache-pig
    name: Apache Pig
    description: Pig provides the Pig Latin scripting language for data analysis, an embedded Pig API for programmatic execution from Java, and a UDF (User Defined Function) API for custom data transformation functions.
    humanURL: https://pig.apache.org/docs/latest/
    tags:
      - Data Analysis
      - Java
      - Pig Latin
      - UDF
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://pig.apache.org/docs/latest/
      - type: OpenAPI
        url: openapi/apache-pig-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/pig
  - type: Documentation
    url: https://pig.apache.org/
  - type: SpectralRules
    url: rules/apache-pig-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-pig-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/pig-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-pig-context.jsonld
  - type: Features
    data:
      - name: Pig Latin Language
        description: High-level dataflow language for expressing data transformations
      - name: MapReduce/Tez Backend
        description: Compiles Pig Latin to MapReduce or Apache Tez execution plans
      - name: UDF Support
        description: User-defined functions in Java, Python, JavaScript, and Ruby
      - name: Streaming
        description: Process data through external programs using STREAM operator
      - name: Schema Evolution
        description: Flexible schema handling for semi-structured data
      - name: Optimization
        description: Automatic logical and physical plan optimization
  - type: UseCases
    data:
      - name: ETL Pipelines
        description: Build data transformation pipelines from raw logs to structured data
      - name: Ad-hoc Data Analysis
        description: Analyze large datasets with ad-hoc Pig Latin queries
      - name: Data Preparation
        description: Clean and prepare data for machine learning workflows
      - name: Log Processing
        description: Process and aggregate web server and application logs
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Native MapReduce execution on YARN/HDFS
      - name: Apache Tez
        description: High-performance Tez execution engine support
      - name: Apache HBase
        description: HBase storage handler for reading/writing HBase tables
      - name: Apache Hive
        description: HCatalog integration for Hive metastore access
      - name: Amazon S3
        description: S3 input/output for cloud-based data processing
---
