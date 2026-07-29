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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Orca Agentic Access
  operation_count: 11
  slug: orca-agentic-access
  summary_line: 11 operations
api_count: 3
apis:
- description: Orca protocol information endpoints
  name: Orca protocol API
  slug: orca-protocol-api
- description: Token information endpoints
  name: Orca tokens API
  slug: orca-tokens-api
- description: Whirlpool information endpoints
  name: Orca whirlpools API
  slug: orca-whirlpools-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: Search Orca Whirlpools for a token pair, then fetch full state for the top-matching pool. Read-only; runs against the open Orca Public REST API.
  name: Find an Orca pool by token pair and read its stats
  slug: orca-find-pool
artifact_total: 9
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orca-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orca.so
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.orca.so/developers/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.orca.so
- group: docs
  title: ''
  type: APIReference
  url: https://docs.orca.so/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.orca.so/liquidity/getting-started/beginner-guide
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orca-so
- group: operate
  title: ''
  type: Support
  url: https://docs.orca.so/support/faqs
- group: auth
  title: ''
  type: Authentication
  url: authentication/orca-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/orca-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/orca-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orca-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orca-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orca-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orca-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orca-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orca-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/orca-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orca-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orca-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/orca-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/orca-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/orca-find-pool.yml
created: '2026-07-17'
description: Orca is the leading user-friendly concentrated-liquidity automated market maker (AMM) on Solana, built around Whirlpools. Liquidity providers concentrate capital within custom price ranges for higher capital efficiency, traders swap tokens with dynamic Adaptive Fees, and creators launch tokens and lock liquidity for launches. Developers and autonomous agents integrate via the open Whirlpools SDKs (TypeScript, Rust, and a Python option) and the read-only Orca Public REST API (api.orca.so) for pool, token, lock, and protocol-wide data.
image: https://mintcdn.com/orca-ccf67c1f/K618mEucxJ6w73gh/logo/orca-logo.png
layout: provider
mcp_servers:
- description: ''
  name: orca-mcp.yml
  slug: orca-mcpyml
modified: '2026-07-20'
name: Orca
nav: Providers
network: true
overview: 'Orca publishes 3 APIs on the [APIs.io](https://apis.io/) network: protocol API, tokens API, and whirlpools API. Tagged areas include Company, Defi Dex, DeFi, DEX, and Solana.


  Orca''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, changelog, and 18 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 40.7
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 49.7
    developer_ergonomics: 79.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Orca Authentication
  slug: orca-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Orca Domain Security
  slug: orca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: orca
tags:
- Company
- Defi Dex
- DeFi
- DEX
- Solana
- AMM
- Liquidity
- Concentrated Liquidity
- Blockchain
- Crypto
website: https://orca.so
---
