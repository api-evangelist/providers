---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: The Analytics API from Sequence — 177 operation(s) for analytics.
  name: Sequence Analytics API
  slug: sequence-analytics-api
- description: The Marketplace API from Sequence — 34 operation(s) for marketplace.
  name: Sequence Marketplace API
  slug: sequence-marketplace-api
- description: Endpoints accessible by passing your project-access-key in the header. This is injected whenever you login automatically.
  name: Sequence public API
  slug: sequence-public-api
- description: The Rpc API from Sequence — 32 operation(s) for rpc.
  name: Sequence Rpc API
  slug: sequence-rpc-api
- description: Endpoints that require a Sequence service token intended to be secret. You can manually generate one on Sequence Builder and pass it as a Bearer Token.
  name: Sequence secret API
  slug: sequence-secret-api
artifact_total: 9
asyncapis:
- description: ''
  name: Sequence Indexer Webhooks
  slug: sequence-indexer-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://sequence.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sequence.build
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sequence.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sequence.xyz/api-references/overview
- group: start
  title: ''
  type: SignUp
  url: https://sequence.build
- group: operate
  title: ''
  type: Support
  url: https://support.sequence.xyz/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.sequence.xyz/en/
- group: company
  title: ''
  type: Blog
  url: https://sequence.xyz/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xsequence
- group: commercial
  title: ''
  type: Pricing
  url: https://sequence.xyz/pricing
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/sequence-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sequence-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/sequence-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sequence-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sequence-cli.yml
- group: design
  title: ''
  type: Components
  url: components/sequence-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sequence-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sequence-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sequence-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sequence-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sequence-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sequence-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sequence-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sequence-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sequence-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sequence-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sequence-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sequence-indexer-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Sequence is a web3 developer platform (0xsequence, now part of Polygon Labs) for building blockchain applications: smart-contract wallets, a universal crypto payments and swap layer, a real-time multi-chain Indexer with balances, token prices, contract events and webhooks, plus Metadata, Marketplace, Transactions (Relayer) and Analytics APIs. Its backend APIs are webrpc-generated (POST /rpc/{Service}/{Method}) authenticated with a project access key and secret JWT, and it ships first-party SDKs for TypeScript, Go, Unity, Unreal, Kotlin and Swift plus a CLI. Backed by a16z and Polychain.'
image: https://sequence.xyz/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: sequence-mcp.yml
  slug: sequence-mcpyml
modified: '2026-07-21'
name: Sequence
nav: Providers
network: true
overview: 'Sequence publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Marketplace API, public API, and 2 more. Tagged areas include Company, Web3, Blockchain, Wallets, and Payments.


  The Sequence catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sequence''s developer surface includes documentation, API reference, signup flow, support, engineering blog, pricing, changelog, and 22 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 58.7
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 45.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Sequence Authentication
  slug: sequence-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sequence Domain Security
  slug: sequence-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sequence
tags:
- Company
- Web3
- Blockchain
- Wallets
- Payments
- Crypto
- Indexer
- NFT
- Developer Platform
- Gaming
website: https://sequence.xyz
---
