---
aid: apache-orc
name: Apache ORC
description: Apache ORC is a self-describing, type-aware columnar file format designed for Hadoop workloads. It provides high compression ratios and fast read performance for large-scale data processing with support for complex data types.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Big Data
  - Columnar Storage
  - Compression
  - File Format
  - Hadoop
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-orc/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-orc:apache-orc
    name: Apache ORC
    description: ORC provides Java and C++ APIs for reading and writing ORC columnar files, with support for predicate pushdown, column projection, compression codecs, and integration with Hive, Spark, Presto, and other query engines.
    humanURL: https://orc.apache.org/docs/
    tags:
      - C++
      - Columnar Format
      - Java
      - Apache
      - Open Source
      - Big Data
    properties:
      - type: Documentation
        url: https://orc.apache.org/docs/
      - type: OpenAPI
        url: openapi/apache-orc-tools-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/orc
  - type: Documentation
    url: https://orc.apache.org/
  - type: SpectralRules
    url: rules/apache-orc-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-orc-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/orc-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-orc-context.jsonld
  - type: Features
    data:
      - name: Columnar Storage
        description: Stores data by column for efficient compression and query performance
      - name: Predicate Pushdown
        description: Skip reading data that does not match query predicates
      - name: Column Projection
        description: Read only the columns needed for a query
      - name: ACID Support
        description: Full ACID transactional support when used with Apache Hive
      - name: Schema Evolution
        description: Add, rename, and remove columns while preserving backward compatibility
      - name: Compression
        description: Supports ZLIB, Snappy, LZO, LZ4, and ZSTD compression codecs
  - type: UseCases
    data:
      - name: Hive Data Warehousing
        description: Store Hive tables in highly efficient ORC format
      - name: Spark Analytics
        description: Process large ORC datasets with Apache Spark SQL
      - name: Presto/Trino Queries
        description: Fast analytical queries over ORC files with Presto or Trino
      - name: Data Lake Storage
        description: Efficient columnar storage for data lake architectures
  - type: Integrations
    data:
      - name: Apache Hive
        description: Native ORC support as default Hive storage format
      - name: Apache Spark
        description: ORC data source support in Spark SQL
      - name: Presto/Trino
        description: Fast ORC reading with native vectorized reader
      - name: Apache Flink
        description: ORC file format support for batch and streaming
      - name: Apache Arrow
        description: ORC to Arrow conversion for in-memory analytics
---
