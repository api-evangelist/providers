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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BigchainDB HTTP Assets API
  slug: open-bigchaindb-assets-api
- collection_type: open
  name: BigchainDB HTTP Assets Blocks API
  slug: open-bigchaindb-blocks-api
- collection_type: open
  name: BigchainDB HTTP Assets Metadata API
  slug: open-bigchaindb-metadata-api
- collection_type: open
  name: BigchainDB HTTP Assets Outputs API
  slug: open-bigchaindb-outputs-api
- collection_type: open
  name: BigchainDB HTTP Assets Root API
  slug: open-bigchaindb-root-api
- collection_type: open
  name: BigchainDB HTTP Assets Transactions API
  slug: open-bigchaindb-transactions-api
- collection_type: open
  name: BigchainDB HTTP Assets Validators API
  slug: open-bigchaindb-validators-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bigchaindb-mcp.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bigchaindb/bigchaindb/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/bigchaindb/bigchaindb/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bigchaindb/bigchaindb/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bigchaindb/bigchaindb/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/bigchaindb/bigchaindb/blob/master/LICENSE
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
mcp_servers:
- description: ''
  name: Bigchaindb MCP Server
  slug: bigchaindb-mcp-server
modified: '2026-07-18'
name: Bigchaindb
nav: Providers
network: true
overview: 'Bigchaindb publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Blocks API, Metadata API, and 4 more. Tagged areas include Company, Crypto, Blockchain, Database, and Decentralization.


  Bigchaindb''s developer surface includes documentation, getting-started guide, engineering blog, and 15 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 11.7
    developer_ergonomics: 58.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  open_source:
    applies: true
    score: 65.0
  previous_composite: 32.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
