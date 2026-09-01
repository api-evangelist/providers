---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Linea Agentic Access
  operation_count: 4
  slug: linea-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Standard Ethereum JSON-RPC API plus Linea-specific extensions available at the public endpoint rpc.linea.build. Supports all eth_* methods (eth_blockNumber, eth_getBlockByNumber, eth_sendRawTransactio
  name: Linea JSON-RPC API
  slug: json-rpc-api
- description: Blockchain data APIs for Linea Mainnet backed by two explorer surfaces. The Lineascan (lineascan.build) explorer uses the Etherscan API V2 interface (chain ID 59144) with modules covering accounts (na
  name: Linea Explorer API (Lineascan / Blockscout)
  slug: explorer-api
- description: Token price history
  name: Linea Prices API
  slug: linea-prices-api
- description: ERC-20 token metadata and information
  name: Linea Tokens API
  slug: linea-tokens-api
artifact_total: 40
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Linea Token Prices API
  slug: open-linea-prices-api
- collection_type: open
  name: Linea Token Prices Tokens API
  slug: open-linea-tokens-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/linea-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linea-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linea-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://linea.build
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linea.build
- group: docs
  title: ''
  type: APIReference
  url: https://docs.linea.build/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linea.build/get-started/build/quickstart/deploy
- group: other
  title: ''
  type: Explorer
  url: https://lineascan.build
- group: other
  title: ''
  type: Testnet
  url: https://sepolia.lineascan.build
- group: other
  title: ''
  type: Bridge
  url: https://bridge.linea.build
- group: commercial
  title: ''
  type: Pricing
  url: https://etherscan.io/apis?id=59144
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ConsenSys
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Consensys
- group: company
  title: ''
  type: XTwitter
  url: https://x.com/lineabuild
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/linea
- group: commercial
  title: ''
  type: Plans
  url: plans/linea-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linea-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/linea-finops.yml
created: '2026-06-13'
description: 'Linea is ConsenSys'' ZK-EVM Layer 2 network built on Ethereum, offering low fees, fast finality, and full EVM compatibility. Developers access on-chain data through three complementary API surfaces: a public JSON-RPC endpoint (rpc.linea.build) supporting all standard Ethereum methods plus Linea-specific extensions (linea_estimateGas, linea_getProof), a REST Token API (token-api.linea.build) for ERC-20 token metadata and price history, and the Lineascan block explorer API (Etherscan V2-compatible) for transactions, blocks, addresses, token transfers, event logs, and contract verification across Linea Mainnet (chainId 59144) and Sepolia testnet (chainId 59141).'
examples:
- key_count: 3
  name: Get Token By Address
  slug: get-token-by-address
- key_count: 3
  name: Get Token Prices
  slug: get-token-prices
- key_count: 3
  name: Get Tokens
  slug: get-tokens
features:
- description: Full Ethereum JSON-RPC compatibility means existing Hardhat, Foundry, Truffle, ethers.js, viem, and web3.py tooling works unchanged on Linea.
  name: EVM-compatible JSON-RPC
- description: linea_estimateGas returns baseFeePerGas, priorityFeePerGas, and gasLimit including L1 finalization costs, enabling accurate fee budgeting on the ZK rollup.
  name: Linea-specific gas estimation
- description: Built-in account abstraction bundler methods (eth_sendUserOperation, eth_estimateUserOperationGas, Pimlico extensions) available on the public RPC.
  name: ERC-4337 bundler endpoint
- description: Dedicated REST service at token-api.linea.build for ERC-20 token listings, metadata, security scoring, and 24-hour price history without requiring an API key.
  name: Token REST API
- description: Lineascan implements the Etherscan API V2 interface, giving access to all standard explorer modules (accounts, transactions, contracts, tokens, logs, stats) via chain ID 59144.
  name: Etherscan-compatible explorer API
- description: Both Lineascan (Etherscan-style) and a Blockscout instance provide redundant explorer APIs with REST and GraphQL options.
  name: Dual explorer surfaces
finops:
- name: Linea Finops
  service_category: Blockchain
  slug: linea-finops
graphqls:
- description: 'The Linea GraphQL API is provided by the Blockscout-based block explorer at `explorer.linea.build`. It exposes blockchain data for Linea Mainnet (chain ID 59144) through a GraphQL interface, enabling '
  name: Linea GraphQL API
  slug: linea-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linea.png
integrations:
- description: Managed Linea RPC nodes with private endpoints and higher rate limits via MetaMask developer services.
  name: Infura
- description: Alchemy provides Linea RPC nodes with enhanced APIs, webhooks, and developer tooling.
  name: Alchemy
- description: Subgraphs can index Linea events for custom GraphQL queries over protocol data.
  name: The Graph
- description: Linea on-chain data is queryable via Dune for SQL-based analytics and dashboards.
  name: Dune Analytics
- description: Standard EVM development frameworks connect to Linea RPC without modification.
  name: Hardhat and Foundry
- description: Price oracles deployed on Linea provide on-chain price feeds for DeFi protocols.
  name: Chainlink and Pyth
json_schemas:
- name: PriceResponse
  property_count: 2
  slug: price-response
- name: TokenPage
  property_count: 2
  slug: token-page
- name: TokenResponse
  property_count: 10
  slug: token-response
jsonld:
- class_count: 5
  name: Linea Context
  property_count: 18
  slug: linea-context
layout: provider
modified: '2026-06-13'
name: Linea
nav: Providers
network: true
overview: 'Linea publishes 2 APIs on the [APIs.io](https://apis.io/) network: Prices API and Tokens API. Tagged areas include Blockchain, Ethereum, Layer 2, zkEVM, and Web3.


  The Linea catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Linea''s developer surface includes developer portal, documentation, API reference, getting-started guide, pricing, and 13 more developer resources.'
plans:
- name: Linea Plans
  plan_count: 8
  slug: linea-plans
random_paper: 17
rate_limits:
- limit_count: 10
  name: Linea Rate Limits
  slug: linea-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Linea API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: linea-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 36.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 61.7
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linea/refs/heads/main/screenshots/linea-2026-06-20T184539.png
security:
- kind: domain-security
  name: Linea Domain Security
  slug: linea-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Linea Vulnerability Disclosure
  slug: linea-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: linea
tags:
- Blockchain
- Ethereum
- Layer 2
- zkEVM
- Web3
- DeFi
- Smart Contracts
- JSON-RPC
- Tokens
- ConsenSys
use_cases:
- description: Query token balances, prices, and swap activity to power DEX front-ends, yield dashboards, and portfolio trackers on Linea.
  name: DeFi application development
- description: Deploy EVM contracts using standard tooling and verify source code via the Lineascan API for public transparency.
  name: Smart contract deployment and verification
- description: Track address activity, internal transactions, and ERC-20 transfers in real time for wallets, compliance, and analytics.
  name: Transaction monitoring
- description: Use linea_estimateGas to accurately budget L1+L2 costs before submitting transactions, avoiding under-gas failures.
  name: Gas cost optimization
- description: Pull token holder lists, supply data, price history, and security scores to build on-chain analytics and due-diligence tools.
  name: Token analytics
- description: Track deposit and withdrawal transactions across the Linea canonical bridge to Ethereum mainnet.
  name: Cross-chain bridge monitoring
website: https://linea.build
---
