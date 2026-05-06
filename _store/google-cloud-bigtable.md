---
aid: google-cloud-bigtable
name: Google Cloud Bigtable
description: Google Cloud Bigtable is a fully managed, scalable NoSQL database service designed for large analytical and operational workloads. It offers consistent sub-10ms latency and seamless scalability, making it ideal for time-series data, IoT, ad tech, fintech, and machine learning applications. Bigtable integrates with popular big data tools like Hadoop, Dataflow, and Dataproc.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-bigtable/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Bigtable
  - Database
  - Google Cloud
  - NoSQL
  - Wide Column
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
common:
  - type: Portal
    url: https://cloud.google.com/bigtable
  - type: Getting Started
    url: https://cloud.google.com/bigtable/docs/quickstarts
  - type: Documentation
    url: https://cloud.google.com/bigtable/docs
  - type: Authentication
    url: https://cloud.google.com/bigtable/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/bigtable/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/bigtable/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-bigtable-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
