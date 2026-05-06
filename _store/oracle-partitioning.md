---
aid: oracle-partitioning
name: Oracle Partitioning
description: Oracle Partitioning enables tables and indexes to be partitioned into smaller, more manageable pieces, improving performance, availability, and manageability of large database objects.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle-partitioning/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-03-16'
specificationVersion: '0.19'
apis:
  - name: Oracle Database REST API - Partitioning
    description: REST API endpoints for managing and monitoring Oracle Database partitioning operations.
    image: https://www.oracle.com/a/ocom/img/cb71-oracle-database.jpg
    baseURL: https://your-oracle-instance.com:8443/ords
    humanURL: https://docs.oracle.com/en/database/oracle/oracle-database/
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html
      - type: OpenAPI
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/
      - type: Swagger
        url: https://your-oracle-instance.com:8443/ords/swagger-ui.html
    contact:
      - FN: Oracle Support
        email: support@oracle.com
        url: https://support.oracle.com
  - name: Oracle SQL Developer REST Services - Partitioning
    description: REST services for partition management through SQL Developer.
    image: https://www.oracle.com/a/ocom/img/sql-dev.jpg
    baseURL: https://your-oracle-instance.com/ords
    humanURL: https://www.oracle.com/database/sqldeveloper/
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/sql-developer/
      - type: Tutorial
        url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-admin.html
  - name: Oracle Cloud Infrastructure Database API - Partitioning
    description: OCI API for managing partitioned databases in Oracle Cloud.
    image: https://www.oracle.com/a/ocom/img/oci-logo.png
    baseURL: https://database.{region}.oraclecloud.com
    humanURL: https://www.oracle.com/cloud/
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/api/#/en/database/
      - type: OpenAPI
        url: https://docs.oracle.com/en-us/iaas/api/swagger/database.json
      - type: SDKs
        url: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/sdks.htm
    contact:
      - FN: Oracle Cloud Support
        email: cloud-support@oracle.com
        url: https://www.oracle.com/support/
common:
  - type: Getting Started
    url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-intro.html
  - type: Best Practices
    url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-strategies.html
  - type: White Papers
    url: https://www.oracle.com/technetwork/database/options/partitioning/
  - type: Pricing
    url: https://www.oracle.com/database/technologies/partitioning/pricing.html
  - type: Support
    url: https://support.oracle.com
  - type: Authentication
    url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/19.2/orrst/authentication.html
  - type: Status
    url: https://status.oracle.com
  - type: Terms of Service
    url: https://www.oracle.com/legal/terms.html
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Composite-Partitioning
  - Database
  - Hash-Partitioning
  - Interval-Partitioning
  - List-Partitioning
  - Oracle
  - Partitioning
  - Performance
  - Range-Partitioning
  - Scalability
  - VLDB
---
