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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: ETHGas v1 REST + WebSocket API for market data, order placement/management, funding (collateral deposits/withdrawals), and validator/builder operations across whole-block commitments and inclusion pre
  name: ETHGas API
  slug: ethgas-api
artifact_total: 5
asyncapis:
- description: ''
  name: Ethgas Websocket Webhooks
  slug: ethgas-websocket-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://ethgas.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ethgas.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ethgas.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.ethgas.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ethgas.com/developer-resources/technical-integration
- group: company
  title: ''
  type: Blog
  url: https://ethgas.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ethgas-developer
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/ethgas
- group: start
  title: ''
  type: SignUp
  url: https://app.ethgas.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ethgas.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ethgas.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/ethgas-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ethgas-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ethgas-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ethgas-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ethgas-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ethgas-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ethgas-websocket-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ethgas-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ethgas-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ethgas-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ethgas-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ethgas-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ethgas-domain-security.yml
created: '2026-07-17'
description: ETHGas is an Ethereum blockspace exchange that turns Ethereum blockspace into a tradable commodity, enabling instant transactions through preconfirmations (execution and inclusion preconfs), whole-block commitments, and base-fee futures. Its public developer platform exposes a v1 REST API and a WebSocket streaming API for market data, order placement and management, funding (collateral deposits and withdrawals), and validator/builder registration. Authentication uses an EIP-712 wallet-signature login that issues a short-lived JWT bearer token; public market-data endpoints under /api/v1/p require none. ETHGas runs on Ethereum mainnet with a Hoodi testnet environment, and backs the exchange with a Commit-Boost validator module and a modified rbuilder block builder. ETHGas is backed by Polychain.
image: https://ethgas.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ethgas-mcp.yml
  slug: ethgas-mcpyml
modified: '2026-07-19'
name: ETHGas
nav: Providers
network: true
overview: 'ETHGas publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Blockchain, Ethereum, and Trading.


  The ETHGas catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ETHGas'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 17 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 45.3
  delta: 4.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 41.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ethgas/refs/heads/main/screenshots/ethgas-2026-07-25T213653.png
security:
- kind: authentication
  name: Ethgas Authentication
  slug: ethgas-authentication
  summary_line: wallet-signature/http-bearer · 2 schemes
- kind: domain-security
  name: Ethgas Domain Security
  slug: ethgas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ethgas
tags:
- Company
- Infrastructure
- Blockchain
- Ethereum
- Trading
- Preconfirmations
- Blockspace
- MEV
- DeFi
- Web3
website: https://ethgas.com
---
