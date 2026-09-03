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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Kadena Agentic Access
  operation_count: 37
  slug: kadena-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 2
apis:
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: These endpoints return whole blocks, headers and payloads, from the chain database. Generally, blocks are returned in ascending order and include orphaned blocks. For only querying blocks that are inc
  name: Kadena block API
  slug: kadena-block-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: These endpoints return block hashes from the chain database. Generally, block hashes are returned in ascending order and include hashes from orphaned blocks. For only querying blocks that are included
  name: Kadena blockhash API
  slug: kadena-blockhash-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The config API from Kadena — 1 operation(s) for config.
  name: Kadena config API
  slug: kadena-config-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: A cut represents a distributed state of a chainweb. It references one block header for each chain, such that those blocks are pairwise concurrent. Two blocks from two different chains are said to be c
  name: Kadena cut API
  slug: kadena-cut-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The endpoint-listen API from Kadena — 1 operation(s) for endpoint-listen.
  name: Kadena endpoint-listen API
  slug: kadena-endpoint-listen-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The endpoint-local API from Kadena — 1 operation(s) for endpoint-local.
  name: Kadena endpoint-local API
  slug: kadena-endpoint-local-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The endpoint-poll API from Kadena — 1 operation(s) for endpoint-poll.
  name: Kadena endpoint-poll API
  slug: kadena-endpoint-poll-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The endpoint-private API from Kadena — 1 operation(s) for endpoint-private.
  name: Kadena endpoint-private API
  slug: kadena-endpoint-private-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The endpoint-send API from Kadena — 1 operation(s) for endpoint-send.
  name: Kadena endpoint-send API
  slug: kadena-endpoint-send-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The endpoint-spv API from Kadena — 1 operation(s) for endpoint-spv.
  name: Kadena endpoint-spv API
  slug: kadena-endpoint-spv-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: These endpoints return block headers from the chain database. Similar to the block endpoints, block headers are generally returned in ascending order and include headers of orphaned blocks. For only q
  name: Kadena header API
  slug: kadena-header-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: Mempool P2P endpoints for communication between mempools. Endusers are not supposed to use these endpoints directly. Instead, the respective Pact endpoints should be used for submitting transactions i
  name: Kadena mempool API
  slug: kadena-mempool-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The Mining API of Chainweb node is disabled by default. It can be enabled and configured in the configuration file. The mining API consists of the following endpoints that are described in detail on t
  name: Kadena mining API
  slug: kadena-mining-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The misc API from Kadena — 7 operation(s) for misc.
  name: Kadena misc API
  slug: kadena-misc-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: Raw literal Block Payloads in the form in which they are stored on the chain. By default only the payload data is returned which is sufficient for validating the blockchain Merkle Tree. It is also suf
  name: Kadena payload API
  slug: kadena-payload-api
- baseURL: https://api.chainweb.com/chainweb/0.0/mainnet01
  baseurl_source: declared
  description: The P2P communication between chainweb-nodes is sharded into several independent P2P network. The `cut` network is exchanging consensus state. There is also one mempool P2P network for each chain.
  name: Kadena peer API
  slug: kadena-peer-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kadena Chainweb Node block API
  slug: open-kadena-block-api
- collection_type: open
  name: Kadena Chainweb Node block blockhash API
  slug: open-kadena-blockhash-api
- collection_type: open
  name: Kadena Chainweb Node block config API
  slug: open-kadena-config-api
- collection_type: open
  name: Kadena Chainweb Node block cut API
  slug: open-kadena-cut-api
- collection_type: open
  name: Kadena Chainweb Node block endpoint-listen API
  slug: open-kadena-endpoint-listen-api
- collection_type: open
  name: Kadena Chainweb Node block endpoint-local API
  slug: open-kadena-endpoint-local-api
- collection_type: open
  name: Kadena Chainweb Node block endpoint-poll API
  slug: open-kadena-endpoint-poll-api
- collection_type: open
  name: Kadena Chainweb Node block endpoint-private API
  slug: open-kadena-endpoint-private-api
- collection_type: open
  name: Kadena Chainweb Node block endpoint-send API
  slug: open-kadena-endpoint-send-api
- collection_type: open
  name: Kadena Chainweb Node block endpoint-spv API
  slug: open-kadena-endpoint-spv-api
- collection_type: open
  name: Kadena Chainweb Node block header API
  slug: open-kadena-header-api
- collection_type: open
  name: Kadena Chainweb Node block mempool API
  slug: open-kadena-mempool-api
- collection_type: open
  name: Kadena Chainweb Node block mining API
  slug: open-kadena-mining-api
- collection_type: open
  name: Kadena Chainweb Node block misc API
  slug: open-kadena-misc-api
- collection_type: open
  name: Kadena Chainweb Node block payload API
  slug: open-kadena-payload-api
- collection_type: open
  name: Kadena Chainweb Node block peer API
  slug: open-kadena-peer-api
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
  name: Kadena MCP Server
  slug: kadena-mcp-server
modified: '2026-07-19'
name: Kadena
nav: Providers
network: true
overview: 'Kadena publishes 16 APIs on the [APIs.io](https://apis.io/) network, including block API, blockhash API, config API, and 13 more. Tagged areas include Company, Crypto Web3, Blockchain, Smart Contracts, and Proof of Work.


  Kadena''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, CLI, sandbox, and 17 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 46.4
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
