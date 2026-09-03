---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Zenodo Agentic Access
  operation_count: 99
  slug: zenodo-agentic-access
  summary_line: 99 operations · 42 acting
api_count: 1
apis:
- baseURL: https://zenodo.org/oai2d
  baseurl_source: declared
  description: Open Archives Initiative Protocol for Metadata Harvesting endpoint that allows bulk harvesting of Zenodo metadata in formats including oai_dc, marcxml, and oai_datacite4. Supports selective harvesting
  name: Zenodo OAI-PMH API
  slug: zenodo-oai-pmh-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Access control and sharing
  name: Zenodo Access API
  slug: zenodo-access-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Audit log entries and search
  name: Zenodo Audit Logs API
  slug: zenodo-audit-logs-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: User and group avatars
  name: Zenodo Avatars API
  slug: zenodo-avatars-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Request comments and discussions
  name: Zenodo Comments API
  slug: zenodo-comments-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Community management endpoints
  name: Zenodo Communities API
  slug: zenodo-communities-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Community invitation management
  name: Zenodo Communities Invitations API
  slug: zenodo-communities-invitations-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Community logo management
  name: Zenodo Communities logo API
  slug: zenodo-communities-logo-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Community membership management
  name: Zenodo Communities Members API
  slug: zenodo-communities-members-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Draft record management
  name: Zenodo Drafts API
  slug: zenodo-drafts-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Draft file upload workflow
  name: Zenodo Drafts Files upload API
  slug: zenodo-drafts-files-upload-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Record export functionality
  name: Zenodo Export API
  slug: zenodo-export-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Featured communities management
  name: Zenodo Featured Communities API
  slug: zenodo-featured-communities-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Group management endpoints
  name: Zenodo Groups API
  slug: zenodo-groups-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: OAI-PMH protocol endpoints
  name: Zenodo OAI-PMH API
  slug: zenodo-oai-pmh-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: OAI-PMH set management
  name: Zenodo OAI-PMH Sets API
  slug: zenodo-oai-pmh-sets-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Record and draft management endpoints
  name: Zenodo Records API
  slug: zenodo-records-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: File management operations on published records
  name: Zenodo Records Files API
  slug: zenodo-records-files-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Record version management
  name: Zenodo Records Versions API
  slug: zenodo-records-versions-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Request actions and lifecycle management
  name: Zenodo Request Actions API
  slug: zenodo-request-actions-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Request management endpoints
  name: Zenodo Requests API
  slug: zenodo-requests-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Statistics and analytics endpoints
  name: Zenodo Statistics API
  slug: zenodo-statistics-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Request timeline and history
  name: Zenodo Timeline API
  slug: zenodo-timeline-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: User management endpoints
  name: Zenodo Users API
  slug: zenodo-users-api
- baseURL: https://zenodo.org/api
  baseurl_source: declared
  description: Vocabulary and controlled terms endpoints
  name: Zenodo Vocabularies API
  slug: zenodo-vocabularies-api
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zenodo REST Access API
  slug: open-zenodo-access-api
- collection_type: open
  name: Zenodo REST Access Audit Logs API
  slug: open-zenodo-audit-logs-api
- collection_type: open
  name: Zenodo REST Access Avatars API
  slug: open-zenodo-avatars-api
- collection_type: open
  name: Zenodo REST Access Comments API
  slug: open-zenodo-comments-api
- collection_type: open
  name: Zenodo REST Access Communities API
  slug: open-zenodo-communities-api
- collection_type: open
  name: Zenodo REST Access Communities Invitations API
  slug: open-zenodo-communities-invitations-api
- collection_type: open
  name: Zenodo REST Access Communities logo API
  slug: open-zenodo-communities-logo-api
- collection_type: open
  name: Zenodo REST Access Communities Members API
  slug: open-zenodo-communities-members-api
- collection_type: open
  name: Zenodo REST Access Drafts API
  slug: open-zenodo-drafts-api
- collection_type: open
  name: Zenodo REST Access Drafts Files upload API
  slug: open-zenodo-drafts-files-upload-api
- collection_type: open
  name: Zenodo REST Access Export API
  slug: open-zenodo-export-api
- collection_type: open
  name: Zenodo REST Access Featured Communities API
  slug: open-zenodo-featured-communities-api
