---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: 'Public and private REST endpoints for market-data summaries, public trade history, positions, holdings, balances, reporting, and MFA. Private endpoints require an ES256 JWT access token. Versioned by '
  name: PowerTrade REST API
  slug: powertrade-rest-api
- description: Real-time WebSocket market-data feeds (reference data, top-of-book, order books, trades, index and settlement prices) and private position-summary feeds.
  name: PowerTrade WebSocket Feeds
  slug: powertrade-websocket-feeds
- description: FIX 4.4 order-entry and drop-copy gateway for order management, with Go example clients published on GitHub.
  name: PowerTrade FIX API
  slug: powertrade-fix-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://power.trade/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.power.trade/api/api-overview.md
- group: docs
  title: ''
  type: Documentation
  url: https://power-trade.github.io/api-docs-source/
- group: docs
  title: ''
  type: APIReference
  url: https://power-trade.github.io/api-docs-source/rest_api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://support.power.trade/api/api-overview.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/powertrade-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Power-Trade
- group: operate
  title: ''
  type: Support
  url: https://support.power.trade/
- group: commercial
  title: ''
  type: Pricing
  url: https://support.power.trade/how-to-use-powertrade/fees.md
- group: start
  title: ''
  type: SignUp
  url: https://app.power.trade/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.power.trade/legal/legal-and-privacy-policies/terms-of-service.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.power.trade/legal/legal-and-privacy-policies/privacy-policy.md
- group: auth
  title: ''
  type: Security
  url: https://support.power.trade/legal/security/security-policy.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/powertrade-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/powertrade-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/powertrade-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/powertrade-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/powertrade-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/powertrade-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/powertrade-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/powertrade-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/powertrade-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/powertrade-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/powertrade-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powertrade-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/powertrade-vulnerability-disclosure.yml
created: '2026-07-17'
description: PowerTrade (power.trade) is a crypto derivatives exchange offering European-style, USDC-settled options on BTC, ETH and 80+ altcoins, plus perpetual futures, spot, and tokenized equity (xStocks) options. For programmatic traders it publishes a public REST API (market data, history, positions, balances), real-time WebSocket market-data and position feeds, and a FIX 4.4 order-entry / drop-copy gateway. Private endpoints authenticate with an ES256 JWT signed from an account API key and private key. The exchange runs production, test and dev environments and provides Go, Python and TypeScript example clients on GitHub. Backed by Pantera Capital.
image: https://power.trade/assets/power-trade-og.jpg
layout: provider
mcp_servers:
- description: ''
  name: powertrade-mcp.yml
  slug: powertrade-mcpyml
modified: '2026-07-20'
name: PowerTrade
nav: Providers
network: true
overview: 'PowerTrade publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Cryptocurrency, Derivatives, and Options.


  PowerTrade''s developer surface includes documentation, API reference, getting-started guide, authentication, support, pricing, signup flow, and 19 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 36.4
  delta: -0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 81.5
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 37.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Powertrade Authentication
  slug: powertrade-authentication
  summary_line: jwt-bearer · 0 schemes
- kind: domain-security
  name: Powertrade Domain Security
  slug: powertrade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Powertrade Vulnerability Disclosure
  slug: powertrade-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: powertrade
tags:
- Company
- Crypto
- Cryptocurrency
- Derivatives
- Options
- Perpetual Futures
- Trading
- Exchange
- Financial Services
- WebSocket
- FIX
- Market Data
website: https://power.trade/
---
