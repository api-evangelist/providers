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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.7
  scored_at: '2026-08-11'
api_count: 6
apis:
- description: Core CDP API v2 for onchain wallets, payments, trading, faucets, policies, and JSON-RPC access, authenticated with short-lived JWTs.
  name: Coinbase Developer Platform (CDP) API
  slug: coinbase-developer-platform-cdp-api
- description: Programmatic spot trading, order management, and market data for the Coinbase retail exchange (Advanced Trade).
  name: Coinbase Advanced Trade API
  slug: coinbase-advanced-trade-api
- description: Retail Coinbase App API v2 for accounts, addresses, transactions, buys/sells, with OAuth2 and API-key HMAC authentication.
  name: Coinbase App API (Sign in with Coinbase)
  slug: coinbase-app-api-sign-in-with-coinbase
- description: Institutional/pro exchange REST and WebSocket API for order books, trading, and market data.
  name: Coinbase Exchange API
  slug: coinbase-exchange-api
- description: Institutional trading, custody, and portfolio management API for Coinbase Prime.
  name: Coinbase Prime API
  slug: coinbase-prime-api
- description: Crypto payments/checkout API for accepting cryptocurrency payments.
  name: Coinbase Commerce API
  slug: coinbase-commerce-api
artifact_total: 11
asyncapis:
- description: ''
  name: Coinbase Global Webhooks
  slug: coinbase-global-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinbase-global-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.cdp.coinbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cdp.coinbase.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cdp.coinbase.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cdp.coinbase.com/get-started/overview
- group: start
  title: ''
  type: SignUp
  url: https://portal.cdp.coinbase.com
- group: company
  title: ''
  type: Blog
  url: https://www.coinbase.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinbase
- group: operate
  title: ''
  type: Support
  url: https://docs.cdp.coinbase.com/support/welcome
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinbase.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cdp.coinbase.com/get-started/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinbase.com/legal/user_agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinbase.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coinbase.com/advanced-fees
- group: build
  title: ''
  type: Packages
  url: packages/coinbase-global-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coinbase-global-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/coinbase-global-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coinbase-global-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coinbase-global-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coinbase-global-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/coinbase-global-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinbase-global-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/coinbase
- group: auth
  title: ''
  type: Authentication
  url: authentication/coinbase-global-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coinbase-global-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/coinbase-global-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coinbase-global-webhooks.yml
created: '2026-07-17'
description: Coinbase Global, Inc. is a publicly traded cryptocurrency platform that operates a retail exchange, an institutional trading and custody business (Coinbase Prime), and the Coinbase Developer Platform (CDP) — a suite of APIs, SDKs, and onchain tooling for wallets, payments, trading, staking, and AI agents. Developers build against the CDP API v2, the Advanced Trade API, the Coinbase App (Sign in with Coinbase) API, the Exchange and Prime APIs, and Coinbase Commerce, with authentication via short-lived JWTs signed by project API keys. CDP ships first-party TypeScript and Python SDKs, a CLI that doubles as a local MCP server, AgentKit for AI agents, webhooks, and idempotent write semantics. This profile was added to the API Evangelist network from a venture-portfolio lead and enriched from Coinbase's public developer surface.
image: https://avatars.githubusercontent.com/u/1885080?s=200&v=4
layout: provider
mcp_servers:
- description: ''
  name: coinbase-global-mcp.yml
  slug: coinbase-global-mcpyml
modified: '2026-07-18'
name: Coinbase Global
nav: Providers
network: true
overview: 'Coinbase Global publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Blockchain, Payments, and Wallets.


  The Coinbase Global catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coinbase Global''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, changelog, and 21 more developer resources.'
random_paper: 114
score:
  band: developing
  composite: 51.4
  delta: -0.9
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 55.3
  previous_composite: 52.3
  provenance:
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 40.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coinbase-global/refs/heads/main/screenshots/coinbase-global-2026-07-25T210033.png
security:
- kind: authentication
  name: Coinbase Global Authentication
  slug: coinbase-global-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Coinbase Global Domain Security
  slug: coinbase-global-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinbase Global Vulnerability Disclosure
  slug: coinbase-global-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: coinbase-global
tags:
- Company
- Cryptocurrency
- Blockchain
- Payments
- Wallets
- Trading
- Onchain
- Web3
- Financial Services
- Developer Platform
- AI Agents
- Stablecoins
website: https://portal.cdp.coinbase.com
---
