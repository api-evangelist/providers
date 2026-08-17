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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Alchemy Agentic Access
  operation_count: 7
  slug: alchemy-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 12
apis:
- description: Multi-chain JSON-RPC over HTTPS and WebSockets covering standard eth_*, solana, and other chain methods, plus Alchemy-enhanced subscriptions (alchemy_minedTransactions, alchemy_pendingTransactions).
  name: Alchemy Node API (JSON-RPC)
  slug: node-rpc
- description: REST endpoints for NFT ownership, metadata, floor price, sales, contract metadata, and transfers across EVM chains and Solana.
  name: Alchemy NFT API
  slug: nft-api
- description: REST endpoints for paginated address-level transfer history (external, internal, ERC-20, ERC-721, ERC-1155).
  name: Alchemy Transfers API
  slug: transfers-api
- description: REST endpoints aggregating multi-chain wallet balances, NFTs, and tokens in a single call.
  name: Alchemy Portfolio API
  slug: portfolio-api
- description: REST endpoints for token spot and historical pricing.
  name: Alchemy Prices API
  slug: prices-api
- description: REST API for managing webhook subscriptions (mined / dropped transactions, address activity, NFT activity, custom).
  name: Alchemy Webhooks (Notify)
  slug: webhooks-notify
- description: JSON-RPC bundler endpoints for ERC-4337 user operations (eth_sendUserOperation, eth_estimateUserOperationGas, alchemy_*).
  name: Alchemy Bundler API (ERC-4337)
  slug: bundler
- description: REST/JSON-RPC API for simulating transactions and asset changes before broadcasting.
  name: Alchemy Simulation API
  slug: simulation-api
- description: Sponsor user operations via ERC-4337 paymaster endpoints.
  name: Alchemy Paymaster API
  slug: alchemy-paymaster-api
- description: Create and manage gas sponsorship policies.
  name: Alchemy Policies API
  slug: alchemy-policies-api
- description: Retrieve ERC-20 token balances for wallet addresses.
  name: Alchemy Token Balances API
  slug: alchemy-token-balances-api
- description: Retrieve metadata for ERC-20 tokens.
  name: Alchemy Token Metadata API
  slug: alchemy-token-metadata-api
artifact_total: 81
asyncapis:
- description: AsyncAPI definition for Alchemy's JSON-RPC WebSocket subscription API. Clients open a `wss://` connection to a per-network Alchemy endpoint and use the standard Ethereum `eth_subscribe` / `eth_unsubsc
  name: Alchemy WebSocket Subscription API
  slug: alchemy-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Alchemy Gas Manager API
  slug: open-alchemy-gas-manager-api
- collection_type: open
  name: Alchemy Gas Manager Paymaster API
  slug: open-alchemy-paymaster-api
- collection_type: open
  name: Alchemy Gas Manager Paymaster Policies API
  slug: open-alchemy-policies-api
- collection_type: open
  name: Alchemy Token API
  slug: open-alchemy-token-api
- collection_type: open
  name: Alchemy Gas Manager Paymaster Token Balances API
  slug: open-alchemy-token-balances-api
- collection_type: open
  name: Alchemy Gas Manager Paymaster Token Metadata API
  slug: open-alchemy-token-metadata-api
- collection_type: open
  name: Alchemy Gas Manager Paymaster Transfers API
  slug: open-alchemy-transfers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alchemy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/alchemy-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alchemy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alchemy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alchemy-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.alchemy.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alchemyplatform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alchemyinc
- group: company
  title: ''
  type: Website
  url: https://www.alchemy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alchemy.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/alchemy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alchemy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alchemy-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://alchemy.com/llms.txt
created: '2026-05-08'
description: Alchemy is a Web3 developer platform offering blockchain JSON-RPC, Data APIs (NFT, Token, Transfers, Portfolio, Prices, Webhooks/Notify, Simulation), Smart Wallets / Account Abstraction (Bundler, Gas Manager), and dedicated Rollup infrastructure across 50+ chains including Ethereum, Polygon, Arbitrum, Optimism, Base, and Solana.
examples:
- key_count: 4
  name: Alchemy Gas Manager Api Create Policy Request Example
  slug: alchemy-gas-manager-api-create-policy-request-example
