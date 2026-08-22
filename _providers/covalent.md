---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Covalent Agentic Access
  operation_count: 58
  slug: covalent-agentic-access
  summary_line: 58 operations · 11 acting
api_count: 18
apis:
- description: WebSocket channels for Hyperliquid markets including l2Book (wire-equal to the public feed), l2BookDiff (GoldRush-exclusive differential updates), and l4Book (order-level GoldRush-exclusive channel) p
  name: GoldRush Hyperliquid WebSocket API
  slug: goldrush-hyperliquid-websocket-api
- description: Manage ABI definitions used for log and function decoding.
  name: Covalent ABI API
  slug: covalent-abi-api
- description: Native, ERC20, ERC721, ERC1155, and historical token balances.
  name: Covalent Balances API
  slug: covalent-balances-api
- description: Blocks, gas prices, log events, address resolution, chain status.
  name: Covalent Base API
  slug: covalent-base-api
- description: Bitcoin balance and transaction lookups (HD and non-HD).
  name: Covalent Bitcoin API
  slug: covalent-bitcoin-api
- description: Discover an address's activity across all supported chains.
  name: Covalent Cross-Chain API
  slug: covalent-cross-chain-api
- description: x402-priced data endpoints.
  name: Covalent Data API
  slug: covalent-data-api
- description: Manage destination connections (ClickHouse, Kafka, S3/GCS/R2, Postgres, SQS, Webhook).
  name: Covalent Destinations API
  slug: covalent-destinations-api
- description: List and search x402 endpoints exposed by GoldRush.
  name: Covalent Discovery API
  slug: covalent-discovery-api
- description: Single GraphQL endpoint serving queries and subscriptions.
  name: Covalent GraphQL API
  slug: covalent-graphql-api
- description: Dispatching POST endpoint for Hyperliquid info types.
  name: Covalent Info API
  slug: covalent-info-api
- description: NFTs held by an address and collection ownership checks.
  name: Covalent NFT API
  slug: covalent-nft-api
- description: Create, list, update, and delete data pipelines.
  name: Covalent Pipelines API
  slug: covalent-pipelines-api
- description: Historical token prices and pool spot prices.
  name: Covalent Pricing API
  slug: covalent-pricing-api
- description: One-shot data queries.
  name: Covalent Queries API
  slug: covalent-queries-api
- description: Token approvals across ERC20 and NFT contracts.
  name: Covalent Security API
  slug: covalent-security-api
- description: Transaction lookups by address, block, and time bucket.
  name: Covalent Transactions API
  slug: covalent-transactions-api
- description: Manage SQL transforms applied to decoded events before delivery.
  name: Covalent Transforms API
  slug: covalent-transforms-api
