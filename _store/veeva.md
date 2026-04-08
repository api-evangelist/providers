---
aid: veeva
url: https://raw.githubusercontent.com/api-evangelist/veeva/refs/heads/main/apis.yml
apis:
- aid: veeva:veeva-vault-api
  name: Veeva Vault Platform API
  tags:
  - Clinical
  - Life Sciences
  - Pharma
  - QMS
  - Regulatory
  image: https://raw.githubusercontent.com/api-evangelist/veeva/refs/heads/main/image.png
  humanURL: https://developer.veevavault.com/
  baseURL: https://myvault.veevavault.com/api/v25.3
  properties:
  - url: https://developer.veevavault.com/
    type: Portal
  - url: https://developer.veevavault.com/docs
    type: Documentation
  - url: https://developer.veevavault.com/api/25.3/
    type: Reference
  - url: https://developer.veevavault.com/api/25.3/
    type: Authentication
  - url: https://developer.veevavault.com/rn/25.3/
    type: ChangeLog
  - url: https://developer.veevavault.com/docs
    type: GettingStarted
  - url: openapi/veeva-vault-openapi.yml
    type: OpenAPI
  description: Veeva Vault provides life sciences cloud platform APIs for regulatory document management, quality management (QMS), clinical operations, and commercial content management. REST APIs enable document lifecycle management, workflow automation, and compliance-validated data exchange.
- aid: veeva:veeva-vault-java-sdk
  name: Veeva Vault Java SDK
  tags:
  - Java
  - Life Sciences
  - Pharma
  - SDK
  image: https://raw.githubusercontent.com/api-evangelist/veeva/refs/heads/main/image.png
  humanURL: https://developer.veevavault.com/sdk/
  baseURL: https://myvault.veevavault.com/api
  properties:
  - url: https://developer.veevavault.com/sdk/
    type: Documentation
  - url: https://github.com/veeva/vault-api-library
    type: SDKs
  description: The Veeva Vault Java SDK (VAPIL) is an open-source Java-based REST API client for the Vault REST API. Provides type-safe access to all Vault API operations including document management, object CRUD, workflow execution, and administrative functions.
- aid: veeva:veeva-vault-query-language
  name: Veeva Vault Query Language (VQL) API
  tags:
  - Life Sciences
  - Pharma
  - Query Language
  - SQL
  image: https://raw.githubusercontent.com/api-evangelist/veeva/refs/heads/main/image.png
  humanURL: https://developer.veevavault.com/vql/
  baseURL: https://myvault.veevavault.com/api
  properties:
  - url: https://developer.veevavault.com/vql/
    type: Documentation
  - url: openapi/veeva-vault-openapi.yml
    type: OpenAPI
  description: Vault Query Language (VQL) provides SQL-like query capabilities for accessing and retrieving Vault data. Supports SELECT, FROM, WHERE, ORDER BY, relationship queries, and functions for querying documents, objects, users, workflows, and system data.
- aid: veeva:veeva-vault-direct-data-api
  name: Veeva Vault Direct Data API
  tags:
  - Bulk Data
  - Data Access
  - Life Sciences
  - Pharma
  image: https://raw.githubusercontent.com/api-evangelist/veeva/refs/heads/main/image.png
  humanURL: https://developer.veevavault.com/docs
  baseURL: https://myvault.veevavault.com/api
  properties:
  - url: https://developer.veevavault.com/docs
    type: Documentation
  description: The Veeva Vault Direct Data API provides high-speed, read-only bulk access to Vault data for integration, analytics, and reporting purposes. Supports bulk export of documents, objects, and attachment field files for up to 500 records.
name: Veeva
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Veeva Systems is a leader in cloud-based software for the global life sciences industry, providing solutions to help pharmaceutical and biotechnology companies bring products to market more efficiently.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

