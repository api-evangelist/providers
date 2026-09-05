---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: The Starknet full-node JSON-RPC API (OpenRPC), covering read methods (blocks, transactions, state, classes, events, fees), write methods (add invoke/declare/deploy-account transactions), trace methods
  name: Starknet Node JSON-RPC API
  slug: starknet-node-json-rpc-api
- description: 'The Starknet wallet JSON-RPC API (SNIP-based) that dApps use to talk to browser/extension wallets: request accounts, permissions, chain switching, typed-data signing, and submitting invoke/declare tra'
  name: Starknet Wallet JSON-RPC API
  slug: starknet-wallet-json-rpc-api
- description: The Starknet proving JSON-RPC API for submitting transactions to be proven by the STARK prover.
  name: Starknet Proving API
  slug: starknet-proving-api
- description: StarkEx application-specific scaling engine REST API for spot and perpetual trading systems, exposing Gateway, Feeder Gateway, and Availability Gateway endpoints plus documented error codes.
  name: StarkEx REST API
  slug: starkex-rest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Starkware Websocket Events
  slug: starkware-websocket-events
common:
- group: company
  title: ''
  type: Website
  url: https://starkware.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.starknet.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.starknet.io/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/starkware-libs/starknet-specs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.starknet.io/developers/
- group: company
  title: ''
  type: Blog
  url: https://starkware.co/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starkware-libs
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/starkware-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/starkware-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/starkware-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/starkware-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/starkware-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/starkware-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/starkware-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/starkware-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/starkware-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/starkware-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/starkware-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/starkware-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/starkware-websocket-events.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/starkware-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starkware-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starkware-llms.txt
created: '2026-07-17'
description: StarkWare Industries builds STARK-proof (Scalable Transparent ARgument of Knowledge) blockchain scaling technology for Ethereum. Its flagship products are Starknet, a permissionless decentralized validity-rollup (ZK-Rollup) where developers deploy Cairo smart contracts, and StarkEx, an application-specific scaling engine for exchanges (spot, perpetual, NFT, and payments). The developer surface centers on the Starknet Node JSON-RPC API (read, write, trace, and WebSocket methods specified in OpenRPC), a Wallet JSON-RPC API, a Proving API, StarkEx REST gateways, first-party SDKs (starknet.js, starknet.py, starkex-js), the starkli CLI, and the Cairo programming language and prover stack (Stwo, Cairo VM). This profile catalogs those machine-readable specs and developer artifacts for the API Evangelist network.
image: https://github.com/starkware-libs.png
layout: provider
mcp_servers:
- description: Official StarkWare MCP (Model Context Protocol) server that exposes all Starknet JSON-RPC v0.10.2+ read and trace methods as agent tools, letting an assistant read blocks, transactions, state, classes
  name: Starkware MCP Server
  slug: starkware-mcp-server
modified: '2026-07-21'
name: Starkware
nav: Providers
network: true
overview: 'Starkware publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Ethereum, Layer 2, and ZK-Rollup.


  The Starkware catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Starkware''s developer surface includes documentation, API reference, getting-started guide, engineering blog, CLI, authentication, changelog, and 18 more developer resources.'
random_paper: 14
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 75.6
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 38.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/starkware/refs/heads/main/screenshots/starkware-2026-09-02T160805.png
security:
- kind: authentication
  name: Starkware Authentication
  slug: starkware-authentication
  summary_line: none/api-key-at-provider · 3 schemes
- kind: domain-security
  name: Starkware Domain Security
  slug: starkware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: starkware
tags:
- Company
- Blockchain
- Ethereum
- Layer 2
- ZK-Rollup
- Zero-Knowledge Proofs
- JSON-RPC
- Cryptography
- Cairo
- Web3
- Scaling
- Starknet
website: https://starkware.co
---
