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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Meter Agentic Access
  operation_count: 28
  slug: meter-agentic-access
  summary_line: 28 operations · 12 acting
api_count: 8
apis:
- description: Access to account objects
  name: Meter Accounts API
  slug: meter-accounts-api
- description: Access to blocks
  name: Meter Blocks API
  slug: meter-blocks-api
- description: Debug utilities
  name: Meter Debug API
  slug: meter-debug-api
- description: Access to event & transfer logs
  name: Meter Logs API
  slug: meter-logs-api
- description: Access to node status info
  name: Meter Node API
  slug: meter-node-api
- description: Access to staking data
  name: Meter Staking API
  slug: meter-staking-api
- description: Subscribe interested subjects
  name: Meter Subscriptions API
  slug: meter-subscriptions-api
- description: Access to transactions
  name: Meter Transactions API
  slug: meter-transactions-api
artifact_total: 12
asyncapis:
- description: 'Real-time WebSocket subscription channels of the Meter native node API, generated from the /subscriptions/* GET (websocket-upgrade) operations declared in the Meter RESTful OpenAPI (Meterest v1.2.2). '
  name: Meter Subscriptions (WebSocket)
  slug: meter-subscriptions-asyncapi
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/meter-openapi-original.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/meter-subscriptions-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/meter-subscriptions-asyncapi.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/meter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meter-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/meter-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/meter-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meter-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meter-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/meter-openapi-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/meter-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/meter-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/meter-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meter-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/meter-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/meter-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/meter-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.meter.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meter.io/developer-documentation/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meter.io/developer-documentation/meterify-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.meter.io/developer-documentation/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meterio
- group: company
  title: ''
  type: Blog
  url: https://medium.com/meter-io
- group: operate
  title: ''
  type: Support
  url: https://forum.meter.io/
- group: start
  title: ''
  type: SignUp
  url: https://wallet.meter.io/
- group: company
  title: ''
  type: Website
  url: https://www.meter.io/
created: '2026-07-17'
description: Meter is a high-performance, EVM-compatible Layer-1 blockchain and cross-chain infrastructure network built for the Web3 economy, backed by General Catalyst and Pantera Capital. Its HotStuff-based hybrid PoV consensus delivers thousands of TPS with instant finality, MEV/censorship resistance, and a metastable gas currency (MTR) pegged to energy alongside the MTRG governance token. Developers reach Meter through a standard Ethereum JSON-RPC endpoint (rpc.meter.io) that works with web3.js, ethers.js, Hardhat, Remix and MetaMask, and through a native RESTful node API ("Meterest") covering accounts, blocks, transactions, event/transfer logs, node status, staking and WebSocket subscriptions. The Meter Passport bridge provides generic cross-chain messaging and asset transfer, and the meterify library gives a web3.js-style adaptor to the native API.
image: https://avatars.githubusercontent.com/u/50934298?v=4
layout: provider
mcp_servers:
- description: ''
  name: meter-mcp.yml
  slug: meter-mcpyml
modified: '2026-07-20'
name: Meter
nav: Providers
network: true
overview: 'Meter publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Debug API, and 5 more. Tagged areas include Blockchain, Web3, Cryptocurrency, Layer-1, and EVM.


  The Meter catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Meter''s developer surface includes changelog, sandbox, documentation, API reference, getting-started guide, engineering blog, support, and 20 more developer resources.'
random_paper: 49
score:
  band: thin
  composite: 40.2
  delta: -4.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 46.4
    developer_ergonomics: 58.2
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 44.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Meter Domain Security
  slug: meter-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meter
tags:
- Blockchain
- Web3
- Cryptocurrency
- Layer-1
- EVM
- Cross-chain Bridge
- Staking
- Developer Tools
website: https://www.meter.io/
---
