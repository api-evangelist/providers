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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Stooq Agentic Access
  operation_count: 1
  slug: stooq-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: The Q API from Stooq — 1 operation(s) for q.
  name: Stooq Q API
  slug: stooq-q-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stooq Historical Data Q API
  slug: open-stooq-q-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stooq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stooq-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://stooq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://stooq.com/db/h/
- group: other
  title: ''
  type: BulkData
  url: https://stooq.com/db/h/
- group: commercial
  title: ''
  type: Plans
  url: plans/stooq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stooq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stooq-finops.yml
created: '2026-06-13'
description: Stooq is a Poland-based financial data platform offering free access to historical and current market data for global equities, indices, currencies, cryptocurrencies, commodities, bonds, and economic indicators. Data is delivered as CSV via a simple REST-style URL interface at https://stooq.com/q/d/l/ using query parameters for ticker symbol, date range, and interval. As of early 2026 an API key (obtained via CAPTCHA on the site) is required. A known daily request quota applies; exceeding it returns an "Exceeded the daily hits limit" message. Bulk point-in-time snapshots of the full database (12,000+ securities) are also available as ZIP-compressed CSVs from https://stooq.com/db/h/.
examples:
- key_count: 4
  name: Stooq Apple Daily Ohlcv Example
  slug: stooq-apple-daily-ohlcv-example
- key_count: 4
  name: Stooq Bitcoin Weekly Ohlcv Example
  slug: stooq-bitcoin-weekly-ohlcv-example
- key_count: 4
  name: Stooq Quota Exceeded Example
  slug: stooq-quota-exceeded-example
finops:
- name: Stooq Finops
  service_category: Fintech
  slug: stooq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stooq.png
json_schemas:
- name: Stooq OHLCV Record
  property_count: 6
  slug: stooq-ohlcv-record
- name: Stooq Historical Data API Query Parameters
  property_count: 5
  slug: stooq-query-parameters
layout: provider
modified: '2026-06-13'
name: Stooq
nav: Providers
network: true
overview: 'Stooq publishes 1 API on the [APIs.io](https://apis.io/) network: Q API. Tagged areas include Fintech, Market Data, Stocks, Indices, and Currency.


  The Stooq catalog on APIs.io includes 1 Spectral governance ruleset.


  Stooq''s developer surface includes developer portal, documentation, and 6 more developer resources.'
plans:
- name: Stooq Plans Pricing
  plan_count: 1
  slug: stooq-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Stooq Rate Limits
  slug: stooq-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Stooq API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stooq-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 13
    catalog_gap: 40.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 63.3
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 21.1
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stooq/refs/heads/main/screenshots/stooq-2026-06-20T194600.png
security:
- kind: domain-security
  name: Stooq Domain Security
  slug: stooq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stooq
tags:
- Fintech
- Market Data
- Stocks
- Indices
- Currency
- Crypto
- Commodities
- Historical Data
- Free
website: https://stooq.com/
---
