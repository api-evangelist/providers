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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 119
  human_in_the_loop: 119
  name: Dxfeed Agentic Access
  operation_count: 269
  slug: dxfeed-agentic-access
  summary_line: 269 operations · 119 acting · 119 human-in-the-loop
api_count: 6
apis:
- description: REST service over the core dxFeed API with /events (snapshot), /eventSource (Server-Sent Events stream), /addSubscription, and /removeSubscription resources across 20+ market event types (Quote, Trade
  name: dxFeed REST Web Service API
  slug: dxfeed-rest-api
- description: dxLink is dxFeed's WebSocket protocol for real-time market data streaming with multiplexed virtual channels, authorization, and FEED/DOM (order book) service channels. The protocol is publicly specifi
  name: dxFeed dxLink WebSocket API
  slug: dxfeed-dxlink-websocket-api
- description: Reference-data web service for requesting instrument profiles in dxFeed's Instrument Profile Format (IPF), including live incremental updates, covering the 3.5M instruments in the dxFeed symbology uni
  name: dxFeed Instrument Profile (IPF) Web Service
  slug: dxfeed-ipf-webservice
- description: Fundamental equity data sourced from Morningstar and Borsa Istanbul for ~45,000 companies - financial statements, valuations, dividends, earnings ratios, insider trading, corporate calendars - 28 data
  name: dxFeed Fundamentals API
  slug: dxfeed-fundamentals-api
- description: Industry-standard FIX protocol access to dxFeed market data for trading systems. Session endpoints and credentials are provisioned during onboarding; no public FIX gateway host is documented.
  name: dxFeed FIX API
  slug: dxfeed-fix-api
- description: Historical data access covering candle/aggregated data and raw tick data extraction (dxFeed stores up to 10TB of raw data per day). The knowledge base documents how to request tick data and read extra
  name: dxFeed Historical Data Services
  slug: dxfeed-historical-data-services
artifact_total: 12
asyncapis:
- description: '## Overview dxLink.WebSocket is a WebSocket-based protocol that allows you to receive market data from dxFeed services. ## Terminology - **Connection** - an instance of the WebSocket connection - **Cl'
  name: dxLink WebSocket
  slug: dxfeed-dxlink-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dxfeed-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/dxfeed-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dxfeed-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dxfeed-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dxfeed-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dxfeed-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dxfeed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dxfeed.com/trust-center/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dxfeed-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dxfeed-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dxfeed-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://kb.dxfeed.com/en/getting-started.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dxfeed.com/dxfeed/api/index.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/dxfeed-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dxfeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dxfeed.com/
- group: start
  title: ''
  type: Portal
  url: https://kb.dxfeed.com/en/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://kb.dxfeed.com/en/index-en.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dxFeed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dxfeed
- group: company
  title: ''
  type: Blog
  url: https://dxfeed.com/dxfeed-news/
- group: start
  title: ''
  type: SignUp
  url: https://get.dxfeed.com/
- group: operate
  title: ''
  type: Support
  url: https://dxfeed.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dxfeed.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dxfeed.com/privacy-policy/
created: '2026-07-21'
description: dxFeed is a market data distributor and subsidiary of Devexperts, headquartered in Munich, delivering real-time, delayed, historical, and on-demand financial market data across equities, ETFs, futures, options, indices, FX, fixed income, and crypto (3.5M instruments, ~200,000 simultaneous streaming clients), plus reference data (instrument profiles, corporate actions, trading schedules), Morningstar-sourced fundamentals, options analytics, and news feeds. Delivery is developer-documented but sales-gated - production credentials (endpoint URLs, login, password) arrive via onboarding after contacting sales - across a REST web service with Server-Sent Events streaming, the dxLink WebSocket protocol (public AsyncAPI spec and live demo endpoint), a binary QD protocol over TCP, FIX, file-based historical/tick data extraction, and Java/C++/.NET/Swift/Go/JavaScript/Python client libraries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dxfeed.png
layout: provider
mcp_servers:
- description: ''
  name: dxfeed-mcp.yml
  slug: dxfeed-mcpyml
modified: '2026-07-22'
name: dxFeed
nav: Providers
network: true
overview: 'dxFeed publishes 2 APIs on the [APIs.io](https://apis.io/) network: dxLink WebSocket API and Fundamentals API. Tagged areas include Financial, Market Data, Real-Time, Historical Data, and Equities.


  The dxFeed catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  dxFeed''s developer surface includes authentication, sandbox, getting-started guide, API reference, developer portal, documentation, engineering blog, and 19 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 50.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 56.9
    developer_ergonomics: 71.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 50.6
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dxfeed/refs/heads/main/screenshots/dxfeed-2026-07-22T202337.png
security:
- kind: authentication
  name: Dxfeed Authentication
  slug: dxfeed-authentication
  summary_line: http-basic (login/password credentials)/dxLink AUTH token (protocol message) · 3 schemes
- kind: domain-security
  name: Dxfeed Domain Security
  slug: dxfeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dxfeed Trust Center
  slug: dxfeed-trust-center
  summary_line: SOC 2
slug: dxfeed
tags:
- Financial
- Market Data
- Real-Time
- Historical Data
- Equities
- Options
- Futures
- Crypto
- Reference Data
- Fundamentals
website: https://dxfeed.com/
---
