---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Veeva Agentic Access
  operation_count: 15
  slug: veeva-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 8
apis:
- description: 'The Veeva Vault Java SDK (VAPIL) is an open-source Java-based REST API client for the Vault REST API. Provides type-safe access to all Vault API operations including document management, object CRUD, '
  name: Veeva Vault Java SDK
  slug: veeva-vault-java-sdk
- description: 'The Veeva Vault Direct Data API provides high-speed, read-only bulk access to Vault data for integration, analytics, and reporting purposes. Supports bulk export of documents, objects, and attachment '
  name: Veeva Vault Direct Data API
  slug: veeva-vault-direct-data-api
- description: Session management
  name: veeva Authentication API
  slug: veeva-authentication-api
- description: Document lifecycle management
  name: veeva Documents API
  slug: veeva-documents-api
- description: Vault object CRUD operations
  name: veeva Objects API
  slug: veeva-objects-api
- description: VQL query execution
  name: veeva Query API
  slug: veeva-query-api
- description: User management
  name: veeva Users API
  slug: veeva-users-api
- description: Workflow and task management
  name: veeva Workflows API
  slug: veeva-workflows-api
artifact_total: 72
collections:
- collection_type: postman
  name: Veeva Vault REST Authentication API
  slug: postman-veeva-authentication-api
- collection_type: postman
  name: Veeva Vault REST Authentication Documents API
  slug: postman-veeva-documents-api
- collection_type: postman
  name: Veeva Vault REST Authentication Objects API
  slug: postman-veeva-objects-api
- collection_type: postman
  name: Veeva Vault REST Authentication Query API
  slug: postman-veeva-query-api
- collection_type: postman
  name: Veeva Vault REST Authentication Users API
  slug: postman-veeva-users-api
- collection_type: postman
  name: Veeva Vault REST Authentication Workflows API
  slug: postman-veeva-workflows-api
- collection_type: open
  name: Veeva Vault REST API
  slug: open-veeva-vault
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/veeva/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/veeva-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veeva-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/veeva-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/veeva-systems
- group: company
  title: ''
  type: Website
  url: https://www.veeva.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.veevavault.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.veevavault.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.veevavault.com/docs
- group: auth
  title: ''
  type: Authentication
  url: https://developer.veevavault.com/api/25.3/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.veevavault.com/rn/25.3/
- group: build
  title: ''
  type: SDKs
  url: https://developer.veevavault.com/sdk/
- group: operate
  title: ''
  type: Support
  url: https://support.veeva.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.veeva.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veeva
- group: docs
  title: Vault Document Schema
  type: JSONSchema
  url: json-schema/veeva-vault-document-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/veeva-context.jsonld
- group: design
  title: Veeva Vault API Spectral Rules
  type: SpectralRules
  url: rules/veeva-spectral-rules.yml
- group: design
  title: Veeva Vocabulary
  type: Vocabulary
  url: vocabulary/veeva-vocabulary.yml
description: Veeva Systems is a leader in cloud-based software for the global life sciences industry, providing solutions to help pharmaceutical and biotechnology companies bring products to market more efficiently.
examples:
- key_count: 5
  name: Veeva Vault Auth Response Example
  slug: veeva-vault-auth-response-example
- key_count: 5
  name: Veeva Vault Document Create Response Example
  slug: veeva-vault-document-create-response-example
- key_count: 15
  name: Veeva Vault Document Example
  slug: veeva-vault-document-example
- key_count: 15
  name: Veeva Vault Document Fields Example
  slug: veeva-vault-document-fields-example
- key_count: 4
  name: Veeva Vault Document List Response Example
  slug: veeva-vault-document-list-response-example
- key_count: 3
  name: Veeva Vault Document Response Example
  slug: veeva-vault-document-response-example
- key_count: 4
  name: Veeva Vault Document Update Response Example
  slug: veeva-vault-document-update-response-example
- key_count: 2
  name: Veeva Vault Object Create Response Example
  slug: veeva-vault-object-create-response-example
- key_count: 4
  name: Veeva Vault Object List Response Example
  slug: veeva-vault-object-list-response-example
- key_count: 2
  name: Veeva Vault Object Record Response Example
  slug: veeva-vault-object-record-response-example
- key_count: 3
  name: Veeva Vault Query Response Example
  slug: veeva-vault-query-response-example
- key_count: 2
  name: Veeva Vault User List Response Example
  slug: veeva-vault-user-list-response-example
features:
- description: Full lifecycle management for controlled documents including draft, review, approval, and archival states with audit trails for regulatory compliance.
  name: Document Lifecycle Management
- description: SQL-like query engine for retrieving Vault data across documents, objects, users, and workflows with support for relationship traversal.
  name: Vault Query Language
- description: High-speed bulk data export for up to 500 records at a time for analytics, reporting, and integration with downstream systems.
  name: Direct Data API
- description: Create, read, update, and delete operations on configurable Vault business objects (studies, products, sites, etc.) via REST API.
  name: Vault Object CRUD
