---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bls Gov Agentic Access
  operation_count: 5
  slug: bls-gov-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: Retrieve the most popular BLS series identifiers
  name: Bureau of Labor Statistics Popular Series API
  slug: bls-gov-popular-series-api
- description: Discover and list available BLS surveys
  name: Bureau of Labor Statistics Surveys API
  slug: bls-gov-surveys-api
- description: Retrieve time series data for BLS statistical series
  name: Bureau of Labor Statistics Time Series API
  slug: bls-gov-time-series-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BLS Public Data Popular Series API
  slug: open-bls-gov-popular-series-api
- collection_type: open
  name: BLS Public Data Popular Series Surveys API
  slug: open-bls-gov-surveys-api
- collection_type: open
  name: BLS Public Data Popular Series Time Series API
  slug: open-bls-gov-time-series-api
- collection_type: open
  name: BLS Public Data API
  slug: open-bls-public-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bls-gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bls-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bls-gov-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bls.gov/
- group: other
  title: ''
  type: Developer
  url: https://www.bls.gov/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bls.gov/developers/home.htm
- group: other
  title: ''
  type: Registration
  url: https://data.bls.gov/registrationEngine/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bls.gov/developers/termsOfService.htm
- group: operate
  title: ''
  type: ContactUs
  url: https://www.bls.gov/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bureau-of-labor-statistics
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/BLS_gov
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/BLSgov
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/blsgov
created: '2026-05-25'
description: The U.S. Bureau of Labor Statistics (BLS) is the principal federal statistical agency responsible for measuring labor market activity, working conditions, price changes, and productivity in the U.S. economy. BLS operates the Public Data API at api.bls.gov, providing programmatic JSON access to published historical time series across more than 75 surveys — including the Consumer Price Index (CPI), Producer Price Index (PPI), Employment Situation (CES), Local Area Unemployment Statistics (LAUS), Quarterly Census of Employment and Wages (QCEW), Occupational Employment and Wage Statistics (OEWS), Employment Cost Index (ECI), Productivity, Import/Export Price Indexes, and Census of Fatal Occupational Injuries (CFOI). Version 1 is open without registration; Version 2 requires a free registration key and provides higher daily limits, more series per request, longer year ranges, catalog metadata, statistical calculations, and annual averages.
examples:
- key_count: 2
  name: Bls Get Unemployment Rate Example
  slug: bls-get-unemployment-rate-example
- key_count: 2
  name: Bls List Surveys Example
  slug: bls-list-surveys-example
finops:
- name: Bls Gov Finops
  service_category: API
  slug: bls-gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bls-gov.png
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
  name: Bls Gov Context
  property_count: 30
  slug: bls-gov-context
layout: provider
modified: '2026-05-25'
name: Bureau of Labor Statistics
nav: Providers
network: true
overview: 'Bureau of Labor Statistics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Popular Series API, Surveys API, and Time Series API. Tagged areas include Federal-Government, Labor Statistics, Economic Data, Consumer Price Index, and Producer Price Index.


  The Bureau of Labor Statistics catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bureau of Labor Statistics'' developer surface includes authentication, documentation, YouTube channel, and 10 more developer resources.'
plans:
- name: Bls Gov Plans Pricing
  plan_count: 3
  slug: bls-gov-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Bls Gov Rate Limits
  slug: bls-gov-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Bureau of Labor Statistics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: bls-gov-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Bureau of Labor Statistics API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 5
  slug: bls-public-data-api-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 16
    catalog_gap: 46.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 68.5
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 45.1
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bls-gov/refs/heads/main/screenshots/bls-gov-2026-06-20T173524.png
security:
- kind: authentication
  name: Bls Gov Authentication
  slug: bls-gov-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bls Gov Domain Security
  slug: bls-gov-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bls-gov
tags:
- Federal-Government
- Labor Statistics
- Economic Data
- Consumer Price Index
- Producer Price Index
- Employment
- Unemployment
- Wages
- Productivity
- Open Data
- Time Series
website: https://www.bls.gov/
---
