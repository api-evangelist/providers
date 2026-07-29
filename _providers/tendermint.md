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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: ABCI APIs
  name: Tendermint ABCI API
  slug: tendermint-abci-api
- description: Informations about the node APIs
  name: Tendermint Info API
  slug: tendermint-info-api
- description: Transactions broadcast APIs
  name: Tendermint Tx API
  slug: tendermint-tx-api
- description: Unsafe APIs
  name: Tendermint Unsafe API
  slug: tendermint-unsafe-api
- description: Subscribe/unsubscribe are reserved for websocket events.
  name: Tendermint Websocket API
  slug: tendermint-websocket-api
artifact_total: 10
asyncapis:
- description: ''
  name: Tendermint Events Webhooks
  slug: tendermint-events-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tendermint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tendermint.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tendermint.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tendermint.com/master/rpc/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tendermint.com/master/introduction/quick-start.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tendermint
- group: company
  title: ''
  type: Blog
  url: https://medium.com/tendermint
- group: operate
  title: ''
  type: Support
  url: https://forum.cosmos.network/c/tendermint
- group: build
  title: ''
  type: Packages
  url: packages/tendermint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tendermint-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tendermint-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tendermint-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tendermint-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tendermint-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tendermint-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tendermint-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tendermint-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tendermint-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tendermint-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tendermint-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tendermint-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tendermint-events-webhooks.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/tendermint-abci.proto
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tendermint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/tendermint/tendermint/blob/main/SECURITY.md
created: '2026-07-17'
description: Tendermint is a core contributor to the Cosmos Network and the original developer of Tendermint Core, a best-in-class Byzantine Fault Tolerant (BFT) consensus engine for state-machine replication, alongside the Cosmos SDK blockchain application framework and the IBC inter-blockchain communication protocol. Its primary developer-facing API is the Tendermint RPC — a JSONRPC 2.0 interface (also exposed as a REST-URI form and over websockets) for querying chain state, blocks, transactions and validators, and broadcasting transactions to a node. Tendermint Core has since been renamed to CometBFT, which is the actively maintained successor.
image: https://raw.githubusercontent.com/api-evangelist/tendermint/main/apis.yml
layout: provider
mcp_servers:
- description: ''
  name: tendermint-mcp.yml
  slug: tendermint-mcpyml
modified: '2026-07-21'
name: Tendermint
nav: Providers
network: true
overview: 'Tendermint publishes 5 APIs on the [APIs.io](https://apis.io/) network, including ABCI API, Info API, Tx API, and 2 more. Tagged areas include Company, Infrastructure, Blockchain, Consensus, and Cosmos.


  The Tendermint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tendermint''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 19 more developer resources.'
random_paper: 42
score:
  band: developing
  composite: 42.4
  delta: -3.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 58.7
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 45.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Tendermint Authentication
  slug: tendermint-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tendermint Domain Security
  slug: tendermint-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tendermint Vulnerability Disclosure
  slug: tendermint-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: tendermint
tags:
- Company
- Infrastructure
- Blockchain
- Consensus
- Cosmos
- Web3
- JSON-RPC
- Node
website: https://tendermint.com
---
