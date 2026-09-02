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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Uspto Gov Agentic Access
  operation_count: 48
  slug: uspto-gov-agentic-access
  summary_line: 48 operations · 1 acting
api_count: 6
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
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) API
  slug: open-uspto-bulk-data
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals API
  slug: open-uspto-gov-appeals-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Application API
  slug: open-uspto-gov-application-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Assignments API
  slug: open-uspto-gov-assignments-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Citations API
  slug: open-uspto-gov-citations-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Datasets API
  slug: open-uspto-gov-datasets-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Decisions API
  slug: open-uspto-gov-decisions-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Documents API
  slug: open-uspto-gov-documents-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Enriched Citations API
  slug: open-uspto-gov-enriched-citations-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Office Actions API
  slug: open-uspto-gov-office-actions-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Patentsview API
  slug: open-uspto-gov-patentsview-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Proceedings API
  slug: open-uspto-gov-proceedings-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Rejections API
  slug: open-uspto-gov-rejections-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Search API
  slug: open-uspto-gov-search-api
- collection_type: open
  name: USPTO Bulk Data Storage System (BDSS) Appeals Status API
  slug: open-uspto-gov-status-api
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/uspto-gov-capability-edges.yml
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


  USPTO''s developer surface includes authentication, developer portal, documentation, support, GitHub presence, engineering blog, and 18 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 2
  name: Uspto Gov Rate Limits
  slug: uspto-gov-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: USPTO API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: uspto-gov-jsonschema-spectral-rules
score:
  band: thin
  composite: 34.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 63.3
    developer_ergonomics: 26.2
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 34.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
