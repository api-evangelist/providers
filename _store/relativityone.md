---
aid: relativityone
name: RelativityOne
description: RelativityOne is a cloud-based eDiscovery and legal technology platform that provides comprehensive REST APIs for legal hold management, document processing, search and analytics, workspace management, identity and access control, and billing insights. The platform integrates with Microsoft 365 and Google Workspace for data preservation and legal hold workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - eDiscovery
  - Legal
  - Legal Hold
  - Document Management
  - Compliance
  - Litigation
url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/apis.yml
created: '2025-03-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: relativityone:legal-hold-api
    name: Legal Hold API
    description: The Legal Hold API enables matter and project management integration with external systems like matter management platforms and HR systems. It provides endpoints for custodian management, preservation workflows, task tracking, entity management, and communication configuration. Authentication is handled via Microsoft Graph API.
    humanURL: https://platform.relativity.com/RelativityOne/Content/Legal_Hold_API/Legal_Hold_API.htm
    baseURL: https://relativity.rest/api
    tags:
      - Legal Hold
      - Custodian Management
      - Preservation
      - eDiscovery
      - Compliance
    properties:
      - type: Documentation
        url: https://platform.relativity.com/RelativityOne/Content/Legal_Hold_API/Legal_Hold_API.htm
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/openapi/relativityone-legal-hold-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/json-schema/relativityone-legal-hold-project-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/json-schema/relativityone-custodian-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/json-structure/relativityone-legal-hold-structure.json
  - aid: relativityone:object-manager-api
    name: Object Manager API
    description: The Object Manager API provides CRUD operations for documents and Relativity Dynamic Objects (RDOs). It supports bulk read, create, update, and delete operations with filtering and search capabilities across workspace objects.
    humanURL: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
    baseURL: https://relativity.rest/api
    tags:
      - Document Management
      - Object Management
      - CRUD Operations
      - Workspace
    properties:
      - type: Documentation
        url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
  - aid: relativityone:workspace-manager-api
    name: Workspace Manager API
    description: The Workspace Manager API provides CRUD operations for Relativity workspaces, including workspace creation, configuration, application installation, and environment management.
    humanURL: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
    baseURL: https://relativity.rest/api
    tags:
      - Workspace Management
      - Administration
      - Configuration
    properties:
      - type: Documentation
        url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
  - aid: relativityone:search-analytics-api
    name: Search and Analytics API
    description: APIs for search and analytics operations in RelativityOne including dtSearch index management, keyword search, Analytics Conceptual Index for LSI and concept discovery, and Pivot queries for data analysis.
    humanURL: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
    baseURL: https://relativity.rest/api
    tags:
      - Search
      - Analytics
      - Full Text Search
      - Concept Search
      - Data Analysis
    properties:
      - type: Documentation
        url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
  - aid: relativityone:user-permission-manager-api
    name: User and Permission Manager API
    description: APIs for identity and access management in RelativityOne. Includes user CRUD operations, permission assignment and management, group administration, and client management.
    humanURL: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
    baseURL: https://relativity.rest/api
    tags:
      - Identity
      - Access Management
      - Permissions
      - User Management
    properties:
      - type: Documentation
        url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
  - aid: relativityone:import-export-api
    name: Import and Export API
    description: Import and Export Services API for handling document and Relativity Dynamic Object (RDO) transfers, including bulk import operations for large data sets.
    humanURL: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
    baseURL: https://relativity.rest/api
    tags:
      - Import
      - Export
      - Data Transfer
      - Bulk Operations
    properties:
      - type: Documentation
        url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
common:
  - type: Website
    url: https://www.relativity.com
  - type: Documentation
    url: https://platform.relativity.com/
  - type: Developer Documentation
    url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
  - type: API Reference
    url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/Relativity_API_reference.htm
  - type: Changelog
    url: https://platform.relativity.com/RelativityOne/Content/What_s_new/What_s_new.htm
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/json-ld/relativityone-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/vocabulary/relativityone-vocabulary.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/rules/relativityone-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/capabilities/legal-hold-management.yaml
  - type: GitHub Organization
    url: https://github.com/relativitydev
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
