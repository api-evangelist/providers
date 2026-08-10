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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Self-hosted gRPC interfaces (proto3, package tari.rpc) to a Tari base node and wallet, for querying the chain and controlling a wallet. Servers run locally on the operator's node rather than at a sing
  name: Tari Base Node & Wallet gRPC
  slug: tari-base-node-wallet-grpc
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://tari.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rfc.tari.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rfc.tari.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://tari.com/integration-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tari-project
- group: company
  title: ''
  type: Blog
  url: https://tari.com/updates
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/tari-project/tari/releases
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/tari-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tari-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tari-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tari-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tari-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tari-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tari-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tari-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tari-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tari-well-known.yml
created: '2026-07-17'
description: 'Tari is an open-source, proof-of-work blockchain protocol designed to be private by default (confidential transactions) and accessible to everyday users. Its Tari Universe application lets people mine XTM tokens by contributing compute, and the protocol has grown to hundreds of thousands of active miners. For developers, exchanges, and dApp builders, Tari exposes self-hosted Base Node and Wallet interfaces over gRPC (proto3, package tari.rpc): the Base Node service queries headers, blocks, mempool, network constants, block templates for miners, and PayRef payment-reference lookups, while the Wallet service handles balances, transfers, fee estimation, one-sided and atomic-swap transactions, transaction history, and a live transaction-event stream. A Layer-2 (Ootle) adds smart-contract templates via the tari-cli. Official TypeScript SDKs (tari.js, typescript-bindings, wallet JSON-RPC client) and Rust crates support integration. Tari is backed by Canaan Partners, Multicoin Capital,
  Pantera Capital, and Trinity Ventures.'
image: https://tari.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: tari-mcp.yml
  slug: tari-mcpyml
modified: '2026-07-21'
name: Tari
nav: Providers
network: true
overview: 'Tari publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Cryptocurrency, Protocol, and gRPC.


  Tari''s developer surface includes documentation, getting-started guide, engineering blog, changelog, CLI, and 13 more developer resources.'
random_paper: 84
score:
  band: emerging
  composite: 20.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 20.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Tari Domain Security
  slug: tari-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tari
tags:
- Company
- Blockchain
- Cryptocurrency
- Protocol
- gRPC
- Wallet
- Mining
- Privacy
- Web3
website: https://tari.com
---
