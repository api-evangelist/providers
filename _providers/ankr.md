---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Ankr Agentic Access
  operation_count: 26
  slug: ankr-agentic-access
  summary_line: 26 operations · 20 acting
api_count: 9
apis:
- description: AnkrScan is Ankr's multi-chain block explorer covering EVM and non-EVM networks. It is a hosted UI consuming Ankr's Node API and Advanced API and does not currently publish a public REST surface.
  name: AnkrScan Block Explorer
  slug: ankr-block-explorer
- description: Standard Ethereum JSON-RPC envelope shared by every EVM chain.
  name: ankr EVM API
  slug: ankr-evm-api
- description: Liquid staking pool statistics (TVL, APR, holders, supply).
  name: ankr Metrics API
  slug: ankr-metrics-api
- description: NFT methods — ownership, metadata, holders, and transfer history.
  name: ankr NFT API
  slug: ankr-nft-api
- description: Query methods — blockchain statistics, blocks, logs, transactions, interactions.
  name: ankr Query API
  slug: ankr-query-api
- description: Trustless exchange ratio between native and liquid staking tokens.
  name: ankr Ratio API
  slug: ankr-ratio-api
- description: Time-based and event-triggered automation tasks.
  name: ankr Tasks API
  slug: ankr-tasks-api
- description: Token methods — balances, prices, holders, currencies, and transfers.
  name: ankr Token API
  slug: ankr-token-api
- description: Validator metadata, unbond times, reward release windows.
  name: ankr Validators API
  slug: ankr-validators-api
arazzos:
- description: Read full blocks for a range, then pull event logs from the same range.
  name: Ankr Block And Log Inspection
  slug: ankr-block-log-inspection-workflow
- description: Read a chain's aggregate stats, then its supported currency catalog.
  name: Ankr Chain Overview
  slug: ankr-chain-overview-workflow
- description: Pull a collection's holders and then its transfer history.
  name: Ankr NFT Collection Audit
  slug: ankr-nft-collection-audit-workflow
- description: List the NFTs owned by a wallet, then enrich one with full metadata.
  name: Ankr Wallet NFT Inventory
  slug: ankr-nft-inventory-workflow
- description: Count an ERC-20 token's holders, then list them and read its price.
  name: Ankr Token Holder Distribution
  slug: ankr-token-holder-distribution-workflow
- description: Read a token's current price, then its historical price series.
  name: Ankr Token Price And History
  slug: ankr-token-price-and-history-workflow
- description: Pull a wallet's transactions, then decode the most recent one in full.
  name: Ankr Transaction Deep Dive
  slug: ankr-transaction-deep-dive-workflow
- description: Discover the chains a wallet uses, then pull its transaction history.
  name: Ankr Wallet Cross-Chain Activity
  slug: ankr-wallet-cross-chain-activity-workflow
- description: Read a wallet's token balances and then its recent ERC-20 transfer history.
  name: Ankr Wallet Portfolio Snapshot
  slug: ankr-wallet-portfolio-workflow
artifact_total: 68
asyncapis:
- description: 'AsyncAPI description of Ankr''s WebSocket JSON-RPC surface for blockchain subscriptions. Ankr exposes a single multichain WSS endpoint at `wss://rpc.ankr.com/{chain_slug}/{apiKey}` for every chain its '
  name: Ankr RPC Service — WebSocket Subscriptions
  slug: ankr-asyncapi
- description: ''
  name: Review
  slug: review
collections:
- collection_type: postman
  name: Ankr Advanced API
  slug: postman-ankr-advanced-api
- collection_type: postman
  name: Ankr Contract Automation API
  slug: postman-ankr-automation-api
- collection_type: postman
  name: Ankr RPC Service (Node API)
  slug: postman-ankr-rpc-service
- collection_type: postman
  name: Ankr Liquid Staking API
  slug: postman-ankr-staking-api
- collection_type: open
  name: Ankr Advanced API
  slug: open-ankr-advanced-api
- collection_type: open
  name: Ankr Contract Automation API
  slug: open-ankr-automation-api
- collection_type: open
  name: Ankr RPC Service (Node API)
  slug: open-ankr-rpc-service
- collection_type: open
  name: Ankr Liquid Staking API
  slug: open-ankr-staking-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ankr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ankr-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ankr-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ankr/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-block-log-inspection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-chain-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-nft-collection-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-nft-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-token-holder-distribution-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-token-price-and-history-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-transaction-deep-dive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-wallet-cross-chain-activity-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ankr-wallet-portfolio-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.ankr.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.ankr.com/docs/
- group: start
  title: ''
  type: Signup
  url: https://www.ankr.com/rpc/
- group: other
  title: ''
  type: Dashboard
  url: https://www.ankr.com/rpc/projects/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ankr.com/rpc/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.ankr.com/blog/
- group: other
  title: ''
  type: Company
  url: https://www.ankr.com/about/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ankr
- group: operate
  title: ''
  type: Forums
  url: https://discord.com/invite/ankrnetwork
- group: operate
  title: ''
  type: Forums
  url: https://t.me/ankrnetwork
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ankr-network
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/ankr.js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/ankr-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/ankr-sdk-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/game-unity-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/game-unreal-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/game-unreal-aptos-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/ankr-compound-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Ankr-network/ankrscan-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/Ankr-network/ankr-cli
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Ankr-network/ankr-docs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Ankr-network/erigon
- group: other
  title: ''
  type: BlockExplorer
  url: https://ankrscan.io
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.ankr.com/reference/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.ankr.com/llms.txt
- group: operate
  title: ''
  type: Status
  url: https://status.ankr.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ankr.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ankr.com/privacy/
