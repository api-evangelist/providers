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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 26.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Ethereum-compatible JSON-RPC 2.0 API served by SKALE Chains (per-chain RPC/WSS endpoints), plus SKALE Programmable Privacy methods (bite_getDecryptedTransactionData, bite_getCommitteesInfo).
  name: SKALE JSON-RPC API
  slug: skale-json-rpc-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skale-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://skale.space
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.skale.space
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skale.space
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skale.space/developers/resources/json-rpc-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skale.space/developers/integrate-skale/connect-to-skale
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/skalenetwork
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/skale
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.skale.space/developers/run-a-skale-chain/pricing-and-payments
- group: build
  title: ''
  type: SDKs
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/packages/skale-labs-packages.yml
- group: build
  title: ''
  type: Packages
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/packages/skale-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/cli/skale-labs-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/mcp/skale-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/llms/skale-labs-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/sandbox/skale-labs-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/authentication/skale-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/conventions/skale-labs-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/conformance/skale-labs-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/changelog/skale-labs-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: https://raw.githubusercontent.com/api-evangelist/skale-labs/refs/heads/main/lifecycle/skale-labs-lifecycle.yml
created: '2026-07-17'
description: Skale Labs is the team behind SKALE, an Ethereum-compatible, zero-gas-fee blockchain network positioned as "the blockchain for a billion agents" with programmable privacy. SKALE runs application-specific L1 SKALE Chains on Base and Ethereum with instant finality and no user gas fees, and exposes an Ethereum JSON-RPC API plus first-party SDKs (BITE threshold-encryption, MPP machine payments), a SKALE CLI built for AI agents, a hosted documentation MCP server, and installable Agent Skills. It supports agentic commerce via the x402 payment protocol and ERC-8004 onchain identity, and native programmable privacy through threshold encryption (encrypted and conditional transactions, confidential tokens).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skale-labs.png
layout: provider
mcp_servers:
- description: ''
  name: skale-labs-mcp.yml
  slug: skale-labs-mcpyml
modified: '2026-07-21'
name: Skale Labs
nav: Providers
network: true
overview: 'Skale Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Web3, Smart Contracts, and Developer Tools.


  Skale Labs'' developer surface includes documentation, API reference, getting-started guide, support, pricing, CLI, sandbox, and 14 more developer resources.'
random_paper: 22
score:
  band: thin
  composite: 31.9
  delta: 0.8
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 84.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.1
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Skale Labs Authentication
  slug: skale-labs-authentication
  summary_line: none/wallet-signature · 3 schemes
- kind: domain-security
  name: Skale Labs Domain Security
  slug: skale-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: skale-labs
tags:
- Company
- Blockchain
- Web3
- Smart Contracts
- Developer Tools
- JSON-RPC
- AI Agents
- Privacy
- Payments
- Cryptocurrency
website: https://skale.space
---