- collection_type: open
  name: Zenodo REST Access Groups API
  slug: open-zenodo-groups-api
- collection_type: open
  name: Zenodo REST Access OAI-PMH API
  slug: open-zenodo-oai-pmh-api
- collection_type: open
  name: Zenodo REST Access OAI-PMH Sets API
  slug: open-zenodo-oai-pmh-sets-api
- collection_type: open
  name: Zenodo REST Access Records API
  slug: open-zenodo-records-api
- collection_type: open
  name: Zenodo REST Access Records Files API
  slug: open-zenodo-records-files-api
- collection_type: open
  name: Zenodo REST Access Records Versions API
  slug: open-zenodo-records-versions-api
- collection_type: open
  name: Zenodo REST Access Request Actions API
  slug: open-zenodo-request-actions-api
- collection_type: open
  name: Zenodo REST Access Requests API
  slug: open-zenodo-requests-api
- collection_type: open
  name: Zenodo REST Access Statistics API
  slug: open-zenodo-statistics-api
- collection_type: open
  name: Zenodo REST Access Timeline API
  slug: open-zenodo-timeline-api
- collection_type: open
  name: Zenodo REST Access Users API
  slug: open-zenodo-users-api
- collection_type: open
  name: Zenodo REST Access Vocabularies API
  slug: open-zenodo-vocabularies-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zenodo-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zenodo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenodo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zenodo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://zenodo.org/
- group: docs
  title: ''
  type: Documentation
  url: https://help.zenodo.org/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.zenodo.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenodo
- group: company
  title: ''
  type: Blog
  url: https://blog.zenodo.org/
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/vlYOVuWgM/
- group: other
  title: ''
  type: X
  url: https://x.com/ZENODO_ORG
- group: operate
  title: ''
  type: Support
  url: https://support.zenodo.org/
- group: company
  title: ''
  type: About
  url: https://about.zenodo.org/
- group: commercial
  title: ''
  type: Plans
  url: plans/zenodo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zenodo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zenodo-finops.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/zenodo-record-schema.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/zenodo-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/zenodo-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/zenodo-create-record-example.json
created: '2026-06-12'
description: Zenodo is a free, open research data repository operated by CERN and co-developed under the European OpenAIRE program. It enables researchers to deposit, share, and preserve any research output — including datasets, software, papers, preprints, presentations, and multimedia — regardless of format, size, or discipline. Every upload receives a Digital Object Identifier (DOI) for persistent citation and discoverability. Zenodo provides a REST API for programmatic deposit management, record search and retrieval, and file management, as well as an OAI-PMH endpoint for metadata harvesting. The platform is built on InvenioRDM and stores all data at the CERN Data Centre with replicas and nightly tape backups.
examples:
- key_count: 6
  name: Zenodo Create Record Example
  slug: zenodo-create-record-example
finops:
- name: Zenodo Finops
  service_category: ''
  slug: zenodo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenodo.png
json_schemas:
- name: Zenodo Record
  property_count: 12
  slug: zenodo-record
jsonld:
- class_count: 48
  name: Zenodo Context
  property_count: 25
  slug: zenodo-context
layout: provider
modified: '2026-06-12'
name: Zenodo
nav: Providers
network: true
overview: 'Zenodo publishes 25 APIs on the [APIs.io](https://apis.io/) network, including OAI-PMH API, Access API, Audit Logs API, and 22 more. Tagged areas include Research, Open Data, Repository, DOI, and Datasets.


  The Zenodo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zenodo''s developer surface includes authentication, documentation, engineering blog, support, code examples, and 15 more developer resources.'
plans:
- name: Zenodo Plans Pricing
  plan_count: 2
  slug: zenodo-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 7
  name: Zenodo Rate Limits
  slug: zenodo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Zenodo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zenodo-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 35.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 65.9
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 50.0
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenodo/refs/heads/main/screenshots/zenodo-2026-06-20T201814.png
security:
- kind: authentication
  name: Zenodo Authentication
  slug: zenodo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zenodo Domain Security
  slug: zenodo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenodo
tags:
- Research
- Open Data
- Repository
- DOI
- Datasets
- Software
- CERN
- OpenAIRE
- InvenioRDM
- Open Science
- Metadata
- Harvesting
website: https://zenodo.org/
---
