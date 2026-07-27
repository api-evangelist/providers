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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Us Bureau Of Labor Statistics Agentic Access
  operation_count: 5
  slug: us-bureau-of-labor-statistics-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 3
apis:
- description: Retrieve the most popular BLS series identifiers
  name: US Bureau of Labor Statistics Popular Series API
  slug: us-bureau-of-labor-statistics-popular-series-api
- description: Discover and list available BLS surveys
  name: US Bureau of Labor Statistics Surveys API
  slug: us-bureau-of-labor-statistics-surveys-api
- description: Retrieve time series data for BLS statistical series
  name: US Bureau of Labor Statistics Time Series API
  slug: us-bureau-of-labor-statistics-time-series-api
artifact_total: 17
collections:
- collection_type: open
  name: BLS Public Data API
  slug: open-bls-public-data-api
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
overview: 'US Bureau of Labor Statistics publishes 3 APIs on the [APIs.io](https://apis.io/) network: Popular Series API, Surveys API, and Time Series API. Tagged areas include Federal Government, Labor Statistics, Economic Data, and Open Data.


  The US Bureau of Labor Statistics catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  US Bureau of Labor Statistics'' developer surface includes authentication and 3 more developer resources.'
plans:
- name: Us Bureau Of Labor Statistics Plans Pricing
  plan_count: 3
  slug: us-bureau-of-labor-statistics-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Us Bureau Of Labor Statistics Rate Limits
  slug: us-bureau-of-labor-statistics-rate-limits
rules:
- name: US Bureau of Labor Statistics API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 5
  slug: bls-public-data-api-rules
- name: US Bureau of Labor Statistics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: us-bureau-of-labor-statistics-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.5
  delta: 2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 67.0
    developer_ergonomics: 10.9
    discoverability: 87.5
    governance: 60.5
    operational_transparency: 31.6
  previous_composite: 42.7
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Federal Government
- Labor Statistics
- Economic Data
- Open Data
---
