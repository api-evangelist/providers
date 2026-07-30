---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: 'The BandChain REST API provides HTTP access to BandChain mainnet data including oracle scripts, data requests, price feeds, validator information, account balances, and all Cosmos SDK module queries. '
  name: BandChain REST API
  slug: bandchain-rest-api
- description: The BandChain gRPC API provides high-performance protocol buffer access to BandChain nodes for querying oracle data, submitting data requests, managing accounts, and interacting with all Cosmos SDK an
  name: BandChain gRPC API
  slug: bandchain-grpc-api
- description: The BandChain V3 Testnet REST API mirrors the mainnet REST API and provides a sandbox environment for developing and testing integrations with BandChain oracle services. Includes a faucet endpoint for
  name: BandChain Testnet REST API
  slug: bandchain-testnet-rest-api
- description: BandChain.js is a comprehensive TypeScript library for seamless interaction with BandChain and Cosmos SDK blockchains. It supports querying oracle scripts, price feeds, validators, and governance prop
  name: BandChain.js SDK
  slug: bandchain-js-sdk
- description: 'PyBand is a Python SDK that offers a comprehensive set of features for interacting with BandChain via gRPC. It enables querying oracle scripts, data sources, request results, account information, and '
  name: PyBand Python SDK
  slug: pyband-sdk
- description: Band VRF is a provably fair, verifiable random function for on-chain randomness. It allows smart contracts to request cryptographically secure random numbers from BandChain validators, suitable for NF
  name: Band VRF
  slug: band-vrf
- description: The Band Standard Dataset is an open standard for creating and accessing custom price feeds that deliver highly efficient and secure financial data directly to smart contracts. Developers can query re
  name: Band Standard Dataset
  slug: band-standard-dataset
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/band-protocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bandprotocol.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bandchain.org
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bandchain.org/develop/api-endpoints
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bandprotocol
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bandprotocol/chain
- group: other
  title: ''
  type: BlockExplorer
  url: https://www.cosmoscan.io/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/3t4bsY7
- group: other
  title: ''
  type: Telegram
  url: https://t.me/bandprotocol
- group: company
  title: ''
  type: Blog
  url: https://medium.com/bandprotocol
created: '2026-06-13'
description: Band Protocol is a cross-chain data oracle platform that aggregates and connects real-world data and APIs to smart contracts. Built on BandChain, a high-performance Cosmos SDK blockchain, it enables developers to query price feeds, oracle scripts, data requests, and verifiable random numbers for use in decentralized applications across multiple blockchains.
finops:
- name: Band Protocol Finops
  service_category: Blockchain / Data Oracle
  slug: band-protocol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/band-protocol.png
layout: provider
modified: '2026-06-13'
name: Band Protocol
nav: Providers
network: true
overview: 'Band Protocol publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Oracle, Data Feeds, Price Feeds, and Cross-Chain.


  Band Protocol''s developer surface includes documentation, getting-started guide, engineering blog, and 7 more developer resources.'
plans:
- name: Band Protocol Plans Pricing
  plan_count: 3
  slug: band-protocol-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Band Protocol Rate Limits
  slug: band-protocol-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 27.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/band-protocol/refs/heads/main/screenshots/band-protocol-2026-06-20T173037.png
security:
- kind: domain-security
  name: Band Protocol Domain Security
  slug: band-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: band-protocol
tags:
- Blockchain
- Oracle
- Data Feeds
- Price Feeds
- Cross-Chain
- DeFi
- Cosmos
website: https://bandprotocol.com
---
