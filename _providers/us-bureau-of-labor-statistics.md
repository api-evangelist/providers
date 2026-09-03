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
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Us Bureau Of Labor Statistics Agentic Access
  operation_count: 5
  slug: us-bureau-of-labor-statistics-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.bls.gov/publicAPI/v2
  baseurl_source: declared
  description: Retrieve the most popular BLS series identifiers
  name: US Bureau of Labor Statistics Popular Series API
  slug: us-bureau-of-labor-statistics-popular-series-api
- baseURL: https://api.bls.gov/publicAPI/v2
  baseurl_source: declared
  description: Discover and list available BLS surveys
  name: US Bureau of Labor Statistics Surveys API
  slug: us-bureau-of-labor-statistics-surveys-api
- baseURL: https://api.bls.gov/publicAPI/v2
  baseurl_source: declared
  description: Retrieve time series data for BLS statistical series
  name: US Bureau of Labor Statistics Time Series API
  slug: us-bureau-of-labor-statistics-time-series-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BLS Public Data API
  slug: open-bls-public-data-api
- collection_type: open
  name: BLS Public Data Popular Series API
  slug: open-us-bureau-of-labor-statistics-popular-series-api
- collection_type: open
  name: BLS Public Data Popular Series Surveys API
  slug: open-us-bureau-of-labor-statistics-surveys-api
- collection_type: open
  name: BLS Public Data Popular Series Time Series API
  slug: open-us-bureau-of-labor-statistics-time-series-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-bureau-of-labor-statistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-bureau-of-labor-statistics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/us-bureau-of-labor-statistics-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-labor-statistics
created: '2025-02-09'
description: The US Bureau of Labor Statistics (BLS) is the principal federal agency responsible for measuring labor market activity, working conditions, price changes, and productivity in the US economy. BLS provides a Public Data API that enables developers to retrieve published historical time series data covering employment, unemployment, inflation, wages, productivity, and occupational statistics across all BLS programs. The API supports both unauthenticated access (v1) and registered access with higher limits (v2), returning data in JSON format for integration into applications, research tools, and economic dashboards.
examples:
- key_count: 2
  name: Bls Get Unemployment Rate Example
  slug: bls-get-unemployment-rate-example
- key_count: 2
  name: Bls List Surveys Example
  slug: bls-list-surveys-example
finops:
- name: Us Bureau Of Labor Statistics Finops
  service_category: API
  slug: us-bureau-of-labor-statistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-bureau-of-labor-statistics.png
json_schemas:
- name: BLS Time Series
  property_count: 4
  slug: bls-time-series
json_structures:
- name: Bls Time Series Structure
  property_count: 0
  slug: bls-time-series-structure
jsonld:
- class_count: 3
  name: Us Bureau Of Labor Statistics Context
  property_count: 30
  slug: us-bureau-of-labor-statistics-context
layout: provider
modified: '2026-05-19'
name: US Bureau of Labor Statistics
nav: Providers
network: true
overview: 'US Bureau of Labor Statistics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Popular Series API, Surveys API, and Time Series API. Tagged areas include Federal-Government, Labor Statistics, Economic Data, and Open Data.


  The US Bureau of Labor Statistics catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Bureau of Labor Statistics'' developer surface includes authentication and 3 more developer resources.'
plans:
- name: Us Bureau Of Labor Statistics Plans Pricing
  plan_count: 3
  slug: us-bureau-of-labor-statistics-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Us Bureau Of Labor Statistics Rate Limits
  slug: us-bureau-of-labor-statistics-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: US Bureau of Labor Statistics API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 5
  slug: bls-public-data-api-rules
- effective_rule_count: 6
  extends: []
  name: US Bureau of Labor Statistics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: us-bureau-of-labor-statistics-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 39.4
    contract_quality: 61.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 39.4
    operational_transparency: 7.9
  previous_composite: 41.9
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
    score: 38.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-bureau-of-labor-statistics/refs/heads/main/screenshots/us-bureau-of-labor-statistics-2026-06-20T200548.png
security:
- kind: authentication
  name: Us Bureau Of Labor Statistics Authentication
  slug: us-bureau-of-labor-statistics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Us Bureau Of Labor Statistics Domain Security
  slug: us-bureau-of-labor-statistics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: us-bureau-of-labor-statistics
tags:
- Federal-Government
- Labor Statistics
- Economic Data
- Open Data
---
