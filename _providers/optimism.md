---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 44.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Optimism Agentic Access
  operation_count: 1
  slug: optimism-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 10
apis:
- description: Public Ethereum JSON-RPC endpoint for OP Mainnet (chain ID 10). Supports standard eth_* methods plus Optimism extensions for L1 fee estimation, deposit tracking, and withdrawal proving. Public endpoin
  name: OP Mainnet JSON-RPC
  slug: mainnet-rpc
- description: Public Ethereum JSON-RPC endpoint for the OP Sepolia testnet (chain ID 11155420) used for development and integration testing.
  name: OP Sepolia JSON-RPC
  slug: sepolia-rpc
- description: Canonical cross-chain bridge for depositing and withdrawing ETH and ERC-20 tokens between Ethereum L1 and OP Mainnet, secured by the OP Stack StandardBridge contracts. Available as a hosted app and vi
  name: Optimism Bridge (Standard Bridge)
  slug: bridge
- description: Open-source, modular Ethereum L2 rollup stack. The monorepo at github.com/ethereum-optimism/optimism contains op-geth (execution), op-node (consensus), op-batcher, op-proposer, op-challenger, op-deplo
  name: OP Stack
  slug: op-stack
- description: Source-of-truth index of chains that are part of the Optimism Superchain — genesis files, deployment addresses, RPC endpoints, explorers, and chain metadata in machine-readable form.
  name: Superchain Registry
  slug: superchain-registry
- description: Modern Optimism SDK exposed as a Viem extension (viem/op-stack) for L1<->L2 message tracking, deposit and withdrawal flows, fee estimation, and Superchain multi-chain helpers.
  name: Optimism SDK (Viem extension)
  slug: viem-sdk
- description: Local Superchain simulator that spins up multiple OP Stack chains for developing and testing cross-chain interop messages (CrossL2Inbox / L2ToL2CrossDomainMessenger) before mainnet rollout.
  name: Supersim
  slug: supersim
- description: Etherscan-family block explorer for OP Mainnet and OP Sepolia with REST API access for contracts, transactions, and addresses.
  name: Optimism Etherscan
  slug: etherscan-explorer
- description: Open-source Blockscout block explorer for OP Mainnet with REST and GraphQL APIs.
  name: Optimism Blockscout
  slug: blockscout-explorer
- description: Standard Ethereum JSON-RPC method invocation.
  name: Optimism JSON-RPC API
  slug: optimism-json-rpc-api
artifact_total: 19
asyncapis:
- description: 'AsyncAPI 2.6 description of the WebSocket JSON-RPC subscription surface exposed by op-geth — the OP Stack execution client used by OP Mainnet (chain ID 10) and OP Sepolia (chain ID 11155420). ## Publi'
  name: Optimism (OP Stack) WebSocket JSON-RPC API
  slug: optimism-asyncapi
collections:
- collection_type: open
  name: OP Mainnet JSON-RPC
  slug: open-optimism
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/optimism-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/optimism-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.optimism.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.optimism.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ethereum-optimism
- group: other
  title: ''
  type: Specs
  url: https://specs.optimism.io
- group: start
  title: ''
  type: SuperchainRegistry
  url: https://github.com/ethereum-optimism/superchain-registry
- group: other
  title: ''
  type: Governance
  url: https://gov.optimism.io
- group: operate
  title: ''
  type: Status
  url: https://status.optimism.io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Optimism
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/optimism
- group: company
  title: ''
  type: Blog
  url: https://blog.oplabs.co
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.optimism.io/llms.txt
created: '2026-05-23'
description: Optimism is an Ethereum Layer 2 scaling network and the originator of the OP Stack — an open-source, modular rollup framework that powers OP Mainnet and a growing Superchain of interoperable chains (Base, Mode, Zora, Worldchain, and others). Developers interact via standard Ethereum JSON-RPC, the Optimism (Viem-based) SDK, the canonical Optimism Bridge, OP Stack operator tooling (op-geth, op-node, op-deployer, op-batcher, op-proposer, op-challenger), and the Superchain Registry.
finops:
- name: Optimism Finops
  service_category: API
  slug: optimism-finops
graphqls:
- description: ''
  name: Optimism GraphQL API
  slug: optimism-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimism.png
layout: provider
modified: '2026-05-29'
name: Optimism
nav: Providers
network: true
overview: 'Optimism publishes 3 APIs on the [APIs.io](https://apis.io/) network: OP Mainnet JSON-RPC, OP Sepolia JSON-RPC, and JSON-RPC API. Tagged areas include Layer 2, Ethereum, OP Stack, Superchain, and JSON-RPC.


  The Optimism catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Optimism''s developer surface includes documentation, GitHub presence, status page, engineering blog, and 9 more developer resources.'
plans:
- name: Optimism Plans Pricing
  plan_count: 1
  slug: optimism-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 2
  name: Optimism Rate Limits
  slug: optimism-rate-limits
rules:
- name: Optimism API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: optimism-asyncapi-spectral-rules
score:
  band: developing
  composite: 45.7
  delta: 3.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.1
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 60.5
    operational_transparency: 26.3
  previous_composite: 42.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optimism/refs/heads/main/screenshots/optimism-2026-06-20T191109.png
security:
- kind: domain-security
  name: Optimism Domain Security
  slug: optimism-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: optimism
tags:
- Layer 2
- Ethereum
- OP Stack
- Superchain
- JSON-RPC
- Rollup
- Bridge
website: https://www.optimism.io
---
