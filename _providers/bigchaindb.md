---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-08-10'
api_count: 7
apis:
- description: Full-text search over asset payloads.
  name: Bigchaindb Assets API
  slug: bigchaindb-assets-api
- description: Read blocks by height or by contained transaction.
  name: Bigchaindb Blocks API
  slug: bigchaindb-blocks-api
- description: Full-text search over transaction metadata.
  name: Bigchaindb Metadata API
  slug: bigchaindb-metadata-api
- description: List transaction outputs by public key.
  name: Bigchaindb Outputs API
  slug: bigchaindb-outputs-api
- description: Node discovery endpoints.
  name: Bigchaindb Root API
  slug: bigchaindb-root-api
- description: Create and read transactions (CREATE and TRANSFER operations).
  name: Bigchaindb Transactions API
  slug: bigchaindb-transactions-api
- description: Read the node's validator set.
  name: Bigchaindb Validators API
  slug: bigchaindb-validators-api
artifact_total: 8
common:
- group: build
  title: ''
  type: Packages
  url: packages/bigchaindb-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bigchaindb-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bigchaindb-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bigchaindb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bigchaindb.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bigchaindb.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.bigchaindb.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bigchaindb
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bigchaindb.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bigchaindb.com/privacy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/bigchaindb/bigchaindb
- group: company
  title: ''
  type: Website
  url: https://www.bigchaindb.com/
created: '2026-07-17'
description: 'BigchainDB is an open-source blockchain database that combines the developer experience and query power of a database with blockchain properties: decentralized (Byzantine fault-tolerant) control, immutable append-only data storage, and built-in support for registering and transferring assets. Developed by BigchainDB GmbH (Berlin) with the IPDB Foundation overseeing the software and public networks, it exposes a simple versioned HTTP API on each node (default port 9984) for creating and reading transactions, assets, outputs, metadata, blocks and validators. Applications sign transactions with Ed25519 crypto-conditions, so authorization is enforced at the payload level rather than via transport authentication. Official Python, JavaScript and Java drivers are published, and the maintained continuation of the codebase is the Planetmint project.'
image: https://github.com/bigchaindb.png
layout: provider
modified: '2026-07-18'
name: Bigchaindb
nav: Providers
network: true
overview: 'Bigchaindb publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Blocks API, Metadata API, and 4 more. Tagged areas include Company, Crypto, Blockchain, Database, and Decentralization.


  Bigchaindb''s developer surface includes documentation, getting-started guide, engineering blog, and 9 more developer resources.'
random_paper: 91
score:
  band: thin
  composite: 34.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 53.4
    developer_ergonomics: 37.0
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 34.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bigchaindb/refs/heads/main/screenshots/bigchaindb-2026-07-25T202922.png
security:
- kind: authentication
  name: Bigchaindb Authentication
  slug: bigchaindb-authentication
  summary_line: none/payload-signature · 0 schemes
slug: bigchaindb
tags:
- Company
- Crypto
- Blockchain
- Database
- Decentralization
- Distributed Ledger
- Assets
- Immutability
website: https://www.bigchaindb.com/
---
