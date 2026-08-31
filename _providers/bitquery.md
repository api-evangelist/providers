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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.1
  scored_at: '2026-08-30'
api_count: 10
apis:
- description: Unified GraphQL endpoint for querying onchain data across 40+ supported blockchains - blocks, transactions, transfers, DEX trades, balances, holders, NFTs, prices, events, traces. Standard GraphQL POS
  name: Bitquery GraphQL API (V2)
  slug: graphql-v2
- description: Legacy GraphQL endpoint covering Bitquery's V1 schema - kept for backward compatibility while customers migrate to V2.
  name: Bitquery GraphQL API (V1)
  slug: graphql-v1
- description: GraphQL subscriptions over WebSocket for real-time blockchain data - live DEX trades, transfers, pending transactions, contract events. Same V2 schema as the HTTP endpoint, delivered as push events. S
  name: Bitquery Streaming Subscriptions
  slug: streaming-subscriptions
- description: Protobuf-encoded streams of decoded blockchain data delivered via managed Kafka topics. Designed for scale-out consumption by indexers, analytics pipelines, and warehouses that need to backfill or str
  name: Bitquery Kafka Streams
  slug: kafka-streams
- description: gRPC streaming API for Solana that delivers decoded block, transaction, and instruction data with sub-second latency. Targeted at Solana-native apps, MEV searchers, and high-throughput indexers.
  name: Bitquery Solana CoreCast (gRPC)
  slug: grpc-corecast
- description: Model Context Protocol server backed by ClickHouse that lets AI agents query Bitquery's onchain dataset using natural language and structured tool calls.
  name: Bitquery MCP Server
  slug: mcp-server
- description: Parquet-format cloud datasets containing Bitquery's decoded onchain data for direct load into data warehouses (Snowflake, BigQuery, Redshift, Databricks).
  name: Bitquery Cloud Datasets
  slug: cloud-datasets
- description: In-browser GraphQL IDE for authoring, testing, and saving Bitquery queries against the V1 and V2 schemas. Used by developers to prototype before wiring queries into apps.
  name: Bitquery IDE
  slug: ide
- description: Multi-chain block explorer surfacing transactions, addresses, tokens, and DEX activity searchable across all chains Bitquery indexes.
  name: Bitquery Explorer
  slug: explorer
- description: Real-time DEX analytics product built on Bitquery's data - tracks trades, liquidity, volumes, and trending tokens across DEXes on multiple chains.
  name: DEXrabbit
  slug: dexrabbit
artifact_total: 17
asyncapis:
- description: AsyncAPI description of Bitquery's real-time blockchain data streams, delivered as GraphQL subscriptions over WebSocket. The same V2 GraphQL schema served from the HTTP endpoint (`https://streaming.bi
  name: Bitquery Streaming GraphQL Subscriptions
  slug: bitquery-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitquery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitquery.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitquery.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bitquery
- group: other
  title: ''
  type: IDE
  url: https://ide.bitquery.io/
- group: other
  title: ''
  type: Explorer
  url: https://explorer.bitquery.io/
- group: other
  title: ''
  type: X
  url: https://x.com/Bitquery_io
- group: company
  title: ''
  type: Blog
  url: https://bitquery.io/blog
created: '2026-05-23'
description: Bitquery is a blockchain data platform that exposes a single unified GraphQL schema across 40+ networks (Ethereum, Solana, BSC, Base, Polygon, Arbitrum, Optimism, Tron, and more) through multiple delivery modes - GraphQL over HTTP, GraphQL subscriptions over WebSocket, Kafka protobuf streams, gRPC (Solana CoreCast), an MCP server backed by ClickHouse, and parquet cloud datasets. Core data products cover token prices and OHLCV, DEX trades, transfers and wallet flows, contract calls and traces, events, NFTs and metadata, balances and holders, and mempool / pending transactions.
finops:
- name: Bitquery Finops
  service_category: API
  slug: bitquery-finops
graphqls:
- description: Unified GraphQL endpoint for querying onchain data across 40+ supported blockchains - blocks, transactions, transfers, DEX trades, balances, holders, NFTs, prices, events, traces. Standard GraphQL POS
  name: Bitquery GraphQL API
  slug: bitquery-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitquery.png
layout: provider
modified: '2026-05-29'
name: Bitquery
nav: Providers
network: true
overview: 'Bitquery publishes 1 API on the [APIs.io](https://apis.io/) network: Streaming Subscriptions. Tagged areas include Blockchain Data, GraphQL, Streaming, Indexer, and DEX.


  The Bitquery catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Bitquery''s developer surface includes documentation, GitHub presence, engineering blog, and 5 more developer resources.'
plans:
- name: Bitquery Plans Pricing
  plan_count: 1
  slug: bitquery-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Bitquery Rate Limits
  slug: bitquery-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Bitquery API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: bitquery-asyncapi-spectral-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 52.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 46.8
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 26.3
  previous_composite: 34.4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitquery/refs/heads/main/screenshots/bitquery-2026-06-20T173319.png
security:
- kind: domain-security
  name: Bitquery Domain Security
  slug: bitquery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitquery
tags:
- Blockchain Data
- GraphQL
- Streaming
- Indexer
- DEX
- NFT
- Crypto
- Web3
website: https://bitquery.io/
---
