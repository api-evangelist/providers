---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
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
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Litecoin Agentic Access
  operation_count: 61
  slug: litecoin-agentic-access
  summary_line: 61 operations · 2 acting
api_count: 10
apis:
- description: 'A real-time WebSocket API provided by Litecoin Space (litecoinspace.org) for subscribing to live Litecoin network events. Clients connect to the WebSocket endpoint and subscribe to channels including '
  name: Litecoin Space WebSocket API
  slug: litecoin-space-websocket-api
- description: Address lookup, transaction history, and UTXO endpoints
  name: Litecoin Addresses API
  slug: litecoin-addresses-api
- description: Chain state information endpoints
  name: Litecoin Blockchain API
  slug: litecoin-blockchain-api
- description: Block and header retrieval endpoints
  name: Litecoin Blocks API
  slug: litecoin-blocks-api
- description: Fee estimation and recommendation endpoints
  name: Litecoin Fees API
  slug: litecoin-fees-api
- description: Litecoin Core JSON-RPC 2.0 interface. All methods are accessed via a single POST endpoint using the method field to select the operation.
  name: Litecoin JSON-RPC API
  slug: litecoin-json-rpc-api
- description: Mempool state and contents endpoints
  name: Litecoin Mempool API
  slug: litecoin-mempool-api
- description: Mining pool statistics, hashrate, and difficulty endpoints
  name: Litecoin Mining API
  slug: litecoin-mining-api
- description: Transaction retrieval endpoints
  name: Litecoin Transactions API
  slug: litecoin-transactions-api
- description: Unspent transaction output query endpoints
  name: Litecoin UTXO API
  slug: litecoin-utxo-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/litecoin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/litecoin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/litecoin-authentication.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/litecoin/refs/heads/main/json-ld/litecoin.json
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/litecoin-project
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/litecoin-foundation
- group: company
  title: ''
  type: Website
  url: https://litecoin.org
- group: company
  title: ''
  type: Blog
  url: https://blog.litecoin.org
- group: other
  title: ''
  type: Explorer
  url: https://litecoinspace.org
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/litecoin-project/litecoin
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/litecoin-project/litecoin/releases
created: '2026-06-14'
description: Litecoin is a peer-to-peer cryptocurrency network based on the Bitcoin protocol, offering faster block times (2.5 minutes) and lower transaction fees. It exposes a JSON-RPC interface via Litecoin Core for direct node interaction, a built-in unauthenticated REST interface for public blockchain queries, and a Litecoin Space block explorer REST and WebSocket API (mempool.space-compatible) for querying transactions, addresses, blocks, UTXO data, mempool state, and fee estimates.
finops:
- name: Litecoin Core Json Rpc
  service_category: ''
  slug: litecoin-core-json-rpc
- name: Litecoin Core Rest
  service_category: ''
  slug: litecoin-core-rest
- name: Litecoin Space Rest
  service_category: ''
  slug: litecoin-space-rest
- name: Litecoin Space Websocket
  service_category: ''
  slug: litecoin-space-websocket
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/litecoin.png
layout: provider
modified: '2026-06-14'
name: Litecoin
nav: Providers
network: true
overview: 'Litecoin publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Blockchain API, Blocks API, and 6 more. Tagged areas include Cryptocurrency, Blockchain, Litecoin, LTC, and Payments.


  Litecoin''s developer surface includes authentication, engineering blog, changelog, and 8 more developer resources.'
plans:
- name: Litecoin Core Json Rpc
  plan_count: 1
  slug: litecoin-core-json-rpc
- name: Litecoin Core Rest
  plan_count: 1
  slug: litecoin-core-rest
- name: Litecoin Space Rest
  plan_count: 2
  slug: litecoin-space-rest
- name: Litecoin Space Websocket
  plan_count: 2
  slug: litecoin-space-websocket
random_paper: 39
rate_limits:
- limit_count: 0
  name: Litecoin Core Json Rpc
  slug: litecoin-core-json-rpc
- limit_count: 0
  name: Litecoin Core Rest
  slug: litecoin-core-rest
- limit_count: 0
  name: Litecoin Space Rest
  slug: litecoin-space-rest
- limit_count: 0
  name: Litecoin Space Websocket
  slug: litecoin-space-websocket
score:
  band: thin
  composite: 32.2
  delta: -1.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.8
    developer_ergonomics: 13.0
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.3
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/litecoin/refs/heads/main/screenshots/litecoin-2026-06-20T184600.png
security:
- kind: authentication
  name: Litecoin Authentication
  slug: litecoin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Litecoin Domain Security
  slug: litecoin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: litecoin
tags:
- Cryptocurrency
- Blockchain
- Litecoin
- LTC
- Payments
- Decentralized Finance
- Block Explorer
- JSON-RPC
website: https://litecoin.org
---
