---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Alpaca Agentic Access
  operation_count: 119
  slug: alpaca-agentic-access
  summary_line: 119 operations · 39 acting
api_count: 23
apis:
- description: The Alpaca Trading API enables commission-free trading of US-listed equities, options, and crypto. It exposes endpoints for orders, positions, account information, watchlists, calendar, clock, and ass
  name: Alpaca Trading API
  slug: trading-api
- description: The Alpaca OAuth API allows third-party applications to authenticate Alpaca users and obtain access tokens for the Trading and Market Data APIs.
  name: Alpaca OAuth API
  slug: oauth-api
- description: Head to https://alpaca.markets/docs/api-references/trading-api/account-activities/ to view complete documentation on the Account Activities API.
  name: Alpaca Account Activities API
  slug: alpaca-account-activities-api
- description: Head to https://alpaca.markets/docs/api-documentation/api-v2/account-configuration/ to view complete documentation on the Account Configurations API.
  name: Alpaca Account Configurations API
  slug: alpaca-account-configurations-api
- description: The Accounts API from Alpaca — 14 operation(s) for accounts.
  name: Alpaca Accounts API
  slug: alpaca-accounts-api
- description: The Assets API from Alpaca — 2 operation(s) for assets.
  name: Alpaca Assets API
  slug: alpaca-assets-api
- description: The Calendar API from Alpaca — 2 operation(s) for calendar.
  name: Alpaca Calendar API
  slug: alpaca-calendar-api
- description: The Clock API from Alpaca — 2 operation(s) for clock.
  name: Alpaca Clock API
  slug: alpaca-clock-api
- description: The Corporate Actions API from Alpaca — 1 operation(s) for corporate actions.
  name: Alpaca Corporate Actions API
  slug: alpaca-corporate-actions-api
- description: The Crypto Pricing Data API API from Alpaca — 17 operation(s) for crypto pricing data api.
  name: Alpaca Crypto Pricing Data API API
  slug: alpaca-crypto-pricing-data-api-api
- description: The Documents API from Alpaca — 3 operation(s) for documents.
  name: Alpaca Documents API
  slug: alpaca-documents-api
- description: The Events API from Alpaca — 4 operation(s) for events.
  name: Alpaca Events API
  slug: alpaca-events-api
- description: The Funding API from Alpaca — 7 operation(s) for funding.
  name: Alpaca Funding API
  slug: alpaca-funding-api
- description: The Journals API from Alpaca — 4 operation(s) for journals.
  name: Alpaca Journals API
  slug: alpaca-journals-api
- description: The Logo API from Alpaca — 1 operation(s) for logo.
  name: Alpaca Logo API
  slug: alpaca-logo-api
- description: The News API from Alpaca — 1 operation(s) for news.
  name: Alpaca News API
  slug: alpaca-news-api
- description: Head to https://alpaca.markets/docs/api-documentation/api-v2/orders/ to view complete documentation on the Orders API.
  name: Alpaca Orders API
  slug: alpaca-orders-api
- description: Head to https://alpaca.markets/docs/api-documentation/api-v2/portfolio-history/ to view complete documentation on the Portfolio History API.
  name: Alpaca Portfolio History API
  slug: alpaca-portfolio-history-api
- description: Head to https://alpaca.markets/docs/api-documentation/api-v2/positions/ to view complete documentation on the Positions API.
  name: Alpaca Positions API
  slug: alpaca-positions-api
- description: The Screener API from Alpaca — 1 operation(s) for screener.
  name: Alpaca Screener API
  slug: alpaca-screener-api
- description: The Stock Pricing Data API API from Alpaca — 16 operation(s) for stock pricing data api.
  name: Alpaca Stock Pricing Data API API
  slug: alpaca-stock-pricing-data-api-api
- description: The Watchlist API from Alpaca — 2 operation(s) for watchlist.
  name: Alpaca Watchlist API
  slug: alpaca-watchlist-api
- description: Head to https://alpaca.markets/docs/api-documentation/api-v2/watchlist/ to view complete documentation on the Watchlist API.
  name: Alpaca Watchlists API
  slug: alpaca-watchlists-api
artifact_total: 61
asyncapis:
- description: AsyncAPI 2.6 description of Alpaca's public WebSocket streaming APIs. Covers real-time stock market data (IEX / SIP / delayed SIP / BOATS), real-time crypto market data (US and Global), real-time news
  name: Alpaca WebSocket Streaming APIs
  slug: alpaca-asyncapi
collections:
- collection_type: postman
  name: Broker Account Activities API
  slug: postman-alpaca-account-activities-api
- collection_type: postman
  name: Broker Account Activities Accounts API
  slug: postman-alpaca-accounts-api
- collection_type: postman
  name: Broker Account Activities Assets API
  slug: postman-alpaca-assets-api
- collection_type: postman
  name: Broker Account Activities Calendar API
  slug: postman-alpaca-calendar-api
- collection_type: postman
  name: Broker Account Activities Clock API
  slug: postman-alpaca-clock-api
- collection_type: postman
  name: Broker Account Activities Corporate Actions API
  slug: postman-alpaca-corporate-actions-api
- collection_type: postman
  name: Broker Account Activities Crypto Pricing Data API API
  slug: postman-alpaca-crypto-pricing-data-api-api
