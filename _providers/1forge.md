---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: 1Forge Agentic Access
  operation_count: 5
  slug: 1forge-agentic-access
  summary_line: 5 operations
api_count: 6
apis:
- description: WebSocket stream that delivers real-time bid/ask updates for subscribed forex and cryptocurrency pairs. Streaming is gated to paid plans.
  name: 1Forge Forex Stream
  slug: 1forge-forex-stream
- description: Convert a quantity from one currency into another at the current rate.
  name: 1Forge Convert API
  slug: 1forge-convert-api
- description: Check whether the forex market is currently open.
  name: 1Forge Market Status API
  slug: 1forge-market-status-api
- description: Inspect API key consumption and remaining quota.
  name: 1Forge Quota API
  slug: 1forge-quota-api
- description: Real-time bid/ask quote data for forex and cryptocurrency pairs.
  name: 1Forge Quotes API
  slug: 1forge-quotes-api
- description: Discover the currency pairs available to the calling API key.
  name: 1Forge Symbols API
  slug: 1forge-symbols-api
artifact_total: 36
asyncapis:
- description: '1Forge streams real-time forex and cryptocurrency price updates over a single WebSocket connection at `wss://sockets.1forge.com/socket`. Messages are pipe-delimited text frames: `{action}|{body}`, whe'
  name: 1Forge Forex Stream API
  slug: 1forge-forex-stream-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 1Forge Forex Data Convert API
  slug: open-1forge-convert-api
- collection_type: open
  name: 1Forge Forex Data API
  slug: open-1forge-forex-data-api
- collection_type: open
  name: 1Forge Forex Data Convert Market Status API
  slug: open-1forge-market-status-api
- collection_type: open
  name: 1Forge Forex Data Convert Quota API
  slug: open-1forge-quota-api
- collection_type: open
  name: 1Forge Forex Data Convert Quotes API
  slug: open-1forge-quotes-api
- collection_type: open
  name: 1Forge Forex Data Convert Symbols API
  slug: open-1forge-symbols-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1forge-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1forge-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/1forge-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://1forge.com
- group: docs
  title: ''
  type: Documentation
  url: https://1forge.com/forex-data-api/api-documentation
- group: start
  title: ''
  type: Signup
  url: https://1forge.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://1forge.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1forge.com/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1Forge
- group: commercial
  title: ''
  type: Plans
  url: plans/1forge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1forge-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/1forge-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/1forge-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/1forge-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/1forge-forex-data-api-context.jsonld
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: 1Forge delivers real-time forex and cryptocurrency quotes for 700+ currency pairs through a simple JSON REST API and a low-latency WebSocket stream. The product targets trading apps, multi-currency checkout flows, treasury and FinOps tooling, and any workload that needs FIX-speed price data without the FIX-grade integration cost.
examples:
- key_count: 3
  name: Forex Data Api Conversion Result Example
  slug: forex-data-api-conversion-result-example
- key_count: 1
  name: Forex Data Api Market Status Example
  slug: forex-data-api-market-status-example
- key_count: 4
  name: Forex Data Api Quota Example
  slug: forex-data-api-quota-example
- key_count: 5
  name: Forex Data Api Quote Example
  slug: forex-data-api-quote-example
finops:
- name: 1Forge Finops
  service_category: Market Data
  slug: 1forge-finops
image: https://1forge.com/assets/images/f-blue.svg
json_schemas:
- name: ConversionResult
  property_count: 3
  slug: forex-data-api-conversion-result
- name: MarketStatus
  property_count: 1
  slug: forex-data-api-market-status
- name: Quota
  property_count: 4
  slug: forex-data-api-quota
- name: Quote
  property_count: 5
  slug: forex-data-api-quote
json_structures:
- name: Forex Data Api Conversion Result Structure
  property_count: 3
  slug: forex-data-api-conversion-result-structure
- name: Forex Data Api Market Status Structure
  property_count: 1
  slug: forex-data-api-market-status-structure
- name: Forex Data Api Quota Structure
  property_count: 4
  slug: forex-data-api-quota-structure
- name: Forex Data Api Quote Structure
  property_count: 5
  slug: forex-data-api-quote-structure
jsonld:
- class_count: 4
  name: 1Forge Forex Data Api Context
  property_count: 12
  slug: 1forge-forex-data-api-context
layout: provider
modified: '2026-05-28'
name: 1Forge
nav: Providers
network: true
overview: '1Forge publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Forex Stream, Convert API, Market Status API, and 3 more. Tagged areas include Currency Exchange, Forex, Cryptocurrency, Market Data, and Financial Data.


  The 1Forge catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  1Forge''s developer surface includes authentication, documentation, signup flow, pricing, and 12 more developer resources.'
plans:
- name: 1Forge Plans Pricing
  plan_count: 4
  slug: 1forge-plans-pricing
random_paper: 133
rate_limits:
- limit_count: 2
  name: 1Forge Rate Limits
  slug: 1forge-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: 1Forge API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: 1forge-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: 1Forge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: 1forge-jsonschema-spectral-rules
- effective_rule_count: 74
  extends:
  - spectral:oas
  name: 1Forge API Rules
  rule_count: 33
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 18
  slug: 1forge-rules
score:
  band: thin
  composite: 35.5
  delta: -9.2
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 26.5
    contract_quality: 30.7
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 26.5
    operational_transparency: 23.7
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/1forge/refs/heads/main/screenshots/1forge-2026-06-20T162445.png
security:
- kind: authentication
  name: 1Forge Authentication
  slug: 1forge-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: 1Forge Domain Security
  slug: 1forge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 1forge
tags:
- Currency Exchange
- Forex
- Cryptocurrency
- Market Data
- Financial Data
- Real-Time Data
website: https://1forge.com
---
