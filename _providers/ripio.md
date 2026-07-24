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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 86.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Ripio Agentic Access
  operation_count: 46
  slug: ripio-agentic-access
  summary_line: 46 operations · 10 acting
api_count: 11
apis:
- description: The Book API from Ripio — 2 operation(s) for book.
  name: Ripio Book API
  slug: ripio-book-api
- description: The Cryptocurrency Deposits API from Ripio — 2 operation(s) for cryptocurrency deposits.
  name: Ripio Cryptocurrency Deposits API
  slug: ripio-cryptocurrency-deposits-api
- description: The Cryptocurrency Withdrawals API from Ripio — 3 operation(s) for cryptocurrency withdrawals.
  name: Ripio Cryptocurrency Withdrawals API
  slug: ripio-cryptocurrency-withdrawals-api
- description: The General endpoints API from Ripio — 3 operation(s) for general endpoints.
  name: Ripio General endpoints API
  slug: ripio-general-endpoints-api
- description: The Orders API from Ripio — 11 operation(s) for orders.
  name: Ripio Orders API
  slug: ripio-orders-api
- description: The public endpoints have a reduced requests limit and a 30 seconds cache. For increased limits, use the private endpoints.
  name: Ripio Public API
  slug: ripio-public-api
- description: The Ticker API from Ripio — 2 operation(s) for ticker.
  name: Ripio Ticker API
  slug: ripio-ticker-api
- description: The Ticket API from Ripio — 1 operation(s) for ticket.
  name: Ripio Ticket API
  slug: ripio-ticket-api
- description: The Transactions API from Ripio — 1 operation(s) for transactions.
  name: Ripio Transactions API
  slug: ripio-transactions-api
- description: The User API from Ripio — 6 operation(s) for user.
  name: Ripio User API
  slug: ripio-user-api
- description: API to check addresses of wallets.
  name: Ripio Wallets API
  slug: ripio-wallets-api
artifact_total: 19
asyncapis:
- description: ''
  name: Ripio Trade Webhooks
  slug: ripio-trade-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.ripio.com/ar/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.ripiotrade.co/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.ripiotrade.co/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.ripiotrade.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://trade.ripio.com/market/api/token
- group: operate
  title: ''
  type: Support
  url: https://help-ar.ripio.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ripio
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ripio.com/
- group: start
  title: ''
  type: SignUp
  url: https://auth.ripio.com/#/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://terms.ripio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://terms.ripio.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ripio-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ripio-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ripio-agentic-access.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ripio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://apidocs.ripiotrade.co/#tag/V3-Endpoint-Migrations
- group: design
  title: ''
  type: Conventions
  url: conventions/ripio-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ripio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ripio-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ripio-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ripio-trade-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ripio-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ripio-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/ripio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ripio-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ripio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.ripio.com/es/seguridad
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ripio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/ripio/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/ripio-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ripio-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/ripio-trade-overlay.yaml
created: '2026-07-17'
description: Ripio is a Latin American cryptocurrency exchange founded in 2013, offering crypto trading, stablecoins, DeFi products, a Visa crypto card, and B2B infrastructure and liquidity across Brazil, Argentina, Chile, Uruguay, Colombia, Mexico, Peru and Spain. Its developer-facing product is the Ripio Trade API (v4) — a REST and WebSocket trading API covering market data, order management, balances, statements, cryptocurrency deposits and withdrawals, and real-time streaming. Authentication uses an API Token plus HMAC-SHA256 request signing. The platform is SOC 2 Type II certified with a HackerOne bug bounty. Backed by Pantera Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ripio.png
layout: provider
mcp_servers:
- description: ''
  name: ripio-mcp.yml
  slug: ripio-mcpyml
modified: '2026-07-21'
name: Ripio
nav: Providers
network: true
overview: 'Ripio publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Book API, Cryptocurrency Deposits API, Cryptocurrency Withdrawals API, and 8 more. Tagged areas include Company, Crypto, Cryptocurrency, Exchange, and Trading.


  The Ripio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ripio''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 27 more developer resources.'
random_paper: 37
rate_limits:
- limit_count: 0
  name: Ripio Rate Limits
  slug: ripio-rate-limits
score:
  band: strong
  composite: 60.6
  delta: 3.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.8
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 57.5
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Ripio Authentication
  slug: ripio-authentication
  summary_line: apiToken · 1 scheme
- kind: domain-security
  name: Ripio Domain Security
  slug: ripio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ripio Vulnerability Disclosure
  slug: ripio-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Ripio Trust Center
  slug: ripio-trust-center
  summary_line: SOC 2 Type II
slug: ripio
tags:
- Company
- Crypto
- Cryptocurrency
- Exchange
- Trading
- Blockchain
- Latin America
- Bitcoin
- Stablecoins
- API
website: https://www.ripio.com/ar/
---