- collection_type: postman
  name: Broker Account Activities Documents API
  slug: postman-alpaca-documents-api
- collection_type: postman
  name: Broker Account Activities Events API
  slug: postman-alpaca-events-api
- collection_type: postman
  name: Broker Account Activities Funding API
  slug: postman-alpaca-funding-api
- collection_type: postman
  name: Broker Account Activities Journals API
  slug: postman-alpaca-journals-api
- collection_type: postman
  name: Broker Account Activities Logo API
  slug: postman-alpaca-logo-api
- collection_type: postman
  name: Broker Account Activities News API
  slug: postman-alpaca-news-api
- collection_type: postman
  name: Broker Account Activities OAuth API
  slug: postman-alpaca-oauth-api
- collection_type: postman
  name: Broker Account Activities Orders API
  slug: postman-alpaca-orders-api
- collection_type: postman
  name: Broker Account Activities Portfolio History API
  slug: postman-alpaca-portfolio-history-api
- collection_type: postman
  name: Broker Account Activities Positions API
  slug: postman-alpaca-positions-api
- collection_type: postman
  name: Broker Account Activities Screener API
  slug: postman-alpaca-screener-api
- collection_type: postman
  name: Broker Account Activities Stock Pricing Data API API
  slug: postman-alpaca-stock-pricing-data-api-api
- collection_type: postman
  name: Broker Account Activities Trading API
  slug: postman-alpaca-trading-api
- collection_type: postman
  name: Broker Account Activities Watchlist API
  slug: postman-alpaca-watchlist-api
- collection_type: postman
  name: Broker Account Activities Watchlists API
  slug: postman-alpaca-watchlists-api
- collection_type: open
  name: Broker API
  slug: open-alpaca-broker-api
- collection_type: open
  name: Market Data API
  slug: open-alpaca-data-api
- collection_type: open
  name: OAuth API
  slug: open-alpaca-oauth-api
- collection_type: open
  name: Trader API
  slug: open-alpaca-trading-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/alpaca/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alpaca-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alpaca-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alpaca-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/alpaca-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alpaca-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alpaca-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alpaca-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/alpaca-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alpaca-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alpaca-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alpaca-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/alpaca-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alpaca-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/alpaca-cli.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alpaca-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alpaca-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alpaca-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/alpaca-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alpaca-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://alpaca.markets/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alpaca-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://alpaca.markets/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.alpaca.markets/
- group: design
  title: ''
  type: DataModel
  url: data-model/alpaca-data-model.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/alpacahq/alpaca-postman
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alpaca.markets/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alpaca.markets/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://alpaca.markets/support
- group: start
  title: ''
  type: SignUp
  url: https://app.alpaca.markets/signup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alpacamarkets
- group: start
  title: ''
  type: Portal
  url: https://alpaca.markets/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alpaca.markets/
- group: commercial
  title: ''
  type: Pricing
  url: https://alpaca.markets/data
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alpacahq
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alpaca.markets/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alpaca.markets/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alpaca.markets/privacy
- group: commercial
  title: ''
  type: Plans
  url: plans/alpaca-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alpaca-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alpaca-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.alpaca.markets/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://alpaca.markets/blog/feed/
created: '2026-05-08'
description: Alpaca is an API-first commission-free stock and crypto trading broker offering trading, market data, options, and broker-as-a-service APIs. Alpaca publishes its OpenAPI specifications publicly via the alpacahq/alpaca-docs GitHub repository, with separate specs for Trading, Broker, Market Data, and OAuth.
finops:
- name: Alpaca Finops
  service_category: Fintech
  slug: alpaca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alpaca.png
layout: provider
mcp_servers:
- description: ''
  name: alpaca-mcp.yml
  slug: alpaca-mcpyml
modified: '2026-07-22'
name: Alpaca
nav: Providers
network: true
overview: 'Alpaca publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Trading API, OAuth API, Account Activities API, and 20 more. Tagged areas include Fintech, Trading, Stocks, Crypto, and Brokerage.


  The Alpaca catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Alpaca''s developer surface includes authentication, sandbox, changelog, CLI, API reference, getting-started guide, support, and 37 more developer resources.'
plans:
- name: Alpaca Plans Pricing
  plan_count: 3
  slug: alpaca-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Alpaca Rate Limits
  slug: alpaca-rate-limits
rules:
- name: Alpaca API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: alpaca-asyncapi-spectral-rules
scopes:
- name: Alpaca Scopes
  scope_count: 4
  slug: alpaca-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 77.9
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 68.6
    developer_ergonomics: 91.3
    discoverability: 92.6
    governance: 68.8
    operational_transparency: 63.2
  previous_composite: 77.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 86.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/screenshots/alpaca-2026-06-20T171542.png
security:
- kind: authentication
  name: Alpaca Authentication
  slug: alpaca-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Alpaca Domain Security
  slug: alpaca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alpaca Vulnerability Disclosure
  slug: alpaca-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Alpaca Trust Center
  slug: alpaca-trust-center
  summary_line: SOC 2 Type 2, ISO 27001:2022, GDPR, UK ICO Data Protection
slug: alpaca
tags:
- Fintech
- Trading
- Stocks
- Crypto
- Brokerage
- Market Data
- Options
website: https://alpaca.markets/
---
