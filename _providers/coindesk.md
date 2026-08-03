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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: CoinDesk's Bitcoin Price Index (BPI) in multiple currencies
  name: CoinDesk
  slug: coindesk
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coindesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://old.coindesk.com/coindesk-api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.coindesk.com/arc/outboundfeeds/rss/
created: '2026-05-28'
description: CoinDesk's Bitcoin Price Index (BPI) in multiple currencies
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coindesk.png
layout: provider
modified: '2026-05-28'
name: CoinDesk
nav: Providers
network: true
overview: 'CoinDesk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency and Public APIs.


  CoinDesk''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 88
score:
  band: minimal
  composite: 6.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coindesk/refs/heads/main/screenshots/coindesk-2026-07-25T210034.png
security:
- kind: domain-security
  name: Coindesk Domain Security
  slug: coindesk-domain-security
  summary_line: DMARC
slug: coindesk
tags:
- Cryptocurrency
- Public APIs
website: https://old.coindesk.com/coindesk-api/
---
