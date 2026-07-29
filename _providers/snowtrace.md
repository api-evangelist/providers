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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Snowtrace Agentic Access
  operation_count: 29
  slug: snowtrace-agentic-access
  summary_line: 29 operations · 1 acting
api_count: 17
apis:
- description: Retrieve address balances, normal and internal transaction histories, ERC-20 token transfers, ERC-721 NFT transfers, ERC-1155 token transfers, and historical balance data by block number for any EVM a
  name: Routescan Etherscan-Compatible Account API
  slug: routescan-etherscan-compatible-account-api
- description: Query block rewards and estimated block countdown for specific block numbers on any Routescan-indexed EVM chain.
  name: Routescan Etherscan-Compatible Block API
  slug: routescan-etherscan-compatible-block-api
- description: Access verified smart contract ABIs, source code, and creation transaction data. Supports contract source code verification via POST with up to 250 verifications per day, and status checking for verif
  name: Routescan Etherscan-Compatible Contract API
  slug: routescan-etherscan-compatible-contract-api
- description: Query event logs emitted by smart contracts using filter parameters including address, block range, and up to four indexed topics. Useful for tracking on-chain events in real time.
  name: Routescan Etherscan-Compatible Logs API
  slug: routescan-etherscan-compatible-logs-api
- description: Retrieve ERC-20 token supply, token holder information, and token metadata for fungible tokens on Routescan-indexed EVM chains.
  name: Routescan Etherscan-Compatible Token API
  slug: routescan-etherscan-compatible-token-api
- description: Access network statistics including total AVAX supply, last price, and validator/node count for the Avalanche C-Chain and other supported EVM networks.
  name: Routescan Etherscan-Compatible Stats API
  slug: routescan-etherscan-compatible-stats-api
- description: Check transaction execution status (success or failure) and receipt status for any transaction hash on Routescan-indexed EVM chains.
  name: Routescan Etherscan-Compatible Transaction API
  slug: routescan-etherscan-compatible-transaction-api
- description: Ethereum JSON-RPC compatible proxy endpoints for standard methods including eth_blockNumber, eth_getBlockByNumber, eth_getTransactionByHash, eth_getTransactionReceipt, eth_call, eth_gasPrice, and eth_
  name: Routescan Geth/Parity Proxy API
  slug: routescan-gethparity-proxy-api
- description: Retrieve address labels and nametags applied to known wallets, contracts, and entities indexed by Routescan across all supported EVM chains.
  name: Routescan Nametags API
  slug: routescan-nametags-api
- description: Address balance and transaction history endpoints.
  name: Routescan (Snowtrace) Accounts API
  slug: snowtrace-accounts-api
- description: Block rewards and countdown endpoints.
  name: Routescan (Snowtrace) Blocks API
  slug: snowtrace-blocks-api
- description: Smart contract ABI, source code, and verification endpoints.
  name: Routescan (Snowtrace) Contracts API
  slug: snowtrace-contracts-api
- description: Smart contract event log query endpoints.
  name: Routescan (Snowtrace) Logs API
  slug: snowtrace-logs-api
- description: Ethereum JSON-RPC compatible proxy endpoints.
  name: Routescan (Snowtrace) Proxy API
  slug: snowtrace-proxy-api
- description: Network statistics including token supply and prices.
  name: Routescan (Snowtrace) Stats API
  slug: snowtrace-stats-api
- description: ERC-20 token supply and holder endpoints.
  name: Routescan (Snowtrace) Tokens API
  slug: snowtrace-tokens-api
- description: Transaction execution and receipt status endpoints.
  name: Routescan (Snowtrace) Transactions API
  slug: snowtrace-transactions-api
artifact_total: 33
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snowtrace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snowtrace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snowtrace-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: /openapi/openapi.yml
- group: start
  title: ''
  type: Portal
  url: https://snowtrace.io/
- group: docs
  title: ''
  type: Documentation
  url: https://snowtrace.io/documentation
- group: commercial
  title: ''
  type: Plans
  url: https://snowtrace.io/documentation
- group: start
  title: ''
  type: Signup
  url: https://routescan.io/
- group: operate
  title: ''
  type: Contact
  url: https://snowtrace.io/contactus
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snowtrace.io/
- group: operate
  title: ''
  type: Status
  url: https://snowtrace.io/
- group: commercial
  title: ''
  type: Plans
  url: /plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: /rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: /finops/finops.yml
created: '2026-06-13'
description: Routescan is the first multichain ecosystem explorer, search, API, and analytics platform for all major EVM chains. Operating as Snowtrace for Avalanche C-Chain, Routescan provides high-speed REST APIs compatible with the Etherscan API format, delivering near real-time access to transactions, token transfers, smart contract data, and event logs across Avalanche C-Chain, Arbitrum, Optimism, Base, and 40+ other EVM networks. A single API key grants multichain access across all indexed chains.
examples:
- key_count: 4
  name: Get Balance
  slug: get-balance
- key_count: 4
  name: Get Contract Abi
  slug: get-contract-abi
- key_count: 4
  name: Get Erc20 Transfers
  slug: get-erc20-transfers
- key_count: 4
  name: Get Logs
  slug: get-logs
- key_count: 3
  name: Get Normal Transactions
  slug: get-normal-transactions
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://snowtrace.io/favicon.ico
json_schemas:
- name: Routescan API Response Envelope
  property_count: 3
  slug: api-response
- name: Routescan Token Transfer
  property_count: 19
  slug: token-transfer
- name: Routescan Transaction
  property_count: 20
  slug: transaction
jsonld:
- class_count: 6
  name: context Context
  property_count: 27
  slug: context
layout: provider
modified: '2026-06-13'
name: Routescan (Snowtrace)
nav: Providers
network: true
overview: 'Routescan (Snowtrace) publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Contracts API, and 5 more. Tagged areas include Blockchain, Explorer, Avalanche, EVM, and Multichain.


  The Routescan (Snowtrace) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Routescan (Snowtrace)''s developer surface includes authentication, developer portal, documentation, signup flow, status page, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 6
  slug: plans
random_paper: 22
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Routescan (Snowtrace) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: snowtrace-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.5
  delta: -4.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.0
    developer_ergonomics: 28.3
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Snowtrace Authentication
  slug: snowtrace-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Snowtrace Domain Security
  slug: snowtrace-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: snowtrace
tags:
- Blockchain
- Explorer
- Avalanche
- EVM
- Multichain
- Web3
- Transactions
- Smart Contracts
- NFTs
- DeFi
website: https://snowtrace.io/
---
