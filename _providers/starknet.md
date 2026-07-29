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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Starknet Agentic Access
  operation_count: 1
  slug: starknet-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 13
apis:
- description: Versioned JSON-RPC specification implemented by Starknet full nodes (Pathfinder, Juno, Papyrus) and infrastructure providers. Defines read methods (starknet_* for blocks, transactions, classes, state,
  name: Starknet JSON-RPC Specification
  slug: json-rpc
- description: 'Starknet Mainnet (chain ID SN_MAIN) is reached via the Starknet JSON-RPC at hosted providers — Infura, Alchemy, Blast, Nethermind Voyager, Lava, Chainstack — or via self-hosted Pathfinder / Juno full '
  name: Starknet Mainnet RPC (Public Providers)
  slug: mainnet-rpc
- description: Public JSON-RPC endpoint for Starknet Sepolia testnet (chain ID SN_SEPOLIA) for development and integration testing.
  name: Starknet Sepolia RPC (Public Providers)
  slug: sepolia-rpc
- description: Canonical L1<->L2 bridge for ETH and ERC-20 tokens between Ethereum and Starknet, operated by StarkWare. Bridge contracts are open-source.
  name: StarkGate Bridge
  slug: starkgate-bridge
- description: JavaScript / TypeScript SDK for Starknet — providers, accounts, contract classes, ABI parsing, transaction signing, and integration with browser wallets via the wallet API (get-starknet).
  name: starknet.js SDK
  slug: starknet-js
- description: Python SDK for Starknet maintained by Software Mansion, covering account / contract interaction, Cairo ABI handling, and the Starknet JSON-RPC.
  name: starknet.py SDK
  slug: starknet-py
- description: Rust SDK for Starknet with high-performance providers, accounts, contract bindings, ABI codegen, and Cairo serialization.
  name: starknet-rs SDK
  slug: starknet-rs
- description: Cairo is StarkWare's Turing-complete language for creating provable programs and the canonical smart contract language for Starknet. Distributed as the Cairo compiler (Rust) and the Scarb package mana
  name: Cairo Language
  slug: cairo
- description: Rust implementation of a Starknet full node from Equilibrium that serves the Starknet JSON-RPC, syncs from Ethereum L1 data, and verifies state transitions.
  name: Pathfinder Full Node
  slug: pathfinder
- description: Go implementation of a Starknet full node from Nethermind that serves the Starknet JSON-RPC and acts as a sequencer / RPC backend.
  name: Juno Full Node
  slug: juno
- description: Nethermind-built block explorer for Starknet Mainnet and Sepolia with a public REST API for blocks, transactions, contracts, classes, events, and tokens.
  name: Voyager Block Explorer
  slug: voyager-explorer
- description: Block explorer for Starknet Mainnet, Sepolia, and Sepolia Integration with a public REST API for blocks, transactions, events, classes, and NFTs.
  name: Starkscan Block Explorer
  slug: starkscan-explorer
- description: The Starknet JSON RPC API API from Starknet — 1 operation(s) for starknet json rpc api.
  name: Starknet Starknet JSON RPC API API
  slug: starknet-starknet-json-rpc-api-api
artifact_total: 21
asyncapis:
- description: AsyncAPI 2.6 description of the Starknet WebSocket JSON-RPC API as defined by the upstream `starknet_ws_api.json` OpenRPC specification (https://github.com/starkware-libs/starknet-specs/blob/master/ap
  name: Starknet WebSocket RPC API
  slug: starknet-asyncapi
collections:
- collection_type: open
  name: Starknet JSON-RPC API
  slug: open-starknet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/starknet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starknet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.starknet.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.starknet.io
- group: other
  title: ''
  type: Foundation
  url: https://www.starknet.io/foundation
- group: build
  title: ''
  type: GitHubStarkWare
  url: https://github.com/starkware-libs
- group: build
  title: ''
  type: GitHubStarknet
  url: https://github.com/starknet-io
- group: other
  title: ''
  type: Specs
  url: https://github.com/starkware-libs/starknet-specs
- group: other
  title: ''
  type: Bridge
  url: https://starkgate.starknet.io
- group: operate
  title: ''
  type: Community
  url: https://community.starknet.io
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Starknet
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/starknet-community
- group: other
  title: ''
  type: Telegram
  url: https://t.me/sncorestars
- group: company
  title: ''
  type: Blog
  url: https://www.starknet.io/blog
created: '2026-05-23'
description: Starknet is a permissionless Ethereum Layer 2 validity rollup developed by StarkWare, powered by STARK proofs and the Cairo smart contract language. Developers interact with Starknet via a versioned Starknet JSON-RPC (served by Pathfinder, Juno, and Papyrus full nodes as well as Infura / Alchemy / Blast / Nethermind providers), the Cairo toolchain (Scarb, Starknet Foundry, Cairo compiler, cairo-vm), client SDKs (starknet.js, starknet.py, starknet-rs), the StarkGate canonical bridge between Ethereum and Starknet, and Voyager / Starkscan block explorers.
finops:
- name: Starknet Finops
  service_category: API
  slug: starknet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/starknet.png
layout: provider
modified: '2026-05-29'
name: Starknet
nav: Providers
network: true
overview: 'Starknet publishes 2 APIs on the [APIs.io](https://apis.io/) network: JSON-RPC Specification and Starknet JSON RPC API API. Tagged areas include Layer 2, Ethereum, Validity Rollup, ZK, and Cairo.


  The Starknet catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Starknet''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Starknet Plans Pricing
  plan_count: 1
  slug: starknet-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 2
  name: Starknet Rate Limits
  slug: starknet-rate-limits
rules:
- name: Starknet API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: starknet-asyncapi-spectral-rules
score:
  band: thin
  composite: 39.7
  delta: -3.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.7
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 21.1
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/starknet/refs/heads/main/screenshots/starknet-2026-06-20T194515.png
security:
- kind: domain-security
  name: Starknet Domain Security
  slug: starknet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: starknet
tags:
- Layer 2
- Ethereum
- Validity Rollup
- ZK
- Cairo
- STARK
- JSON-RPC
- Bridge
website: https://www.starknet.io
---
