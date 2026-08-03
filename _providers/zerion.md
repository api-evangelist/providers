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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.5
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Zerion Agentic Access
  operation_count: 39
  slug: zerion-agentic-access
  summary_line: 39 operations · 8 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Operations related to chains, such as list all chains.
  name: Zerion chains API
  slug: zerion-chains-api
- description: Operations related to decentralized applications, such as list them all, search or get by ID.
  name: Zerion dapps API
  slug: zerion-dapps-api
- description: Operations related to fungible assets, such as list them all, search or get by ID.
  name: Zerion fungibles API
  slug: zerion-fungibles-api
- description: Operations related to gas.
  name: Zerion gas API
  slug: zerion-gas-api
- description: Operations related to non fungible assets, such list them, search or get by ID.
  name: Zerion nfts API
  slug: zerion-nfts-api
- description: Operations related to subscriptions to transactions.
  name: Zerion subscriptions to transactions API
  slug: zerion-subscriptions-to-transactions-api
- description: Operations related to swapping and bridging assets.
  name: Zerion swap API
  slug: zerion-swap-api
- description: Operations on a wallet set — aggregated portfolio data across at most one EVM address and one Solana address queried together.
  name: Zerion wallet sets API
  slug: zerion-wallet-sets-api
- description: Operations related to wallets, such as portfolio charts, positions, and transactions.
  name: Zerion wallets API
  slug: zerion-wallets-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Create a transaction webhook subscription for a set of wallets, confirm it, then verify the watched-wallet count.
  name: Zerion wallet activity subscription
  slug: zerion-wallet-activity-subscription.arazzo
- description: Pull a wallet's portfolio, positions, transaction history, and PnL in one flow.
  name: Zerion wallet overview
  slug: zerion-wallet-overview.arazzo
artifact_total: 28
asyncapis:
- description: ''
  name: Zerion Transactions Webhooks
  slug: zerion-transactions-webhooks
collections:
- collection_type: postman
  name: REST chains API
  slug: postman-zerion-chains-api
- collection_type: postman
  name: REST chains dapps API
  slug: postman-zerion-dapps-api
- collection_type: postman
  name: REST chains fungibles API
  slug: postman-zerion-fungibles-api
- collection_type: postman
  name: REST chains gas API
  slug: postman-zerion-gas-api
- collection_type: postman
  name: REST chains nfts API
  slug: postman-zerion-nfts-api
- collection_type: postman
  name: REST chains subscriptions to transactions API
  slug: postman-zerion-subscriptions-to-transactions-api
- collection_type: postman
  name: REST chains swap API
  slug: postman-zerion-swap-api
- collection_type: postman
  name: REST chains wallet sets API
  slug: postman-zerion-wallet-sets-api
- collection_type: postman
  name: REST chains wallets API
  slug: postman-zerion-wallets-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zerion/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.zerion.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zerion.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.zerion.io/api-reference/wallets/get-wallet-portfolio
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.zerion.io/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.zerion.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.zerion.io
- group: company
  title: ''
  type: Blog
  url: https://zerion.io/blog/tag/zerion-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zeriontech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zerion.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zerion.io/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/zerion-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/zerion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zerion-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/zerion-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zerion-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zerion-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zerion-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zerion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zerion-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zerion-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zerion-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.zerion.io/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/zerion-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zerion-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zerion-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zerion-transactions-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zerion-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zerion-api-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zerion-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zerion-plans.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zerion-wallet-overview.arazzo.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/zerion-wallet-activity-subscription.arazzo.yml
created: '2026-07-17'
description: Zerion is an Ethereum and Solana wallet and developer platform focused on making onchain data easy to use. The Zerion API delivers clean, normalized wallet data, token analytics, DeFi positions, transaction history, PnL, NFTs, gas prices, swap and bridge quotes, and real-time transaction webhooks across EVM chains and Solana. The same infrastructure powers the Zerion wallet app used by millions. It is a JSON:API REST service with HTTP Basic (API key) authentication plus pay-per-request x402 (Base/Solana USDC) and MPP (Tempo USDC) options aimed at AI agents, an open-source CLI, six packaged agent skills, a hosted MCP server, and Kafka streaming for high-throughput pipelines.
image: https://developers.zerion.io/logo/dark.svg
layout: provider
mcp_servers:
- description: ''
  name: zerion-mcp.yml
  slug: zerion-mcpyml
modified: '2026-07-21'
name: Zerion
nav: Providers
network: true
overview: 'Zerion publishes 9 APIs on the [APIs.io](https://apis.io/) network, including chains API, dapps API, fungibles API, and 6 more. Tagged areas include Company, Web3, Blockchain, Cryptocurrency, and DeFi.


  The Zerion catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zerion''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, authentication, and 27 more developer resources.'
plans:
- name: Zerion Plans
  plan_count: 5
  slug: zerion-plans
random_paper: 93
rate_limits:
- limit_count: 5
  name: Zerion Rate Limits
  slug: zerion-rate-limits
score:
  band: strong
  composite: 63.9
  delta: 3.5
  facets:
    commercial_clarity: 76.3
    contract_quality: 73.5
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 68.4
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Zerion Authentication
  slug: zerion-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zerion Domain Security
  slug: zerion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zerion
tags:
- Company
- Web3
- Blockchain
- Cryptocurrency
- DeFi
- Wallet
- NFT
- Ethereum
- Solana
- Portfolio
- Onchain Data
- Transactions
website: https://developers.zerion.io/
---
