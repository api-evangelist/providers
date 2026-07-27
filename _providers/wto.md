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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The WTO flagship API providing programmatic access to a large number of statistical indicators related to WTO issues. Data covers merchandise trade and trade in services statistics (annual, quarterly,
  name: WTO Timeseries API
  slug: timeseries
- description: Provides programmatic access to WTO quantitative restrictions data, including member notifications, product-level restrictions, and QR listings. Enables retrieval of trade measure data by member econo
  name: WTO Quantitative Restrictions API
  slug: quantitative-restrictions
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wto.org/
- group: docs
  title: ''
  type: Documentation
  url: https://apiportal.wto.org/apis
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/wto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/world-trade-organization/
- group: company
  title: ''
  type: Blog
  url: https://www.wto.org/english/news_e/news_e.htm
- group: commercial
  title: ''
  type: Pricing
  url: https://apiportal.wto.org/products
- group: operate
  title: ''
  type: StatusPage
  url: https://apiportal.wto.org/
- group: other
  title: ''
  type: X
  url: https://twitter.com/WTO
- group: commercial
  title: ''
  type: Plans
  url: plans/wto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wto-finops.yml
created: '2026-06-13'
description: The World Trade Organization (WTO) provides a REST API for programmatic access to global trade statistics, tariff data, trade flows, quantitative restrictions, dispute settlement records, and trade policy notifications. The flagship Timeseries API covers merchandise trade and services statistics (annual, quarterly, monthly), market access indicators including bound, applied, and preferential tariffs, non-tariff measures, and other WTO-related indicators. API access requires a free API key obtained from the WTO API Developer Portal at apiportal.wto.org.
finops:
- name: Wto Finops
  service_category: Open Government Data / Trade Statistics
  slug: wto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wto.png
layout: provider
modified: '2026-06-13'
name: WTO
nav: Providers
network: true
overview: 'WTO publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include World Trade, Trade Statistics, Tariffs, Trade Flows, and Trade Policy.


  WTO''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Wto Plans Pricing
  plan_count: 1
  slug: wto-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Wto Rate Limits
  slug: wto-rate-limits
score:
  band: emerging
  composite: 23.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 23.0
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wto/refs/heads/main/screenshots/wto-2026-06-20T201642.png
security:
- kind: domain-security
  name: Wto Domain Security
  slug: wto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wto
tags:
- World Trade
- Trade Statistics
- Tariffs
- Trade Flows
- Trade Policy
- International Trade
- Global Trade
- Merchandise Trade
- Services Trade
- Market Access
- Non-Tariff Measures
- Quantitative Restrictions
- Dispute Settlement
- Trade Notifications
- Open Data
website: https://www.wto.org/
---
