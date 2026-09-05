---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Uspto Gov Agentic Access
  operation_count: 48
  slug: uspto-gov-agentic-access
  summary_line: 48 operations · 1 acting
api_count: 6
apis:
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: PTAB appeal and interference decisions
  name: USPTO Appeals API
  slug: uspto-gov-appeals-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: Retrieve patent application data
  name: USPTO Application API
  slug: uspto-gov-application-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: Retrieve assignment records
  name: USPTO Assignments API
  slug: uspto-gov-assignments-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: The Citations API from USPTO — 2 operation(s) for citations.
  name: USPTO Citations API
  slug: uspto-gov-citations-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: The Datasets API from USPTO — 3 operation(s) for datasets.
  name: USPTO Datasets API
  slug: uspto-gov-datasets-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: PTAB decisions
  name: USPTO Decisions API
  slug: uspto-gov-decisions-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: Retrieve patent application documents
  name: USPTO Documents API
  slug: uspto-gov-documents-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: The Enriched Citations API from USPTO — 2 operation(s) for enriched citations.
  name: USPTO Enriched Citations API
  slug: uspto-gov-enriched-citations-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: The Office Actions API from USPTO — 2 operation(s) for office actions.
  name: USPTO Office Actions API
  slug: uspto-gov-office-actions-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: The Patentsview API from USPTO — 5 operation(s) for patentsview.
  name: USPTO Patentsview API
  slug: uspto-gov-patentsview-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: PTAB trial proceedings
  name: USPTO Proceedings API
  slug: uspto-gov-proceedings-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: The Rejections API from USPTO — 2 operation(s) for rejections.
  name: USPTO Rejections API
  slug: uspto-gov-rejections-api
- baseURL: https://api.uspto.gov
  baseurl_source: spec
  description: Search patent applications
  name: USPTO Search API
  slug: uspto-gov-search-api
- baseURL: https://tsdrapi.uspto.gov
  baseurl_source: spec
  description: Trademark case status
  name: USPTO Status API
  slug: uspto-gov-status-api
- description: The USPTO Patent Assignment Search API retrieves patent assignment information including ownership transfers, recorded assignments, and assignment history for individual patents and patent portfolios.
  name: USPTO Patent Assignment Search API
  slug: assignment-search-api
- description: Patent assignment records
  name: USPTO Assignments API
  slug: uspto-assignments-api
- description: Patent search and retrieval
  name: USPTO Patents API
  slug: uspto-patents-api
- description: Patent Trial and Appeal Board proceedings
  name: USPTO PTAB API
  slug: uspto-ptab-api
- description: Trademark status and documents
  name: USPTO Trademarks API
  slug: uspto-trademarks-api
artifact_total: 48
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
- group: start
  title: ''
  type: Portal
  url: https://developer.uspto.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uspto.gov/
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
overview: 'USPTO publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Appeals API, Application API, Assignments API, and 15 more. Tagged areas include Patents, Trademarks, Intellectual Property, Government, and Federal.


  The USPTO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  USPTO''s developer surface includes authentication, developer portal, documentation, support, GitHub presence, engineering blog, and 20 more developer resources.'
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
  composite: 35.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 64.3
    catalog_earned_first_party: 0.0
    catalog_gap: 50.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 25.0
    contract_quality: 63.3
    developer_ergonomics: 33.3
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 35.4
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