- description: Username/password authentication returning a session ID for subsequent API calls, with multi-vault support for complex enterprise deployments.
  name: Session Authentication
- description: Open-source Java client library providing type-safe access to all Vault REST API operations with automatic session management and error handling.
  name: Java SDK (VAPIL)
finops:
- name: Veeva Finops
  service_category: Life Sciences SaaS
  slug: veeva-finops
graphqls:
- description: Veeva Systems provides cloud solutions for the life sciences industry. The Vault API covers document management, quality management, clinical data, regulatory submissions, medical content, and CRM dat
  name: Veeva Systems GraphQL API
  slug: veeva-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veeva.png
json_schemas:
- name: AuthResponse
  property_count: 5
  slug: veeva-vault-auth-response
- name: DocumentCreateResponse
  property_count: 5
  slug: veeva-vault-document-create-response
- name: DocumentFields
  property_count: 17
  slug: veeva-vault-document-fields
- name: DocumentListResponse
  property_count: 4
  slug: veeva-vault-document-list-response
- name: DocumentResponse
  property_count: 3
  slug: veeva-vault-document-response
- name: Veeva Vault Document
  property_count: 22
  slug: veeva-vault-document
- name: DocumentUpdateResponse
  property_count: 4
  slug: veeva-vault-document-update-response
- name: ObjectCreateResponse
  property_count: 2
  slug: veeva-vault-object-create-response
- name: ObjectListResponse
  property_count: 4
  slug: veeva-vault-object-list-response
- name: ObjectRecordResponse
  property_count: 2
  slug: veeva-vault-object-record-response
- name: QueryResponse
  property_count: 3
  slug: veeva-vault-query-response
- name: UserListResponse
  property_count: 2
  slug: veeva-vault-user-list-response
json_structures:
- name: Veeva Vault Auth Response Structure
  property_count: 5
  slug: veeva-vault-auth-response-structure
- name: Veeva Vault Document Create Response Structure
  property_count: 5
  slug: veeva-vault-document-create-response-structure
- name: Veeva Vault Document Fields Structure
  property_count: 17
  slug: veeva-vault-document-fields-structure
- name: Veeva Vault Document List Response Structure
  property_count: 4
  slug: veeva-vault-document-list-response-structure
- name: Veeva Vault Document Response Structure
  property_count: 3
  slug: veeva-vault-document-response-structure
- name: Veeva Vault Document Structure
  property_count: 22
  slug: veeva-vault-document-structure
- name: Veeva Vault Document Update Response Structure
  property_count: 4
  slug: veeva-vault-document-update-response-structure
- name: Veeva Vault Object Create Response Structure
  property_count: 2
  slug: veeva-vault-object-create-response-structure
- name: Veeva Vault Object List Response Structure
  property_count: 4
  slug: veeva-vault-object-list-response-structure
- name: Veeva Vault Object Record Response Structure
  property_count: 2
  slug: veeva-vault-object-record-response-structure
- name: Veeva Vault Query Response Structure
  property_count: 3
  slug: veeva-vault-query-response-structure
- name: Veeva Vault User List Response Structure
  property_count: 2
  slug: veeva-vault-user-list-response-structure
jsonld:
- class_count: 25
  name: Veeva Context
  property_count: 7
  slug: veeva-context
layout: provider
modified: '2026-05-19'
name: veeva
nav: Providers
network: true
overview: 'veeva publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Objects API, and 3 more.


  The veeva catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  veeva''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, support, and 13 more developer resources.'
plans:
- name: Veeva Plans Pricing
  plan_count: 1
  slug: veeva-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 2
  name: Veeva Rate Limits
  slug: veeva-rate-limits
rules:
- name: veeva API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: veeva-jsonschema-spectral-rules
- name: veeva API Rules
  rule_count: 38
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 23
  slug: veeva-spectral-rules
score:
  band: strong
  composite: 57.6
  delta: -4.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 74.6
    developer_ergonomics: 54.3
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 61.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veeva/refs/heads/main/screenshots/veeva-2026-06-20T200859.png
security:
- kind: authentication
  name: Veeva Authentication
  slug: veeva-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Veeva Domain Security
  slug: veeva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: veeva
use_cases:
- description: Automate the assembly and submission of regulatory dossiers (CTD, eCTD) by programmatically managing document lifecycle, approvals, and publishing.
  name: Regulatory Document Submission
- description: Integrate Vault with CTMS, EDC, and LIMS systems to automate study document workflows, protocol amendments, and site activation packages.
  name: Clinical Trial Data Management
- description: Automate SOPs, CAPAs, deviations, and audit workflows in QMS Vault through lifecycle actions, object creation, and workflow task assignment.
  name: Quality Management Automation
- description: Export Vault document and object data in bulk for BI dashboards, compliance reporting, and cross-Vault analytics using the Direct Data API.
  name: Content Analytics
- description: Integrate Vault with SAP, Salesforce, Veeva CRM, and other enterprise systems using REST APIs for bidirectional data synchronization.
  name: Enterprise Integration
website: https://www.veeva.com/
---
