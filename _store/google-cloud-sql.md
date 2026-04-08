---
aid: google-cloud-sql
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-sql/refs/heads/main/apis.yml
apis:
- name: Cloud SQL Admin API
  description: The Cloud SQL Admin API provides programmatic management of Cloud SQL instances, databases, users, backup runs, SSL certificates, and flags. It enables automated provisioning and configuration of managed MySQL, PostgreSQL, and SQL Server instances, including high-availability setup, storage management, network configuration, and user access control.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/sql/docs
  baseURL: https://sqladmin.googleapis.com/v1
  tags:
  - Backups
  - Database
  - Instances
  - SQL
  properties:
  - type: Documentation
    url: https://cloud.google.com/sql/docs/mysql/admin-api/rest
  - type: OpenAPI
    url: openapi/cloud-sql-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/sql/docs/mysql/authentication
  - type: Getting Started
    url: https://cloud.google.com/sql/docs/mysql/quickstart
  - type: JSONSchema
    url: json-schema/instance-schema.json
name: Google Cloud SQL
tags:
- Database
- Google Cloud
- MySQL
- PostgreSQL
- Relational
- SQL
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud SQL is a fully managed relational database service that supports MySQL, PostgreSQL, and SQL Server. It handles routine database tasks such as provisioning, replication, backups, and failover, allowing developers to focus on application development. Cloud SQL provides high availability, automatic storage scaling, and integrated security features.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

