---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Airstack Agentic Access
  operation_count: 27
  slug: airstack-agentic-access
  summary_line: 27 operations · 5 acting
api_count: 14
apis:
- description: The primary Airstack API offering composable GraphQL queries across on-chain and off-chain Web3 data. Query NFT balances, token transfers, wallet identities, ENS names, POAP badges, and social graph d
  name: Airstack GraphQL API
  slug: airstack-graphql-api
- description: The Casts API from Airstack — 4 operation(s) for casts.
  name: Airstack Casts API
  slug: airstack-casts-api
- description: The FIDs API from Airstack — 1 operation(s) for fids.
  name: Airstack FIDs API
  slug: airstack-fids-api
- description: The HubEvents API from Airstack — 2 operation(s) for hubevents.
  name: Airstack HubEvents API
  slug: airstack-hubevents-api
- description: The Links API from Airstack — 3 operation(s) for links.
  name: Airstack Links API
  slug: airstack-links-api
- description: The OnChainEvents API from Airstack — 3 operation(s) for onchainevents.
  name: Airstack OnChainEvents API
  slug: airstack-onchainevents-api
- description: The Reactions API from Airstack — 4 operation(s) for reactions.
  name: Airstack Reactions API
  slug: airstack-reactions-api
- description: The Storage API from Airstack — 1 operation(s) for storage.
  name: Airstack Storage API
  slug: airstack-storage-api
- description: The SubmitMessage API from Airstack — 1 operation(s) for submitmessage.
  name: Airstack SubmitMessage API
  slug: airstack-submitmessage-api
- description: The UserData API from Airstack — 1 operation(s) for userdata.
  name: Airstack UserData API
  slug: airstack-userdata-api
- description: The Usernames API from Airstack — 2 operation(s) for usernames.
  name: Airstack Usernames API
  slug: airstack-usernames-api
- description: The ValidateMessage API from Airstack — 1 operation(s) for validatemessage.
  name: Airstack ValidateMessage API
  slug: airstack-validatemessage-api
- description: The Verifications API from Airstack — 1 operation(s) for verifications.
  name: Airstack Verifications API
  slug: airstack-verifications-api
- description: The Webhooks API from Airstack — 3 operation(s) for webhooks.
  name: Airstack Webhooks API
  slug: airstack-webhooks-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airstack-authentication.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/airstack/refs/heads/main/json-ld/airstack-context.json
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airstack/refs/heads/main/vocabulary/airstack-vocabulary.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/airstack/refs/heads/main/json-schema/farcaster-hub-api-schemas.json
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Airstack-xyz
- group: build
  title: ''
  type: WebSDK
  url: https://github.com/Airstack-xyz/airstack-web-sdk
- group: build
  title: ''
  type: NodeSDK
  url: https://github.com/Airstack-xyz/airstack-node-sdk
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/Airstack-xyz/airstack-python-sdk
- group: build
  title: ''
  type: FramesSDK
  url: https://github.com/Airstack-xyz/airstack-frames-sdk
- group: other
  title: ''
  type: Explorer
  url: https://explorer.airstack.xyz
- group: other
  title: ''
  type: Dashboard
  url: https://app.airstack.xyz
- group: company
  title: ''
  type: Blog
  url: https://blog.airstack.xyz
- group: other
  title: ''
  type: Telegram
  url: https://t.me/+1k3c2FR7z51mNDRh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airstack-xyz
created: '2024-01-01'
description: Airstack is a Web3 data aggregation platform providing GraphQL and REST APIs for querying on-chain and off-chain data across multiple blockchains. Developers can query NFT ownership, token balances, wallet identities, ENS names, POAP badges, and cross-chain data in a single composable request. The platform indexes Ethereum, Polygon, Base, and other EVM-compatible chains, enabling complex cross-project queries without running your own infrastructure.
graphqls:
- description: Airstack exposes a composable GraphQL API for querying on-chain and off-chain Web3 data across multiple EVM-compatible blockchains. The API aggregates token balances, NFT metadata, token transfers, wa
  name: Airstack GraphQL API
  slug: airstack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airstack.png
json_schemas:
- name: Airstack Farcaster Hub API Schemas
  property_count: 0
  slug: farcaster-hub-api-schemas
layout: provider
modified: '2026-06-13'
name: Airstack
nav: Providers
network: true
overview: 'Airstack publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Casts API, FIDs API, HubEvents API, and 10 more. Tagged areas include Web3, Blockchain, GraphQL, NFT, and Tokens.


  The Airstack catalog on APIs.io includes 1 Spectral governance ruleset.


  Airstack''s developer surface includes authentication, GitHub presence, engineering blog, and 13 more developer resources.'
random_paper: 30
rules:
- name: Airstack API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: airstack-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.5
  delta: -4.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.6
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airstack/refs/heads/main/screenshots/airstack-2026-06-20T171431.png
security:
- kind: authentication
  name: Airstack Authentication
  slug: airstack-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Airstack Domain Security
  slug: airstack-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: airstack
tags:
- Web3
- Blockchain
- GraphQL
- NFT
- Tokens
- On-Chain Data
- Ethereum
- Polygon
- Base
- ENS
- POAP
- Social Graph
- Wallet
- Identity
---