artifact_total: 74
asyncapis:
- description: Real-time blockchain data from GoldRush (Covalent) delivered over a single WebSocket endpoint that speaks the GraphQL over WebSocket protocol (`graphql-transport-ws`, the protocol implemented by the `
  name: GoldRush Streaming API
  slug: covalent-asyncapi
collections:
- collection_type: postman
  name: GoldRush Foundational ABI API
  slug: postman-covalent-abi-api
- collection_type: postman
  name: GoldRush Foundational ABI Balances API
  slug: postman-covalent-balances-api
- collection_type: postman
  name: GoldRush Foundational ABI Base API
  slug: postman-covalent-base-api
- collection_type: postman
  name: GoldRush Foundational ABI Bitcoin API
  slug: postman-covalent-bitcoin-api
- collection_type: postman
  name: GoldRush Foundational ABI Cross-Chain API
  slug: postman-covalent-cross-chain-api
- collection_type: postman
  name: GoldRush Foundational ABI Data API
  slug: postman-covalent-data-api
- collection_type: postman
  name: GoldRush Foundational ABI Destinations API
  slug: postman-covalent-destinations-api
- collection_type: postman
  name: GoldRush Foundational ABI Discovery API
  slug: postman-covalent-discovery-api
- collection_type: postman
  name: GoldRush Foundational ABI GraphQL API
  slug: postman-covalent-graphql-api
- collection_type: postman
  name: GoldRush Foundational ABI Info API
  slug: postman-covalent-info-api
- collection_type: postman
  name: GoldRush Foundational ABI NFT API
  slug: postman-covalent-nft-api
- collection_type: postman
  name: GoldRush Foundational ABI Pipelines API
  slug: postman-covalent-pipelines-api
- collection_type: postman
  name: GoldRush Foundational ABI Pricing API
  slug: postman-covalent-pricing-api
- collection_type: postman
  name: GoldRush Foundational ABI Queries API
  slug: postman-covalent-queries-api
- collection_type: postman
  name: GoldRush Foundational ABI Security API
  slug: postman-covalent-security-api
- collection_type: postman
  name: GoldRush Foundational ABI Transactions API
  slug: postman-covalent-transactions-api
- collection_type: postman
  name: GoldRush Foundational ABI Transforms API
  slug: postman-covalent-transforms-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GoldRush Foundational ABI API
  slug: open-covalent-abi-api
- collection_type: open
  name: GoldRush Foundational ABI Balances API
  slug: open-covalent-balances-api
- collection_type: open
  name: GoldRush Foundational ABI Base API
  slug: open-covalent-base-api
- collection_type: open
  name: GoldRush Foundational ABI Bitcoin API
  slug: open-covalent-bitcoin-api
- collection_type: open
  name: GoldRush Foundational ABI Cross-Chain API
  slug: open-covalent-cross-chain-api
- collection_type: open
  name: GoldRush Foundational ABI Data API
  slug: open-covalent-data-api
- collection_type: open
  name: GoldRush Foundational ABI Destinations API
  slug: open-covalent-destinations-api
- collection_type: open
  name: GoldRush Foundational ABI Discovery API
  slug: open-covalent-discovery-api
- collection_type: open
  name: GoldRush Foundational API
  slug: open-covalent-foundational-api
- collection_type: open
  name: GoldRush Foundational ABI GraphQL API
  slug: open-covalent-graphql-api
- collection_type: open
  name: GoldRush Hyperliquid Info API
  slug: open-covalent-hyperliquid-info-api
- collection_type: open
  name: GoldRush Foundational ABI Info API
  slug: open-covalent-info-api
- collection_type: open
  name: GoldRush Foundational ABI NFT API
  slug: open-covalent-nft-api
- collection_type: open
  name: GoldRush Pipeline API
  slug: open-covalent-pipeline-api
- collection_type: open
  name: GoldRush Foundational ABI Pipelines API
  slug: open-covalent-pipelines-api
- collection_type: open
  name: GoldRush Foundational ABI Pricing API
  slug: open-covalent-pricing-api
- collection_type: open
  name: GoldRush Foundational ABI Queries API
  slug: open-covalent-queries-api
- collection_type: open
  name: GoldRush Foundational ABI Security API
  slug: open-covalent-security-api
- collection_type: open
  name: GoldRush Streaming API
  slug: open-covalent-streaming-api
- collection_type: open
  name: GoldRush Foundational ABI Transactions API
  slug: open-covalent-transactions-api
- collection_type: open
  name: GoldRush Foundational ABI Transforms API
  slug: open-covalent-transforms-api
- collection_type: open
  name: GoldRush x402 API
  slug: open-covalent-x402-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/covalent/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/covalent-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/covalent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/covalent-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/covalent-hq
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Covalent_HQ
- group: build
  title: ''
  type: GitHub
  url: https://github.com/covalenthq
- group: company
  title: ''
  type: Website
  url: https://www.covalenthq.com
- group: company
  title: ''
  type: Website
  url: https://goldrush.dev
- group: start
  title: ''
  type: Portal
  url: https://goldrush.dev/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://goldrush.dev/docs/api-reference/foundational-api/
- group: docs
  title: ''
  type: Documentation
  url: https://goldrush.dev/docs/api-reference/streaming-api/
- group: docs
  title: ''
  type: Documentation
  url: https://goldrush.dev/docs/api-reference/pipeline-api/
- group: docs
  title: ''
  type: Documentation
  url: https://goldrush.dev/docs/api-reference/hyperliquid/
- group: operate
  title: ''
  type: ChangeLog
  url: https://goldrush.dev/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://goldrush.dev/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goldrush.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://goldrush.dev/pricing/
- group: start
  title: ''
  type: Login
  url: https://goldrush.dev/platform/
- group: operate
  title: ''
  type: Support
  url: https://goldrush.dev/support/
- group: docs
  title: ''
  type: Documentation
  url: https://goldrush.dev/chains/
- group: docs
  title: ''
  type: Documentation
  url: https://goldrush.dev/guides/
- group: other
  title: ''
  type: CaseStudies
  url: https://goldrush.dev/case-studies/
- group: docs
  title: ''
  type: Documentation
  url: https://goldrush.dev/agents/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@covalenthq/client-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/covalenthq/covalent-api-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/covalenthq/goldrush-mcp-server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/covalenthq/goldrush-agent-skills
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@covalenthq/goldrush-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/covalenthq/goldrush-kit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/covalenthq/ai-agent-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/covalenthq/goldrush-enhanced-spam-lists
- group: build
  title: ''
  type: Tools
  url: https://github.com/covalenthq/refiner
- group: build
  title: ''
  type: Tools
  url: https://github.com/covalenthq/bsp-agent
- group: build
  title: ''
  type: Tools
  url: https://github.com/covalenthq/bsp-geth
- group: auth
  title: ''
  type: Authentication
  url: https://goldrush.dev/docs/api-reference/foundational-api/authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://goldrush.dev/docs/api-reference/foundational-api/rate-limits
- group: commercial
  title: ''
  type: Plans
  url: plans/covalent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/covalent-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/covalent-finops.yml
- group: commercial
  title: ''
  type: Plans
  url: https://goldrush.dev/pricing/
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: docs
  title: ''
  type: Documentation
  url: ''
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/covalent-vocabulary.json
- group: auth
  title: ''
  type: Compliance
  url: ''
examples:
- key_count: 2
  name: Covalent Balances Example
  slug: covalent-balances-example
- key_count: 2
  name: Covalent Cross Chain Activity Example
  slug: covalent-cross-chain-activity-example
- key_count: 2
  name: Covalent Hyperliquid Info Example
  slug: covalent-hyperliquid-info-example
finops:
- name: Covalent Finops
  service_category: Blockchain Data
  slug: covalent-finops
graphqls:
- description: Real-time blockchain events via GraphQL over WebSockets with sub-second latency. Includes one-shot queries (OHLCV pairs and tokens, token search, top trader wallets, wallet PnL by token) and live subs
  name: Covalent GraphQL API
  slug: covalent-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/covalent.png
json_schemas:
- name: GoldRush Balance
  property_count: 0
  slug: covalent-balance
- name: GoldRush Transaction
  property_count: 0
  slug: covalent-transaction
jsonld:
- class_count: 0
  name: Covalent Context
  property_count: 9
  slug: covalent-context
layout: provider
modified: 2026-06-14
name: Covalent
nav: Providers
network: true
overview: 'Covalent publishes 17 APIs on the [APIs.io](https://apis.io/) network, including ABI API, Balances API, Base API, and 14 more. Tagged areas include Blockchain, Web3, Multi-Chain, Data Infrastructure, and Crypto.


  The Covalent catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Covalent''s developer surface includes authentication, GitHub presence, developer portal, documentation, changelog, engineering blog, pricing, and 35 more developer resources.'
plans:
- name: Covalent Plans Pricing
  plan_count: 4
  slug: covalent-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Covalent Rate Limits
  slug: covalent-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Covalent API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: covalent-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Covalent API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: covalent-jsonschema-spectral-rules
score:
  band: strong
  composite: 60.6
  delta: -6.3
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 26.5
    contract_quality: 67.5
    developer_ergonomics: 66.7
    discoverability: 40.7
    governance: 26.5
    operational_transparency: 68.4
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/covalent/refs/heads/main/screenshots/covalent-2026-06-20T175115.png
security:
- kind: authentication
  name: Covalent Authentication
  slug: covalent-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Covalent Domain Security
  slug: covalent-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: covalent
tags:
- Blockchain
- Web3
- Multi-Chain
- Data Infrastructure
- Crypto
- DeFi
- NFT
- Hyperliquid
- GoldRush
- AI Agents
website: https://www.covalenthq.com
---
