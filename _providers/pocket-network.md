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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pocket Network Agentic Access
  operation_count: 29
  slug: pocket-network-agentic-access
  summary_line: 29 operations · 3 acting
api_count: 16
apis:
- description: Pocket application module — applications stake POKT to consume relays
  name: Pocket Network Application API
  slug: pocket-network-application-api
- description: POKT supply, balances, and burn tracking
  name: Pocket Network Bank API
  slug: pocket-network-bank-api
- description: Block and consensus state queries
  name: Pocket Network Blocks API
  slug: pocket-network-blocks-api
- description: Block, header, and consensus queries
  name: Pocket Network Consensus API
  slug: pocket-network-consensus-api
- description: Pocket gateway module — gateways stake POKT and proxy relays for applications
  name: Pocket Network Gateway API
  slug: pocket-network-gateway-api
- description: PATH service liveness and readiness probes
  name: Pocket Network Health API
  slug: pocket-network-health-api
- description: Mempool inspection and broadcast
  name: Pocket Network Mempool API
  slug: pocket-network-mempool-api
- description: Pocket proof module — claims and proofs that suppliers submit to earn POKT
  name: Pocket Network Proof API
  slug: pocket-network-proof-api
- description: JSON-RPC, REST, and WebSocket relays proxied to Shannon suppliers
  name: Pocket Network Relays API
  slug: pocket-network-relays-api
- description: Pocket service module — services represent the data sources (EVM chains, Solana, etc.) the network serves
  name: Pocket Network Service API
  slug: pocket-network-service-api
- description: Pocket session module — sessions group applications, suppliers, and services for a given block window
  name: Pocket Network Session API
  slug: pocket-network-session-api
- description: Node status and network info
  name: Pocket Network Status API
  slug: pocket-network-status-api
- description: Pocket supplier module — suppliers stake POKT and serve relays via RelayMiner
  name: Pocket Network Supplier API
  slug: pocket-network-supplier-api
- description: Pocket tokenomics module — global mint, burn, and reward parameters
  name: Pocket Network Tokenomics API
  slug: pocket-network-tokenomics-api
- description: Transaction lookup and broadcast
  name: Pocket Network Transactions API
  slug: pocket-network-transactions-api
- description: Staking and validator queries
  name: Pocket Network Validators API
  slug: pocket-network-validators-api
arazzos:
- description: Read node status for the latest height, fetch that block, then its ABCI results.
  name: Pocket Network CometBFT Node Block Inspect
  slug: pocket-network-cometbft-node-block-inspect-workflow
- description: Confirm the PATH gateway is ready, then send an authenticated JSON-RPC relay through it.
  name: Pocket Network PATH Relay Readiness
  slug: pocket-network-path-relay-readiness-workflow
- description: Look up a Shannon application, then read the on-chain balances of its address.
  name: Pocket Network Shannon Application Balance
  slug: pocket-network-shannon-application-balance-workflow
- description: Resolve an application, confirm the target service exists, then fetch its active session.
  name: Pocket Network Shannon Application Session
  slug: pocket-network-shannon-application-session-workflow
- description: Read the latest Shannon block height, then fetch that exact block by height.
  name: Pocket Network Shannon Block Explorer
  slug: pocket-network-shannon-block-explorer-workflow
- description: Read a service definition, the network tokenomics parameters, and total supply.
  name: Pocket Network Shannon Service Economics
  slug: pocket-network-shannon-service-economics-workflow
- description: List suppliers, drill into the first supplier, then list gateways for network context.
  name: Pocket Network Shannon Supplier and Gateway Survey
  slug: pocket-network-shannon-supplier-gateway-survey-workflow
- description: Find the latest block, then look up a supplied transaction hash on Shannon.
  name: Pocket Network Shannon Transaction Lookup
  slug: pocket-network-shannon-transaction-lookup-workflow
artifact_total: 80
collections:
- collection_type: postman
  name: Pocket Network CometBFT RPC API
  slug: postman-pocket-network-cometbft-rpc-api
- collection_type: postman
  name: Pocket Network PATH Gateway API
  slug: postman-pocket-network-path-gateway-api
- collection_type: postman
  name: Pocket Network Shannon RPC API
  slug: postman-pocket-network-shannon-rpc-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pocket Network CometBFT RPC Application API
  slug: open-pocket-network-application-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Bank API
  slug: open-pocket-network-bank-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Blocks API
  slug: open-pocket-network-blocks-api
