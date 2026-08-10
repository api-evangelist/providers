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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 53.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Public JSON-RPC 2.0 interface to Nervos CKB nodes for querying chain state (blocks, transactions, cells), submitting signed transactions, and subscribing to new-tip events over WebSocket. Unauthentica
  name: CKB JSON-RPC API
  slug: ckb-json-rpc-api
artifact_total: 5
asyncapis:
- description: ''
  name: Nervos Ckb Subscriptions
  slug: nervos-ckb-subscriptions
common:
- group: company
  title: ''
  type: Website
  url: https://nervos.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nervos.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nervos.org/docs/getting-started/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/nervosnetwork/ckb/blob/master/rpc/README.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nervosnetwork
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/nervosnetwork/ckb/releases
- group: build
  title: ''
  type: Packages
  url: packages/nervos-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nervos-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nervos-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nervos-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nervos-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nervos-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nervos-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nervos-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nervos-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nervos-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nervos-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nervos-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nervos-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nervos-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nervos-ckb-subscriptions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nervos-changelog.yml
created: '2026-07-17'
description: Nervos is the organization behind Nervos CKB (Common Knowledge Base), a proof-of-work layer 1 blockchain built around the Cell Model - a flexible, UTXO-like state model - and CKB-VM, a RISC-V virtual machine for on-chain scripts. Developers interact with the network through a public JSON-RPC 2.0 API (HTTP, TCP, and WebSocket subscriptions), official SDKs for JavaScript/TypeScript (CCC), Rust, Go, and Java, and CLI tooling (ckb-cli, OffCKB). The docs surface first-class AI resources including an llms.txt map, agent instructions, packaged CKB Dev Skills, and a CKB AI MCP server. Nervos was surfaced as a portfolio company of Multicoin Capital and enriched from its public developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nervos.png
layout: provider
mcp_servers:
- description: ''
  name: nervos-mcp.yml
  slug: nervos-mcpyml
modified: '2026-07-20'
name: Nervos
nav: Providers
network: true
overview: 'Nervos publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Blockchain, Layer 1, and JSON-RPC.


  The Nervos catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nervos'' developer surface includes documentation, getting-started guide, API reference, changelog, CLI, authentication, sandbox, and 16 more developer resources.'
random_paper: 89
score:
  band: developing
  composite: 42.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 42.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Nervos Authentication
  slug: nervos-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Nervos Domain Security
  slug: nervos-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: nervos
tags:
- Company
- Crypto Web3
- Blockchain
- Layer 1
- JSON-RPC
- Smart Contracts
- Web3 Infrastructure
- Developer Tools
website: https://nervos.org
---
