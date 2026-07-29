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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Provides programmatic access to Bloomberg's extensive financial data including market data, reference data, historical data, and real-time information.
  name: Bloomberg Data API
  slug: bloomberg-data-api
- description: Subscription-based service providing bulk downloads of historical and reference data for quantitative analysis and research.
  name: Bloomberg Data License
  slug: bloomberg-data-license
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-data-sets-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-data-sets-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bloomberg.com/professional/support/api-library/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/privacy/
created: '2024-01-01'
description: Bloomberg provides comprehensive financial data, analytics, and news services through various APIs and data feeds, serving financial professionals worldwide.
finops:
- name: Bloomberg Data Sets Finops
  service_category: API
  slug: bloomberg-data-sets-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-data-sets.png
layout: provider
modified: '2026-03-16'
name: Bloomberg Data Sets
nav: Providers
network: true
overview: 'Bloomberg Data Sets publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Data Sets, Financial Services, and Market Data.


  Bloomberg Data Sets'' developer surface includes developer portal, support, getting-started guide, and 4 more developer resources.'
plans:
- name: Bloomberg Data Sets Plans Pricing
  plan_count: 3
  slug: bloomberg-data-sets-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Bloomberg Data Sets Rate Limits
  slug: bloomberg-data-sets-rate-limits
score:
  band: emerging
  composite: 27.8
  delta: -1.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 29.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-data-sets/refs/heads/main/screenshots/bloomberg-data-sets-2026-06-20T173438.png
security:
- kind: domain-security
  name: Bloomberg Data Sets Domain Security
  slug: bloomberg-data-sets-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Data Sets Vulnerability Disclosure
  slug: bloomberg-data-sets-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-data-sets
tags:
- Analytics
- Data Sets
- Financial Services
- Market Data
website: https://www.bloomberg.com/professional/
---
