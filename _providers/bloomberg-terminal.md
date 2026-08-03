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
  scored_at: '2026-08-03'
api_count: 4
apis:
- description: The Bloomberg Open API (BLPAPI) enables programmatic access to Bloomberg Terminal data from applications running on the same machine or connecting via Bloomberg's network. Provides real-time data subs
  name: Bloomberg Open API (BLPAPI)
  slug: blpapi
- description: Extends Bloomberg Terminal functionality into Microsoft Excel with BDP, BDH, BDS, and BQL formula functions for retrieving real-time, historical, and reference data directly in spreadsheet cells.
  name: Bloomberg Excel Add-in
  slug: bloomberg-excel-addin
- description: Secure messaging platform built into the Bloomberg Terminal enabling real-time communication between financial professionals globally, with compliance archiving and monitoring capabilities.
  name: Bloomberg IB (Instant Bloomberg)
  slug: bloomberg-ib
- description: Electronic trading and order management system integrated in the Bloomberg Terminal for routing orders to brokers across equities, fixed income, FX, and derivatives with FIX connectivity and algorithm
  name: Bloomberg EMSX
  slug: bloomberg-emsx
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-terminal-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bloomberg.com/professional/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bloomberg.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bloomberg
- group: build
  title: Python SDK (blpapi)
  type: SDKs
  url: https://pypi.org/project/blpapi/
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/blpapi
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
description: The Bloomberg Terminal (Bloomberg Professional Service) is the flagship product of Bloomberg LP, providing financial professionals with real-time market data, news, analytics, trading capabilities, and secure messaging through a unified workstation. The Terminal connects over 325,000 subscribers globally and is the standard infrastructure for financial markets professionals. Developers can access Terminal data programmatically via the Bloomberg Open API (BLPAPI).
features:
- description: Streaming real-time prices and quotes across global markets.
  name: Real-Time Market Data
- description: Security attributes, identifiers, corporate actions, and fundamentals.
  name: Reference Data
- description: End-of-day and intraday historical data for all asset classes.
  name: Historical Data
- description: Bond pricing, yield calculations, risk analytics, and scenario analysis.
  name: Fixed Income Analytics
- description: Equity valuation, relative value, and quantitative screening tools.
  name: Equity Analytics
- description: Bloomberg News, analyst research, and Bloomberg Intelligence.
  name: News and Research
- description: Compliant secure messaging for the Bloomberg professional network.
  name: IB Messaging
- description: EMSX for order routing and execution across asset classes.
  name: Electronic Trading
- description: BDP, BDH, BDS formulas for Excel integration.
  name: Bloomberg Excel Add-in
- description: Mobile and remote access to Terminal capabilities.
  name: Bloomberg Anywhere
finops:
- name: Bloomberg Terminal Finops
  service_category: API
  slug: bloomberg-terminal-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-terminal.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Terminal
nav: Providers
network: true
overview: 'Bloomberg Terminal publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Terminal, Bloomberg Professional Service, Market Data, Financial Workstation, and Trading.


  Bloomberg Terminal''s developer surface includes developer portal, documentation, support, and 6 more developer resources.'
plans:
- name: Bloomberg Terminal Plans Pricing
  plan_count: 3
  slug: bloomberg-terminal-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 5
  name: Bloomberg Terminal Rate Limits
  slug: bloomberg-terminal-rate-limits
score:
  band: thin
  composite: 29.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-terminal/refs/heads/main/screenshots/bloomberg-terminal-2026-06-20T173517.png
security:
- kind: domain-security
  name: Bloomberg Terminal Domain Security
  slug: bloomberg-terminal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bloomberg-terminal
tags:
- Terminal
- Bloomberg Professional Service
- Market Data
- Financial Workstation
- Trading
- Analytics
- Bloomberg
use_cases:
- description: Track real-time price movements and market events across global markets.
  name: Market Monitoring
- description: Analyze bonds using Bloomberg's fixed income analytics functions.
  name: Fixed Income Research
- description: Screen, analyze, and value equities using Terminal data and functions.
  name: Equity Research
- description: Monitor FX rates and execute currency trades through EMSX.
  name: FX Trading
- description: Manage and analyze investment portfolios with Bloomberg data.
  name: Portfolio Management
- description: Build quantitative models and strategies using BLPAPI data access.
  name: Quantitative Development
website: https://www.bloomberg.com/professional/
---
