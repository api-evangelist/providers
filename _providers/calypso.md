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
api_count: 8
apis:
- description: Main REST API for the Nasdaq Calypso platform. Provides programmatic access to remotely control calls to the Calypso platform from other software, enabling regulatory analytics, current limits usage q
  name: Calypso Core API
  slug: calypso-core-api
- description: Provides programmatic access to Calypso front office capabilities including real-time portfolio insights, instant order generation, pricing, live risk and P&L monitoring, trade entry, and scenario ana
  name: Calypso Front Office API
  slug: calypso-front-office-api
- description: Enables integration with Calypso middle office and trading risk capabilities including market risk, credit risk, clearing risk, and liquidity risk metrics. Supports VaR calculations, stress testing, b
  name: Calypso Middle Office and Trading Risk API
  slug: calypso-middle-office-trading-risk-api
- description: Provides access to Calypso treasury management capabilities for front-to-back treasury operations including cross-asset trading decisions, analytics, risk tools, real-time monitoring, and management o
  name: Calypso Treasury API
  slug: calypso-treasury-api
- description: Provides integration with Calypso collateral management, margin calculation, and securities financing capabilities. Supports management of exposures for cleared and uncleared trades, real-time collate
  name: Calypso Collateral, Margin and Securities Finance API
  slug: calypso-collateral-margin-securities-finance-api
- description: Provides access to Calypso integrated cross-asset OTC and exchange-traded derivatives clearing capabilities including trade connectivity, processing, collateral management and optimization, margin cal
  name: Calypso Clearing API
  slug: calypso-clearing-api
- description: Enables integration with Calypso back-office processing capabilities including trade comparison, netting, settlement, profitability analysis, corporate actions, accounting, and regulatory reporting. S
  name: Calypso Post-Trade Processing API
  slug: calypso-post-trade-processing-api
- description: 'Provides integration capabilities for central bank reserve management and monetary policy operations on the Calypso platform. Supports monitoring and managing debt and liquidity, regulating financial '
  name: Calypso Reserve and Monetary Policy Management API
  slug: calypso-reserve-monetary-policy-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/calypso-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso
- group: docs
  title: ''
  type: Documentation
  url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso
- group: company
  title: ''
  type: Website
  url: https://www.calypso.com/
- group: operate
  title: ''
  type: Support
  url: https://www.nasdaq.com/solutions/fintech/nasdaq-calypso/resources
- group: learn
  title: ''
  type: Learning
  url: https://learncalypso.nasdaq.com/
- group: auth
  title: ''
  type: Certification
  url: https://www.nasdaq.com/solutions/fintech/services/education-learning/nasdaq-calypso/certification
- group: learn
  title: ''
  type: Training
  url: https://www.nasdaq.com/solutions/fintech/services/education-learning/nasdaq-calypso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.calypso.com/Privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://km.calypso.com/pages/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/calypso-technology
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Adenza
created: '2024-01-01'
description: APIs and developer resources for Nasdaq Calypso (formerly Adenza / Calypso Technology), a cross-asset front-to-back capital markets technology platform for trading, risk management, collateral, treasury, processing, and accounting used by banks, asset managers, central banks, and clearing houses worldwide.
finops:
- name: Calypso Finops
  service_category: API
  slug: calypso-finops
image: https://www.calypso.com/favicon.ico
layout: provider
modified: '2026-04-23'
name: Calypso
nav: Providers
network: true
overview: 'Calypso publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Capital Markets, Collateral Management, Enterprise Software, Financial Technology, and Post-Trade Processing.


  Calypso''s developer surface includes developer portal, documentation, support, training material, and 8 more developer resources.'
plans:
- name: Calypso Plans Pricing
  plan_count: 3
  slug: calypso-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Calypso Rate Limits
  slug: calypso-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 22.1
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/calypso/refs/heads/main/screenshots/calypso-2026-06-20T173858.png
security:
- kind: domain-security
  name: Calypso Domain Security
  slug: calypso-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calypso
tags:
- Capital Markets
- Collateral Management
- Enterprise Software
- Financial Technology
- Post-Trade Processing
- Risk Management
- Trading
- Treasury
website: https://www.calypso.com/
---