- collection_type: open
  name: Pocket Network CometBFT RPC API
  slug: open-pocket-network-cometbft-rpc-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Consensus API
  slug: open-pocket-network-consensus-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Gateway API
  slug: open-pocket-network-gateway-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Health API
  slug: open-pocket-network-health-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Mempool API
  slug: open-pocket-network-mempool-api
- collection_type: open
  name: Pocket Network PATH Gateway API
  slug: open-pocket-network-path-gateway-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Proof API
  slug: open-pocket-network-proof-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Relays API
  slug: open-pocket-network-relays-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Service API
  slug: open-pocket-network-service-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Session API
  slug: open-pocket-network-session-api
- collection_type: open
  name: Pocket Network Shannon RPC API
  slug: open-pocket-network-shannon-rpc-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Status API
  slug: open-pocket-network-status-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Supplier API
  slug: open-pocket-network-supplier-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Tokenomics API
  slug: open-pocket-network-tokenomics-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Transactions API
  slug: open-pocket-network-transactions-api
- collection_type: open
  name: Pocket Network CometBFT RPC Application Validators API
  slug: open-pocket-network-validators-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/buildwithgrove/path/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pocket-network-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pocket-network-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pocket-network-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pocket-network/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-cometbft-node-block-inspect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-path-relay-readiness-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-shannon-application-balance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-shannon-application-session-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-shannon-block-explorer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-shannon-service-economics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-shannon-supplier-gateway-survey-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/pocket-network-shannon-transaction-lookup-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://pocket.network
- group: start
  title: ''
  type: Portal
  url: https://grove.city
- group: docs
  title: ''
  type: Documentation
  url: https://path.grove.city/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pokt.network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.grove.city/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.poktroll.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pocket.network/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.grove.city/
- group: docs
  title: ''
  type: Documentation
  url: https://explorer.pocket.network/pocket-mainnet
- group: docs
  title: ''
  type: Documentation
  url: https://wallet.pocket.network/
- group: operate
  title: ''
  type: Forums
  url: https://forum.pokt.network/
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/pocket-network
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pokt-network
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buildwithgrove
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pokt-network/poktroll
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/buildwithgrove/path
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pokt-network/path
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pokt-network/shannon-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pokt-network/poktroll-clients-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pokt-network/shannon-tx-builder
- group: build
  title: ''
  type: SDKs
  url: https://github.com/pokt-network/pocket-js
- group: build
  title: ''
  type: Tools
  url: https://github.com/pokt-network/homebrew-pocketd
- group: build
  title: ''
  type: Tools
  url: https://github.com/pokt-network/pocketdex
- group: build
  title: ''
  type: Tools
  url: https://github.com/pokt-network/pocket-explorer
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/pokt-network/poktroll/releases
- group: company
  title: ''
  type: Blog
  url: https://medium.com/decentralized-infrastructure
- group: company
  title: ''
  type: Blog
  url: https://pocket.network/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://pocket.network/pocket-developer-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://pocket.network/shannon-upgrade-faq/
- group: docs
  title: ''
  type: Documentation
  url: https://pocket.network/decentralized-data-stack/
- group: docs
  title: ''
  type: Documentation
  url: https://grove.city/chains
- group: docs
  title: ''
  type: Documentation
  url: https://grove.city/partners
- group: commercial
  title: ''
  type: Pricing
  url: https://grove.city/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pocket.network/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pocket.network/legal/terms-of-service/
- group: commercial
  title: ''
  type: Plans
  url: plans/pocket-network-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pocket-network-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pocket-network-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/pocket-network-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pocket-network-vocabulary.yml
