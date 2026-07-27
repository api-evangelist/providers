---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bis Agentic Access
  operation_count: 18
  slug: bis-agentic-access
  summary_line: 18 operations
api_count: 4
apis:
- description: The Data availability queries API from BIS — 1 operation(s) for data availability queries.
  name: BIS Data availability queries API
  slug: bis-data-availability-queries-api
- description: The Data queries API from BIS — 1 operation(s) for data queries.
  name: BIS Data queries API
  slug: bis-data-queries-api
- description: The Item queries API from BIS — 4 operation(s) for item queries.
  name: BIS Item queries API
  slug: bis-item-queries-api
- description: The Structure queries API from BIS — 12 operation(s) for structure queries.
  name: BIS Structure queries API
  slug: bis-structure-queries-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bis.org/
- group: docs
  title: ''
  type: Documentation
  url: https://stats.bis.org/api-doc/v1/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bis-org
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bis
- group: company
  title: ''
  type: Blog
  url: https://www.bis.org/rss/index.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bis.org/terms_statistics.htm
- group: operate
  title: ''
  type: StatusPage
  url: https://data.bis.org/
- group: other
  title: ''
  type: X
  url: https://twitter.com/BIS_org
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/bis/refs/heads/main/plans/bis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/bis/refs/heads/main/rate-limits/bis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/bis/refs/heads/main/finops/bis-finops.yml
created: '2026-06-13'
description: The Bank for International Settlements (BIS) provides a free SDMX RESTful API offering programmatic access to global financial statistics, international banking data, derivatives market statistics, property prices, exchange rates, and central bank research data. The API follows the SDMX REST v1.4.0 specification and supports JSON, XML, and CSV response formats with no authentication required.
examples:
- key_count: 4
  name: Get Availability Example
  slug: get-availability-example
- key_count: 4
  name: Get Data Example
  slug: get-data-example
- key_count: 4
  name: Get Dataflow Example
  slug: get-dataflow-example
finops:
- name: Bis Finops
  service_category: ''
  slug: bis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bis.png
json_schemas:
- name: BIS Stats API Schema
  property_count: 0
  slug: bis-stats-api
jsonld:
- class_count: 0
  name: Bis Stats Api Context
  property_count: 0
  slug: bis-stats-api
layout: provider
modified: '2026-06-13'
name: BIS
nav: Providers
network: true
overview: 'BIS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data availability queries API, Data queries API, Item queries API, and 1 more. Tagged areas include Financial Statistics, Banking Data, Derivatives, Exchange Rates, and Central Bank.


  The BIS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BIS''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Bis Plans Pricing
  plan_count: 1
  slug: bis-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 2
  name: Bis Rate Limits
  slug: bis-rate-limits
rules:
- name: BIS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bis-jsonschema-spectral-rules
score:
  band: thin
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 44.2
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 42.1
  previous_composite: 42.2
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bis/refs/heads/main/screenshots/bis-2026-06-20T173300.png
security:
- kind: domain-security
  name: Bis Domain Security
  slug: bis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bis
tags:
- Financial Statistics
- Banking Data
- Derivatives
- Exchange Rates
- Central Bank
- SDMX
- Open Data
- International Finance
website: https://www.bis.org/
---
