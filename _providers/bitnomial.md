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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 34.6
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Public HTTPS REST API for the Bitnomial exchange — products and contract specs, orders, fills, block trades, indexes, funding rates, and market statistics. HMAC-SHA256 signed authentication; cursor pa
  name: Bitnomial Exchange REST API
  slug: bitnomial-exchange-rest-api
- description: Real-time WebSocket market-data feed delivering trade, order book, block trade, and market status messages for subscribed products.
  name: Bitnomial Market Data WebSocket API
  slug: bitnomial-market-data-websocket-api
artifact_total: 7
asyncapis:
- description: Real-time market-data feed for Bitnomial's CFTC-regulated derivatives exchange. Clients open a WebSocket connection and must send a subscribe message within 10 seconds or they are disconnected. Faithf
  name: Bitnomial Market Data WebSocket API
  slug: bitnomial-market-data-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://bitnomial.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bitnomial.com/exchange/docs
- group: docs
  title: ''
  type: Documentation
  url: https://bitnomial.com/exchange/docs/api/overview/
- group: docs
  title: ''
  type: APIReference
  url: https://bitnomial.com/exchange/docs/api/rest/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://bitnomial.com/exchange/docs/api/rest/authentication/
- group: company
  title: ''
  type: Blog
  url: https://bitnomial.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:help@exchange.bitnomial.com
- group: operate
  title: ''
  type: StatusPage
  url: https://bitnomial.statuspage.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitnomial
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitnomial-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitnomial-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitnomial-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitnomial-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitnomial-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bitnomial-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitnomial-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bitnomial-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/bitnomial-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitnomial-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitnomial-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/bitnomial-market-data-asyncapi.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitnomial-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitnomial-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bitnomial-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bitnomial.com/security
created: '2026-07-17'
description: Bitnomial is a Chicago-based derivatives exchange company that owns and operates U.S. CFTC-regulated subsidiaries — a Designated Contract Market (exchange/DCM), a Derivatives Clearing Organization (clearinghouse/DCO), and a Futures Commission Merchant (clearing brokerage/FCM). It offers leveraged spot, perpetuals, futures, options, and prediction markets on a single regulated venue with crypto margin and settlement. For developers, Bitnomial publishes a public HTTPS REST API (products, orders, fills, block trades, indexes, funding rates, market stats), a real-time WebSocket market-data feed (trade, book, block, status channels), a low-latency binary order-entry protocol (BTP), and a FIX 4.4 API with dropcopy. REST authentication uses HMAC-SHA256 request signing with per-connection credentials. Surfaced as a portfolio company of Electric Capital and enriched by the API Evangelist pipeline.
image: https://bitnomial.com/images/social-preview.jpg
layout: provider
mcp_servers:
- description: ''
  name: bitnomial-mcp.yml
  slug: bitnomial-mcpyml
modified: '2026-07-18'
name: Bitnomial
nav: Providers
network: true
overview: 'Bitnomial publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data WebSocket API. Tagged areas include Company, Fintech, Cryptocurrency, Derivatives, and Exchange.


  The Bitnomial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bitnomial''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 18 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 38.4
  delta: 2.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 27.8
    developer_ergonomics: 80.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Bitnomial Authentication
  slug: bitnomial-authentication
  summary_line: hmac-signed-api-key · 1 scheme
- kind: domain-security
  name: Bitnomial Domain Security
  slug: bitnomial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bitnomial Vulnerability Disclosure
  slug: bitnomial-vulnerability-disclosure
  summary_line: disclosure policy published
slug: bitnomial
tags:
- Company
- Fintech
- Cryptocurrency
- Derivatives
- Exchange
- Trading
- Market Data
- Futures
- Options
- CFTC Regulated
website: https://bitnomial.com/
---
