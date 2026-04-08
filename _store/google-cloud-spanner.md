---
aid: google-cloud-spanner
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-spanner/refs/heads/main/apis.yml
apis:
- name: Cloud Spanner API
  description: The Cloud Spanner API provides programmatic access to manage Cloud Spanner instances, databases, and sessions. It supports creating and configuring globally distributed database infrastructure, executing SQL queries and DML statements, managing transactions with strong consistency guarantees, and handling database backups and restore operations.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/spanner/docs
  baseURL: https://spanner.googleapis.com/v1
  tags:
  - Database
  - Instances
  - SQL
  - Transactions
  properties:
  - type: Documentation
    url: https://cloud.google.com/spanner/docs/reference/rest
  - type: OpenAPI
    url: openapi/cloud-spanner-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/spanner/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/spanner/docs/getting-started/rest
  - type: JSONSchema
    url: json-schema/instance-schema.json
name: Google Cloud Spanner
tags:
- Database
- Distributed
- Google Cloud
- Relational
- SQL
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Spanner is a fully managed, mission-critical relational database service that offers transactional consistency at global scale, automatic synchronous replication, and schemas with SQL support. It combines the benefits of relational database structure with non-relational horizontal scale, providing up to 99.999% availability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

