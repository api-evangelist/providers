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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Sponge Agentic Access
  operation_count: 57
  slug: sponge-agentic-access
  summary_line: 57 operations · 33 acting
api_count: 10
apis:
- description: The Agents API from Sponge — 5 operation(s) for agents.
  name: Sponge Agents API
  slug: sponge-agents-api
- description: The Cards API from Sponge — 6 operation(s) for cards.
  name: Sponge Cards API
  slug: sponge-cards-api
- description: The Fiat API from Sponge — 11 operation(s) for fiat.
  name: Sponge Fiat API
  slug: sponge-fiat-api
- description: The MPP API from Sponge — 5 operation(s) for mpp.
  name: Sponge MPP API
  slug: sponge-mpp-api
- description: The Payments API from Sponge — 1 operation(s) for payments.
  name: Sponge Payments API
  slug: sponge-payments-api
- description: The Secrets API from Sponge — 2 operation(s) for secrets.
  name: Sponge Secrets API
  slug: sponge-secrets-api
- description: The Sponge Card API from Sponge — 7 operation(s) for sponge card.
  name: Sponge Sponge Card API
  slug: sponge-sponge-card-api
- description: The Trading API from Sponge — 1 operation(s) for trading.
  name: Sponge Trading API
  slug: sponge-trading-api
- description: The Transfers API from Sponge — 9 operation(s) for transfers.
  name: Sponge Transfers API
  slug: sponge-transfers-api
- description: The Wallet API from Sponge — 4 operation(s) for wallet.
  name: Sponge Wallet API
  slug: sponge-wallet-api
arazzos:
- description: Platform backend creates a new agent, then mints an agent API key for runtime use.
  name: Sponge — create an agent and issue its key
  slug: sponge-agent-onboarding
- description: Read wallet balances, send an EVM transfer, then poll transaction status.
  name: Sponge — check balance, transfer, and confirm
  slug: sponge-transfer-and-confirm
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sponge public Agents API
  slug: open-sponge-agents-api
- collection_type: open
  name: Sponge public Agents Cards API
  slug: open-sponge-cards-api
- collection_type: open
  name: Sponge public Agents Fiat API
  slug: open-sponge-fiat-api
- collection_type: open
  name: Sponge public Agents MPP API
  slug: open-sponge-mpp-api
- collection_type: open
  name: Sponge public Agents Payments API
  slug: open-sponge-payments-api
- collection_type: open
  name: Sponge public Agents Secrets API
  slug: open-sponge-secrets-api
- collection_type: open
  name: Sponge public Agents Sponge Card API
  slug: open-sponge-sponge-card-api
- collection_type: open
  name: Sponge public Agents Trading API
  slug: open-sponge-trading-api
- collection_type: open
  name: Sponge public Agents Transfers API
  slug: open-sponge-transfers-api
- collection_type: open
  name: Sponge public Agents Wallet API
  slug: open-sponge-wallet-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sponge-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://paysponge.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paysponge.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paysponge.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paysponge.com/wallet/sdk.md
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/gwH2QqMDaX
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paysponge
- group: start
  title: ''
  type: SignUp
  url: https://wallet.paysponge.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paysponge.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paysponge.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/sponge-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sponge-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sponge-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sponge-agentic-access.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sponge-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sponge-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sponge-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sponge-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sponge-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sponge-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sponge-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sponge-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sponge-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sponge-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sponge-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sponge-transfer-and-confirm.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sponge-agent-onboarding.yml
created: '2026-07-17'
description: Sponge builds financial infrastructure for the agent economy — wallets that let AI agents hold and spend money, and a gateway that lets businesses sell services directly to agents. The Sponge Wallet API gives an agent its own multi-chain crypto wallet with balances, transfers, swaps, cross-chain bridges, payment links, cards (including a Rain-issued Visa Sponge Card), fiat onramps (Coinbase, Stripe), and trading on Hyperliquid and Polymarket, plus paid access to external services via the x402 and MPP agent-payment protocols. A TypeScript and Python SDK, a spongewallet CLI, and hosted MCP servers ship first-party. Backed by Y Combinator (W2026).
image: https://paysponge.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: sponge-mcp.yml
  slug: sponge-mcpyml
modified: '2026-07-21'
name: Sponge
nav: Providers
network: true
overview: 'Sponge publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Cards API, Fiat API, and 7 more. Tagged areas include Company, Agent Payments, AI Agents, Wallets, and Cryptocurrency.


  Sponge''s developer surface includes documentation, getting-started guide, support, signup flow, authentication, CLI, sandbox, and 21 more developer resources.'
random_paper: 1
scopes:
- name: Sponge Scopes
  scope_count: 5
  slug: sponge-scopes
  summary_line: 5 scopes
score:
  band: developing
  composite: 50.9
  delta: 2.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 53.6
    developer_ergonomics: 76.2
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 2.6
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sponge/refs/heads/main/screenshots/sponge-2026-08-17T082030.png
security:
- kind: authentication
  name: Sponge Authentication
  slug: sponge-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Sponge Domain Security
  slug: sponge-domain-security
  summary_line: TLSv1.3
slug: sponge
tags:
- Company
- Agent Payments
- AI Agents
- Wallets
- Cryptocurrency
- Payments
- Stablecoins
- x402
- MPP
- Financial Infrastructure
- MCP
- Fintech
- Cards
- Onramp
website: https://paysponge.com
---
