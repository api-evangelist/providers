---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ecfr Agentic Access
  operation_count: 15
  slug: ecfr-agentic-access
  summary_line: 15 operations
api_count: 3
apis:
- description: Access eCFR metadata through JSON
  name: eCFR Admin Service API
  slug: ecfr-admin-service-api
- description: Historical search of the eCFR
  name: eCFR Search Service API
  slug: ecfr-search-service-api
- description: Access CFR content and structure files through JSON and XML
  name: eCFR Versioner Service API
  slug: ecfr-versioner-service-api
artifact_total: 22
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ecfr-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ecfr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ecfr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ecfr.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.ecfr.gov/developers/documentation/api/v1
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/usgpo
- group: company
  title: ''
  type: Blog
  url: https://www.federalregister.gov/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ecfr.gov/developers
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/plans/ecfr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/rate-limits/ecfr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/finops/ecfr-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/openapi/ecfr-openapi.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/json-schema/agency.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/json-schema/cfr-title.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/json-schema/search-result.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/json-schema/content-version.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/json-schema/correction.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/json-schema/cfr-ancestor.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/vocabulary/ecfr-vocabulary.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/json-ld/ecfr-context.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/examples/titles-response.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/examples/agencies-response.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/examples/search-results-response.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/examples/ancestry-response.json
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/examples/versions-response.json
created: '2026-06-13'
description: Electronic Code of Federal Regulations REST API for accessing the official US Code of Federal Regulations, searching regulations, and retrieving regulatory version history.
examples:
- key_count: 1
  name: Agencies Response
  slug: agencies-response
- key_count: 1
  name: Ancestry Response
  slug: ancestry-response
- key_count: 2
  name: Search Results Response
  slug: search-results-response
- key_count: 2
  name: Titles Response
  slug: titles-response
- key_count: 2
  name: Versions Response
  slug: versions-response
finops:
- name: Ecfr Finops
  service_category: ''
  slug: ecfr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ecfr.png
json_schemas:
- name: AgenciesResponse
  property_count: 1
  slug: agencies-response
- name: Agency
  property_count: 7
  slug: agency
- name: CfrAncestor
  property_count: 6
  slug: cfr-ancestor
- name: CfrTitle
  property_count: 6
  slug: cfr-title
- name: ContentVersion
  property_count: 10
  slug: content-version
- name: EcfrCorrection
  property_count: 13
  slug: correction
- name: SearchResult
  property_count: 12
  slug: search-result
layout: provider
modified: '2026-06-13'
name: eCFR
nav: Providers
network: true
overview: 'eCFR publishes 3 APIs on the [APIs.io](https://apis.io/) network: Admin Service API, Search Service API, and Versioner Service API. Tagged areas include Federal Regulations, Government, Legal, Compliance, and Open Data.


  The eCFR catalog on APIs.io includes 1 Spectral governance ruleset.


  eCFR''s developer surface includes documentation, engineering blog, pricing, code examples, and 21 more developer resources.'
plans:
- name: Ecfr Plans Pricing
  plan_count: 1
  slug: ecfr-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Ecfr Rate Limits
  slug: ecfr-rate-limits
rules:
- name: eCFR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ecfr-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.6
  delta: -5.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ecfr/refs/heads/main/screenshots/ecfr-2026-07-25T212731.png
security:
- kind: domain-security
  name: Ecfr Domain Security
  slug: ecfr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ecfr Vulnerability Disclosure
  slug: ecfr-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ecfr
tags:
- Federal Regulations
- Government
- Legal
- Compliance
- Open Data
- United States
website: https://www.ecfr.gov
---
