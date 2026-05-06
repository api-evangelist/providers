---
aid: data-warehouse-schemas
name: Data Warehouse Schemas
description: Data Warehouse Schemas is the landscape of analytical schema patterns used to organize fact and dimension data for business intelligence and reporting. It spans star, snowflake, and galaxy schemas, the Kimball dimensional modeling methodology, the Inmon Corporate Information Factory, Data Vault 2.0, and modern lakehouse table formats like Delta Lake, Apache Iceberg, and Apache Hudi.
type: Topic
xType: topic
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Business Intelligence
  - Data Warehouse Schemas
  - Data Warehousing
  - Database Design
  - Dimensional Modeling
created: '2025-01-01'
modified: '2026-04-30'
url: https://raw.githubusercontent.com/api-evangelist/data-warehouse-schemas/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis: []
common:
  - url: https://en.wikipedia.org/wiki/Data_warehouse#Schemas
    name: Wikipedia
    type: Reference
    description: Wikipedia overview of data warehouse schema patterns.
  - url: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/
    name: Kimball Dimensional Modeling
    type: Reference
    description: Kimball Group's catalog of dimensional modeling techniques.
  - url: https://en.wikipedia.org/wiki/Star_schema
    name: Star Schema
    type: Reference
    description: Star schema pattern with a central fact table joined to denormalized dimensions.
  - url: https://en.wikipedia.org/wiki/Snowflake_schema
    name: Snowflake Schema
    type: Reference
    description: Snowflake schema pattern with normalized dimension hierarchies.
  - url: https://en.wikipedia.org/wiki/Fact_constellation
    name: Galaxy / Fact Constellation
    type: Reference
    description: Multi-fact schema sharing dimensions across fact tables.
  - url: https://datavaultalliance.com/
    name: Data Vault Alliance
    type: Reference
    description: Standards body for the Data Vault 2.0 modeling approach.
  - url: https://www.amazon.com/dp/0470174420
    name: Building the Data Warehouse (Inmon)
    type: Reference
    description: Bill Inmon's foundational text on the Corporate Information Factory.
  - url: https://delta.io/
    name: Delta Lake
    type: Tool
    description: ACID table format for lakehouse architectures.
  - url: https://iceberg.apache.org/
    name: Apache Iceberg
    type: Tool
    description: Open table format for huge analytic datasets.
  - url: https://hudi.apache.org/
    name: Apache Hudi
    type: Tool
    description: Streaming-first lakehouse table format.
  - url: https://docs.getdbt.com/
    name: dbt
    type: Tool
    description: Tool for building dimensional models in cloud warehouses with SQL.
  - url: https://www.snowflake.com/
    name: Snowflake
    type: Platform
    description: Cloud data warehouse platform.
  - url: https://cloud.google.com/bigquery
    name: Google BigQuery
    type: Platform
    description: Serverless cloud data warehouse from Google.
  - url: https://www.databricks.com/
    name: Databricks Lakehouse
    type: Platform
    description: Unified analytics platform combining warehouse and lake.
  - url: vocabulary/data-warehouse-schemas-vocabulary.yml
    name: Vocabulary
    type: Vocabulary
    description: Vocabulary of data warehouse schema concepts.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
