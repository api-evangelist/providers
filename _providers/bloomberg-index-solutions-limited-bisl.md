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
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Access Bloomberg index constituent data, returns, analytics, and historical data for the Bloomberg Global Aggregate, US Aggregate, Euro Aggregate, and other benchmark indices via BLPAPI and Data Licen
  name: Bloomberg Index Data API
  slug: index-data-api
- description: License Bloomberg indices for use in ETFs, mutual funds, structured products, and other financial instruments. BISL provides benchmark administration services compliant with EU Benchmark Regulation (B
  name: Bloomberg Index Licensing
  slug: index-licensing
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-index-solutions-limited-bisl-domain-security.yml
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
description: Bloomberg Index Solutions Limited (BISL) is the entity that administers Bloomberg's fixed income and multi-asset indices, including the Bloomberg Global Aggregate Bond Index and other benchmark indices. BISL provides index data, calculations, and licensing for asset managers and financial institutions using Bloomberg indices as benchmarks or for financial product construction.
features:
- description: Daily constituent data including weights, yields, durations, and analytics.
  name: Index Constituents
- description: Daily, monthly, and historical total and excess returns for Bloomberg indices.
  name: Index Returns
- description: Duration, spread, yield, and risk analytics for fixed income indices.
  name: Index Analytics
- description: EU BMR-compliant benchmark administration and governance.
  name: Benchmark Administration
- description: Custom index design and calculation services for institutional clients.
  name: Custom Index Construction
finops:
- name: Bloomberg Index Solutions Limited Bisl Finops
  service_category: API
  slug: bloomberg-index-solutions-limited-bisl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-index-solutions-limited-bisl.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Index Solutions Limited (BISL)
nav: Providers
network: true
overview: 'Bloomberg Index Solutions Limited (BISL) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Index, Fixed Income, Benchmark, Multi-Asset, and Index Administration.


  Bloomberg Index Solutions Limited (BISL)''s developer surface includes developer portal, documentation, support, and 3 more developer resources.'
plans:
- name: Bloomberg Index Solutions Limited Bisl Plans Pricing
  plan_count: 3
  slug: bloomberg-index-solutions-limited-bisl-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Bloomberg Index Solutions Limited Bisl Rate Limits
  slug: bloomberg-index-solutions-limited-bisl-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 18.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-index-solutions-limited-bisl/refs/heads/main/screenshots/bloomberg-index-solutions-limited-bisl-2026-07-25T203402.png
security:
- kind: domain-security
  name: Bloomberg Index Solutions Limited Bisl Domain Security
  slug: bloomberg-index-solutions-limited-bisl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-index-solutions-limited-bisl
tags:
- Index
- Fixed Income
- Benchmark
- Multi-Asset
- Index Administration
- Bloomberg
use_cases:
- description: Compare portfolio performance against Bloomberg benchmark indices.
  name: Benchmark Comparison
- description: Replicate Bloomberg indices for passive investment products.
  name: ETF and Fund Replication
- description: Attribute portfolio risk relative to Bloomberg index benchmarks.
  name: Risk Attribution
- description: Use Bloomberg indices as underlying benchmarks for structured products.
  name: Product Structuring
website: https://www.bloomberg.com/professional/
---
