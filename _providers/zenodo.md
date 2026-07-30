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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Zenodo Agentic Access
  operation_count: 99
  slug: zenodo-agentic-access
  summary_line: 99 operations · 42 acting
api_count: 25
apis:
- description: Open Archives Initiative Protocol for Metadata Harvesting endpoint that allows bulk harvesting of Zenodo metadata in formats including oai_dc, marcxml, and oai_datacite4. Supports selective harvesting
  name: Zenodo OAI-PMH API
  slug: zenodo-oai-pmh-api
- description: Access control and sharing
  name: Zenodo Access API
  slug: zenodo-access-api
- description: Audit log entries and search
  name: Zenodo Audit Logs API
  slug: zenodo-audit-logs-api
- description: User and group avatars
  name: Zenodo Avatars API
  slug: zenodo-avatars-api
- description: Request comments and discussions
  name: Zenodo Comments API
  slug: zenodo-comments-api
- description: Community management endpoints
  name: Zenodo Communities API
  slug: zenodo-communities-api
- description: Community invitation management
  name: Zenodo Communities Invitations API
  slug: zenodo-communities-invitations-api
- description: Community logo management
  name: Zenodo Communities logo API
  slug: zenodo-communities-logo-api
- description: Community membership management
  name: Zenodo Communities Members API
  slug: zenodo-communities-members-api
- description: Draft record management
  name: Zenodo Drafts API
  slug: zenodo-drafts-api
- description: Draft file upload workflow
  name: Zenodo Drafts Files upload API
  slug: zenodo-drafts-files-upload-api
- description: Record export functionality
  name: Zenodo Export API
  slug: zenodo-export-api
- description: Featured communities management
  name: Zenodo Featured Communities API
  slug: zenodo-featured-communities-api
- description: Group management endpoints
  name: Zenodo Groups API
  slug: zenodo-groups-api
- description: OAI-PMH protocol endpoints
  name: Zenodo OAI-PMH API
  slug: zenodo-oai-pmh-api
- description: OAI-PMH set management
  name: Zenodo OAI-PMH Sets API
  slug: zenodo-oai-pmh-sets-api
- description: Record and draft management endpoints
  name: Zenodo Records API
  slug: zenodo-records-api
- description: File management operations on published records
  name: Zenodo Records Files API
  slug: zenodo-records-files-api
- description: Record version management
  name: Zenodo Records Versions API
  slug: zenodo-records-versions-api
- description: Request actions and lifecycle management
  name: Zenodo Request Actions API
  slug: zenodo-request-actions-api
- description: Request management endpoints
  name: Zenodo Requests API
  slug: zenodo-requests-api
- description: Statistics and analytics endpoints
  name: Zenodo Statistics API
  slug: zenodo-statistics-api
- description: Request timeline and history
  name: Zenodo Timeline API
  slug: zenodo-timeline-api
- description: User management endpoints
  name: Zenodo Users API
  slug: zenodo-users-api
- description: Vocabulary and controlled terms endpoints
  name: Zenodo Vocabularies API
  slug: zenodo-vocabularies-api
artifact_total: 35
common:
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


  Zenodo''s developer surface includes authentication, documentation, engineering blog, support, code examples, and 14 more developer resources.'
plans:
- name: Zenodo Plans Pricing
  plan_count: 2
  slug: zenodo-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 7
  name: Zenodo Rate Limits
  slug: zenodo-rate-limits
rules:
- name: Zenodo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zenodo-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.5
  delta: -4.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.2
    developer_ergonomics: 34.8
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 53.4
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
