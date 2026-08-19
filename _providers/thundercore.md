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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: Ethereum-compatible JSON-RPC 2.0 API for the ThunderCore mainnet (chain ID 108, TT gas token). Supports the standard eth_/net_/web3_ method surface over HTTPS, with WebSocket endpoints for subscriptio
  name: ThunderCore Mainnet JSON-RPC API
  slug: thundercore-mainnet-json-rpc-api
- description: Ethereum-compatible JSON-RPC 2.0 API for the ThunderCore testnet (chain ID 18, TST gas token), with a faucet that dispenses TST every 86400 seconds for testing DApps without risking real assets.
  name: ThunderCore Testnet JSON-RPC API
  slug: thundercore-testnet-json-rpc-api
- description: Etherscan-compatible REST API (?module=&action=) and ETH RPC API exposed by the BlockScout block explorer for the ThunderCore mainnet — accounts, transactions, token balances, contract verification, a
  name: ThunderCore Explorer API (BlockScout)
  slug: thundercore-explorer-api-blockscout
- description: GraphQL query surface over official ThunderCore subgraphs (TTSwap DEX and TT Mining) served from ThunderCore's Graph node; third-party subgraph deployment is available on request via support@thunderco
  name: ThunderCore Subgraph GraphQL API
  slug: thundercore-subgraph-graphql-api
artifact_total: 9
asyncapis:
- description: GENERATED (not provider-published) AsyncAPI description of ThunderCore's documented WebSocket endpoints. ThunderCore publishes WebSocket URLs for mainnet and testnet and recommends WebSockets for havi
  name: ThunderCore WebSocket JSON-RPC event surface
  slug: thundercore-ws-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thundercore-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thundercore.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developers.thundercore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.thundercore.com/
- group: docs
  title: ''
  type: APIReference
  url: https://explorer-mainnet.thundercore.com/eth-rpc-api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developers.thundercore.com/deploying-on-thundercore
- group: operate
  title: ''
  type: Support
  url: https://help.thundercore.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://news.thundercore.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thundercore
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thundercore.com/documents/tc.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thundercore.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/4117254/ethereum-json-rpc/RVu7CT5J?version=latest
- group: other
  title: ''
  type: Whitepaper
  url: https://docs.thundercore.com/thunder-whitepaper.pdf
- group: build
  title: ''
  type: Packages
  url: packages/thundercore-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thundercore-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thundercore-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thundercore-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/thundercore-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thundercore-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thundercore-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thundercore-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thundercore-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thundercore-conventions.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/thundercore-ws-asyncapi.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thundercore-rate-limits.yml
created: '2026-07-17'
description: ThunderCore is an EVM-compatible layer-1 public blockchain with roughly one-second block times and single-block finality, using TT as its native gas token (chain ID 108). Its external protocol is Ethereum-compatible, so standard Ethereum JSON-RPC methods, wallets, and Solidity toolchains (Hardhat, Foundry, Truffle, Remix) work against the public RPC and WebSocket endpoints, alongside a BlockScout explorer API, official subgraphs on The Graph, a cross-chain bridge, and a public testnet with a faucet. Backed by Pantera Capital.
image: https://www.thundercore.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: thundercore-mcp.yml
  slug: thundercore-mcpyml
modified: '2026-07-21'
name: ThunderCore
nav: Providers
network: true
overview: 'ThunderCore publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, EVM, and JSON-RPC.


  The ThunderCore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThunderCore''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 18 more developer resources.'
random_paper: 144
rate_limits:
- limit_count: 4
  name: Thundercore Rate Limits
  slug: thundercore-rate-limits
score:
  band: developing
  composite: 42.9
  delta: -3.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 45.1
    developer_ergonomics: 76.2
    discoverability: 92.6
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 45.9
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thundercore/refs/heads/main/screenshots/thundercore-2026-08-17T082355.png
security:
- kind: authentication
  name: Thundercore Authentication
  slug: thundercore-authentication
  summary_line: none/cryptographic-signature · 3 schemes
- kind: domain-security
  name: Thundercore Domain Security
  slug: thundercore-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: thundercore
tags:
- Company
- Crypto
- Blockchain
- EVM
- JSON-RPC
- Web3
- Layer 1
website: https://www.thundercore.com/
---
