---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Veeva Agentic Access
  operation_count: 15
  slug: veeva-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 1
apis:
- description: 'The Veeva Vault Java SDK (VAPIL) is an open-source Java-based REST API client for the Vault REST API. Provides type-safe access to all Vault API operations including document management, object CRUD, '
  name: Veeva Vault Java SDK
  slug: veeva-vault-java-sdk
- description: 'The Veeva Vault Direct Data API provides high-speed, read-only bulk access to Vault data for integration, analytics, and reporting purposes. Supports bulk export of documents, objects, and attachment '
  name: Veeva Vault Direct Data API
  slug: veeva-vault-direct-data-api
- baseURL: https://myvault.veevavault.com/api/v25.3
  baseurl_source: declared
  description: Session management
  name: veeva Authentication API
  phrasing_intents:
  - id: authenticateUser
    intent: Sign in to Vault and get a session ID
    question: How do I get a session ID to call the Veeva Vault API?
  phrasing_ops: 1
  slug: veeva-authentication-api
- baseURL: https://myvault.veevavault.com/api/v25.3
  baseurl_source: declared
  description: Document lifecycle management
  name: veeva Documents API
  phrasing_intents:
  - id: listDocuments
    intent: List documents I can access in Vault
    question: Which documents in Veeva Vault can I see?
  - id: createDocument
    intent: Create a new document in Vault
    question: How do I create a new document record and upload its source file at the same time?
  - id: getDocument
    intent: Get a document's metadata
    question: How do I see the properties and metadata of one Vault document?
  - id: updateDocument
    intent: Update a document's field values
    question: How do I change the metadata fields on a document without replacing its file?
  - id: deleteDocument
    intent: Delete a document and all its versions
    question: How do I permanently delete a document from Vault?
  - id: downloadDocumentFile
    intent: Download a document's source file
    question: How do I download the actual file behind a Vault document?
  - id: performDocumentAction
    intent: Run a lifecycle action on a document
    question: How do I approve a document so it changes lifecycle state?
  phrasing_ops: 7
  slug: veeva-documents-api
- baseURL: https://myvault.veevavault.com/api/v25.3
  baseurl_source: declared
  description: Vault object CRUD operations
  name: veeva Objects API
  phrasing_intents:
  - id: listObjectRecords
    intent: List records of a Vault object
    question: How do I list all the study or product records stored in a Vault object?
  - id: createObjectRecord
    intent: Create a Vault object record
    question: How do I add a new site or product record to a Vault object?
  - id: getObjectRecord
    intent: Get one Vault object record
    question: How do I look up a single object record in Vault by its ID?
  - id: updateObjectRecord
    intent: Update fields on a Vault object record
    question: How do I change field values on an existing Vault object record?
  - id: deleteObjectRecord
    intent: Delete a Vault object record
    question: How do I remove an object record from Vault?
  phrasing_ops: 5
  slug: veeva-objects-api
- baseURL: https://myvault.veevavault.com/api/v25.3
  baseurl_source: declared
  description: VQL query execution
  name: veeva Query API
  phrasing_intents:
  - id: executeVQLQuery
    intent: Run a VQL query across Vault data
    question: How do I run a Vault Query Language query against my vault?
  phrasing_ops: 1
  slug: veeva-query-api
- baseURL: https://myvault.veevavault.com/api/v25.3
  baseurl_source: declared
  description: User management
  name: veeva Users API
  phrasing_intents:
  - id: listUsers
    intent: List active Vault users
    question: Who are the active users in my Veeva Vault?
  phrasing_ops: 1
  slug: veeva-users-api
- baseURL: https://myvault.veevavault.com/api/v25.3
  baseurl_source: declared
  description: Workflow and task management
  name: veeva Workflows API
  phrasing_intents:
  - id: performDocumentAction
    intent: Move a document through its lifecycle workflow
    question: How do I send a Vault document for review as part of a workflow?
  phrasing_ops: 1
  slug: veeva-workflows-api
- description: Veeva ships two first-party Model Context Protocol servers. The Vault Documentation MCP at https://docs.veevavault.dev/mcp is public and anonymous, exposing one search_documentation tool over the Vaul
  name: Veeva Vault MCP
  slug: vault-mcp
artifact_total: 86
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
- group: design
  href: https://artifacts.apis.io/veeva/rules/veeva-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/veeva-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/veeva/rules/veeva-rules.yml
  title: ''
  type: Spectral
  url: rules/veeva-rules.yml
- group: design
  href: https://artifacts.apis.io/veeva/rules/veeva-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/veeva-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/veeva/json-ld/veeva-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veeva-context.jsonld
- group: auth
  href: https://artifacts.apis.io/veeva/security/veeva-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/veeva-trust-center.yml
- group: operate
  href: https://artifacts.apis.io/veeva/lifecycle/veeva-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/veeva-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/veeva/hosts/veeva-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veeva-hosts.yml
- group: other
  href: https://artifacts.apis.io/veeva/vendors/veeva-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veeva-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.veeva.com/events/rd-summit/register/
- group: company
  title: ''
  type: Newsroom
  url: https://www.veeva.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.veeva.com/leadership/management/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.veeva.com/products/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/veeva/overview
- group: agent
  href: https://artifacts.apis.io/veeva/agentic-access/veeva-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/veeva-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/veeva/security/veeva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veeva-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/veeva/authentication/veeva-authentication.yml
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
  href: https://artifacts.apis.io/veeva/json-schema/veeva-vault-document-schema.json
  title: Vault Document Schema
  type: JSONSchema
  url: json-schema/veeva-vault-document-schema.json
