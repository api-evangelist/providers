---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: wss://data.infoway.io/ws
  baseurl_source: declared
  description: Persistent WebSocket connection for real-time trades, order-book depth, candlesticks and multilingual news. Integer protocol-code framing (10000 subscribe trade, 10002 trade push, 10003/10005 depth, 1
  name: Infoway WebSocket Streaming API
  slug: infoway-websocket-streaming-api
- description: 'Official Model Context Protocol server (PyPI infoway-mcp-server) exposing 17 tools over stdio for real-time quotes, depth, K-line, market temperature and breadth, global indexes, industry and concept '
  name: Infoway Financial Data MCP Server
  slug: infoway-financial-data-mcp-server
- baseURL: https://data.infoway.io
  baseurl_source: declared
  description: The Common API from Infoway Real-time Market Data API — 7 operation(s) for common.
  name: Infoway Real-time Market Data API Common API
  slug: infoway-real-time-market-data-api-common-api
- baseURL: https://data.infoway.io
  baseurl_source: declared
  description: The Crypto API from Infoway Real-time Market Data API — 3 operation(s) for crypto.
  name: Infoway Real-time Market Data API Crypto API
  slug: infoway-real-time-market-data-api-crypto-api
- baseURL: https://data.infoway.io
  baseurl_source: declared
  description: The Stock API from Infoway Real-time Market Data API — 3 operation(s) for stock.
  name: Infoway Real-time Market Data API Stock API
  slug: infoway-real-time-market-data-api-stock-api
artifact_total: 14
asyncapis:
- description: 'Real-time push of trades, order-book depth, candlesticks (K-line) and news over a single WebSocket connection. PROVENANCE: Infoway publishes NO AsyncAPI document. This document was DERIVED by API Evan'
  name: Infoway WebSocket Streaming API
  slug: infoway-real-time-market-data-api-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: REST Common API
  slug: open-infoway-real-time-market-data-api-common-api
- collection_type: open
  name: REST Crypto API
  slug: open-infoway-real-time-market-data-api-crypto-api
- collection_type: open
  name: REST Stock API
  slug: open-infoway-real-time-market-data-api-stock-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/infoway-real-time-market-data-api-openapi-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/infoway-api/infoway-mcp-server/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infoway-real-time-market-data-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infoway-real-time-market-data-api-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/infoway-real-time-market-data-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/infoway-real-time-market-data-api-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infoway-real-time-market-data-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infoway-real-time-market-data-api-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/infoway-real-time-market-data-api-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infoway-real-time-market-data-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infoway.io
- group: design
  title: ''
  type: Conformance
  url: conformance/infoway-real-time-market-data-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infoway-real-time-market-data-api-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infoway-real-time-market-data-api-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.infoway.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infoway.io/
- group: docs
  title: ''
  type: APIReference
  url: https://infoway.readme.io/reference/quick-start
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.infoway.io/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://infoway.io/en/feedback
- group: company
  title: ''
  type: Blog
  url: https://blog.infoway.io/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infoway-api
- group: commercial
  title: ''
  type: Pricing
  url: https://infoway.io/en#pricing
- group: start
  title: ''
  type: SignUp
  url: https://infoway.io/en/create-account
- group: start
  title: ''
  type: Login
  url: https://infoway.io/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infoway.io/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infoway.io/en/privacy-policy
created: '2026-08-08'
description: 'Infoway is a real-time and historical financial market-data provider covering equities (US, Hong Kong, China A-shares, Japan, South Korea, India), forex, cryptocurrencies across 30+ exchanges, and commodities/futures. It ships two surfaces from the host data.infoway.io: a REST/HTTP API for symbol reference data, trading calendars, last-trade ticks, order-book depth and candlestick (K-line) history, and a WebSocket streaming API that pushes trades, depth, candles and multilingual news with millisecond latency. Both authenticate with a single API key whose entitlements follow the plan it was issued against (Free through Professional). Infoway publishes per-endpoint OpenAPI 3.0.0 definitions on its ReadMe developer hub, official Python, Node.js and Java SDKs, an llms.txt documentation index, and a stdio MCP server exposing 17 financial-data tools with a provider-authored Agent Skill.'
image: https://infoway.io/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Infoway Real-time Market Data API MCP Server
  slug: infoway-real-time-market-data-api-mcp-server
modified: '2026-08-09'
name: Infoway Real-time Market Data API
nav: Providers
network: true
overview: 'Infoway Real-time Market Data API publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Infoway WebSocket Streaming API, Common API, Crypto API, and 1 more. Tagged areas include stock-api, forex-api, crypto-api, commodities-api, and futures-api.


  The Infoway Real-time Market Data API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Infoway Real-time Market Data API''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 20 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Infoway Real Time Market Data Api Rate Limits
  slug: infoway-real-time-market-data-api-rate-limits
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 52.1
    developer_ergonomics: 67.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 45.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infoway-real-time-market-data-api/refs/heads/main/screenshots/infoway-real-time-market-data-api-2026-08-17T081000.png
security:
- kind: authentication
  name: Infoway Real Time Market Data Api Authentication
  slug: infoway-real-time-market-data-api-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Infoway Real Time Market Data Api Domain Security
  slug: infoway-real-time-market-data-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: infoway-real-time-market-data-api
tags:
- stock-api
- forex-api
- crypto-api
- commodities-api
- futures-api
- Market Data
- Real-Time Data
- WebSocket
- Financial Data
- Fintech
- Historical Data
website: https://docs.infoway.io/
---
