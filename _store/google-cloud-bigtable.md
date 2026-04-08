---
aid: google-cloud-bigtable
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/apis.yml
apis:
- name: Cloud Bigtable Admin API
  description: The Cloud Bigtable Admin API provides programmatic access to manage Cloud Bigtable instances, clusters, tables, and related resources. It enables creating and configuring Bigtable infrastructure, managing column families, handling backups, and setting access control policies for high-throughput NoSQL workloads.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/bigtable/docs
  baseURL: https://bigtableadmin.googleapis.com/v2
  tags:
  - Clusters
  - Instances
  - NoSQL
  - Tables
  properties:
  - type: Documentation
    url: https://cloud.google.com/bigtable/docs/reference/admin/rest
  - type: OpenAPI
    url: openapi/cloud-bigtable-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/bigtable/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/bigtable/docs/quickstarts
  - type: JSONSchema
    url: json-schema/instance-schema.json
name: Google Cloud Bigtable
tags:
- Bigtable
- Database
- Google Cloud
- NoSQL
- Wide Column
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Bigtable is a fully managed, scalable NoSQL database service designed for large analytical and operational workloads. It offers consistent sub-10ms latency and seamless scalability, making it ideal for time-series data, IoT, ad tech, fintech, and machine learning applications. Bigtable integrates with popular big data tools like Hadoop, Dataflow, and Dataproc.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

