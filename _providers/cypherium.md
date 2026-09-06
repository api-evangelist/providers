---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: Ethereum-compatible JSON-RPC node API for the Cypherium Layer-1 mainnet — eth, web3, net, personal, miner, txpool and admin namespaces over HTTP, WebSocket and IPC. EVM chain ID 16166, native currency
  name: Cypherium JSON-RPC API
  slug: cypherium-json-rpc-api
- description: Coinbase Rosetta API (Data + Construction) reference implementation for Cypherium, enabling standardized blockchain data access and stateless offline transaction construction for exchanges and wallets
  name: Rosetta Cypherium API
  slug: rosetta-cypherium-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.cypherium.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cypherium
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/cypherium/cypher
- group: company
  title: ''
  type: Blog
  url: https://www.cypherium.io/blog
- group: build
  title: ''
  type: Packages
  url: packages/cypherium-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cypherium-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cypherium-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cypherium-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cypherium-llms.txt
created: '2026-07-17'
description: Cypherium is a permissionless Layer-1 blockchain built to bridge centralized (CeFi) and decentralized (DeFi) finance and bring real-world assets on-chain at scale. It runs CypherBFT, a hybrid consensus that pairs GPU proof-of-work committee election with HotStuff Byzantine Fault Tolerance for near-instant finality, and is EVM/Solidity compatible (EVM chain ID 16166). Products include CypherLink (cross-ledger notary), Cypherium Connect (bank integration plugin, marketed as ISO 20022 compliant), the Cypherium Validator, and Cypherium ID (decentralized identity). Developers integrate through an Ethereum-style JSON-RPC node API (eth/web3/net/ personal/miner/txpool/admin namespaces over HTTP, WS and IPC) and a Coinbase Rosetta API implementation for exchange and wallet integration. Surfaced as a portfolio company of Pantera Capital and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cypherium.png
layout: provider
modified: '2026-07-18'
name: Cypherium
nav: Providers
network: true
overview: 'Cypherium publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, Layer 1, and JSON-RPC.


  Cypherium''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 13.9
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cypherium/refs/heads/main/screenshots/cypherium-2026-07-25T211054.png
security:
- kind: domain-security
  name: Cypherium Domain Security
  slug: cypherium-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cypherium
tags:
- Company
- Crypto
- Blockchain
- Layer 1
- JSON-RPC
- EVM
- DeFi
- Rosetta
- Consensus
website: https://www.cypherium.io/
---