- group: commercial
  title: ''
  type: Plans
  url: plans/ankr-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ankr-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ankr-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ankr-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/ankr-rules.yml
created: '2026-05-25'
description: Ankr is a Web3 infrastructure provider whose multichain RPC, Advanced API, liquid staking, contract automation, and Rollup-as-a-Service products serve developers, exchanges, and enterprises across 80+ blockchains. The Node API exposes JSON-RPC and WebSocket endpoints at rpc.ankr.com/{chain}; the Advanced API (AAPI) layers an indexed query surface across 19 EVM mainnets for NFT, token, and historical-data reads. Ankr also operates liquid staking pools (ankrETH, ankrBNB, ankrPOL, ankrAVAX, ankrFTM, ankrDOT, ankrFLOW), a contract automation service on BNB Smart Chain, and an enterprise Rollup-as-a-Service practice that supports OP Stack, Polygon CDK, and Arbitrum Orbit variants. Infrastructure runs as a global DePIN of bare-metal nodes in 30+ regions serving roughly 8 billion daily RPC requests.
examples:
- key_count: 3
  name: Ankr Eth Rpc Call Example
  slug: ankr-eth-rpc-call-example
- key_count: 2
  name: Ankr Get Account Balance Example
  slug: ankr-get-account-balance-example
- key_count: 2
  name: Ankr Get Nfts By Owner Example
  slug: ankr-get-nfts-by-owner-example
features:
- 80+ blockchain networks behind a single multichain RPC surface (rpc.ankr.com/{chain})
- Average response time of 56ms with claimed 99.99% uptime across a 30+ region DePIN
- 8 billion daily RPC requests served as of May 2026
- Public Plan free with anonymous IP-scoped throttling — production should use Premium
- Premium Plan multiplies Node API throughput x50 and Advanced API x30
- WebSocket (WSS) endpoints, archive access, IP whitelisting, and multi-project statistics
- Advanced API — indexed JSON-RPC over 19 EVM mainnets exposing NFT, Token, and Query methods
- ankr_getAccountBalance returns native + ERC-20 balances across multiple chains in one call
- ankr_getNFTsByOwner / ankr_getNFTMetadata / ankr_getNFTHolders / ankr_getNftTransfers
- ankr_getTokenPrice and ankr_getTokenPriceHistory for on-chain pricing without third-party
- ankr_getLogs and ankr_getTransactionsByAddress for indexer-grade history reads
- Liquid staking on 7+ chains via ankrETH, ankrBNB, ankrPOL, ankrAVAX, ankrFTM, ankrDOT, ankrFLOW
- Liquid Staking RESTful metrics API (https://api.staking.ankr.com/v1.0/metrics)
- Trustless ratio oracles and PancakeSwap price oracle for ankr* tokens
- Smart Contract Automation on BNB Smart Chain with CRON + event triggers
- Rollup-as-a-Service (RaaS) — OP Stack, Polygon CDK, Arbitrum Orbit and custom appchains
- Bitcoin Secured Infrastructure for chains anchoring security to Bitcoin
- Enterprise DVN infrastructure on LayerZero for cross-chain messaging
- Recent RPC launches — HyperEVM, Unichain, AB Chain, Kite (AI Payment Blockchain)
- Powers AI / blockchain integrations including ChainGPT AI Hub V2 (March 2026)
- SDKs — ankr.js (TypeScript), ankr-python-sdk, Mirage Unity SDK, Mirage Unreal SDK
- AnkrScan multi-chain block explorer at ankrscan.io
- Open-source Erigon and BSC-Erigon forks operated for archive workloads
finops:
- name: Ankr Finops
  service_category: Blockchain Infrastructure
  slug: ankr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ankr.png
json_schemas:
- name: Ankr Account Balance
  property_count: 2
  slug: ankr-account-balance
- name: Ankr NFT Asset
  property_count: 10
  slug: ankr-nft-asset
- name: Ankr Liquid Staking Metrics
  property_count: 6
  slug: ankr-staking-metrics
json_structures:
- name: Ankr Account Balance Structure
  property_count: 0
  slug: ankr-account-balance-structure
jsonld:
- class_count: 25
  name: Ankr Context
  property_count: 5
  slug: ankr-context
layout: provider
modified: '2026-05-29'
name: ankr
nav: Providers
network: true
overview: 'ankr publishes 8 APIs on the [APIs.io](https://apis.io/) network, including EVM API, Metrics API, NFT API, and 5 more.


  The ankr catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  ankr''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, engineering blog, CLI, and 39 more developer resources.'
plans:
- name: Ankr Plans Pricing
  plan_count: 4
  slug: ankr-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Ankr Rate Limits
  slug: ankr-rate-limits
rules:
- name: ankr API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: ankr-asyncapi-spectral-rules
- name: ankr API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ankr-jsonschema-spectral-rules
- name: ankr API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 3
  slug: ankr-rules
score:
  band: strong
  composite: 69.0
  delta: 5.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 88.1
    developer_ergonomics: 56.5
    discoverability: 87.5
    governance: 65.8
    operational_transparency: 36.8
  previous_composite: 63.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ankr/refs/heads/main/screenshots/ankr-2026-06-20T172009.png
security:
- kind: authentication
  name: Ankr Authentication
  slug: ankr-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ankr Domain Security
  slug: ankr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ankr
website: https://www.ankr.com/about/
---
