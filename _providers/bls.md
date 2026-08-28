---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bls Agentic Access
  operation_count: 5
  slug: bls-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- description: Retrieve the list of available BLS surveys
  name: Bureau of Labor Statistics Surveys API
  slug: bls-surveys-api
- description: Retrieve single or multiple time series data
  name: Bureau of Labor Statistics Time Series API
  slug: bls-time-series-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BLS Public Data Surveys API
  slug: open-bls-surveys-api
- collection_type: open
  name: BLS Public Data Surveys Time Series API
  slug: open-bls-time-series-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bls-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bls-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bls-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bls.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.bls.gov/developers/home.htm
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/topics/bureau-of-labor-statistics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-labor-statistics
- group: company
  title: ''
  type: Blog
  url: https://www.bls.gov/bls/news.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bls.gov/developers/home.htm
- group: operate
  title: ''
  type: StatusPage
  url: https://www.bls.gov/developers/api_faqs.htm
- group: other
  title: ''
  type: X
  url: https://x.com/BLS_gov
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/bls/refs/heads/main/vocabulary/bls-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/bls/refs/heads/main/json-ld/bls-context.jsonld
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
- group: commercial
  title: ''
  type: Plans
  url: plans/bls-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bls-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bls-finops.yml
created: '2026-06-12'
description: 'The Bureau of Labor Statistics (BLS) Public Data API provides developers programmatic access to the full catalog of official federal labor and economic statistics published by the U.S. Department of Labor. The API delivers historical time-series data spanning employment, unemployment rates, Consumer Price Index (CPI), Producer Price Index (PPI), wages and earnings, and productivity metrics drawn from major BLS surveys. Two versions are available: an unauthenticated Version 1.0 suitable for lightweight exploration and an enhanced Version 2.0 that requires free registration and returns richer results including catalog metadata, statistical calculations, and annual averages. Responses are served in JSON format, and the API is freely available to the public with no cost for access.'
examples:
- key_count: 7
  name: Bls Multi Series V2 Request
  slug: bls-multi-series-v2-request
- key_count: 4
  name: Bls Multi Series V2 Response
  slug: bls-multi-series-v2-response
- key_count: 3
  name: Bls Unemployment Rate Request
  slug: bls-unemployment-rate-request
- key_count: 4
  name: Bls Unemployment Rate Response
  slug: bls-unemployment-rate-response
finops:
- name: Bls Finops
  service_category: ''
  slug: bls-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bls.png
json_schemas:
- name: BLS Time Series Data Request
  property_count: 8
  slug: bls-time-series-request
- name: BLS Time Series Data Response
  property_count: 4
  slug: bls-time-series-response
jsonld:
- class_count: 6
  name: Bls Context
  property_count: 32
  slug: bls-context
layout: provider
modified: '2026-06-12'
name: Bureau of Labor Statistics
nav: Providers
network: true
overview: 'Bureau of Labor Statistics publishes 2 APIs on the [APIs.io](https://apis.io/) network: Surveys API and Time Series API. Tagged areas include Bureau of Labor Statistics, BLS, Employment, Unemployment, and CPI.


  The Bureau of Labor Statistics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bureau of Labor Statistics'' developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Bls Plans Pricing
  plan_count: 2
  slug: bls-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Bls Rate Limits
  slug: bls-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Bureau of Labor Statistics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: bls-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.7
  delta: 2.7
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 25.0
    contract_quality: 66.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bls/refs/heads/main/screenshots/bls-2026-06-20T173523.png
security:
- kind: authentication
  name: Bls Authentication
  slug: bls-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bls Domain Security
  slug: bls-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bls
tags:
- Bureau of Labor Statistics
- BLS
- Employment
- Unemployment
- CPI
- Consumer Price Index
- PPI
- Producer Price Index
- Wages
- Labor Statistics
- Economic Indicators
- Federal-Government
- Open Data
website: https://www.bls.gov
---
