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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 8
apis:
- description: Managed subgraph hosting compatible with The Graph - deploy subgraph definitions and get a hosted GraphQL endpoint per subgraph for querying indexed onchain data. Includes sync acceleration and direct
  name: Goldsky Subgraphs
  slug: subgraphs
- description: Change-data-capture pipelines that stream decoded onchain data from Goldsky's indexers into customer-managed sinks - PostgreSQL, ClickHouse, Kafka, MySQL, Webhook, S3, AWS SQS, Elasticsearch, S2, Parq
  name: Goldsky Mirror
  slug: mirror
- description: Vectorized real-time data pipelines with SQL transforms over decoded onchain data, with the same multi-sink delivery model as Mirror. Designed for high-throughput analytics and ML feature pipelines.
  name: Goldsky Turbo
  slug: turbo
- description: Execution layer for orchestrating onchain-x-offchain workflows - compose smart-contract calls, external APIs, and managed tasks into reliable pipelines triggered by onchain events.
  name: Goldsky Compose
  slug: compose
- description: High-performance JSON-RPC service for EVM networks with advanced debugging and tracing methods. Used as a drop-in replacement for vanilla RPC providers when apps need debug_traceTransaction-class meth
  name: Goldsky Edge RPC
  slug: edge-rpc
- description: REST API for managing Mirror and Turbo pipelines - create, delete, list, pause, resume, restart - plus pipeline logs (with cursor pagination) and pipeline status endpoints. Same API used by the CLI.
  name: Goldsky Pipeline REST API
  slug: pipeline-api
- description: Command-line tool for deploying and managing subgraphs, Mirror pipelines, Turbo pipelines, and Compose applications. Authenticates with a Goldsky API key and wraps the public REST API.
  name: Goldsky CLI
  slug: cli
- description: Web dashboard for managing Goldsky projects - subgraph deployments, pipeline status, logs, billing, and API keys.
  name: Goldsky Dashboard
  slug: dashboard
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goldsky-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goldsky.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goldsky.com/
- group: other
  title: ''
  type: Dashboard
  url: https://app.goldsky.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/goldsky-io
- group: company
  title: ''
  type: Blog
  url: https://goldsky.com/blog
- group: other
  title: ''
  type: X
  url: https://x.com/goldskyio
- group: other
  title: ''
  type: Email
  url: support@goldsky.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.goldsky.com/llms.txt
created: '2026-05-23'
description: Goldsky is a blockchain data platform that provides managed indexing, streaming, and RPC infrastructure for EVM and non-EVM chains. Core products are Subgraphs (hosted GraphQL indexers compatible with The Graph), Mirror (change-data-capture streaming of onchain data into customer databases and data warehouses), Turbo (vectorized real-time data pipelines with SQL transforms), Compose (orchestration of onchain-x-offchain workflows), and Edge RPC (high-performance EVM RPC with debug and trace). Developers interact via a CLI, a web dashboard, and REST + GraphQL APIs. Sinks supported include PostgreSQL, ClickHouse, Kafka, MySQL, Webhooks, S3, AWS SQS, Elasticsearch, S2, and Parquet.
finops:
- name: Goldsky Finops
  service_category: API
  slug: goldsky-finops
graphqls:
- description: Managed subgraph hosting compatible with The Graph - deploy subgraph definitions and get a hosted GraphQL endpoint per subgraph for querying indexed onchain data. Includes sync acceleration and direct
  name: Goldsky GraphQL API
  slug: goldsky-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goldsky.png
layout: provider
modified: '2026-05-23'
name: Goldsky
nav: Providers
network: true
overview: 'Goldsky publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain Data, Indexer, Subgraphs, CDC, and Streaming.


  Goldsky''s developer surface includes documentation, GitHub presence, engineering blog, and 6 more developer resources.'
plans:
- name: Goldsky Plans Pricing
  plan_count: 1
  slug: goldsky-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Goldsky Rate Limits
  slug: goldsky-rate-limits
score:
  band: emerging
  composite: 19.7
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 19.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goldsky/refs/heads/main/screenshots/goldsky-2026-06-20T181952.png
security:
- kind: domain-security
  name: Goldsky Domain Security
  slug: goldsky-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goldsky
tags:
- Blockchain Data
- Indexer
- Subgraphs
- CDC
- Streaming
- RPC
- Crypto
- Web3
website: https://goldsky.com/
---
