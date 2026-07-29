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
api_count: 3
apis:
- description: The core big xyt (xyt hub) API gives trading firms and exchanges programmatic access to normalised and raw tick data and analytics across 120+ venues without in-house tick data infrastructure. Publicl
  name: big xyt API
  slug: big-xyt-api
- description: API access to the Liquidity Cockpit, big xyt's dark and lit liquidity, market share, and market quality analytics for navigating fragmented equity market structure. Publicly named on the xythub.github
  name: Liquidity Cockpit API
  slug: liquidity-cockpit-api
- description: Execution analytics API spanning basic Transaction Cost Analysis - benchmarking trades and orders for best execution, compliance, and client reporting - through full API access to quantitative modelli
  name: TCA API
  slug: tca-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/big-xyt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/big-xyt-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/big-xyt-llms.txt
- group: start
  title: ''
  type: Login
  url: https://platform.xyt.one/
- group: company
  title: ''
  type: Website
  url: https://xyt.one/
- group: start
  title: ''
  type: Portal
  url: https://xythub.github.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.big-xyt.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xythub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/big-xyt/
- group: company
  title: ''
  type: Blog
  url: https://xyt.one/insights
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xyt.one/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://xythub.github.io/support.html
created: '2026-07-21'
description: big xyt AG (now branded simply xyt, with big-xyt.com redirecting to xyt.one) is an independent, majority employee-owned market data analytics firm headquartered in Frankfurt am Main, Germany. It sells tick-data-driven market intelligence covering equities, ETFs, listed derivatives, FX, and fixed income across 120+ venues, processing 12bn+ messages per day with roughly ten years of history at nanosecond precision and market-by-order granularity. Products include the Liquidity Cockpit (market share and liquidity analytics), Transaction Cost Analysis against its SMART benchmark, pre-trade cost modeling, a Datashop of analysis-ready datasets and APIs, and an xyt AI natural-language query layer. Three API products are publicly named - the big xyt API, Liquidity Cockpit API, and TCA API - but their reference documentation sits behind a login at docs.big-xyt.com (HTTP 403 unauthenticated), and access is sales-gated via a book-a-demo motion with no self-serve signup, public pricing,
  or public OpenAPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/big-xyt.png
layout: provider
modified: '2026-07-22'
name: big xyt
nav: Providers
network: true
overview: 'big xyt publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Tick Data, Trading, and Analytics.


  big xyt''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 7 more developer resources.'
random_paper: 68
score:
  band: emerging
  composite: 21.6
  delta: -1.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 83.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/big-xyt/refs/heads/main/screenshots/big-xyt-2026-07-22T202227.png
security:
- kind: authentication
  name: Big Xyt Authentication
  slug: big-xyt-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Big Xyt Domain Security
  slug: big-xyt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: big-xyt
tags:
- Financial
- Market Data
- Tick Data
- Trading
- Analytics
- Equities
- ETFs
- Transaction Cost Analysis
- Liquidity
- Order Book
website: https://xyt.one/
---
