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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Superform Agentic Access
  operation_count: 66
  slug: superform-agentic-access
  summary_line: 66 operations · 8 acting
api_count: 15
apis:
- description: The Auxiliary API from Superform — 8 operation(s) for auxiliary.
  name: Superform Auxiliary API
  slug: superform-auxiliary-api
- description: The Balances API from Superform — 2 operation(s) for balances.
  name: Superform Balances API
  slug: superform-balances-api
- description: The Contract Checker API from Superform — 1 operation(s) for contract checker.
  name: Superform Contract Checker API
  slug: superform-contract-checker-api
- description: The Data API from Superform — 1 operation(s) for data.
  name: Superform Data API
  slug: superform-data-api
- description: The Execution API from Superform — 6 operation(s) for execution.
  name: Superform Execution API
  slug: superform-execution-api
- description: The Explorer API from Superform — 5 operation(s) for explorer.
  name: Superform Explorer API
  slug: superform-explorer-api
- description: The Health API from Superform — 8 operation(s) for health.
  name: Superform Health API
  slug: superform-health-api
- description: The Migrate API from Superform — 2 operation(s) for migrate.
  name: Superform Migrate API
  slug: superform-migrate-api
- description: The Protocol API from Superform — 3 operation(s) for protocol.
  name: Superform Protocol API
  slug: superform-protocol-api
- description: The Protocol Rewards API from Superform — 5 operation(s) for protocol rewards.
  name: Superform Protocol Rewards API
  slug: superform-protocol-rewards-api
- description: The Simulator API from Superform — 1 operation(s) for simulator.
  name: Superform Simulator API
  slug: superform-simulator-api
- description: The Stats API from Superform — 2 operation(s) for stats.
  name: Superform Stats API
  slug: superform-stats-api
- description: The SuperRewardsAPI API from Superform — 13 operation(s) for superrewardsapi.
  name: Superform SuperRewardsAPI API
  slug: superform-superrewardsapi-api
- description: The Token Distribution API from Superform — 6 operation(s) for token distribution.
  name: Superform Token Distribution API
  slug: superform-token-distribution-api
- description: The Vault API from Superform — 3 operation(s) for vault.
  name: Superform Vault API
  slug: superform-vault-api
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://superform.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.superform.xyz/build
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superform.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.superform.xyz/operate/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.superform.xyz/operate/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.superform.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superform-xyz
- group: company
  title: ''
  type: Blog
  url: https://mirror.xyz/superform.eth
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superform-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superform-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superform-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superform-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superform-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superform-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/superform-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/superform-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superform-domain-security.yml
created: '2026-07-17'
description: Superform is a user-owned onchain neobank and the operating system for programmable DeFi vaults. The protocol enables single-signature execution of arbitrary actions across chains and optimized yield vaults, built on ERC-4626 / ERC-7540 tokenized vaults and ERC-7579 smart accounts. Its public API (api.superform.xyz) exposes vault and protocol data, cross-chain deposit/withdraw/rebalance transaction routing, user portfolios and balances, superpositions, and protocol rewards. A separate SuperformOS "operate" API (Erebor, Strategy Engine, and OMS) lets vault managers create, configure, and automate SuperVaults. Originally added as a Polychain portfolio lead, this profile has been enriched from Superform's real developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superform.png
layout: provider
mcp_servers:
- description: ''
  name: superform-mcp.yml
  slug: superform-mcpyml
modified: '2026-07-21'
name: Superform
nav: Providers
network: true
overview: 'Superform publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Auxiliary API, Balances API, Contract Checker API, and 12 more. Tagged areas include Company, Defi Yield, DeFi, Vaults, and Yield Aggregation.


  Superform''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 12 more developer resources.'
random_paper: 67
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 60.3
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Superform Authentication
  slug: superform-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Superform Domain Security
  slug: superform-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: superform
tags:
- Company
- Defi Yield
- DeFi
- Vaults
- Yield Aggregation
- Cross Chain
- Onchain
- Blockchain
- Smart Accounts
website: https://superform.xyz
---
