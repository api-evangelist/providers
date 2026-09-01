---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 4
apis:
- description: Finds and returns the optimal swap route across 420+ liquidity sources on 17+ EVM chains. Returns the best route and encodes calldata for submission to the KyberSwap Aggregator smart contract.
  name: KyberSwap Aggregator API
  slug: kyberswap-aggregator-api
- description: Enables creation, management, and fulfillment of gasless limit orders. Exposes General, Maker, and Taker endpoint sets for reading order pairs, signing and submitting orders, and encoding fill calldat
  name: KyberSwap Limit Order API
  slug: kyberswap-limit-order-api
- description: Streamlines adding and removing concentrated liquidity positions using any single token. Provides Zap-In, Zap-Out, and Zap-Migrate endpoints via HTTP REST and gRPC. Powers KyberSwap Earn and the Liqui
  name: KyberSwap Zap as a Service (ZaaS) API
  slug: kyberswap-zap-as-a-service-zaas-api
- description: Delivers accurate, reliable, and tradable on-chain token price data for each supported network, reflecting real liquidity rather than averaged aggregations. Available on all chains supported by KyberS
  name: KyberSwap OnChain Price Service API
  slug: kyberswap-onchain-price-service-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyberswap-domain-security.yml
created: '2026-06-14'
description: KyberSwap is a multi-chain DEX aggregator and liquidity protocol offering REST APIs for swap routing, limit orders, liquidity provision via Zap-as-a-Service, and on-chain token pricing. It aggregates liquidity across 420+ sources on 17+ EVM chains, enabling developers to access best-rate swaps, manage limit orders gaslessly, and enter or exit concentrated liquidity positions with any single token.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: KyberSwap Elastic exposes on-chain liquidity data through The Graph Protocol subgraph. The subgraph indexes all events from the KyberSwap Elastic (concentrated liquidity) smart contracts on Ethereum m
  name: KyberSwap GraphQL API
  slug: kyberswap-graphql
image: https://kyberswap.com/favicon.ico
jsonld:
- class_count: 0
  name: Kyberswap Context
  property_count: 39
  slug: kyberswap-context
layout: provider
modified: '2026-06-14'
name: KyberSwap
nav: Providers
network: true
overview: 'KyberSwap publishes 2 APIs on the [APIs.io](https://apis.io/) network: Aggregator API and Limit Order API. Tagged areas include DeFi, DEX, Aggregator, Swap, and Liquidity.


  The KyberSwap catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 18
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 27.3
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
    contract_quality: 45.7
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 27.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyberswap/refs/heads/main/screenshots/kyberswap-2026-06-20T184226.png
security:
- kind: domain-security
  name: Kyberswap Domain Security
  slug: kyberswap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kyberswap
tags:
- DeFi
- DEX
- Aggregator
- Swap
- Liquidity
- Blockchain
- Web3
- Multi-Chain
- EVM
website: https://kyberswap.com
---
