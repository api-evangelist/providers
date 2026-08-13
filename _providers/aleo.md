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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aleo Agentic Access
  operation_count: 13
  slug: aleo-agentic-access
  summary_line: 13 operations · 1 acting
api_count: 5
apis:
- description: Block and transaction queries
  name: Aleo Blocks API
  slug: aleo-blocks-api
- description: Latest chain state
  name: Aleo Chain API
  slug: aleo-chain-api
- description: Committee and consensus state
  name: Aleo Network API
  slug: aleo-network-api
- description: Deployed program and mapping queries
  name: Aleo Programs API
  slug: aleo-programs-api
- description: Transaction submission
  name: Aleo Transactions API
  slug: aleo-transactions-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aleo-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aleo-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aleo.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aleo.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aleo.org/build/sdk/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aleo.org/build/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProvableHQ
- group: company
  title: ''
  type: Blog
  url: https://provable.com/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/aleo
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aleo-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://play.leo-lang.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://provable.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aleo.org/
- group: other
  title: ''
  type: X
  url: https://x.com/provablehq
- group: build
  title: ''
  type: Packages
  url: packages/aleo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aleo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/aleo-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aleo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aleo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aleo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/aleo-node-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/aleo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aleo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aleo-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aleo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aleo-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/aleo-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/aleo-data-model.yml
created: '2026-07-17'
description: Aleo is a privacy-first, zero-knowledge Layer-1 blockchain for building fully private applications. Developers write smart contracts in Leo — a purpose-built language for zero-knowledge applications — compile them with snarkVM, and run them on the decentralized snarkOS network, keeping inputs, outputs, and program state private using zk-SNARK proofs while still being publicly verifiable. The ecosystem, developed by Provable (ProvableHQ), includes the Leo language and CLI, the snarkVM zkVM and snarkOS operating system, JavaScript/TypeScript and Python SDKs, a WASM runtime for in-browser proving, the Aleo Explorer, and a public node REST API for reading on-chain state and broadcasting transactions across mainnet and testnet. Aleo is a portfolio company of a16z.
image: https://aleo.org/social.webp
layout: provider
mcp_servers:
- description: ''
  name: aleo-mcp.yml
  slug: aleo-mcpyml
modified: '2026-07-17'
name: Aleo
nav: Providers
network: true
overview: 'Aleo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Blocks API, Chain API, Network API, and 2 more. Tagged areas include Company, Blockchain, Zero-Knowledge, Cryptography, and Privacy.


  Aleo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, sandbox, CLI, and 22 more developer resources.'
random_paper: 57
score:
  band: developing
  composite: 45.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 55.2
    developer_ergonomics: 75.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aleo/refs/heads/main/screenshots/aleo-2026-07-25T195557.png
security:
- kind: authentication
  name: Aleo Authentication
  slug: aleo-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Aleo Domain Security
  slug: aleo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: aleo
tags:
- Company
- Blockchain
- Zero-Knowledge
- Cryptography
- Privacy
- Web3
- Developer Tools
- Cryptocurrency
- Smart Contracts
website: https://docs.aleo.org/
---
