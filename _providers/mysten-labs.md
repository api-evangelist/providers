---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-17'
api_count: 3
apis:
- description: The Sui full-node JSON-RPC API (OpenRPC 1.2.6) for reading objects, coins, balances, events, checkpoints, dynamic fields, and system state, and for dry-running/executing transaction blocks. 56 methods
  name: Sui JSON-RPC API
  slug: sui-json-rpc-api
- description: The Sui GraphQL RPC API — a GraphQL interface over Sui network data (objects, transactions, events, checkpoints, coins, name service) served from indexed full-node data. Recommended replacement for JS
  name: Sui GraphQL RPC API
  slug: sui-graphql-rpc-api
- description: The Sui full-node gRPC API (Protobuf, sui.rpc.v2) exposing LedgerService, StateService, TransactionExecutionService, MovePackageService, SignatureVerificationService, and SubscriptionService for high-
  name: Sui gRPC API
  slug: sui-grpc-api
artifact_total: 8
asyncapis:
- description: ''
  name: Mysten Labs Subscriptions
  slug: mysten-labs-subscriptions
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sui.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sui.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sui.io/references/sui-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sui.io/guides/developer/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MystenLabs
- group: company
  title: ''
  type: Blog
  url: https://blog.sui.io
- group: company
  title: ''
  type: Website
  url: https://mystenlabs.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sui.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mysten-labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mysten-labs-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/mysten-labs-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/mysten-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mysten-labs-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mysten-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/sui/rpc/v2/ledger_service.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/mysten-labs-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mysten-labs-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mysten-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/mysten-labs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mysten-labs-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/mysten-labs-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mysten-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mysten-labs-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mysten-labs-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mysten-labs-subscriptions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mysten-labs-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mysten-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/MystenLabs/sui/blob/main/SECURITY.md
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mysten-labs-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/mysten-labs-components.yml
created: '2026-07-17'
description: 'Mysten Labs is the web3 infrastructure company that created Sui, a Layer 1 blockchain and smart-contract platform built on the Move programming language, and Walrus, a decentralized blob-storage network coordinated on Sui. Mysten Labs publishes the Sui developer platform: a JSON-RPC (OpenRPC) API, a GraphQL RPC API, and a gRPC (Protobuf) API for reading chain state, querying objects and events, and executing transactions, together with first-party TypeScript, Rust, and Move SDKs, the `sui` command-line interface, dApp Kit, and zkLogin/Enoki authentication tooling. The public full-node RPC endpoints are open (no API key), and the platform is fully open source under Apache 2.0.'
image: https://avatars.githubusercontent.com/MystenLabs
layout: provider
mcp_servers:
- description: ''
  name: mysten-labs-mcp.yml
  slug: mysten-labs-mcpyml
modified: '2026-07-20'
name: Mysten Labs
nav: Providers
network: true
overview: 'Mysten Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Web3, Sui, and Move.


  The Mysten Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mysten Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, CLI, and 24 more developer resources.'
random_paper: 92
score:
  band: developing
  composite: 46.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.6
    developer_ergonomics: 82.6
    discoverability: 81.5
    governance: 3.1
    operational_transparency: 63.2
  previous_composite: 46.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mysten-labs/refs/heads/main/screenshots/mysten-labs-2026-08-07T184544.png
security:
- kind: authentication
  name: Mysten Labs Authentication
  slug: mysten-labs-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Mysten Labs Domain Security
  slug: mysten-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mysten Labs Vulnerability Disclosure
  slug: mysten-labs-vulnerability-disclosure
  summary_line: contact published
slug: mysten-labs
tags:
- Company
- Blockchain
- Web3
- Sui
- Move
- JSON-RPC
- GraphQL
- gRPC
- SDK
- Smart Contracts
- Decentralized Storage
- Cryptocurrency
website: https://mystenlabs.com
---
