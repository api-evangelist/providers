---
aid: table-format
name: Table Format
description: Open Table Format is a category of open standards for organizing and managing data in data lakehouses. The three dominant formats are Apache Iceberg (the emerging industry standard with snapshot-based metadata and broad engine support), Delta Lake (Databricks-originated, transaction-log-based), and Apache Hudi (upsert-optimized with Copy-on-Write and Merge-on-Read modes). These formats bring ACID transactions, schema evolution, time travel, and efficient query planning to data lake storage. Apache Iceberg defines a REST Catalog API (OpenAPI spec) that enables standardized catalog operations across implementations like Polaris, Nessie, AWS Glue, and Google BigLake.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Lakehouse
  - Open Table Format
  - Apache Iceberg
  - Delta Lake
  - Apache Hudi
  - Data Lake
  - ACID Transactions
  - Schema Evolution
  - Time Travel
url: https://raw.githubusercontent.com/api-evangelist/table-format/refs/heads/main/apis.yml
created: '2025'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: table-format:apache-iceberg-rest-catalog
    name: Apache Iceberg REST Catalog API
    description: The Apache Iceberg REST Catalog API is an open OpenAPI specification that defines a standard interface for interacting with Apache Iceberg table catalogs. It enables catalog operations including namespace management, table creation, schema updates, and metadata retrieval across any compliant catalog implementation (Polaris, Nessie, AWS Glue, Google BigLake).
    humanURL: https://iceberg.apache.org/rest-catalog-spec/
    baseURL: https://catalog-service/
    tags:
      - Apache Iceberg
      - Data Catalog
      - REST Catalog
      - Data Lakehouse
    properties:
      - type: Documentation
        url: https://iceberg.apache.org/rest-catalog-spec/
      - type: OpenAPI
        url: https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml
      - type: GitHub
        url: https://github.com/apache/iceberg
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/table-format/refs/heads/main/openapi/apache-iceberg-rest-catalog-openapi.yml
  - aid: table-format:delta-lake
    name: Delta Lake
    description: Delta Lake is an open-source storage framework developed by Databricks that adds reliability, performance, and ACID compliance to data lakes. It uses a transaction log (delta log) to record all changes to data. Delta Lake is deeply integrated with Apache Spark and supports batch and streaming workloads, schema enforcement, time travel, and MERGE operations.
    humanURL: https://delta.io/
    tags:
      - Delta Lake
      - Data Lake
      - ACID Transactions
      - Apache Spark
      - Databricks
    properties:
      - type: Documentation
        url: https://docs.delta.io/
      - type: GitHub
        url: https://github.com/delta-io/delta
  - aid: table-format:apache-hudi
    name: Apache Hudi
    description: Apache Hudi (Hadoop Upserts Deletes and Incrementals) is an open-source data lakehouse platform optimized for upserts, deletes, and incremental data processing. It supports Copy-on-Write (COW) and Merge-on-Read (MOR) table types and is used for CDC-based data pipelines and streaming analytics.
    humanURL: https://hudi.apache.org/
    tags:
      - Apache Hudi
      - Data Lake
      - CDC
      - Incremental Processing
    properties:
      - type: Documentation
        url: https://hudi.apache.org/docs/overview/
      - type: GitHub
        url: https://github.com/apache/hudi
  - aid: table-format:unity-catalog
    name: Unity Catalog
    description: Unity Catalog is an open-source, multi-modal catalog for data and AI that supports Apache Iceberg REST Catalog API, Apache Hive Metastore (HMS) API, and Delta Sharing. It provides unified governance across Delta Lake, Iceberg, and Hudi tables with an OpenAPI specification under Apache 2.0 license.
    humanURL: https://www.unitycatalog.io/
    tags:
      - Data Catalog
      - Unity Catalog
      - Data Governance
      - Multi-format
    properties:
      - type: Documentation
        url: https://www.unitycatalog.io/
      - type: OpenAPI
        url: https://github.com/unitycatalog/unitycatalog/blob/main/api/all.yaml
      - type: GitHub
        url: https://github.com/unitycatalog/unitycatalog
common:
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/Apache_Iceberg
  - type: Apache Iceberg
    url: https://iceberg.apache.org/
  - type: Delta Lake
    url: https://delta.io/
  - type: Apache Hudi
    url: https://hudi.apache.org/
  - type: Unity Catalog
    url: https://www.unitycatalog.io/
  - type: Apache Iceberg GitHub
    url: https://github.com/apache/iceberg
  - type: Delta Lake GitHub
    url: https://github.com/delta-io/delta
  - type: Apache Hudi GitHub
    url: https://github.com/apache/hudi
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/table-format/refs/heads/main/vocabulary/table-format-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
