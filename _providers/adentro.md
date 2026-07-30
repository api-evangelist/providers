---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adentro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adentro.com/
- group: operate
  title: ''
  type: Support
  url: https://support.adentro.com/s/
- group: docs
  title: ''
  type: Documentation
  url: https://support.adentro.com/s/
- group: commercial
  title: ''
  type: Pricing
  url: https://adentro.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://my.zenreach.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adentro.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adentro.com/terms/
- group: auth
  title: ''
  type: Authentication
  url: authentication/adentro-authentication.yml
created: '2026-07-17'
description: Adentro (formerly Zenreach) is a WiFi marketing and customer-intelligence platform that connects online marketing spend to real-world, in-store visits for brick-and-mortar businesses. Branded guest-WiFi portals capture and enrich first-party customer profiles, measure foot traffic and a "Walk-Through Rate" attribution metric, and power automated email and audience-targeting campaigns across roughly 100 million verified US consumer profiles. Adentro serves retail, food and beverage, venues and arenas, and entertainment and hospitality brands. It exposes a partner/customer-gated Contacts API and a Location & Scanning API (V2/V3) for syncing captured contacts, visits, and location data into CRMs and loyalty platforms such as Fishbowl and Alpine IQ; access is granted via an Adentro-issued token passed in the Authorization header rather than through a public self-serve developer portal.
image: https://adentro.com/wp-content/uploads/2024/06/adentro-logo.png
layout: provider
modified: '2026-07-17'
name: Adentro
nav: Providers
network: true
overview: 'Adentro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, WiFi Marketing, Customer Intelligence, and Location Analytics.


  Adentro''s developer surface includes support, documentation, pricing, authentication, and 5 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 18.7
  delta: -1.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adentro/refs/heads/main/screenshots/adentro-2026-07-25T181621.png
security:
- kind: authentication
  name: Adentro Authentication
  slug: adentro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adentro Domain Security
  slug: adentro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adentro
tags:
- Company
- Ai Apps
- WiFi Marketing
- Customer Intelligence
- Location Analytics
- Retail
- Marketing Attribution
- Guest WiFi
website: https://adentro.com/
---
