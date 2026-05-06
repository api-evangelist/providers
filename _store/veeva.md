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
      - url: json-schema/veeva-vault-auth-response-schema.json
        type: JSONSchema
        title: Auth Response Schema
      - url: json-schema/veeva-vault-document-fields-schema.json
        type: JSONSchema
        title: Document Fields Schema
      - url: json-schema/veeva-vault-document-list-response-schema.json
        type: JSONSchema
        title: Document List Response Schema
      - url: json-schema/veeva-vault-document-create-response-schema.json
        type: JSONSchema
        title: Document Create Response Schema
      - url: json-schema/veeva-vault-document-update-response-schema.json
        type: JSONSchema
        title: Document Update Response Schema
      - url: json-schema/veeva-vault-document-response-schema.json
        type: JSONSchema
        title: Document Response Schema
      - url: json-schema/veeva-vault-object-list-response-schema.json
        type: JSONSchema
        title: Object List Response Schema
      - url: json-schema/veeva-vault-object-create-response-schema.json
        type: JSONSchema
        title: Object Create Response Schema
      - url: json-schema/veeva-vault-object-record-response-schema.json
        type: JSONSchema
        title: Object Record Response Schema
      - url: json-schema/veeva-vault-query-response-schema.json
        type: JSONSchema
        title: Query Response Schema
      - url: json-schema/veeva-vault-user-list-response-schema.json
        type: JSONSchema
        title: User List Response Schema
      - url: json-structure/veeva-vault-auth-response-structure.json
        type: JSONStructure
        title: Auth Response Structure
      - url: json-structure/veeva-vault-document-fields-structure.json
        type: JSONStructure
        title: Document Fields Structure
      - url: json-structure/veeva-vault-document-list-response-structure.json
        type: JSONStructure
        title: Document List Response Structure
      - url: json-structure/veeva-vault-query-response-structure.json
        type: JSONStructure
        title: Query Response Structure
      - url: examples/veeva-vault-auth-response-example.json
        type: Example
        title: Auth Response Example
      - url: examples/veeva-vault-document-fields-example.json
        type: Example
        title: Document Fields Example
      - url: examples/veeva-vault-document-list-response-example.json
        type: Example
        title: Document List Response Example
      - url: examples/veeva-vault-query-response-example.json
        type: Example
        title: Query Response Example
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
      - url: https://mvnrepository.com/artifact/com.veeva/vault-api-library
        type: SDKs
        title: Maven Central
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
common:
  - url: https://www.veeva.com/
    type: Website
  - url: https://developer.veevavault.com/
    type: Portal
  - url: https://developer.veevavault.com/docs
    type: Documentation
  - url: https://developer.veevavault.com/docs
    type: GettingStarted
  - url: https://developer.veevavault.com/api/25.3/
    type: Authentication
  - url: https://developer.veevavault.com/rn/25.3/
    type: ChangeLog
  - url: https://developer.veevavault.com/sdk/
    type: SDKs
  - url: https://support.veeva.com/hc/en-us
    type: Support
  - url: https://www.veeva.com/privacy/
    type: PrivacyPolicy
  - url: https://github.com/veeva
    type: GitHubOrganization
  - url: json-schema/veeva-vault-document-schema.json
    type: JSONSchema
    title: Vault Document Schema
  - url: json-ld/veeva-context.jsonld
    type: JSONLDContext
  - url: rules/veeva-spectral-rules.yml
    type: SpectralRules
    title: Veeva Vault API Spectral Rules
  - url: vocabulary/veeva-vocabulary.yml
    type: Vocabulary
    title: Veeva Vocabulary
  - url: capabilities/vault-document-management.yaml
    type: NaftikoCapability
    title: Vault Document Management
  - type: Features
    data:
      - name: Document Lifecycle Management
        description: Full lifecycle management for controlled documents including draft, review, approval, and archival states with audit trails for regulatory compliance.
      - name: Vault Query Language
        description: SQL-like query engine for retrieving Vault data across documents, objects, users, and workflows with support for relationship traversal.
      - name: Direct Data API
        description: High-speed bulk data export for up to 500 records at a time for analytics, reporting, and integration with downstream systems.
      - name: Vault Object CRUD
        description: Create, read, update, and delete operations on configurable Vault business objects (studies, products, sites, etc.) via REST API.
      - name: Session Authentication
        description: Username/password authentication returning a session ID for subsequent API calls, with multi-vault support for complex enterprise deployments.
      - name: Java SDK (VAPIL)
        description: Open-source Java client library providing type-safe access to all Vault REST API operations with automatic session management and error handling.
  - type: UseCases
    data:
      - name: Regulatory Document Submission
        description: Automate the assembly and submission of regulatory dossiers (CTD, eCTD) by programmatically managing document lifecycle, approvals, and publishing.
      - name: Clinical Trial Data Management
        description: Integrate Vault with CTMS, EDC, and LIMS systems to automate study document workflows, protocol amendments, and site activation packages.
      - name: Quality Management Automation
        description: Automate SOPs, CAPAs, deviations, and audit workflows in QMS Vault through lifecycle actions, object creation, and workflow task assignment.
      - name: Content Analytics
        description: Export Vault document and object data in bulk for BI dashboards, compliance reporting, and cross-Vault analytics using the Direct Data API.
      - name: Enterprise Integration
        description: Integrate Vault with SAP, Salesforce, Veeva CRM, and other enterprise systems using REST APIs for bidirectional data synchronization.
  - type: Integrations
    data:
      - name: Veeva CRM
        description: Bidirectional integration between Vault and Veeva CRM for commercial content lifecycle management and promotional material approval workflows.
      - name: Salesforce
        description: Connect Vault document approval workflows with Salesforce opportunities, accounts, and contacts via REST API integration.
      - name: SAP
        description: Synchronize quality events, deviations, and regulatory submissions between Vault and SAP ERP using REST API and Direct Data API.
      - name: MuleSoft
        description: Pre-built MuleSoft connectors for Vault REST API integration with enterprise middleware platforms and iPaaS solutions.
      - name: Microsoft Azure
        description: Deploy Vault integrations on Azure using Logic Apps, Azure Functions, or Azure Data Factory with Vault REST API support.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-05-03'
description: Veeva Systems is a leader in cloud-based software for the global life sciences industry, providing solutions to help pharmaceutical and biotechnology companies bring products to market more efficiently.
---
