---
aid: delta-lake
name: Delta Lake
description: Delta Lake is a graduated project of the Linux Foundation AI & Data Foundation providing an open source storage framework for building Lakehouse architectures. Originally contributed by Databricks, it adds reliability, quality, and performance to data lakes with ACID transactions, schema enforcement, time travel, and Iceberg/Hudi interoperability via UniForm. Delta Lake projects also include Delta Sharing (an open protocol for secure data sharing) and catalog-managed tables built on the Iceberg REST Catalog protocol.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data
  - Data Lake
  - Lakehouse
  - Linux Foundation
  - Open Source
  - Storage
  - Streaming
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/delta-lake/refs/heads/main/apis.yml
specificationVersion: '0.19'
xType: opensource
apis:
  - aid: delta-lake:delta-lake-storage
    name: Delta Lake Storage Framework
    description: The Delta Lake storage framework defines the on-disk transaction log and protocol that adds ACID transactions, schema enforcement, and time travel to Parquet-based data lakes. Delta Lake exposes Spark, Rust, and Python APIs (delta-spark, delta-rs, deltalake) rather than a network API.
    humanURL: https://docs.delta.io/
    tags:
      - Lakehouse
      - Protocol
      - Storage
      - Transaction Log
    properties:
      - type: Documentation
        url: https://docs.delta.io/
      - type: Protocol
        url: https://github.com/delta-io/delta/blob/master/PROTOCOL.md
      - type: SourceCode
        url: https://github.com/delta-io/delta
      - type: Releases
        url: https://github.com/delta-io/delta/releases
  - aid: delta-lake:delta-sharing
    name: Delta Sharing Protocol
    description: Delta Sharing is an open protocol for secure data sharing across organizations, defined as a REST API specification. Sharing servers expose endpoints for listing shares, schemas, and tables, and for retrieving signed URLs to underlying data files.
    humanURL: https://delta.io/sharing/
    tags:
      - Data Sharing
      - Open Protocol
      - REST
    properties:
      - type: Documentation
        url: https://github.com/delta-io/delta-sharing
      - type: Protocol
        url: https://github.com/delta-io/delta-sharing/blob/main/PROTOCOL.md
      - type: SourceCode
        url: https://github.com/delta-io/delta-sharing
  - aid: delta-lake:delta-catalog
    name: Delta Catalog-Managed Tables
    description: Catalog-managed Delta tables delegate table scan planning to an external catalog using the Iceberg REST Catalog protocol, enabling interoperability with Unity Catalog and other catalog services.
    humanURL: https://delta.io/blog/2026-02-02-delta-catalog-managed-tables/
    tags:
      - Catalog
      - Iceberg REST
      - Interoperability
    properties:
      - type: Documentation
        url: https://delta.io/blog/2026-02-02-delta-catalog-managed-tables/
      - type: Protocol
        url: https://github.com/delta-io/delta/blob/master/PROTOCOL.md
common:
  - type: Website
    url: https://delta.io/
  - type: Documentation
    url: https://docs.delta.io/
  - type: GitHubOrg
    url: https://github.com/delta-io
  - type: Blog
    url: https://delta.io/blog/
  - type: LinuxFoundation
    url: https://lfaidata.foundation/projects/delta-lake/
  - type: Slack
    url: https://go.delta.io/slack
  - type: Vocabulary
    url: vocabulary/delta-lake-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
