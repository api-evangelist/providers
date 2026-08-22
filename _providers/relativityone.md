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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Relativityone Agentic Access
  operation_count: 13
  slug: relativityone-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 11
apis:
- description: The Object Manager API provides CRUD operations for documents and Relativity Dynamic Objects (RDOs). It supports bulk read, create, update, and delete operations with filtering and search capabilities
  name: Object Manager API
  slug: object-manager-api
- description: The Workspace Manager API provides CRUD operations for Relativity workspaces, including workspace creation, configuration, application installation, and environment management.
  name: Workspace Manager API
  slug: workspace-manager-api
- description: APIs for search and analytics operations in RelativityOne including dtSearch index management, keyword search, Analytics Conceptual Index for LSI and concept discovery, and Pivot queries for data anal
  name: Search and Analytics API
  slug: search-analytics-api
- description: APIs for identity and access management in RelativityOne. Includes user CRUD operations, permission assignment and management, group administration, and client management.
  name: User and Permission Manager API
  slug: user-permission-manager-api
- description: Import and Export Services API for handling document and Relativity Dynamic Object (RDO) transfers, including bulk import operations for large data sets.
  name: Import and Export API
  slug: import-export-api
- description: Operations for legal hold communications and notifications
  name: RelativityOne Communications API
  slug: relativityone-communications-api
- description: Operations for managing legal hold custodians
  name: RelativityOne Custodians API
  slug: relativityone-custodians-api
- description: Operations for managing HR entities and employees
  name: RelativityOne Entities API
  slug: relativityone-entities-api
- description: Operations for managing legal hold projects
  name: RelativityOne Legal Hold Projects API
  slug: relativityone-legal-hold-projects-api
- description: Operations for data preservation and releases
  name: RelativityOne Preservation API
  slug: relativityone-preservation-api
- description: Operations for legal hold task management
  name: RelativityOne Tasks API
  slug: relativityone-tasks-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RelativityOne Legal Hold Communications API
  slug: open-relativityone-communications-api
- collection_type: open
  name: RelativityOne Legal Hold Communications Custodians API
  slug: open-relativityone-custodians-api
- collection_type: open
  name: RelativityOne Legal Hold Communications Entities API
  slug: open-relativityone-entities-api
- collection_type: open
  name: RelativityOne Legal Hold Communications Legal Hold Projects API
  slug: open-relativityone-legal-hold-projects-api
- collection_type: open
  name: RelativityOne Legal Hold API
  slug: open-relativityone-legal-hold
- collection_type: open
  name: RelativityOne Legal Hold Communications Preservation API
  slug: open-relativityone-preservation-api
- collection_type: open
  name: RelativityOne Legal Hold Communications Tasks API
  slug: open-relativityone-tasks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/relativityone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/relativityone-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/relativityone-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relativityone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/relativityone-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/relativityhq
- group: company
  title: ''
  type: Website
  url: https://www.relativity.com
- group: docs
  title: ''
  type: Documentation
  url: https://platform.relativity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/index.htm
- group: docs
  title: ''
  type: APIReference
  url: https://platform.relativity.com/RelativityOne/Content/Relativity_Platform/Relativity_API_reference.htm
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.relativity.com/RelativityOne/Content/What_s_new/What_s_new.htm
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/json-ld/relativityone-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/vocabulary/relativityone-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/rules/relativityone-rules.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/relativitydev
- group: company
  title: ''
  type: Blog
  url: https://feeds.feedburner.com/relativity/blog
created: '2025-03-01'
description: RelativityOne is a cloud-based eDiscovery and legal technology platform that provides comprehensive REST APIs for legal hold management, document processing, search and analytics, workspace management, identity and access control, and billing insights. The platform integrates with Microsoft 365 and Google Workspace for data preservation and legal hold workflows.
examples:
- key_count: 4
  name: Relativityone Add Custodian Example
  slug: relativityone-add-custodian-example
- key_count: 4
  name: Relativityone Create Legal Hold Project Example
  slug: relativityone-create-legal-hold-project-example
finops:
- name: Relativityone Finops
  service_category: eDiscovery
  slug: relativityone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relativityone.png
json_schemas:
- name: ActiveCustodianSummary
  property_count: 6
  slug: relativityone-activecustodiansummary
- name: ActiveCustodianSummaryList
  property_count: 2
  slug: relativityone-activecustodiansummarylist
- name: AddCustodianRequest
  property_count: 2
  slug: relativityone-addcustodianrequest
- name: CreateCommunicationRequest
  property_count: 4
  slug: relativityone-createcommunicationrequest
- name: CreateEntityRequest
  property_count: 4
  slug: relativityone-createentityrequest
- name: CreateLegalHoldProjectRequest
  property_count: 4
  slug: relativityone-createlegalholdprojectrequest
- name: CreateTaskRequest
  property_count: 4
  slug: relativityone-createtaskrequest
- name: Legal Hold Custodian
  property_count: 6
  slug: relativityone-custodian
- name: CustodianList
  property_count: 2
  slug: relativityone-custodianlist
- name: Entity
  property_count: 5
  slug: relativityone-entity
- name: Legal Hold Project
  property_count: 7
  slug: relativityone-legal-hold-project
- name: LegalHoldProject
  property_count: 7
  slug: relativityone-legalholdproject
- name: LegalHoldProjectList
  property_count: 2
  slug: relativityone-legalholdprojectlist
- name: PreservationRequest
  property_count: 2
  slug: relativityone-preservationrequest
- name: ReleaseRequest
  property_count: 1
  slug: relativityone-releaserequest
- name: Task
  property_count: 5
  slug: relativityone-task
- name: UpdateEntityStatusRequest
  property_count: 1
  slug: relativityone-updateentitystatusrequest
- name: UpdateTaskRequest
  property_count: 2
  slug: relativityone-updatetaskrequest
json_structures:
- name: Relativityone Legal Hold Structure
  property_count: 0
  slug: relativityone-legal-hold-structure
- name: Relativityone Structure
  property_count: 0
  slug: relativityone-structure
jsonld:
- class_count: 0
  name: Relativityone Context
  property_count: 27
  slug: relativityone-context
layout: provider
modified: '2026-05-19'
name: RelativityOne
nav: Providers
network: true
overview: 'RelativityOne publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Communications API, Custodians API, Entities API, and 3 more. Tagged areas include eDiscovery, Legal, Legal Hold, Document Management, and Compliance.


  The RelativityOne catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RelativityOne''s developer surface includes authentication, documentation, API reference, changelog, engineering blog, and 11 more developer resources.'
plans:
- name: Relativityone Plans Pricing
  plan_count: 1
  slug: relativityone-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Relativityone Rate Limits
  slug: relativityone-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RelativityOne API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: relativityone-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: RelativityOne API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 5
  slug: relativityone-rules
score:
  band: developing
  composite: 41.2
  delta: -6.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 25.0
    contract_quality: 69.3
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/relativityone/refs/heads/main/screenshots/relativityone-2026-06-20T192820.png
security:
- kind: authentication
  name: Relativityone Authentication
  slug: relativityone-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Relativityone Domain Security
  slug: relativityone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Relativityone Vulnerability Disclosure
  slug: relativityone-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Relativityone Trust Center
  slug: relativityone-trust-center
  summary_line: FedRAMP, GDPR
slug: relativityone
tags:
- eDiscovery
- Legal
- Legal Hold
- Document Management
- Compliance
- Litigation
website: https://www.relativity.com
---
