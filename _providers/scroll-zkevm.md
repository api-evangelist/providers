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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Scroll Zkevm Agentic Access
  operation_count: 1
  slug: scroll-zkevm-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Standard Ethereum JSON-RPC interface for Scroll mainnet (chain ID 534352). Used by wallets, dApps, indexers, and tools to read chain state and submit transactions. Compatible with eth_*, net_*, web3_*
  name: Scroll JSON-RPC (Mainnet)
  slug: json-rpc-mainnet
- description: Standard Ethereum JSON-RPC endpoint for Scroll Sepolia testnet (chain ID 534351), used for development, integration testing, and contract deployment dry runs before mainnet.
  name: Scroll JSON-RPC (Sepolia Testnet)
  slug: json-rpc-sepolia
- description: Etherscan-compatible REST API for Scroll mainnet served by Scrollscan - block, transaction, account, token, contract verification, gas, and event log endpoints. Used by analytics dashboards, portfolio
  name: Scrollscan API
  slug: scrollscan-api
- description: Etherscan-compatible REST API for the Scroll Sepolia testnet explorer, mirroring the mainnet Scrollscan API surface for development use.
  name: Scrollscan API (Sepolia)
  slug: scrollscan-sepolia-api
- description: Web explorer for Scroll rollup batches and proof status - shows L1 batch commit, finalization, and proof submission for each L2 batch. Useful for bridge operators and users tracking L2 to L1 message f
  name: Scroll Rollup Scanner
  slug: rollup-explorer
- description: Canonical L1 <-> L2 bridge for ETH, ERC-20, and arbitrary messages between Ethereum mainnet and Scroll. Backed by the L1 and L2 Scroll Messenger and Gateway contracts; dApps integrate via the publishe
  name: Scroll Native Bridge
  slug: bridge
- description: Solidity contracts that implement the Scroll rollup - L1 / L2 messengers, gateways, ScrollChain commit/finalize logic, and the proving system verifiers. Reference implementation used to integrate with
  name: Scroll Contracts
  slug: contracts
- description: Scroll's fork of go-ethereum that runs the Scroll zkEVM execution layer and serves the JSON-RPC API. Used by node operators and infrastructure providers running Scroll nodes.
  name: Scroll go-ethereum (l2geth)
  slug: go-ethereum
- baseURL: https://rpc.scroll.io
  baseurl_source: declared
  description: Ethereum JSON-RPC over HTTP POST
  name: Scroll JSON-RPC API
  slug: scroll-zkevm-json-rpc-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scroll JSON-RPC API
  slug: open-scroll-zkevm-json-rpc-api
- collection_type: open
  name: Scroll JSON-RPC
  slug: open-scroll-zkevm
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/scroll-tech/scroll-contracts/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/scroll-tech/scroll-contracts/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scroll-zkevm-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scroll-zkevm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scroll.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scroll.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/scroll-tech
- group: other
  title: ''
  type: Explorer
  url: https://scrollscan.com/
- group: company
  title: ''
  type: Blog
  url: https://scroll.io/blog
- group: other
  title: ''
  type: X
  url: https://x.com/Scroll_ZKP
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/scroll
created: '2026-05-23'
description: Scroll is a native zkEVM Layer 2 for Ethereum, built by Scroll Foundation, that uses zero-knowledge proofs to scale Ethereum while preserving bytecode equivalence with the EVM. Developer surface is dominated by standard Ethereum JSON-RPC endpoints on mainnet and Sepolia testnet, the Scrollscan block explorer (with an Etherscan-compatible REST API), a canonical L1<>L2 bridge with messenger contracts, and a rollup explorer that surfaces batch and proof status. dApp builders use Scroll as a drop-in EVM target with Hardhat, Foundry, viem, ethers, and other standard EVM tooling.
finops:
- name: Scroll Zkevm Finops
  service_category: API
  slug: scroll-zkevm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scroll-zkevm.png
layout: provider
modified: '2026-05-23'
name: Scroll
nav: Providers
network: true
overview: 'Scroll publishes 1 API on the [APIs.io](https://apis.io/) network: JSON-RPC API. Tagged areas include zkEVM, Layer 2, Ethereum, Rollup, and Zero Knowledge.


  Scroll''s developer surface includes documentation, GitHub presence, engineering blog, and 8 more developer resources.'
plans:
- name: Scroll Zkevm Plans Pricing
  plan_count: 1
  slug: scroll-zkevm-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Scroll Zkevm Rate Limits
  slug: scroll-zkevm-rate-limits
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scroll-zkevm/refs/heads/main/screenshots/scroll-zkevm-2026-06-20T193608.png
security:
- kind: domain-security
  name: Scroll Zkevm Domain Security
  slug: scroll-zkevm-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scroll-zkevm
tags:
- zkEVM
- Layer 2
- Ethereum
- Rollup
- Zero Knowledge
- JSON-RPC
- Crypto
- Web3
website: https://scroll.io/
---