- key_count: 6
  name: Alchemy Gas Manager Api Policy Example
  slug: alchemy-gas-manager-api-policy-example
- key_count: 1
  name: Alchemy Gas Manager Api Policy List Response Example
  slug: alchemy-gas-manager-api-policy-list-response-example
- key_count: 4
  name: Alchemy Gas Manager Api Sponsor User Operation Request Example
  slug: alchemy-gas-manager-api-sponsor-user-operation-request-example
- key_count: 3
  name: Alchemy Gas Manager Api Sponsor User Operation Response Example
  slug: alchemy-gas-manager-api-sponsor-user-operation-response-example
- key_count: 4
  name: Alchemy Gas Manager Api Sponsor User Operation Result Example
  slug: alchemy-gas-manager-api-sponsor-user-operation-result-example
- key_count: 3
  name: Alchemy Token Api Token Balance Example
  slug: alchemy-token-api-token-balance-example
- key_count: 3
  name: Alchemy Token Api Token Balances Response Example
  slug: alchemy-token-api-token-balances-response-example
- key_count: 3
  name: Alchemy Token Api Token Balances Result Example
  slug: alchemy-token-api-token-balances-result-example
- key_count: 4
  name: Alchemy Token Api Token Metadata Example
  slug: alchemy-token-api-token-metadata-example
- key_count: 3
  name: Alchemy Token Api Token Metadata Response Example
  slug: alchemy-token-api-token-metadata-response-example
- key_count: 8
  name: Alchemy Transfers Api Asset Transfer Example
  slug: alchemy-transfers-api-asset-transfer-example
- key_count: 3
  name: Alchemy Transfers Api Asset Transfers Response Example
  slug: alchemy-transfers-api-asset-transfers-response-example
- key_count: 2
  name: Alchemy Transfers Api Asset Transfers Result Example
  slug: alchemy-transfers-api-asset-transfers-result-example
- key_count: 1
  name: Alchemy Transfers Api Transfer Metadata Example
  slug: alchemy-transfers-api-transfer-metadata-example
finops:
- name: Alchemy Finops
  service_category: Web3
  slug: alchemy-finops
graphqls:
- description: 'This conceptual GraphQL schema models the Alchemy Web3 developer platform, covering the full surface of Alchemy''s blockchain APIs: Node RPC (JSON-RPC over HTTPS/WebSockets), NFT API, Token API, Transf'
  name: Alchemy GraphQL Schema
  slug: alchemy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alchemy.png
json_schemas:
- name: Create Policy Request
  property_count: 4
  slug: alchemy-gas-manager-api-create-policy-request
- name: Policy List Response
  property_count: 1
  slug: alchemy-gas-manager-api-policy-list-response
- name: Gas Manager Policy
  property_count: 6
  slug: alchemy-gas-manager-api-policy
- name: Sponsor User Operation Request
  property_count: 4
  slug: alchemy-gas-manager-api-sponsor-user-operation-request
- name: Sponsor User Operation Response
  property_count: 3
  slug: alchemy-gas-manager-api-sponsor-user-operation-response
- name: Sponsor User Operation Result
  property_count: 4
  slug: alchemy-gas-manager-api-sponsor-user-operation-result
- name: Token Balance
  property_count: 3
  slug: alchemy-token-api-token-balance
- name: Token Balances Response
  property_count: 3
  slug: alchemy-token-api-token-balances-response
- name: Token Balances Result
  property_count: 3
  slug: alchemy-token-api-token-balances-result
- name: Token Metadata Response
  property_count: 3
  slug: alchemy-token-api-token-metadata-response
- name: Token Metadata
  property_count: 4
  slug: alchemy-token-api-token-metadata
- name: Asset Transfer
  property_count: 8
  slug: alchemy-transfers-api-asset-transfer
- name: Asset Transfers Response
  property_count: 3
  slug: alchemy-transfers-api-asset-transfers-response
- name: Asset Transfers Result
  property_count: 2
  slug: alchemy-transfers-api-asset-transfers-result
- name: Transfer Metadata
  property_count: 1
  slug: alchemy-transfers-api-transfer-metadata
json_structures:
- name: Alchemy Gas Manager Api Create Policy Request Structure
  property_count: 4
  slug: alchemy-gas-manager-api-create-policy-request-structure
