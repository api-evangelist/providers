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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ecfr Agentic Access
  operation_count: 15
  slug: ecfr-agentic-access
  summary_line: 15 operations
api_count: 1
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
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: eCFR API Documentation Admin Service API
  slug: open-ecfr-admin-service-api
- collection_type: open
  name: eCFR API Documentation Admin Service Search Service API
  slug: open-ecfr-search-service-api
- collection_type: open
  name: eCFR API Documentation Admin Service Versioner Service API
  slug: open-ecfr-versioner-service-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ecfr-capability-edges.yml
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


  eCFR''s developer surface includes documentation, engineering blog, pricing, code examples, and 22 more developer resources.'
plans:
- name: Ecfr Plans Pricing
  plan_count: 1
  slug: ecfr-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Ecfr Rate Limits
  slug: ecfr-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: eCFR API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ecfr-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 45.6
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
