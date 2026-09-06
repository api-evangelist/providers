---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Auto-generated GraphQL API exposing indexed smart contract events from any EVM-compatible chain. HyperIndex processes on-chain events into queryable databases, supports multichain indexing from a sing
  name: HyperIndex GraphQL API
  slug: hyperindex-graphql-api
- description: 'High-performance data retrieval layer offering up to 2,000x faster blockchain data access than standard JSON-RPC endpoints. Supports structured queries over logs, transactions, and traces across 100+ '
  name: HyperSync REST API
  slug: hypersync-rest-api
- description: Read-only JSON-RPC endpoint optimised for data-intensive operations, providing up to 5x performance improvement over standard node providers. Functions as a drop-in replacement for existing Ethereum J
  name: HyperRPC JSON-RPC API
  slug: hyperrpc-json-rpc-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/envio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://envio.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.envio.dev/docs/HyperIndex/overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/enviodev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/envio_indexer
- group: company
  title: ''
  type: Blog
  url: https://docs.envio.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://envio.dev/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/envio_indexer
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/envio
- group: commercial
  title: ''
  type: Plans
  url: plans/envio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/envio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/envio-finops.yml
created: '2026-06-13'
description: Envio is a high-performance blockchain data indexing platform providing developers with the fastest and most flexible way to access on-chain data. Its core products — HyperIndex, HyperSync, and HyperRPC — enable real-time and historical indexing across 100+ EVM networks and beyond, exposing indexed smart contract events through auto-generated GraphQL APIs and a REST-based HyperSync data retrieval layer. Envio Cloud offers fully managed hosting with git-based deployments, zero-downtime rollbacks, and multi-region support.
finops:
- name: Envio Finops
  service_category: ''
  slug: envio-finops
graphqls:
- description: The Envio HyperIndex GraphQL API exposes indexed smart contract events and blockchain state from any EVM-compatible chain. Each HyperIndex deployment auto-generates a GraphQL API based on the user-def
  name: Envio GraphQL API
  slug: envio-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/envio.png
jsonld:
- class_count: 35
  name: Envio Context
  property_count: 0
  slug: envio-context
layout: provider
modified: '2026-06-13'
name: Envio
nav: Providers
network: true
overview: 'Envio publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Indexer, GraphQL, Web3, and EVM.


  The Envio catalog on APIs.io includes 1 JSON-LD context.


  Envio''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Envio Plans Pricing
  plan_count: 5
  slug: envio-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Envio Rate Limits
  slug: envio-rate-limits
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 63.0
    catalog_earned_first_party: 0.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 36.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/envio/refs/heads/main/screenshots/envio-2026-06-20T180740.png
security:
- kind: domain-security
  name: Envio Domain Security
  slug: envio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: envio
tags:
- Blockchain
- Indexer
- GraphQL
- Web3
- EVM
- Smart Contracts
- Data
- HyperSync
- HyperIndex
- Multi-Chain
website: https://envio.dev
---
