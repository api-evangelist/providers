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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: EVM-compatible JSON-RPC interface for Kite Chain mainnet (chain ID 2366, native token KITE), available over HTTPS and WSS from a global endpoint plus Virginia, Tokyo, and Ireland regional endpoints.
  name: Kite Chain JSON-RPC (Mainnet)
  slug: kite-chain-mainnet
- description: EVM-compatible JSON-RPC interface for Kite Chain testnet (chain ID 2368), paired with a public faucet and the testnet Kitescan block explorer for development and integration testing.
  name: Kite Chain JSON-RPC (Testnet)
  slug: kite-chain-testnet
- description: REST relayer that executes stablecoin transfers on behalf of users who hold no native gas token, authorized off-chain with EIP-3009 signed authorizations. GET /supported_tokens lists the tokens enable
  name: Kite Stablecoin Gasless Transfer API
  slug: kite-gasless-transfer
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://gokite.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gokite.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gokite.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gokite.ai/kite-chain/9-gasless-integration
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gokite.ai/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gokite-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gokite.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gokite.ai/privacy
- group: start
  title: ''
  type: SignUp
  url: https://agentpassport.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gokite.ai/
- group: other
  title: ''
  type: Whitepaper
  url: https://gokite.ai/kite-whitepaper
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kite-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kite-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/kite-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/kite-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kite-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kite-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kite-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kite-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kite-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kite-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kite-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kite-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kite-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kite-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kite-domain-security.yml
- group: auth
  title: ''
  type: SecurityOverview
  url: https://docs.gokite.ai/kite-chain/6-reference
created: '2026-07-17'
description: Kite (gokite.ai, formerly Zettablock) builds agentic payment infrastructure for the machine-to-machine economy. Kite Agent Passport gives autonomous AI agents their own identity, a funded wallet, user-set spending rules, delegated payment authority, and verifiable on-chain receipts, driven from a coding agent through the kpass and ksearch CLIs and a set of published Passport agent skills. Kite also operates Kite Chain, an EVM-compatible Avalanche-subnet Layer 1 (mainnet chain ID 2366, testnet 2368) with public HTTPS and WSS JSON-RPC endpoints, a stablecoin gasless transfer relayer built on EIP-3009 signed authorizations, and an x402 HTTP-402 payment surface with support for the Stripe/Tempo Machine Payments Protocol (MPP). Kite raised an $18M Series A led by PayPal Ventures and General Catalyst in September 2025.
image: https://gokite.ai/preview-newkiteai.png
layout: provider
mcp_servers:
- description: ''
  name: kite-mcp.yml
  slug: kite-mcpyml
modified: '2026-07-19'
name: Kite
nav: Providers
network: true
overview: 'Kite publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agentic Payments, AI Agents, x402, Stablecoins, and Blockchain.


  Kite''s developer surface includes documentation, API reference, getting-started guide, signup flow, CLI, changelog, authentication, and 21 more developer resources.'
random_paper: 34
score:
  band: thin
  composite: 38.6
  delta: -1.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 40.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kite/refs/heads/main/screenshots/kite-2026-07-25T223907.png
security:
- kind: authentication
  name: Kite Authentication
  slug: kite-authentication
  summary_line: passkey/email-otp/oauth2/signed-authorization/delegated-session · 8 schemes
- kind: domain-security
  name: Kite Domain Security
  slug: kite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kite
tags:
- Agentic Payments
- AI Agents
- x402
- Stablecoins
- Blockchain
- EVM
- Layer 1
- Machine-to-Machine
- Identity
- Payments
- JSON-RPC
- Account Abstraction
website: https://gokite.ai/
---
