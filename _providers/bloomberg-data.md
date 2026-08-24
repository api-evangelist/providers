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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: Provides access to Bloomberg's extensive financial data including real-time quotes, historical data, reference data, and analytics.
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: Real-time streaming market data API delivering quotes, trades, and market depth.
  name: Bloomberg B-PIPE API
  slug: bloomberg-b-pipe-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-data-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-data-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bloomberg.com/professional/support/api-library/
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
description: Bloomberg provides financial, software, data, and media services. Their APIs offer access to real-time and historical market data, analytics, and financial information.
finops:
- name: Bloomberg Data Finops
  service_category: API
  slug: bloomberg-data-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-data.png
layout: provider
modified: '2026-03-16'
name: Bloomberg Data
nav: Providers
network: true
overview: 'Bloomberg Data publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Financial-Services, Market Data, News, and Real-Time Data.


  Bloomberg Data''s developer surface includes developer portal, documentation, support, and 4 more developer resources.'
plans:
- name: Bloomberg Data Plans Pricing
  plan_count: 3
  slug: bloomberg-data-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Bloomberg Data Rate Limits
  slug: bloomberg-data-rate-limits
score:
  band: emerging
  composite: 19.4
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-data/refs/heads/main/screenshots/bloomberg-data-2026-06-20T173410.png
security:
- kind: domain-security
  name: Bloomberg Data Domain Security
  slug: bloomberg-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Data Vulnerability Disclosure
  slug: bloomberg-data-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-data
tags:
- Analytics
- Financial-Services
- Market Data
- News
- Real-Time Data
- Trading
website: https://developer.bloomberg.com/
---
