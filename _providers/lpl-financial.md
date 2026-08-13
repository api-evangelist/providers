---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lpl-financial-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lpl-financial
- group: company
  title: ''
  type: Website
  url: https://www.lpl.com
- group: operate
  title: ''
  type: ContactForm
  url: https://www.lpl.com/contact-us.html
created: '2026-03-21'
description: LPL Financial is a leading retail investment advisory firm and the largest independent broker-dealer in the United States, providing technology, brokerage, and investment advisor services to financial advisors and institutions. LPL does not currently publish a public developer portal or open APIs; integrations are typically provided through the ClientWorks platform and partner programs available to affiliated advisors.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lpl-financial.png
layout: provider
modified: '2026-04-28'
name: LPL Financial
nav: Providers
network: true
overview: LPL Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Investment Advisory, Broker-Dealer, and Wealth Management.
random_paper: 106
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lpl-financial/refs/heads/main/screenshots/lpl-financial-2026-06-20T184736.png
security:
- kind: domain-security
  name: Lpl Financial Domain Security
  slug: lpl-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lpl-financial
tags:
- Financial Services
- Investment Advisory
- Broker-Dealer
- Wealth Management
website: https://www.lpl.com
---
