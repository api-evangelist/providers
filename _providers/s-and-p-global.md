---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: S And P Global Agentic Access
  operation_count: 8
  slug: s-and-p-global-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 7
apis:
- description: Comprehensive financial data API providing access to fundamental data, industry-specific and segment data, valuations and pricing, S&P Global Credit Ratings and Research, and reference and terms and c
  name: S&P Capital IQ Market Intelligence API
  slug: market-intelligence
- description: API providing programmatic access to the S&P Global Marketplace catalog of premium fundamental and alternative datasets. Enables discovery and integration of datasets available on the marketplace plat
  name: S&P Global Marketplace Catalog API
  slug: marketplace-catalog
- description: Token-based authentication
  name: S&P Global Authentication API
  slug: s-and-p-global-authentication-api
- description: Entity linking and resolution operations
  name: S&P Global Entity Resolution API
  slug: s-and-p-global-entity-resolution-api
- description: Real-time and historical commodity market prices
  name: S&P Global Market Data API
  slug: s-and-p-global-market-data-api
- description: Symbol and contract reference data
  name: S&P Global Reference Data API
  slug: s-and-p-global-reference-data-api
- description: Entity search and discovery
  name: S&P Global Search API
  slug: s-and-p-global-search-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: S&P Global Commodity Insights Authentication API
  slug: open-s-and-p-global-authentication-api
- collection_type: open
  name: S&P Global Commodity Insights API
  slug: open-s-and-p-global-commodity-insights
- collection_type: open
  name: S&P Global Commodity Insights Authentication Entity Resolution API
  slug: open-s-and-p-global-entity-resolution-api
- collection_type: open
  name: Kensho Link API
  slug: open-s-and-p-global-kensho-link
- collection_type: open
  name: S&P Global Commodity Insights Authentication Market Data API
  slug: open-s-and-p-global-market-data-api
- collection_type: open
  name: S&P Global Commodity Insights Authentication Reference Data API
  slug: open-s-and-p-global-reference-data-api
- collection_type: open
  name: S&P Global Commodity Insights Authentication Search API
  slug: open-s-and-p-global-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/s-and-p-global-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/s-and-p-global-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/s-and-p-global-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.spglobal.com
- group: other
  title: ''
  type: Developer
  url: https://developer.spglobal.com/
- group: other
  title: ''
  type: Marketplace
  url: https://www.marketplace.spglobal.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.spglobal.com/commodityinsights/api/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.spglobal.com/commodityinsights/api/getting-started?tab=authentication
- group: company
  title: ''
  type: Blog
  url: https://www.spglobal.com/en/research-insights/articles
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spglobal/
- group: other
  title: ''
  type: X
  url: https://twitter.com/SPGlobal
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marketplace.spglobal.com/en/solutions/api-solutions-(61953ac7-ea64-4fac-926a-feb7f846c2be)
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/spgci/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.spglobal.com/llms.txt
created: '2026-03-21'
description: S&P Global is a leading provider of credit ratings, benchmarks, analytics, and workflow solutions in the global capital, commodity, and automotive markets. Through its divisions — S&P Global Market Intelligence, S&P Global Ratings, S&P Global Commodity Insights, S&P Global Mobility, and S&P Dow Jones Indices — the company delivers data, analytics, and decisioning capabilities to financial institutions, corporations, governments, and individuals worldwide. S&P Global APIs enable programmatic access to financial data, market prices, energy market data, credit ratings, and geospatial intelligence.
examples:
- key_count: 2
  name: S And P Global Get Current Market Data Example
  slug: s-and-p-global-get-current-market-data-example
- key_count: 2
  name: S And P Global Link Entity Example
  slug: s-and-p-global-link-entity-example
finops:
- name: S And P Global Finops
  service_category: Financial Data / Capital Markets
  slug: s-and-p-global-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/s-and-p-global.png
json_schemas:
- name: S&P Global Commodity Market Data Point
  property_count: 7
  slug: s-and-p-global-market-data-point
json_structures:
- name: S And P Global Market Data Structure
  property_count: 0
  slug: s-and-p-global-market-data-structure
jsonld:
- class_count: 2
  name: S And P Global Context
  property_count: 8
  slug: s-and-p-global-context
layout: provider
modified: '2026-05-19'
name: S&P Global
nav: Providers
network: true
overview: 'S&P Global publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Entity Resolution API, Market Data API, and 2 more. Tagged areas include Financial Data, Credit Ratings, Market Intelligence, Commodity Insights, and Energy Markets.


  The S&P Global catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  S&P Global''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: S And P Global Plans Pricing
  plan_count: 1
  slug: s-and-p-global-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 1
  name: S And P Global Rate Limits
  slug: s-and-p-global-rate-limits
rules:
- name: S&P Global API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: s-and-p-global-jsonschema-spectral-rules
- name: S&P Global API Rules
  rule_count: 14
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 10
  slug: s-and-p-global-spectral-rules
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 63.3
    developer_ergonomics: 28.3
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/s-and-p-global/refs/heads/main/screenshots/s-and-p-global-2026-06-20T193312.png
security:
- kind: authentication
  name: S And P Global Authentication
  slug: s-and-p-global-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: S And P Global Domain Security
  slug: s-and-p-global-domain-security
  summary_line: TLSv1.3 · DMARC
slug: s-and-p-global
tags:
- Financial Data
- Credit Ratings
- Market Intelligence
- Commodity Insights
- Energy Markets
- Capital Markets
- Fortune 500
website: https://www.spglobal.com
---
