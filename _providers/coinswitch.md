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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Professional REST + WebSocket trading API for Spot (INR/USDT), USDT-margined Perpetual Futures, HFT, and Options on the CoinSwitch PRO venue. Ed25519 request signing; v2 base path /trade/api/v2.
  name: CoinSwitch PRO Trading API
  slug: coinswitch-pro-trading-api
artifact_total: 6
asyncapis:
- description: ''
  name: Coinswitch Streams Webhooks
  slug: coinswitch-streams-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://coinswitch.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-trading.coinswitch.co/
- group: docs
  title: ''
  type: Documentation
  url: https://api-trading.coinswitch.co/get-started/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api-trading.coinswitch.co/resources/reference-client
- group: start
  title: ''
  type: GettingStarted
  url: https://api-trading.coinswitch.co/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://coinswitch.co/blog
- group: operate
  title: ''
  type: Support
  url: https://coinswitch.co/faqs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinswitch.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinswitch.co/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinswitch.co/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-trading.coinswitch.co/resources/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coinswitch-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/coinswitch-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coinswitch-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coinswitch-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coinswitch-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coinswitch-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coinswitch-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coinswitch-streams-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coinswitch-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coinswitch-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/coinswitch-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinswitch-domain-security.yml
created: '2026-07-17'
description: CoinSwitch is one of India's largest retail crypto investing platforms, based in Bengaluru and backed by a16z, Paradigm, and Ribbit Capital. Alongside its consumer buy/sell app it operates CoinSwitch PRO, a professional trading venue that exposes a public REST and WebSocket API for programmatic trading. The CoinSwitch PRO API (base https://coinswitch.co/trade/api/v2) covers Spot trading on INR and USDT pairs, USDT-margined Perpetual Futures with up to 100x leverage, low-latency High-Frequency Trading (HFT) endpoints, and Options (private beta). Developers can place, cancel, and track orders, read portfolios and trading fees, and subscribe to real-time order, balance, and candlestick streams over Socket.IO. Requests authenticate with an API key and an Ed25519 request signature (X-AUTH-APIKEY / X-AUTH-SIGNATURE / X-AUTH-EPOCH), with reference signing implementations published for Python, Java, Go, and Node.js.
image: https://api-trading.coinswitch.co/img/social-card.png
layout: provider
mcp_servers:
- description: ''
  name: CoinSwitch MCP Server
  slug: coinswitch-mcp-server
modified: '2026-07-18'
name: CoinSwitch
nav: Providers
network: true
overview: 'CoinSwitch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Crypto Exchange, Trading, and Fintech.


  The CoinSwitch catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CoinSwitch''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 16 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 17
  name: Coinswitch Rate Limits
  slug: coinswitch-rate-limits
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 71.1
  previous_composite: 42.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 33.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinswitch/refs/heads/main/screenshots/coinswitch-2026-07-25T210036.png
security:
- kind: authentication
  name: Coinswitch Authentication
  slug: coinswitch-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Coinswitch Domain Security
  slug: coinswitch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: coinswitch
tags:
- Company
- Cryptocurrency
- Crypto Exchange
- Trading
- Fintech
- Futures
- Spot Trading
- WebSocket
- India
website: https://coinswitch.co
---