- name: Alchemy Gas Manager Api Policy List Response Structure
  property_count: 1
  slug: alchemy-gas-manager-api-policy-list-response-structure
- name: Alchemy Gas Manager Api Policy Structure
  property_count: 6
  slug: alchemy-gas-manager-api-policy-structure
- name: Alchemy Gas Manager Api Sponsor User Operation Request Structure
  property_count: 4
  slug: alchemy-gas-manager-api-sponsor-user-operation-request-structure
- name: Alchemy Gas Manager Api Sponsor User Operation Response Structure
  property_count: 3
  slug: alchemy-gas-manager-api-sponsor-user-operation-response-structure
- name: Alchemy Gas Manager Api Sponsor User Operation Result Structure
  property_count: 4
  slug: alchemy-gas-manager-api-sponsor-user-operation-result-structure
- name: Alchemy Token Api Token Balance Structure
  property_count: 3
  slug: alchemy-token-api-token-balance-structure
- name: Alchemy Token Api Token Balances Response Structure
  property_count: 3
  slug: alchemy-token-api-token-balances-response-structure
- name: Alchemy Token Api Token Balances Result Structure
  property_count: 3
  slug: alchemy-token-api-token-balances-result-structure
- name: Alchemy Token Api Token Metadata Response Structure
  property_count: 3
  slug: alchemy-token-api-token-metadata-response-structure
- name: Alchemy Token Api Token Metadata Structure
  property_count: 4
  slug: alchemy-token-api-token-metadata-structure
- name: Alchemy Transfers Api Asset Transfer Structure
  property_count: 8
  slug: alchemy-transfers-api-asset-transfer-structure
- name: Alchemy Transfers Api Asset Transfers Response Structure
  property_count: 3
  slug: alchemy-transfers-api-asset-transfers-response-structure
- name: Alchemy Transfers Api Asset Transfers Result Structure
  property_count: 2
  slug: alchemy-transfers-api-asset-transfers-result-structure
- name: Alchemy Transfers Api Transfer Metadata Structure
  property_count: 1
  slug: alchemy-transfers-api-transfer-metadata-structure
jsonld:
- class_count: 7
  name: Alchemy Gas Manager Api Context
  property_count: 15
  slug: alchemy-gas-manager-api-context
- class_count: 6
  name: Alchemy Token Api Context
  property_count: 12
  slug: alchemy-token-api-context
- class_count: 4
  name: Alchemy Transfers Api Context
  property_count: 14
  slug: alchemy-transfers-api-context
layout: provider
modified: '2026-08-07'
name: Alchemy
nav: Providers
network: true
overview: 'Alchemy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Node API (JSON-RPC), Transfers API, Paymaster API, and 3 more. Tagged areas include Web3, Blockchain, RPC, NFT, and Indexing.


  The Alchemy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 3 JSON-LD contexts, and 3 Spectral governance rulesets.


  Alchemy''s developer surface includes authentication, engineering blog, documentation, and 11 more developer resources.'
plans:
- name: Alchemy Plans Pricing
  plan_count: 4
  slug: alchemy-plans-pricing
random_paper: 143
rate_limits:
- limit_count: 4
  name: Alchemy Rate Limits
  slug: alchemy-rate-limits
rules:
- name: Alchemy API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: alchemy-asyncapi-spectral-rules
- name: Alchemy API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: alchemy-jsonschema-spectral-rules
- name: Alchemy API Rules
  rule_count: 37
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 19
  slug: alchemy-spectral-rules
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 43.8
    developer_ergonomics: 21.7
    discoverability: 81.5
    governance: 47.9
    operational_transparency: 13.2
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alchemy/refs/heads/main/screenshots/alchemy-2026-06-20T171514.png
security:
- kind: authentication
  name: Alchemy Authentication
  slug: alchemy-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Alchemy Domain Security
  slug: alchemy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alchemy Vulnerability Disclosure
  slug: alchemy-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Alchemy Trust Center
  slug: alchemy-trust-center
  summary_line: SOC 2
slug: alchemy
tags:
- Web3
- Blockchain
- RPC
- NFT
- Indexing
- Account Abstraction
website: https://www.alchemy.com/
---
