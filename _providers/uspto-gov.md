---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Uspto Gov Agentic Access
  operation_count: 48
  slug: uspto-gov-agentic-access
  summary_line: 48 operations · 1 acting
api_count: 14
apis:
- description: PTAB appeal and interference decisions
  name: USPTO Appeals API
  slug: uspto-gov-appeals-api
- description: Retrieve patent application data
  name: USPTO Application API
  slug: uspto-gov-application-api
- description: Retrieve assignment records
  name: USPTO Assignments API
  slug: uspto-gov-assignments-api
- description: The Citations API from USPTO — 2 operation(s) for citations.
  name: USPTO Citations API
  slug: uspto-gov-citations-api
- description: The Datasets API from USPTO — 3 operation(s) for datasets.
  name: USPTO Datasets API
  slug: uspto-gov-datasets-api
- description: PTAB decisions
  name: USPTO Decisions API
  slug: uspto-gov-decisions-api
- description: Retrieve patent application documents
  name: USPTO Documents API
  slug: uspto-gov-documents-api
- description: The Enriched Citations API from USPTO — 2 operation(s) for enriched citations.
  name: USPTO Enriched Citations API
  slug: uspto-gov-enriched-citations-api
- description: The Office Actions API from USPTO — 2 operation(s) for office actions.
  name: USPTO Office Actions API
  slug: uspto-gov-office-actions-api
- description: The Patentsview API from USPTO — 5 operation(s) for patentsview.
  name: USPTO Patentsview API
  slug: uspto-gov-patentsview-api
- description: PTAB trial proceedings
  name: USPTO Proceedings API
  slug: uspto-gov-proceedings-api
- description: The Rejections API from USPTO — 2 operation(s) for rejections.
  name: USPTO Rejections API
  slug: uspto-gov-rejections-api
- description: Search patent applications
  name: USPTO Search API
  slug: uspto-gov-search-api
- description: Trademark case status
  name: USPTO Status API
  slug: uspto-gov-status-api
artifact_total: 28
collections:
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) API
  slug: open-uspto-bulk-data
- collection_type: open
  name: USPTO Office Action APIs
  slug: open-uspto-office-actions
- collection_type: open
  name: USPTO Patent File Wrapper API
  slug: open-uspto-patent-file-wrapper
- collection_type: open
  name: USPTO PatentsView API
  slug: open-uspto-patentsview
- collection_type: open
  name: USPTO Patent Trial and Appeal Board (PTAB) API
  slug: open-uspto-ptab
- collection_type: open
  name: USPTO Trademark Status and Document Retrieval (TSDR) API
  slug: open-uspto-tsdr
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uspto-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uspto-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uspto-gov-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uspto.gov/
- group: start
  title: ''
  type: Portal
  url: https://data.uspto.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uspto.gov/api-catalog
- group: docs
  title: ''
  type: Documentation
  url: https://data.uspto.gov/apis/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://data.uspto.gov/apis/transition-guide
- group: docs
  title: ''
  type: Documentation
  url: https://data.uspto.gov/documents/documents/BDSS-to-ODP-API-Mapping.pdf
- group: docs
  title: ''
  type: Documentation
  url: https://www.uspto.gov/sites/default/files/documents/tm-enterprise-api-user-guide-v2.pdf
- group: auth
  title: ''
  type: Authentication
  url: https://data.uspto.gov/apis/getting-started
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.uspto.gov/files/tsdr-api-key-manager-user-guide
- group: operate
  title: ''
  type: Support
  url: mailto:APIhelp@uspto.gov
- group: operate
  title: ''
  type: Support
  url: mailto:contactUXD@uspto.gov
- group: build
  title: ''
  type: GitHub
  url: https://github.com/USPTO
- group: start
  title: ''
  type: DataPortal
  url: https://catalog.data.gov/organization/uspto-gov
- group: other
  title: ''
  type: BulkData
  url: https://data.uspto.gov/patent-file-wrapper/bulkdata/entire
- group: other
  title: ''
  type: Trademark
  url: https://tsdr.uspto.gov/
- group: other
  title: ''
  type: Trademark
  url: https://www.uspto.gov/trademarks/apply/check-status-view-documents/trademark-bulk-data
- group: other
  title: ''
  type: Patent
  url: https://patentcenter.uspto.gov/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uspto-gov-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uspto-gov-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.uspto.gov/rss.xml
created: '2026-05-25'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uspto-gov.png
json_schemas:
- name: USPTO Patent Application
  property_count: 19
  slug: uspto-patent-application
- name: USPTO Trademark Case
  property_count: 12
  slug: uspto-trademark-case
jsonld:
- class_count: 20
  name: Uspto Gov Context
  property_count: 17
  slug: uspto-gov-context
layout: provider
modified: '2026-05-25'
name: USPTO
nav: Providers
network: true
overview: 'USPTO publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Appeals API, Application API, Assignments API, and 11 more. Tagged areas include Patents, Trademarks, Intellectual Property, Government, and Federal.


  The USPTO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  USPTO''s developer surface includes authentication, developer portal, documentation, support, GitHub presence, engineering blog, and 17 more developer resources.'
random_paper: 30
rate_limits:
- limit_count: 0
  name: Uspto Gov Rate Limits
  slug: uspto-gov-rate-limits
rules:
- name: USPTO API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: uspto-gov-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.2
  delta: -0.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 59.5
    developer_ergonomics: 34.8
    discoverability: 55.0
    governance: 86.8
    operational_transparency: 5.3
  previous_composite: 38.4
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uspto-gov/refs/heads/main/screenshots/uspto-gov-2026-06-20T200720.png
security:
- kind: authentication
  name: Uspto Gov Authentication
  slug: uspto-gov-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Uspto Gov Domain Security
  slug: uspto-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uspto-gov
tags:
- Patents
- Trademarks
- Intellectual Property
- Government
- Federal
- Open Data
- PTAB
- TSDR
website: https://www.uspto.gov/
---
