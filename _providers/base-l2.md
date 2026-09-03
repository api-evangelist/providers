---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - '{''url'': ''https://www.smartwallet.dev'', ''status'': 308, ''note'': ''declared website redirects to https://www.base.org/ — a different registrable domain (smartwallet.dev -> base.org), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Base L2 Agentic Access
  operation_count: 1
  slug: base-l2-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Standard Ethereum JSON-RPC endpoint for Base Mainnet (chain ID 8453). Supports eth_*, net_*, web3_*, and Optimism-specific extensions for fee estimation and L1 messaging. The public endpoint is rate-l
  name: Base Mainnet JSON-RPC
  slug: mainnet-rpc
- description: Public JSON-RPC endpoint for the Base Sepolia testnet (chain ID 84532) used for development, contract deployment, and integration testing.
  name: Base Sepolia JSON-RPC
  slug: sepolia-rpc
- description: Pre-confirmation JSON-RPC endpoint exposing Flashblocks — sub-block streams of ordered transactions that allow apps to react to pending state with sub-second latency.
  name: Base Flashblocks RPC
  slug: flashblocks-rpc
- description: Canonical cross-chain bridge between Ethereum L1 and Base L2 for depositing and withdrawing ETH and ERC-20 tokens, secured by the OP Stack bridge contracts.
  name: Base Bridge
  slug: bridge
- description: Cross-chain bridge enabling asset transfers between Base and Solana, integrated into the Base ecosystem app surface.
  name: Base / Solana Bridge
  slug: solana-bridge
- description: Base Account (formerly Coinbase Smart Wallet) is an ERC-4337 smart contract wallet with passkey sign-in, sub-accounts, session keys, sponsored transactions via paymaster, and SDK + React component int
  name: Base Account / Smart Wallet
  slug: account
- description: React component library and TypeScript SDK (@coinbase/onchainkit) for building onchain apps on Base — wallet, identity, transaction, swap, checkout, fund, and NFT components with built-in Smart Wallet
  name: OnchainKit
  slug: onchainkit
- description: Etherscan-family block explorer for Base Mainnet and Sepolia with a public contract / transaction / address API.
  name: BaseScan Block Explorer
  slug: basescan-explorer
- description: Blockscout-powered open-source block explorer for Base with REST and GraphQL APIs.
  name: Base Blockscout Block Explorer
  slug: blockscout-explorer
- baseURL: https://mainnet.base.org
  baseurl_source: declared
  description: Ethereum JSON-RPC 2.0 endpoint
  name: Base JSON-RPC API
  slug: base-l2-json-rpc-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Base JSON-RPC API
  slug: open-base-l2-json-rpc-api
- collection_type: open
  name: Base JSON-RPC API
  slug: open-base-l2
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/coinbase/onchainkit/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/coinbase/onchainkit/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/coinbase/onchainkit/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/base-l2-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/base-l2-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.base.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.base.org
- group: build
  title: ''
  type: GitHub
  url: https://github.com/base-org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/base
- group: operate
  title: ''
  type: Status
  url: https://status.base.org
- group: other
  title: ''
  type: Bridge
  url: https://bridge.base.org
- group: other
  title: ''
  type: Ecosystem
  url: https://www.base.org/ecosystem
- group: company
  title: ''
  type: Twitter
  url: https://x.com/base
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/buildonbase
- group: company
  title: ''
  type: Blog
  url: https://base.mirror.xyz
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.base.org/llms.txt
created: '2026-05-23'
description: Base is Coinbase's Ethereum Layer 2 network built on the OP Stack and part of the Optimism Superchain. It exposes a standard Ethereum JSON-RPC interface for smart contracts and dApps, plus higher-level developer surfaces including Base Account (Smart Wallet, Sub Accounts, passkeys, paymaster-sponsored transactions), OnchainKit React components, Mini Apps, the canonical Bridge to Ethereum, and a Solana cross- chain bridge. Block exploration is available through BaseScan and Blockscout.
finops:
- name: Base L2 Finops
  service_category: API
  slug: base-l2-finops
graphqls:
- description: ''
  name: Base GraphQL API
  slug: base-l2-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/base-l2.png
layout: provider
modified: '2026-05-23'
name: Base
nav: Providers
network: true
overview: 'Base publishes 1 API on the [APIs.io](https://apis.io/) network: JSON-RPC API. Tagged areas include Layer 2, Ethereum, OP Stack, Superchain, and JSON-RPC.


  Base''s developer surface includes documentation, GitHub presence, status page, engineering blog, and 12 more developer resources.'
plans:
- name: Base L2 Plans Pricing
  plan_count: 1
  slug: base-l2-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Base L2 Rate Limits
  slug: base-l2-rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 25.0
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/base-l2/refs/heads/main/screenshots/base-l2-2026-06-20T173043.png
security:
- kind: domain-security
  name: Base L2 Domain Security
  slug: base-l2-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: base-l2
tags:
- Layer 2
- Ethereum
- OP Stack
- Superchain
- JSON-RPC
- Smart Wallet
- Bridge
website: https://www.base.org
---
