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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: The Graph Agentic Access
  operation_count: 2
  slug: the-graph-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 6
apis:
- description: Per-subgraph GraphQL endpoints served by the decentralized network of Indexers. Each subgraph defines its own schema; queries are billed in GRT or via a hosted gateway in USD.
  name: The Graph Subgraphs (GraphQL)
  slug: subgraphs
- description: REST API for cross-chain token data (balances, holders, prices, transfers, metadata) with built-in MCP server for AI agents.
  name: The Graph Token API
  slug: token-api
- description: gRPC streaming protocol for parallelized blockchain dataflows backed by Firehose. Substreams power high-throughput indexing pipelines.
  name: The Graph Substreams
  slug: substreams
- description: JSON-RPC admin interface to a self-hosted Graph Node for deploying, listing, and managing subgraphs. Public hosted-service is deprecated; this surface applies to self-managed indexers.
  name: Graph Node Admin JSON-RPC (self-hosted)
  slug: graph-node-rpc
- description: Open-source flat-file extraction layer that powers Substreams. Provides chain-specific gRPC streams of blocks and transactions.
  name: Firehose
  slug: firehose
- description: The Subgraphs API from The Graph — 2 operation(s) for subgraphs.
  name: The Graph Subgraphs API
  slug: the-graph-subgraphs-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: The Graph Gateway ( GraphQL) Subgraphs API
  slug: open-the-graph-subgraphs-api
- collection_type: open
  name: The Graph Gateway (Subgraphs GraphQL)
  slug: open-the-graph
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-graph-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/the-graph-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-graph-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-graph-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/thegraph
- group: company
  title: ''
  type: Website
  url: https://thegraph.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/the-graph-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-graph-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/the-graph-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://token-api.thegraph.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://thegraph.com/blog
created: '2026-05-08'
description: The Graph is a decentralized blockchain data indexing protocol. It exposes Subgraphs (GraphQL APIs over indexed on-chain data), Substreams (parallel streaming dataflows), the Token API (REST/MCP for token data), and supports 80+ chains. Self-hosted Graph Node and Firehose are open-source.
finops:
- name: The Graph Finops
  service_category: Web3
  slug: the-graph-finops
graphqls:
- description: Per-subgraph GraphQL endpoints served by the decentralized network of Indexers. Each subgraph defines its own schema; queries are billed in GRT or via a hosted gateway in USD.
  name: The Graph GraphQL API
  slug: the-graph-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-graph.png
layout: provider
modified: '2026-05-08'
name: The Graph
nav: Providers
network: true
overview: 'The Graph publishes 1 API on the [APIs.io](https://apis.io/) network: Subgraphs API. Tagged areas include Web3, Indexing, GraphQL, Subgraphs, and Multi-chain.


  The Graph''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: The Graph Plans Pricing
  plan_count: 3
  slug: the-graph-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: The Graph Rate Limits
  slug: the-graph-rate-limits
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 55.2
    developer_ergonomics: 13.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-graph/refs/heads/main/screenshots/the-graph-2026-06-20T195224.png
security:
- kind: authentication
  name: The Graph Authentication
  slug: the-graph-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: The Graph Domain Security
  slug: the-graph-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: The Graph Vulnerability Disclosure
  slug: the-graph-vulnerability-disclosure
  summary_line: disclosure policy published
slug: the-graph
tags:
- Web3
- Indexing
- GraphQL
- Subgraphs
- Multi-chain
website: https://thegraph.com/
---
