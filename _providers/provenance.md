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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Public Cosmos SDK REST (LCD / gRPC-gateway), gRPC, and Tendermint RPC interface to the Provenance Blockchain. Query and broadcast transactions against the marker, metadata, exchange, ledger, name, att
  name: Provenance Blockchain API
  slug: provenance-blockchain-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://provenance.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.provenance.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.provenance.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.provenance.io/build/sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.provenance.io/build/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/provenance-io
- group: operate
  title: ''
  type: Support
  url: https://docs.provenance.io/community/support
- group: other
  title: ''
  type: Protobuf
  url: grpc/provenance-marker-query.proto
- group: build
  title: ''
  type: Packages
  url: packages/provenance-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/provenance-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/provenance-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/provenance-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/provenance-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/provenance-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/provenance-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/provenance-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/provenance-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/provenance-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/provenance-domain-security.yml
created: '2026-07-17'
description: Provenance Blockchain is a public, proof-of-stake blockchain purpose-built for financial services and the tokenization of real-world assets. Built on the Cosmos SDK with CometBFT consensus, it exposes its functionality through first-party modules including marker (token/marker issuance), metadata (asset registry and the p8e contract execution environment), exchange (on-chain order book), ledger, name, attribute, hold, trigger, and msgfees/flatfees. Applications integrate over the public Cosmos REST (LCD / gRPC-gateway) API at api.provenance.io, gRPC, and Tendermint RPC at rpc.provenance.io, and via first-party SDKs (Go, Kotlin gRPC client, Rust/CosmWasm provwasm bindings, and JavaScript wallet libraries). HASH is the native staking and gas token. The chain, protobuf data model, and SDKs are open source under the provenance-io GitHub organization.
image: https://avatars.githubusercontent.com/provenance-io
layout: provider
mcp_servers:
- description: ''
  name: provenance-mcp.yml
  slug: provenance-mcpyml
modified: '2026-07-20'
name: Provenance
nav: Providers
network: true
overview: 'Provenance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Financial Services, Tokenization, and Real-World Assets.


  Provenance''s developer surface includes documentation, API reference, getting-started guide, support, changelog, authentication, and 13 more developer resources.'
random_paper: 33
score:
  band: emerging
  composite: 23.6
  delta: -1.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 25.0
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Provenance Authentication
  slug: provenance-authentication
  summary_line: none-for-reads/signature-based-for-writes · 2 schemes
- kind: domain-security
  name: Provenance Domain Security
  slug: provenance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: provenance
tags:
- Company
- Blockchain
- Financial Services
- Tokenization
- Real-World Assets
- Cosmos SDK
- gRPC
- Web3
- DeFi
- Digital Assets
website: https://provenance.io/
---
