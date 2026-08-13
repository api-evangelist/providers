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
api_count: 1
apis:
- description: 'Calypso Workstation is the end-user desktop application for the Nasdaq Calypso platform. It delivers real-time market data, trade entry, order management, risk monitoring, P&L, scenario analysis, and '
  name: Calypso Workstation
  slug: calypso-workstation
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calypso-workstation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.calypso.com/
- group: start
  title: ''
  type: Portal
  url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calypso.com/Privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://km.calypso.com/pages/terms
- group: learn
  title: ''
  type: Learning
  url: https://learncalypso.nasdaq.com/
created: '2024-01-15'
description: Nasdaq Calypso Workstation is the user-facing desktop component of the Nasdaq Calypso (formerly Adenza / Calypso Technology) capital markets platform. It gives capital markets professionals access to market data, trading operations, risk management, and portfolio analytics across asset classes. The Workstation is an integrated client application rather than a publicly documented REST API; programmatic integration is delivered through the broader Calypso platform interfaces used by banks, asset managers, central banks, and clearing houses.
finops:
- name: Calypso Workstation Finops
  service_category: API
  slug: calypso-workstation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/calypso-workstation.png
layout: provider
modified: '2026-04-23'
name: Calypso Workstation
nav: Providers
network: true
overview: 'Calypso Workstation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Capital Markets, Financial Technology, Market Data, Portfolio Management, and Risk Management.


  Calypso Workstation''s developer surface includes developer portal and 5 more developer resources.'
plans:
- name: Calypso Workstation Plans Pricing
  plan_count: 3
  slug: calypso-workstation-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 5
  name: Calypso Workstation Rate Limits
  slug: calypso-workstation-rate-limits
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 18.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calypso-workstation/refs/heads/main/screenshots/calypso-workstation-2026-06-20T173905.png
security:
- kind: domain-security
  name: Calypso Workstation Domain Security
  slug: calypso-workstation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calypso-workstation
tags:
- Capital Markets
- Financial Technology
- Market Data
- Portfolio Management
- Risk Management
- Trading
website: https://www.calypso.com/
---
