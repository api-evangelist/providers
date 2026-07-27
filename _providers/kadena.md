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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 51.0
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Kadena Agentic Access
  operation_count: 37
  slug: kadena-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 16
apis:
- description: These endpoints return whole blocks, headers and payloads, from the chain database. Generally, blocks are returned in ascending order and include orphaned blocks. For only querying blocks that are inc
  name: Kadena block API
  slug: kadena-block-api
- description: These endpoints return block hashes from the chain database. Generally, block hashes are returned in ascending order and include hashes from orphaned blocks. For only querying blocks that are included
  name: Kadena blockhash API
  slug: kadena-blockhash-api
- description: The config API from Kadena — 1 operation(s) for config.
  name: Kadena config API
  slug: kadena-config-api
- description: A cut represents a distributed state of a chainweb. It references one block header for each chain, such that those blocks are pairwise concurrent. Two blocks from two different chains are said to be c
  name: Kadena cut API
  slug: kadena-cut-api
- description: The endpoint-listen API from Kadena — 1 operation(s) for endpoint-listen.
  name: Kadena endpoint-listen API
  slug: kadena-endpoint-listen-api
- description: The endpoint-local API from Kadena — 1 operation(s) for endpoint-local.
  name: Kadena endpoint-local API
  slug: kadena-endpoint-local-api
- description: The endpoint-poll API from Kadena — 1 operation(s) for endpoint-poll.
  name: Kadena endpoint-poll API
  slug: kadena-endpoint-poll-api
- description: The endpoint-private API from Kadena — 1 operation(s) for endpoint-private.
  name: Kadena endpoint-private API
  slug: kadena-endpoint-private-api
- description: The endpoint-send API from Kadena — 1 operation(s) for endpoint-send.
  name: Kadena endpoint-send API
  slug: kadena-endpoint-send-api
- description: The endpoint-spv API from Kadena — 1 operation(s) for endpoint-spv.
  name: Kadena endpoint-spv API
  slug: kadena-endpoint-spv-api
- description: These endpoints return block headers from the chain database. Similar to the block endpoints, block headers are generally returned in ascending order and include headers of orphaned blocks. For only q
  name: Kadena header API
  slug: kadena-header-api
- description: Mempool P2P endpoints for communication between mempools. Endusers are not supposed to use these endpoints directly. Instead, the respective Pact endpoints should be used for submitting transactions i
  name: Kadena mempool API
  slug: kadena-mempool-api
- description: The Mining API of Chainweb node is disabled by default. It can be enabled and configured in the configuration file. The mining API consists of the following endpoints that are described in detail on t
  name: Kadena mining API
  slug: kadena-mining-api
- description: The misc API from Kadena — 7 operation(s) for misc.
  name: Kadena misc API
  slug: kadena-misc-api
- description: Raw literal Block Payloads in the form in which they are stored on the chain. By default only the payload data is returned which is sufficient for validating the blockchain Merkle Tree. It is also suf
  name: Kadena payload API
  slug: kadena-payload-api
- description: The P2P communication between chainweb-nodes is sharded into several independent P2P network. The `cut` network is exchanging consensus state. There is also one mempool P2P network for each chain.
  name: Kadena peer API
  slug: kadena-peer-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kadena-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kadena-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kadena.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kadena.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kadena.io
- group: docs
  title: ''
  type: APIReference
  url: https://kadena-io.github.io/chainweb-openapi/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kadena.io/build/quickstart
- group: company
  title: ''
  type: Blog
  url: https://medium.com/kadena-io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kadena-io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.kadena.io/changelogs/chainweb-node
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kadena-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/kadena-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kadena-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kadena-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kadena-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kadena-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/kadena-chainweb-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/kadena-pact-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/kadena-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kadena-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kadena-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kadena-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kadena-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kadena-data-model.yml
created: '2026-07-17'
description: 'Kadena was a layer-1 Proof-of-Work blockchain platform built around Chainweb, a braided, parallelized Nakamoto-consensus protocol that scales Bitcoin-style security across many chains for high transaction throughput, together with Pact, its human-readable, Turing-incomplete smart-contract language. Kadena exposed two primary public APIs: the Chainweb Node API (P2P and service endpoints for cuts, blocks, headers, payloads, the mempool, mining, and node info) and the Pact REST API (local, send, poll, listen, spv) for submitting and querying smart-contract transactions on mainnet and testnet. The developer surface includes the kadena.js TypeScript client libraries, the pactjs CLI for type generation, and extensive docs at docs.kadena.io. Kadena Eco supported an ecosystem of dApps, the Marmalade NFT standard, and tooling. NOTE: Kadena the company announced it would cease operations on 2025-10-21; Kadena Mainnet stopped producing blocks on 2025-11-15 and the kadena-io GitHub organization
  was archived on 2025-12-23. A community edition (kda-community) forked from mainnet on 2025-11-08 and continues the open-source protocol. This profile documents the public API surface as published.'
image: https://cdn.sanity.io/images/agrhq0bu/production/73f06e78e066f86e21cb84f82292494fe04b9be8-1438x472.png
layout: provider
mcp_servers:
- description: ''
  name: kadena-mcp.yml
  slug: kadena-mcpyml
modified: '2026-07-19'
name: Kadena
nav: Providers
network: true
overview: 'Kadena publishes 16 APIs on the [APIs.io](https://apis.io/) network, including block API, blockhash API, config API, and 13 more. Tagged areas include Company, Crypto Web3, Blockchain, Smart Contracts, and Proof of Work.


  Kadena''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, CLI, sandbox, and 17 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 45.5
    developer_ergonomics: 65.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kadena/refs/heads/main/screenshots/kadena-2026-07-25T223401.png
security:
- kind: domain-security
  name: Kadena Domain Security
  slug: kadena-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kadena
tags:
- Company
- Crypto Web3
- Blockchain
- Smart Contracts
- Proof of Work
- Layer 1
- Web3
- Cryptocurrency
- Developer Tools
- Decentralized
website: https://kadena.io
---
