---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Coinpaprika Agentic Access
  operation_count: 5
  slug: coinpaprika-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: The coins API from CoinPaprika — 1 operation(s) for coins.
  name: CoinPaprika coins API
  slug: coinpaprika-coins-api
- description: The global API from CoinPaprika — 1 operation(s) for global.
  name: CoinPaprika global API
  slug: coinpaprika-global-api
- description: The search API from CoinPaprika — 1 operation(s) for search.
  name: CoinPaprika search API
  slug: coinpaprika-search-api
- description: The ticker API from CoinPaprika — 2 operation(s) for ticker.
  name: CoinPaprika ticker API
  slug: coinpaprika-ticker-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Coinpaprika coins API
  slug: open-coinpaprika-coins-api
- collection_type: open
  name: Coinpaprika coins global API
  slug: open-coinpaprika-global-api
- collection_type: open
  name: Coinpaprika coins search API
  slug: open-coinpaprika-search-api
- collection_type: open
  name: Coinpaprika coins ticker API
  slug: open-coinpaprika-ticker-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coinpaprika-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinpaprika-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinpaprika-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coinpaprika.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coinpaprika.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/coinpaprika
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coinpaprika/
- group: company
  title: ''
  type: Blog
  url: https://coinpaprika.com/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://coinpaprika.com/api/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinpaprika.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/coinpaprika
- group: commercial
  title: ''
  type: Plans
  url: plans/coinpaprika-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coinpaprika-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coinpaprika-finops.yml
created: '2026-06-13'
description: Free cryptocurrency data REST API providing coin information, exchanges, market data, OHLCV history, ICO data, and global market statistics for 2,000+ coins on the free tier and 59,000+ assets on paid plans.
examples:
- key_count: 6
  name: Coin
  slug: coin
- key_count: 5
  name: Global
  slug: global
- key_count: 5
  name: Search Results
  slug: search-results
- key_count: 15
  name: Tick
  slug: tick
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coinpaprika.png
json_schemas:
- name: Coin
  property_count: 6
  slug: coin
- name: Global
  property_count: 5
  slug: global
- name: SearchResults
  property_count: 5
  slug: search-results
- name: Tick
  property_count: 15
  slug: tick
layout: provider
modified: '2026-06-13'
name: CoinPaprika
nav: Providers
network: true
overview: 'CoinPaprika publishes 4 APIs on the [APIs.io](https://apis.io/) network, including coins API, global API, search API, and 1 more. Tagged areas include Cryptocurrency, Market Data, Finance, OHLCV, and Exchanges.


  The CoinPaprika catalog on APIs.io includes 1 Spectral governance ruleset.


  CoinPaprika''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 5
  extends: []
  name: CoinPaprika API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: coinpaprika-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.7
  delta: -6.7
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 9.8
    contract_quality: 40.6
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/coinpaprika/refs/heads/main/screenshots/coinpaprika-2026-06-20T174741.png
security:
- kind: domain-security
  name: Coinpaprika Domain Security
  slug: coinpaprika-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coinpaprika Vulnerability Disclosure
  slug: coinpaprika-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coinpaprika
tags:
- Cryptocurrency
- Market Data
- Finance
- OHLCV
- Exchanges
- Blockchain
website: https://coinpaprika.com/
---