created: '2026-05-25'
description: Pocket Network is the decentralized RPC layer of Web3 — a permissionless, fully open data delivery protocol built on Cosmos SDK and CometBFT (the Shannon upgrade, June 2025). 5,000+ independent supplier nodes serve relays across 60-69+ blockchains, metered in compute units at $1/billion and settled on-chain in POKT under deflationary tokenomics (PIP-41, 97.5% mint ratio). Grove (grove.city) is the for-profit infrastructure company that operates the largest gateway on the network — rpc.grove.city — and maintains PATH, the open-source Go gateway any operator can run to expose Pocket Network as a single HTTP endpoint. Grove offers free no-API-key per-IP public endpoints per chain (eth.rpc.grove.city, solana.rpc.grove.city, etc.) plus paid portal applications with relay analytics and SLAs. Together they form the canonical decentralized alternative to Alchemy / Infura / QuickNode for serving JSON-RPC, REST, and WebSocket traffic to any public blockchain.
examples:
- key_count: 5
  name: Pocket Network Eth Block Number Example
  slug: pocket-network-eth-block-number-example
- key_count: 5
  name: Pocket Network List Shannon Services Example
  slug: pocket-network-list-shannon-services-example
- key_count: 5
  name: Pocket Network Shannon Latest Block Example
  slug: pocket-network-shannon-latest-block-example
features:
- Shannon protocol — Cosmos SDK + CometBFT chain replacing Morse in June 2025
- 5,000+ independent nodes serving 60-69+ blockchains (EVM, Layer-2s, Cosmos, Solana)
- PATH gateway (Go, MIT) — open-source single-binary gateway for any operator to run
- Grove hosted endpoints — rpc.grove.city per-chain subdomains for portal and public traffic
- Compute-unit metering — $1 = 1B CU, deflationary via POKT burn on every relay (PIP-41)
- On-chain actors — Application, Supplier, Gateway, Validator, Source Owner
- RelayMiner — supplier-side daemon proxying relays with revenue-share splits
- Quality-of-Service scoring inside PATH routes around degraded suppliers automatically
- Public free per-IP endpoints across every supported chain for development
- 99.9% uptime target on Grove public endpoints
- Authenticated portal applications via opaque Application IDs in URL path
- Permissionless service registration — anyone can add a new chain by staking a service
- F-Chains public-data program for non-profit/public-goods consumers
- $1 per billion compute units wholesale, $1 per million relays Grove pay-as-you-go (RELAY2025)
- poktrolld CLI (homebrew-pocketd) for full Cosmos SDK tx/query/keys operations
- Shannon SDK (Go), poktroll-clients-py (Python), shannon-tx-builder (Python)
- Pocketdex (SubQuery) indexer powering Pocket Explorer
- Pocket Network Foundation governance with on-chain PIP proposals
- Available as decentralized RPC backend for Cosmos Keplr chain registry integrations
finops:
- name: Pocket Network Finops
  service_category: Infrastructure (Web3 / RPC)
  slug: pocket-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pocket-network.png
json_schemas:
- name: Pocket Network Relay
  property_count: 3
  slug: pocket-network-relay
- name: Pocket Network Shannon Actor
  property_count: 0
  slug: pocket-network-shannon-actor
jsonld:
- class_count: 0
  name: Pocket Network Context
  property_count: 7
  slug: pocket-network-context
layout: provider
modified: '2026-05-25'
name: Pocket Network
nav: Providers
network: true
overview: 'Pocket Network publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Application API, Bank API, Blocks API, and 13 more. Tagged areas include Web3, Blockchain, RPC, Decentralized Infrastructure, and Pocket Network.


  The Pocket Network catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Pocket Network''s developer surface includes authentication, developer portal, documentation, tooling, changelog, engineering blog, getting-started guide, and 46 more developer resources.'
plans:
- name: Pocket Network Plans Pricing
  plan_count: 4
  slug: pocket-network-plans-pricing
random_paper: 128
rate_limits:
- limit_count: 3
  name: Pocket Network Rate Limits
  slug: pocket-network-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Pocket Network API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: pocket-network-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  - spectral:asyncapi
  name: Pocket Network API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: pocket-network-rules
score:
  band: strong
  composite: 62.3
  delta: -5.1
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 25.0
    contract_quality: 61.8
    developer_ergonomics: 71.4
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 68.4
  previous_composite: 67.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/pocket-network/refs/heads/main/screenshots/pocket-network-2026-06-20T191825.png
security:
- kind: authentication
  name: Pocket Network Authentication
  slug: pocket-network-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pocket Network Domain Security
  slug: pocket-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pocket-network
tags:
- Web3
- Blockchain
- RPC
- Decentralized Infrastructure
- Pocket Network
- Grove
- PATH
- Shannon
- Cosmos
- POKT
website: https://pocket.network
---
