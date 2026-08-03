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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.3
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Arbitrum Agentic Access
  operation_count: 1
  slug: arbitrum-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 10
apis:
- description: Public Ethereum JSON-RPC endpoint for Arbitrum One mainnet (chain ID 42161), the flagship optimistic rollup secured directly by Ethereum L1. Supports standard eth_* methods plus Arbitrum-specific prec
  name: Arbitrum One JSON-RPC
  slug: one-rpc
- description: Public Ethereum JSON-RPC endpoint for Arbitrum Nova (chain ID 42170), an AnyTrust chain with a Data Availability Committee for high-throughput, low-cost transactions suited to gaming and social apps.
  name: Arbitrum Nova JSON-RPC
  slug: nova-rpc
- description: Public Ethereum JSON-RPC endpoint for the Arbitrum Sepolia testnet (chain ID 421614).
  name: Arbitrum Sepolia JSON-RPC
  slug: sepolia-rpc
- description: Canonical cross-chain bridge for transferring ETH and ERC-20 tokens between Ethereum L1, Arbitrum One, Arbitrum Nova, and connected Orbit chains. Bridge operations and underlying token-bridge contract
  name: Arbitrum Bridge
  slug: bridge
- description: Official TypeScript SDK (@arbitrum/sdk) for cross-chain interactions — building L1-to-L2 and L2-to-L1 messages, deposit and withdrawal flows, retryable tickets, and gas estimation for Arbitrum chains.
  name: Arbitrum SDK
  slug: sdk
- description: Stylus lets developers write EVM-compatible smart contracts in Rust, C, and C++ that compile to WASM and run alongside Solidity contracts. The Rust SDK provides storage primitives, host I/O, and macro
  name: Stylus SDK (Rust)
  slug: stylus-sdk
- description: Open-source Nitro node implementation that runs Arbitrum One, Nova, and Orbit chains. Includes the sequencer, batch poster, validator, and a fork of go- ethereum patched for Arbitrum's execution layer
  name: Arbitrum Nitro
  slug: nitro
- description: TypeScript SDK and tooling for deploying and operating Orbit chains — custom Arbitrum L2 / L3 chains that settle to Arbitrum One, Nova, or other Orbit chains.
  name: Arbitrum Orbit SDK
  slug: orbit-sdk
- description: Etherscan-family block explorer for Arbitrum One, Nova, and Sepolia with a public REST API for contracts, transactions, and addresses.
  name: Arbiscan Block Explorer
  slug: arbiscan-explorer
- description: Ethereum-compatible JSON-RPC 2.0 endpoint
  name: Arbitrum JSON-RPC API
  slug: arbitrum-json-rpc-api
artifact_total: 18
asyncapis:
- description: 'AsyncAPI description of the WebSocket surface that Arbitrum exposes from publicly documented endpoints. ## Important scope notes (from Arbitrum docs) Arbitrum''s public RPC endpoints — `arb1.arbitrum.i'
  name: Arbitrum Public WebSocket APIs
  slug: arbitrum-asyncapi
collections:
- collection_type: open
  name: Arbitrum JSON-RPC API
  slug: open-arbitrum
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arbitrum-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arbitrum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arbitrum.io
- group: other
  title: ''
  type: Foundation
  url: https://arbitrum.foundation
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arbitrum.io
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OffchainLabs
- group: start
  title: ''
  type: Portal
  url: https://portal.arbitrum.io
- group: other
  title: ''
  type: Bridge
  url: https://bridge.arbitrum.io
- group: operate
  title: ''
  type: Status
  url: https://status.arbitrum.io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/arbitrum
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/arbitrum
- group: company
  title: ''
  type: Blog
  url: https://medium.com/offchainlabs
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.arbitrum.io/llms.txt
created: '2026-05-23'
description: Arbitrum is the Ethereum Layer 2 rollup ecosystem from Offchain Labs. It includes Arbitrum One (general-purpose rollup secured by Ethereum), Arbitrum Nova (AnyTrust chain for high-throughput, low-cost apps), Arbitrum Sepolia (testnet), and Arbitrum Orbit (settlement framework for custom L2 / L3 chains). Developers interact via standard Ethereum JSON-RPC, the Stylus SDK for Rust / C / C++ smart contracts, the Arbitrum SDK for cross-chain messaging and bridging, and the Arbitrum Bridge for canonical asset transfer between Ethereum and Arbitrum chains.
finops:
- name: Arbitrum Finops
  service_category: API
  slug: arbitrum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arbitrum.png
layout: provider
modified: '2026-05-29'
name: Arbitrum
nav: Providers
network: true
overview: 'Arbitrum publishes 4 APIs on the [APIs.io](https://apis.io/) network, including One JSON-RPC, Nova JSON-RPC, Sepolia JSON-RPC, and 1 more. Tagged areas include Layer 2, Ethereum, Rollup, JSON-RPC, and Stylus.


  The Arbitrum catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Arbitrum''s developer surface includes documentation, GitHub presence, developer portal, status page, engineering blog, and 8 more developer resources.'
plans:
- name: Arbitrum Plans Pricing
  plan_count: 1
  slug: arbitrum-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Arbitrum Rate Limits
  slug: arbitrum-rate-limits
rules:
- name: Arbitrum API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: arbitrum-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 68.9
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 26.3
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arbitrum/refs/heads/main/screenshots/arbitrum-2026-06-20T172358.png
security:
- kind: domain-security
  name: Arbitrum Domain Security
  slug: arbitrum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arbitrum
tags:
- Layer 2
- Ethereum
- Rollup
- JSON-RPC
- Stylus
- Nitro
- Orbit
- Bridge
website: https://arbitrum.io
---
