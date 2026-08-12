---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Access index constituent data, weights, analytics, total returns, and historical data for Bloomberg's family of fixed income, equity, and multi-asset indices via BLPAPI and Data License.
  name: Bloomberg Index Data API
  slug: index-data-api
- description: 'Access Bloomberg Commodity Index data including futures-based commodity index returns, constituent weights, and rebalancing data. BCOM is a broadly diversified index tracking commodity futures across '
  name: Bloomberg Commodity Index (BCOM)
  slug: commodity-index-api
- description: Access cryptocurrency index data from the Bloomberg Galaxy Crypto Index family, tracking the performance of the largest and most liquid cryptocurrencies.
  name: Bloomberg Galaxy Crypto Index
  slug: galaxy-crypto-index
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-indices-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/solution/indices/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Bloomberg Indices are a comprehensive family of fixed income, equity, commodity, and multi-asset benchmark indices used by institutional investors worldwide. The Bloomberg Global Aggregate Bond Index, US Aggregate Bond Index, and related indices serve as key benchmarks for fixed income markets. Bloomberg provides index data, analytics, and constituent information through its Terminal and data delivery platforms.
features:
- description: Global Aggregate, US Aggregate, Euro Aggregate, and other fixed income benchmarks.
  name: Fixed Income Indices
- description: Bloomberg equity indices across regions, sectors, and themes.
  name: Equity Indices
- description: Bloomberg Commodity Index (BCOM) and sub-indices for energy, metals, and agriculture.
  name: Commodity Indices
- description: Blended fixed income and equity indices for balanced portfolio benchmarking.
  name: Multi-Asset Indices
- description: Bloomberg Galaxy Crypto Index and cryptocurrency benchmark series.
  name: Crypto Indices
- description: Sustainability-screened index variants for ESG-oriented portfolios.
  name: ESG Indices
finops:
- name: Bloomberg Indices Finops
  service_category: API
  slug: bloomberg-indices-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-indices.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Indices
nav: Providers
network: true
overview: 'Bloomberg Indices publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Indices, Fixed Income, Equity, Commodities, and Benchmark.


  Bloomberg Indices'' developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Indices Plans Pricing
  plan_count: 3
  slug: bloomberg-indices-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 5
  name: Bloomberg Indices Rate Limits
  slug: bloomberg-indices-rate-limits
score:
  band: emerging
  composite: 19.2
  delta: -7.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-indices/refs/heads/main/screenshots/bloomberg-indices-2026-07-25T203402.png
security:
- kind: domain-security
  name: Bloomberg Indices Domain Security
  slug: bloomberg-indices-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-indices
tags:
- Indices
- Fixed Income
- Equity
- Commodities
- Benchmark
- Global Aggregate
- Bloomberg
use_cases:
- description: Replicate Bloomberg indices in ETFs and index funds.
  name: Passive Fund Management
- description: Compare active portfolio performance against Bloomberg benchmarks.
  name: Benchmark Attribution
- description: Use Bloomberg indices as underlying benchmarks for notes and structured products.
  name: Structured Product Design
- description: Measure portfolio risk relative to Bloomberg index benchmarks.
  name: Risk Measurement
website: https://www.bloomberg.com/professional/
---
