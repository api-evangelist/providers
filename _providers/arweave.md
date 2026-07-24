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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 7
apis:
- description: GraphQL API for querying Arweave transaction and block metadata by tags, owner addresses, recipients, block height ranges, and transaction IDs. Supports cursor-based pagination and sorting. Primary en
  name: Arweave GraphQL API
  slug: arweave-graphql-api
- description: Managed bundling upload service (ar.io Turbo) that implements ANS-104 bundling for high-throughput data uploads to Arweave. Handles millions of uploads daily with automatic retry, sub-100 KiB free tie
  name: Arweave Turbo Upload API
  slug: arweave-turbo-upload-api
- description: Endpoints for retrieving block data
  name: Arweave Blocks API
  slug: arweave-blocks-api
- description: Endpoints for uploading and downloading data chunks
  name: Arweave Chunks API
  slug: arweave-chunks-api
- description: Endpoints for querying network state and peer information
  name: Arweave Network API
  slug: arweave-network-api
- description: Endpoints for submitting and retrieving transactions
  name: Arweave Transactions API
  slug: arweave-transactions-api
- description: Endpoints for querying wallet balances and transaction history
  name: Arweave Wallets API
  slug: arweave-wallets-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arweave-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arweave.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.arweave.org/developers
- group: learn
  title: ''
  type: Cookbook
  url: https://cookbook.arweave.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ar.io/build/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArweaveTeam
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/arweave/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/arweave/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/arweave/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: PricingPage
  url: https://docs.ar.io/build/upload/turbo-credits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ar.io/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/arweave
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ArweaveTeam
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arweave.org/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arweave.org/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://arweave.medium.com/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/arweave/refs/heads/main/vocabulary/arweave-vocabulary.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/arweave/refs/heads/main/json-ld/arweave-context.jsonld
description: Arweave is a permanent decentralized data storage network that enables developers to store data forever with a single upfront payment. It provides REST and GraphQL APIs for uploading data, querying blocks and transactions by tags and metadata, retrieving wallet balances, and accessing the permaweb data ecosystem. The network uses the AR token for storage fees and supports bundled uploads via the Turbo service with fiat and multi-chain crypto payment options.
examples:
- key_count: 4
  name: Get Network Info
  slug: get-network-info
- key_count: 5
  name: Get Transaction Price
  slug: get-transaction-price
- key_count: 5
  name: Get Wallet Balance
  slug: get-wallet-balance
- key_count: 4
  name: Submit Transaction
  slug: submit-transaction
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: 'The Arweave GraphQL API exposes a read-only query interface for searching and retrieving Arweave transaction and block metadata. It allows developers to find transactions by owner address, recipient, '
  name: Arweave GraphQL API
  slug: arweave-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arweave.png
json_schemas:
- name: Arweave Data Chunk
  property_count: 5
  slug: chunk
- name: Arweave Network Info
  property_count: 9
  slug: network-info
- name: Arweave Transaction
  property_count: 12
  slug: transaction
jsonld:
- class_count: 6
  name: Arweave Context
  property_count: 34
  slug: arweave-context
layout: provider
modified: '2026-06-13'
name: Arweave
nav: Providers
network: true
overview: 'Arweave publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Blocks API, Chunks API, Network API, and 2 more. Tagged areas include Decentralized Storage, Blockchain, Permaweb, Web3, and Data Storage.


  The Arweave catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arweave''s developer surface includes documentation, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 33
rate_limits:
- limit_count: 3
  name: Rate Limits
  slug: rate-limits
rules:
- name: Arweave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: arweave-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 61.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arweave/refs/heads/main/screenshots/arweave-2026-06-20T172449.png
security:
- kind: domain-security
  name: Arweave Domain Security
  slug: arweave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arweave
tags:
- Decentralized Storage
- Blockchain
- Permaweb
- Web3
- Data Storage
- GraphQL
website: https://www.arweave.org/
---
