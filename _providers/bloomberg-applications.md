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
api_count: 2
apis:
- description: Provides programmatic access to Bloomberg's financial market data including real-time and historical pricing, reference data, and analytics.
  name: Bloomberg Data API
  slug: bloomberg-data-api
- description: Desktop API for accessing Bloomberg Terminal functionality programmatically through Excel, custom applications, and third-party systems.
  name: Bloomberg Terminal Connect API
  slug: bloomberg-terminal-connect-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-applications-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-applications-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bloomberg.com/professional/support/api-library/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Collection of Bloomberg's financial data and application APIs for accessing market data, terminal connectivity, real-time streaming feeds, and server-side data access.
finops:
- name: Bloomberg Applications Finops
  service_category: API
  slug: bloomberg-applications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-applications.png
layout: provider
modified: '2026-03-16'
name: Bloomberg Applications
nav: Providers
network: true
overview: 'Bloomberg Applications publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise API, Financial Analytics, Financial Services, Market Data, and Real-Time Data.


  Bloomberg Applications'' developer surface includes developer portal, getting-started guide, support, and 4 more developer resources.'
plans:
- name: Bloomberg Applications Plans Pricing
  plan_count: 3
  slug: bloomberg-applications-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 5
  name: Bloomberg Applications Rate Limits
  slug: bloomberg-applications-rate-limits
score:
  band: emerging
  composite: 21.9
  delta: -6.7
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-applications/refs/heads/main/screenshots/bloomberg-applications-2026-06-20T173410.png
security:
- kind: domain-security
  name: Bloomberg Applications Domain Security
  slug: bloomberg-applications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Applications Vulnerability Disclosure
  slug: bloomberg-applications-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-applications
tags:
- Enterprise API
- Financial Analytics
- Financial Services
- Market Data
- Real-Time Data
website: https://developer.bloomberg.com/
---