- group: design
  href: https://artifacts.apis.io/veeva/json-ld/veeva-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/veeva-context.jsonld
- group: design
  href: https://artifacts.apis.io/veeva/rules/veeva-spectral-rules.yml
  title: Veeva Vault API Spectral Rules
  type: SpectralRules
  url: rules/veeva-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/veeva/vocabulary/veeva-vocabulary.yml
  title: Veeva Vocabulary
  type: Vocabulary
  url: vocabulary/veeva-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/veeva/packages/veeva-packages.yml
  title: Veeva first-party packages
  type: Packages
  url: packages/veeva-packages.yml
- group: build
  href: https://artifacts.apis.io/veeva/packages/veeva-packages.yml
  title: Veeva SDK inventory
  type: SDKs
  url: packages/veeva-packages.yml
- group: agent
  href: https://artifacts.apis.io/veeva/mcp/veeva-mcp.yml
  title: Vault Documentation MCP + Vault MCP Server
  type: MCPServer
  url: mcp/veeva-mcp.yml
- group: build
  href: https://artifacts.apis.io/veeva/mcp/veeva-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/veeva-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/veeva/llms/veeva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veeva-llms.txt
- group: design
  href: https://artifacts.apis.io/veeva/conformance/veeva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veeva-conformance.yml
- group: auth
  href: https://artifacts.apis.io/veeva/conformance/veeva-conformance.yml
  title: ISO 27001/27017/27018, ISO 9001, SOC 2 Type II
  type: Compliance
  url: conformance/veeva-conformance.yml
- group: design
  href: https://artifacts.apis.io/veeva/errors/veeva-problem-types.yml
  title: Vault API error types
  type: ErrorCatalog
  url: errors/veeva-problem-types.yml
- group: design
  href: https://artifacts.apis.io/veeva/lifecycle/veeva-lifecycle.yml
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
  href: https://artifacts.apis.io/veeva/sandbox/veeva-sandbox.yml
  title: Vault sandbox Vaults
  type: Sandbox
  url: sandbox/veeva-sandbox.yml
- group: design
  href: https://artifacts.apis.io/veeva/conventions/veeva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veeva-conventions.yml
- group: operate
  href: https://artifacts.apis.io/veeva/changelog/veeva-changelog.yml
  title: Developer release notes, structured
  type: ChangeLog
  url: changelog/veeva-changelog.yml
- group: design
  href: https://artifacts.apis.io/veeva/components/veeva-components.yml
  title: Custom Pages, Vault Web SDK, Vault Toolbox
  type: Components
  url: components/veeva-components.yml
- group: design
  href: https://artifacts.apis.io/veeva/data-model/veeva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veeva-data-model.yml
- group: design
  href: https://artifacts.apis.io/veeva/asyncapi/veeva-spark-messaging-webhooks.yml
  title: Spark Messaging signed outbound events
  type: Webhooks
  url: asyncapi/veeva-spark-messaging-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/veeva/skills/_index.yml
  title: API Evangelist agent skills for Vault
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/veeva/rate-limits/veeva-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/veeva-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/veeva/plans/veeva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/veeva-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/veeva/finops/veeva-finops.yml
  title: ''
  type: FinOps
  url: finops/veeva-finops.yml
- group: other
  href: https://artifacts.apis.io/veeva/overlays/veeva-documents-api-overlay.yaml
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
- has_sources: true
  method: derived
  name: Veeva Finops
  primary_unit: ''
  service_category: ''
  slug: veeva-finops
  template: true
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
- description: Remote MCP server at docs.veevavault.dev; 2 tools listed.
  name: Vault Documentation MCP + Vault MCP Server
  slug: vault-documentation-mcp-vault-mcp-server
modified: '2026-08-15'
name: Veeva
nav: Providers
network: true
overview: 'Veeva publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Documents API, Objects API, and 6 more. Tagged areas include Life Sciences, Pharmaceuticals, Clinical Trials, Regulatory, and Quality Management.


  The Veeva catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Veeva''s developer surface includes signup flow, pricing, authentication, developer portal, documentation, getting-started guide, changelog, and 55 more developer resources.'
plans:
- name: Veeva Plans Pricing
  plan_count: 1
  slug: veeva-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Veeva Rate Limits
  slug: veeva-rate-limits
rules:
- authorship: generated
  effective_rule_count: 4
  extends: []
  name: Veeva — jsonschema rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: veeva-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Veeva API Rules
  rule_count: 15
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 0
  slug: veeva-rules
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Veeva API Rules
  rule_count: 38
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 23
  slug: veeva-spectral-rules
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 39
    catalog_earned: 79.8
    catalog_earned_first_party: 20.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 69.7
    contract_governance: 35.6
    contract_quality: 77.0
    developer_ergonomics: 82.7
    discoverability: 76.7
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 76.1
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
    score: 23.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/veeva/veeva-2026-06-20T200859.png
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
skill_count: 4
skills:
- name: veeva-authenticate-and-query
  slug: veeva-authenticate-and-query
- name: veeva-manage-document-lifecycle
  slug: veeva-manage-document-lifecycle
- name: veeva-manage-object-records
  slug: veeva-manage-object-records
- name: veeva-run-document-workflow-action
  slug: veeva-run-document-workflow-action
slug: veeva
tags:
- Life Sciences
- Pharmaceuticals
- Clinical Trials
- Regulatory
- Quality Management
- Document Management
- Content Management
- Healthcare
- Software-as-a-Service
- Enterprise
- MCP
- Agents
- Clinical Research
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
