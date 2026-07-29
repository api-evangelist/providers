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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for Luno market data, accounts, trading, transfers and withdrawals, plus a WebSocket market-data stream. Legacy API under /api/1/ and the newer Exchange API under /api/exchange/{1,2,3}/.
  name: Luno API
  slug: luno-api
artifact_total: 8
asyncapis:
- description: 'Real-time market data stream for the Luno Exchange. A client opens one WebSocket connection per trading pair, authenticates with its API key pair, receives an initial full order book snapshot, then a '
  name: Luno Streaming API
  slug: luno-streaming-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.luno.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.luno.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.luno.com/developers/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.luno.com/developers/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.luno.com/developers/api
- group: company
  title: ''
  type: Blog
  url: https://www.luno.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/luno
- group: start
  title: ''
  type: SignUp
  url: https://www.luno.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.luno.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.luno.com/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.luno.com/legal/compliance
- group: operate
  title: ''
  type: StatusPage
  url: https://status.luno.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/luno-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.luno.com/.well-known/security.txt
- group: build
  title: ''
  type: Packages
  url: packages/luno-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/luno-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/luno-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/luno-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/luno-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/luno-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/luno-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/luno-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/luno-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/luno-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/luno-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/luno-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luno-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/luno-vulnerability-disclosure.yml
created: '2026-07-17'
description: Luno is a cryptocurrency exchange founded in 2013 and operating across South Africa, Nigeria, Europe, Malaysia, Indonesia and other markets, providing wallets and the ability to buy, sell, store and trade Bitcoin, Ethereum and other digital assets. The Luno API is a REST API (with an accompanying WebSocket market-data stream) covering market data, account balances, order placement and trading, transfers, sends and withdrawals. It authenticates with an API key pair over HTTP Basic and is used by Luno's official Go, Python, PHP and Java SDKs and by the official Luno MCP server.
image: https://github.com/luno.png
layout: provider
mcp_servers:
- description: ''
  name: luno-mcp.yml
  slug: luno-mcpyml
modified: '2026-07-20'
name: Luno
nav: Providers
network: true
overview: 'Luno publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Exchange, Bitcoin, and Ethereum.


  The Luno catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Luno''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 41
rate_limits:
- limit_count: 1
  name: Luno Rate Limits
  slug: luno-rate-limits
score:
  band: developing
  composite: 51.9
  delta: 1.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 44.4
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 50.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luno/refs/heads/main/screenshots/luno-2026-07-25T225732.png
security:
- kind: authentication
  name: Luno Authentication
  slug: luno-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Luno Domain Security
  slug: luno-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Luno Vulnerability Disclosure
  slug: luno-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Luno Trust Center
  slug: luno-trust-center
  summary_line: SOC 2, ISO 27001
slug: luno
tags:
- Company
- Cryptocurrency
- Exchange
- Bitcoin
- Ethereum
- Trading
- Fintech
- Wallet
- Blockchain
- Financial Services
website: https://www.luno.com/
---
