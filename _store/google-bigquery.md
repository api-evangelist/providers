---
aid: google-bigquery
url: https://raw.githubusercontent.com/api-evangelist/google-bigquery/refs/heads/main/apis.yml
apis:
- aid: google-bigquery:bigquery
  name: BigQuery API
  description: The BigQuery API provides programmatic access to Google BigQuery for creating, managing, and querying datasets, tables, jobs, and other BigQuery resources. Developers can use the API to load data, run queries, export results, and manage access control on BigQuery resources. The API supports SQL-based analytics over petabytes of data with serverless infrastructure.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/bigquery/docs
  baseURL: https://bigquery.googleapis.com
  tags:
  - Analytics
  - Data Warehouse
  - Datasets
  - Queries
  - SQL
  properties:
  - type: Documentation
    url: https://cloud.google.com/bigquery/docs/reference/rest
  - type: OpenAPI
    url: openapi/bigquery-api-openapi.yml
  - type: JSONSchema
    url: json-schema/google-bigquery-query-schema.json
  - type: JSONSchema
    url: json-schema/google-bigquery-table-schema.json
- aid: google-bigquery:bigquery-connection
  name: BigQuery Connection API
  description: The BigQuery Connection API enables developers to create and manage connections between BigQuery and external data sources such as Cloud SQL, Cloud Spanner, and other databases. These connections allow BigQuery to query data in external sources without moving or copying data. The API supports creating, updating, deleting, and listing connections as well as managing IAM policies on connections.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest
  baseURL: https://bigqueryconnection.googleapis.com
  tags:
  - Connections
  - External Data
  - Federation
  properties:
  - type: Documentation
    url: https://cloud.google.com/bigquery/docs/reference/bigqueryconnection/rest
- aid: google-bigquery:bigquery-migration
  name: BigQuery Migration API
  description: The BigQuery Migration API provides tools for migrating data warehouse workloads to BigQuery from other platforms. It supports assessment and planning of migration tasks, translation of SQL dialects, and orchestration of migration workflows. The API helps enterprises move their analytics workloads to BigQuery with automated tooling and migration tracking.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/bigquery/docs/reference/migration/rest
  baseURL: https://bigquerymigration.googleapis.com
  tags:
  - Data Migration
  - Migration
  - SQL Translation
  properties:
  - type: Documentation
    url: https://cloud.google.com/bigquery/docs/reference/migration/rest
- aid: google-bigquery:bigquery-reservation
  name: BigQuery Reservation API
  description: The BigQuery Reservation API allows developers to manage slot reservations and capacity commitments for BigQuery compute resources. It provides programmatic control over how compute capacity is allocated across projects and organizations, enabling cost optimization and workload management. The API supports creating reservations, managing assignments, and purchasing capacity commitments.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/bigquery/docs/reference/reservations/rest
  baseURL: https://bigqueryreservation.googleapis.com
  tags:
  - Capacity
  - Compute
  - Reservations
  properties:
  - type: Documentation
    url: https://cloud.google.com/bigquery/docs/reference/reservations/rest
- aid: google-bigquery:bigquery-storage
  name: BigQuery Storage API
  description: The BigQuery Storage API provides high-throughput read and write access to BigQuery managed storage. It enables developers to read data from BigQuery tables using an efficient streaming protocol that is significantly faster than the traditional tabledata.list method. The API supports parallel reads, column filtering, and row filtering to optimize data transfer performance.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/bigquery/docs/reference/storage
  baseURL: https://bigquerystorage.googleapis.com
  tags:
  - High Throughput
  - Storage
  - Streaming
  properties:
  - type: Documentation
    url: https://cloud.google.com/bigquery/docs/reference/storage
name: Google BigQuery
tags:
- Analytics
- Big Data
- Cloud
- Data Warehouse
- Serverless
- SQL
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google BigQuery is a fully managed, serverless data warehouse that enables scalable analysis over petabytes of data using SQL.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

