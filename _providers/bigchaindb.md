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
api_count: 1
apis:
- baseURL: https://test.ipdb.io:9984
  baseurl_source: declared
  description: Full-text search over asset payloads.
  name: Bigchaindb Assets API
  slug: bigchaindb-assets-api
- baseURL: https://test.ipdb.io:9984
  baseurl_source: declared
  description: Read blocks by height or by contained transaction.
  name: Bigchaindb Blocks API
  slug: bigchaindb-blocks-api
- baseURL: https://test.ipdb.io:9984
  baseurl_source: declared
  description: Full-text search over transaction metadata.
  name: Bigchaindb Metadata API
  slug: bigchaindb-metadata-api
- baseURL: https://test.ipdb.io:9984
  baseurl_source: declared
  description: List transaction outputs by public key.
  name: Bigchaindb Outputs API
  slug: bigchaindb-outputs-api
- baseURL: https://test.ipdb.io:9984
  baseurl_source: declared
  description: Node discovery endpoints.
  name: Bigchaindb Root API
  slug: bigchaindb-root-api
- baseURL: https://test.ipdb.io:9984
  baseurl_source: declared
  description: Create and read transactions (CREATE and TRANSFER operations).
  name: Bigchaindb Transactions API
  slug: bigchaindb-transactions-api
- baseURL: https://test.ipdb.io:9984
  baseurl_source: declared
  description: Read the node's validator set.
  name: Bigchaindb Validators API
  slug: bigchaindb-validators-api
artifact_total: 16
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
  type: X-MCPServerCandidate
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
modified: '2026-07-18'
name: Bigchaindb
nav: Providers
network: true
overview: 'Bigchaindb publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Blocks API, Metadata API, and 4 more. Tagged areas include Company, Crypto, Blockchain, Database, and Decentralization.


  Bigchaindb''s developer surface includes documentation, getting-started guide, engineering blog, and 15 more developer resources.'
random_paper: 11
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
