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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Ethereum-compatible JSON-RPC API for Quai Network in the `quai_` namespace. Query balances, code, storage and proofs; read blocks, headers and uncles; look up and send transactions (Protobuf-encoded);
  name: Quai Network JSON-RPC API
  slug: quai-network-json-rpc-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://qu.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qu.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qu.ai/build/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qu.ai/build/playground/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qu.ai/build/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dominant-strategies
- group: company
  title: ''
  type: Blog
  url: https://quainetwork.com/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/ngw88VXXnV
- group: other
  title: ''
  type: Grants
  url: https://docs.qu.ai/build/grants
- group: build
  title: ''
  type: Postman
  url: https://docs.qu.ai/build/apis/postman/setup
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quai-network-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/quai-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quai-network-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/quai-network-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quai-network-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quai-network-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quai-network-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quai-network-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quai-network-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/quai-network-mcp.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/quai-network-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quai-network-domain-security.yml
created: '2026-07-17'
description: 'Quai Network is a sharded, EVM-compatible proof-of-work Layer-1 blockchain built by Dominant Strategies, featuring two native assets: QUAI, a smart-contract account-model asset, and Qi, a UTXO-model privacy asset. Quai uses Proof-of-Entropy-Minima (PoEM) consensus with merged mining across a hierarchical structure of Prime, Region, and Zone chains braided into one network. For developers, Quai exposes an Ethereum-compatible JSON-RPC API in the `quai_` namespace (plus a GraphQL endpoint and Postman collection), the Quais SDK (a fork of Ethers v6) for JavaScript/TypeScript dApps and wallets, and the go-quai node/CLI for running nodes and miners. The canonical active zone is Cyprus-1 (chainId 9 on mainnet, 15000 on the Orchard testnet).'
image: https://avatars.githubusercontent.com/u/54382906?v=4
layout: provider
mcp_servers:
- description: ''
  name: Quai Network MCP Server
  slug: quai-network-mcp-server
modified: '2026-07-20'
name: Quai Network
nav: Providers
network: true
overview: 'Quai Network publishes 1 API on the [APIs.io](https://apis.io/) network: JSON-RPC API. Tagged areas include Company, Layer 1, Blockchain, Cryptocurrency, and Web3.


  Quai Network''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 15 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 25.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Quai Network Authentication
  slug: quai-network-authentication
  summary_line: none · 2 schemes
- kind: domain-security
  name: Quai Network Domain Security
  slug: quai-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quai-network
tags:
- Company
- Layer 1
- Blockchain
- Cryptocurrency
- Web3
- Smart Contracts
- EVM
- JSON-RPC
- Proof of Work
- Developer Tools
website: https://qu.ai
---
