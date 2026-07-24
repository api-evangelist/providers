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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eurostat Agentic Access
  operation_count: 30
  slug: eurostat-agentic-access
  summary_line: 30 operations
api_count: 12
apis:
- description: The primary REST API for accessing Eurostat datasets in JSON-stat 2.0 format. Supports filtering by geography, time period, and any dataset dimension. Returns synchronous or asynchronous responses dep
  name: Eurostat Statistics API
  slug: eurostat-statistics-api
- description: SDMX 3.0-compliant web service providing access to Eurostat datasets, dataflows, data structure definitions, and codelists. Supports SDMX-ML 3.0 and 2.1, SDMX-CSV 2.0 and 1.0, TSV, and JSON-stat forma
  name: Eurostat SDMX 3.0 API
  slug: eurostat-sdmx-30-api
- description: Asynchronous dissemination API for large dataset extractions between 500,000 and 5,000,000 cells. Clients submit a request, receive a unique key, poll for status, and download results when available.
  name: Eurostat Asynchronous API
  slug: eurostat-asynchronous-api
- description: API for discovering all publicly available Eurostat datasets, browsing the navigation tree, and retrieving dataset metadata before querying.
  name: Eurostat Catalogue API
  slug: eurostat-catalogue-api
- description: asynchronous processing
  name: Eurostat Async API
  slug: eurostat-async-api
- description: The Catalogue queries API from Eurostat — 7 operation(s) for catalogue queries.
  name: Eurostat Catalogue queries API
  slug: eurostat-catalogue-queries-api
- description: The SDMX 2.1 Data queries API from Eurostat — 1 operation(s) for sdmx 2.1 data queries.
  name: Eurostat SDMX 2.1 Data queries API
  slug: eurostat-sdmx-2-1-data-queries-api
- description: The SDMX 2.1 Navigation Structure queries API from Eurostat — 2 operation(s) for sdmx 2.1 navigation structure queries.
  name: Eurostat SDMX 2.1 Navigation Structure queries API
  slug: eurostat-sdmx-2-1-navigation-structure-queries-api
- description: The SDMX 2.1 Structure queries API from Eurostat — 5 operation(s) for sdmx 2.1 structure queries.
  name: Eurostat SDMX 2.1 Structure queries API
  slug: eurostat-sdmx-2-1-structure-queries-api
- description: The SDMX 3.0 Data queries API from Eurostat — 2 operation(s) for sdmx 3.0 data queries.
  name: Eurostat SDMX 3.0 Data queries API
  slug: eurostat-sdmx-3-0-data-queries-api
- description: The SDMX 3.0 Structure queries API from Eurostat — 10 operation(s) for sdmx 3.0 structure queries.
  name: Eurostat SDMX 3.0 Structure queries API
  slug: eurostat-sdmx-3-0-structure-queries-api
- description: The Statistics data queries API from Eurostat — 1 operation(s) for statistics data queries.
  name: Eurostat Statistics data queries API
  slug: eurostat-statistics-data-queries-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eurostat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eurostat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ec.europa.eu/eurostat
- group: docs
  title: ''
  type: Documentation
  url: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/eurostat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/eurostat/
- group: company
  title: ''
  type: Blog
  url: https://ec.europa.eu/eurostat/news/news-articles
- group: commercial
  title: ''
  type: Pricing
  url: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-introduction
- group: operate
  title: ''
  type: StatusPage
  url: https://ec.europa.eu/eurostat/help/maintenance-information
- group: other
  title: ''
  type: X
  url: https://x.com/EU_Eurostat
- group: commercial
  title: ''
  type: Plans
  url: plans/eurostat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eurostat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eurostat-finops.yml
- group: operate
  title: ''
  type: FAQ
  url: https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-faq
created: '2026-06-13'
description: Eurostat is the statistical office of the European Union, providing free and open REST APIs for programmatic access to European statistical data covering demographics, economy, trade, agriculture, transport, environment, and dozens of other indicators across EU member states and regions.
examples:
- key_count: 3
  name: Eurostat Statistics Api Example
  slug: eurostat-statistics-api-example
finops:
- name: Eurostat Finops
  service_category: ''
  slug: eurostat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eurostat.png
json_schemas:
- name: Eurostat Data Query Parameters
  property_count: 6
  slug: eurostat-data-query
layout: provider
modified: '2026-06-13'
name: Eurostat
nav: Providers
network: true
overview: 'Eurostat publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Async API, Catalogue queries API, SDMX 2.1 Data queries API, and 5 more. Tagged areas include Statistics, European Union, Open Data, Demographics, and Economy.


  The Eurostat catalog on APIs.io includes 1 Spectral governance ruleset.


  Eurostat''s developer surface includes documentation, engineering blog, pricing, FAQ, and 10 more developer resources.'
plans:
- name: Eurostat Plans Pricing
  plan_count: 1
  slug: eurostat-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Eurostat Rate Limits
  slug: eurostat-rate-limits
rules:
- name: Eurostat API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: eurostat-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.8
  delta: -5.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 44.5
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 46.9
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/eurostat/refs/heads/main/screenshots/eurostat-2026-06-20T180900.png
security:
- kind: domain-security
  name: Eurostat Domain Security
  slug: eurostat-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: eurostat
tags:
- Statistics
- European Union
- Open Data
- Demographics
- Economy
- Trade
- Agriculture
- Transport
- Environment
- SDMX
website: https://ec.europa.eu/eurostat
---
