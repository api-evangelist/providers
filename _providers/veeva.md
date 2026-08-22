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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Veeva Agentic Access
  operation_count: 15
  slug: veeva-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 9
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
- description: Veeva ships two first-party Model Context Protocol servers. The Vault Documentation MCP at https://docs.veevavault.dev/mcp is public and anonymous, exposing one search_documentation tool over the Vaul
  name: Veeva Vault MCP
  slug: vault-mcp
artifact_total: 83
asyncapis:
- description: ''
  name: Veeva Spark Messaging Webhooks
  slug: veeva-spark-messaging-webhooks
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Veeva Vault REST Authentication API
  slug: open-veeva-authentication-api
- collection_type: open
  name: Veeva Vault REST Authentication Documents API
  slug: open-veeva-documents-api
- collection_type: open
  name: Veeva Vault REST Authentication Objects API
  slug: open-veeva-objects-api
- collection_type: open
  name: Veeva Vault REST Authentication Query API
  slug: open-veeva-query-api
- collection_type: open
  name: Veeva Vault REST Authentication Users API
  slug: open-veeva-users-api
- collection_type: open
  name: Veeva Vault REST API
  slug: open-veeva-vault
- collection_type: open
  name: Veeva Vault REST Authentication Workflows API
  slug: open-veeva-workflows-api
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
- group: build
  title: Veeva first-party packages
  type: Packages
  url: packages/veeva-packages.yml
- group: build
  title: Veeva SDK inventory
  type: SDKs
  url: packages/veeva-packages.yml
- group: agent
  title: Vault Documentation MCP + Vault MCP Server
  type: MCPServer
  url: mcp/veeva-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/veeva-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veeva-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/veeva-conformance.yml
- group: auth
  title: ISO 27001/27017/27018, ISO 9001, SOC 2 Type II
  type: Compliance
  url: conformance/veeva-conformance.yml
- group: design
  title: Vault API error types
  type: ErrorCatalog
  url: errors/veeva-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/veeva-lifecycle.yml
- group: operate
  title: Veeva Systems status page
  type: StatusPage
  url: https://trust.veeva.com/
- group: auth
  title: Veeva Security Program Overview
  type: TrustCenter
  url: https://www.veeva.com/trust/
- group: start
  title: Vault sandbox Vaults
  type: Sandbox
  url: sandbox/veeva-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/veeva-conventions.yml
- group: operate
  title: Developer release notes, structured
  type: ChangeLog
  url: changelog/veeva-changelog.yml
- group: design
  title: Custom Pages, Vault Web SDK, Vault Toolbox
  type: Components
  url: components/veeva-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/veeva-data-model.yml
- group: design
  title: Spark Messaging signed outbound events
  type: Webhooks
  url: asyncapi/veeva-spark-messaging-webhooks.yml
- group: agent
  title: API Evangelist agent skills for Vault
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/veeva-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/veeva-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/veeva-finops.yml
- group: other
  title: API Evangelist overlays for the Vault OpenAPIs
  type: Overlay
  url: overlays/veeva-documents-api-overlay.yaml
- group: build
  title: Veeva Vault public Postman workspace
  type: Postman
  url: https://www.postman.com/veevavault
- group: start
  title: Vault Developer Portal
  type: DeveloperPortal
  url: https://veevavault.dev
- group: docs
  title: Vault API Reference v26.2
  type: APIReference
  url: https://general.veevavault.dev/vault-api/api-reference/26.2
- group: docs
  title: Vault API documentation (current portal)
  type: Documentation
  url: https://general.veevavault.dev/vault-api
- group: start
  title: ''
  type: GettingStarted
  url: https://general.veevavault.dev/vault-api/getting-started/prerequisites
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.veeva.com/terms/
- group: company
  title: ''
  type: Blog
  url: https://www.veeva.com/veeva-blog/
- group: operate
  title: Veeva Developer Community
  type: Community
  url: http://devcommunity.veevavault.com/
- group: company
  title: ''
  type: Partners
  url: https://www.veeva.com/meet-veeva/partners/
created: '2026-05-03'
description: 'Veeva Systems is the leading cloud software provider for the global life sciences industry, serving pharmaceutical, biotechnology, medical device and CRO customers across commercial, clinical, quality, regulatory, medical and safety operations. Its Vault platform is a single content-and-data cloud whose REST API covers documents, binders, configurable Vault objects, workflows, users, groups, SCIM provisioning, sandbox management and the Direct Data API for high-speed bulk export, all queryable with VQL and extensible through the Vault Java SDK, Custom Pages and Spark Messaging. Veeva also ships two first-party MCP servers: a public Vault Documentation MCP and a tenant-scoped Vault MCP Server that exposes Vault AI agent actions as MCP tools.'
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
mcp_servers:
- description: ''
  name: veeva-mcp.yml
  slug: veeva-mcpyml
modified: '2026-08-15'
name: veeva
nav: Providers
network: true
overview: 'veeva publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Objects API, and 3 more. Tagged areas include Life Sciences, Pharmaceutical, Clinical Trials, Regulatory, and Quality Management.


  The veeva catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  veeva''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, support, sandbox, and 43 more developer resources.'
plans:
- name: Veeva Plans Pricing
  plan_count: 1
  slug: veeva-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Veeva Rate Limits
  slug: veeva-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: veeva API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: veeva-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: veeva API Rules
  rule_count: 38
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 23
  slug: veeva-spectral-rules
score:
  band: exemplar
  composite: 75.0
  delta: 7.2
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 55.3
    contract_quality: 80.7
    developer_ergonomics: 70.8
    discoverability: 81.5
    governance: 55.3
    operational_transparency: 76.3
  previous_composite: 67.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/veeva/refs/heads/main/screenshots/veeva-2026-06-20T200859.png
security:
- kind: authentication
  name: Veeva Authentication
  slug: veeva-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 6 schemes
- kind: domain-security
  name: Veeva Domain Security
  slug: veeva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Veeva Trust Center
  slug: veeva-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO 9001, SOC 2 Type II
slug: veeva
tags:
- Life Sciences
- Pharmaceutical
- Clinical Trials
- Regulatory
- Quality Management
- Document Management
- Content Management
- Healthcare
- SaaS
- Enterprise
- MCP
- Agents
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
