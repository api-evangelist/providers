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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Babylon Labs Agentic Access
  operation_count: 19
  slug: babylon-labs-agentic-access
  summary_line: 19 operations · 1 acting
api_count: 3
apis:
- description: Shared API endpoints
  name: Babylon Labs shared API
  slug: babylon-labs-shared-api
- description: Babylon Phase-1 API endpoints (Deprecated)
  name: Babylon Labs v1 API
  slug: babylon-labs-v1-api
- description: Babylon Phase-2 API endpoints
  name: Babylon Labs v2 API
  slug: babylon-labs-v2-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/babylon-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/babylon-labs-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/babylon-labs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/babylon-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/babylon-labs-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/babylon-labs-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/babylon-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/babylon-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/babylon-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/babylon-labs-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/babylon-labs-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/babylon-labs-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/babylon-labs-staking-api-overlay.yaml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/babylon-labs-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.babylonlabs.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.babylonlabs.io/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.babylonlabs.io/stakers/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/babylonlabs-io
- group: company
  title: ''
  type: Blog
  url: https://babylonlabs.io/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/babylonglobal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://babylonlabs.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://babylonlabs.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://babylonlabs.io
created: '2026-07-17'
description: Babylon Labs builds the Bitcoin staking protocol that lets BTC holders secure Proof-of-Stake networks without custody, bridges, or wrapping. BTC is locked in time-locked covenant scripts on Bitcoin L1 and delegated to finality providers, providing Bitcoin-grade economic security to Cosmos chains, rollups, and other Bitcoin Supercharged Networks (BSNs) while stakers retain self-custody. Its mainnet, Babylon Genesis, launched April 2025 on CometBFT with CosmWasm smart contracts and the BABY native token. Babylon exposes a public Babylon Staking API for querying delegations, finality providers, network parameters, stats, prices, and APR, plus Go and TypeScript SDKs, node/operator daemons, and CosmWasm contracts.
image: https://avatars.githubusercontent.com/u/175623330?v=4
layout: provider
mcp_servers:
- description: ''
  name: babylon-labs-mcp.yml
  slug: babylon-labs-mcpyml
modified: '2026-07-18'
name: Babylon Labs
nav: Providers
network: true
overview: 'Babylon Labs publishes 3 APIs on the [APIs.io](https://apis.io/) network: shared API, v1 API, and v2 API. Tagged areas include Company, Crypto Defi, Bitcoin, Bitcoin Staking, and Blockchain.


  Babylon Labs'' developer surface includes changelog, documentation, getting-started guide, engineering blog, support, and 19 more developer resources.'
random_paper: 33
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 37.7
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 38.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Babylon Labs Domain Security
  slug: babylon-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: babylon-labs
tags:
- Company
- Crypto Defi
- Bitcoin
- Bitcoin Staking
- Blockchain
- Cosmos
- Proof of Stake
- DeFi
- Staking
- API
website: https://babylonlabs.io
---
