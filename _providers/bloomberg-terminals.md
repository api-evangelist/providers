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
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Bloomberg Open API provides programmatic access to data available in the Bloomberg Terminal including real-time prices, reference data, historical data, news, and analytics. SDKs for C++, Java, Py
  name: Bloomberg Open API (BLPAPI)
  slug: blpapi
- description: Remote access service extending Bloomberg Terminal functionality to any internet-connected device. Provides authentication and secure remote access to Terminal data, analytics, and messaging.
  name: Bloomberg Anywhere
  slug: bloomberg-anywhere-api
- description: Customizable Bloomberg Terminal display consisting of smaller panels for monitoring multiple securities, markets, and data streams simultaneously. Supports custom configurations for different workflow
  name: Bloomberg Launchpad
  slug: bloomberg-launchpad
artifact_total: 17
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bloomberg/blpapi-node/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bloomberg/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bloomberg/.github/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-terminals-domain-security.yml
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
description: Bloomberg Terminals (Bloomberg Professional Service) are financial software systems providing real-time financial market data, news, analytics, and trading capabilities to financial professionals worldwide. The Terminal offers access to over 35,000 different data types for financial instruments globally, integrated analytics, messaging, and the Bloomberg Open API (BLPAPI) for programmatic data access.
features:
- description: Live prices, quotes, and market data for 35,000+ data types globally.
  name: Real-Time Market Data
- description: Static and semi-static security attributes, corporate actions, and fundamentals.
  name: Reference Data
- description: Historical pricing, volume, and analytics data.
  name: Historical Data
- description: Fixed income, equity, and derivatives analytics functions.
  name: Bloomberg Analytics
- description: Secure messaging for the Bloomberg professional community.
  name: Bloomberg IB Messaging
- description: Remote and mobile access to Terminal capabilities.
  name: Bloomberg Anywhere
finops:
- name: Bloomberg Terminals Finops
  service_category: API
  slug: bloomberg-terminals-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-terminals.png
layout: provider
modified: '2026-04-21'
name: Bloomberg Terminals
nav: Providers
network: true
overview: 'Bloomberg Terminals publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Terminal, Bloomberg Professional, Market Data, Financial Data, and Trading.


  Bloomberg Terminals'' developer surface includes developer portal, documentation, support, and 9 more developer resources.'
plans:
- name: Bloomberg Terminals Plans Pricing
  plan_count: 3
  slug: bloomberg-terminals-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Bloomberg Terminals Rate Limits
  slug: bloomberg-terminals-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: -1.9
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 23.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-terminals/refs/heads/main/screenshots/bloomberg-terminals-2026-06-20T173520.png
security:
- kind: domain-security
  name: Bloomberg Terminals Domain Security
  slug: bloomberg-terminals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomberg-terminals
tags:
- Terminal
- Bloomberg Professional
- Market Data
- Financial Data
- Trading
- Analytics
- Bloomberg
use_cases:
- description: Monitor markets and execute trades using Terminal data and analytics.
  name: Trading
- description: Conduct fundamental and quantitative research using Bloomberg data.
  name: Research
- description: Monitor and manage portfolio risk using Terminal analytics.
  name: Risk Management
- description: Analyze bonds and credit using Bloomberg fixed income functions.
  name: Fixed Income Analysis
website: https://www.bloomberg.com/professional/
---
