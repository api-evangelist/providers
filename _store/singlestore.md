---
aid: singlestore
name: SingleStore
description: SingleStore is a cloud-native distributed SQL database designed for real-time analytics and mixed workloads. It offers a management API for provisioning and managing cloud workspaces, and a data API for executing SQL statements over HTTP without requiring native database drivers. SingleStore Helios is the fully managed cloud service providing serverless database capabilities with elastic scaling.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Database
  - SQL
  - Analytics
  - Cloud
  - Distributed SQL
created: '2025-01-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/singlestore/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: singlestore:data-api
    name: SingleStore Data API
    description: The SingleStore Data API enables developers to execute SQL statements against a SingleStore Helios database over standard HTTP connections without requiring a native database driver or MySQL-compatible client. It supports all SQL statements via /api/v2/exec, and returns query result sets via /api/v2/query/rows and /api/v2/query/tuples. Authentication is handled using HTTP Basic or Bearer Authentication over HTTPS.
    humanURL: https://docs.singlestore.com/cloud/reference/data-api/
    baseURL: https://{workspaceHost}
    tags:
      - SQL
      - Database
      - Query
      - HTTP SQL
    properties:
      - type: Documentation
        url: https://docs.singlestore.com/cloud/reference/data-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/singlestore/refs/heads/main/openapi/singlestore-data-api-openapi.yml
  - aid: singlestore:management-api
    name: SingleStore Management API
    description: The SingleStore Management API is a REST interface for programmatically creating and managing workspace groups and workspaces within SingleStore Helios. It supports provisioning, updating, suspending, resuming, and deleting workspaces, as well as managing private connections, regions, organizations, jobs, files, secrets, and teams.
    humanURL: https://docs.singlestore.com/cloud/reference/management-api/
    baseURL: https://api.singlestore.com/v1
    tags:
      - Management
      - Workspaces
      - Provisioning
      - Database
    properties:
      - type: Documentation
        url: https://docs.singlestore.com/cloud/reference/management-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/singlestore/refs/heads/main/openapi/singlestore-management-api-openapi.yml
common:
  - type: Website
    url: https://www.singlestore.com/
  - type: DeveloperPortal
    url: https://docs.singlestore.com/
  - type: Documentation
    url: https://docs.singlestore.com/cloud/
  - type: Pricing
    url: https://www.singlestore.com/pricing/
  - type: Blog
    url: https://www.singlestore.com/blog/
  - type: GitHubOrg
    url: https://github.com/singlestore-labs
  - type: SignUp
    url: https://www.singlestore.com/cloud-trial/
  - type: TermsOfService
    url: https://www.singlestore.com/cloud-terms-and-conditions/
  - type: PrivacyPolicy
    url: https://www.singlestore.com/privacy-policy/
  - type: Support
    url: https://support.singlestore.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
