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
  score: 41.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Parafi Agentic Access
  operation_count: 23
  slug: parafi-agentic-access
  summary_line: 23 operations
api_count: 4
apis:
- description: Avalanche validator and network supply endpoints.
  name: Parafi Avalanche API
  slug: parafi-avalanche-api
- description: Ethereum network and sidecar metrics.
  name: Parafi Ethereum API
  slug: parafi-ethereum-api
- description: Token price endpoints for supported assets.
  name: Parafi Market API
  slug: parafi-market-api
- description: ParaFi validator, rewards, stake, and Solana network endpoints.
  name: Parafi Solana API
  slug: parafi-solana-api
artifact_total: 8
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/parafi-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://parafi.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://parafi.tech/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://parafi.tech/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://parafi.tech/solana/integration-guide
- group: operate
  title: ''
  type: Support
  url: mailto:info@parafi.tech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://parafi.tech/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://parafi.tech/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/parafi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/parafi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/parafi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/parafi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/parafi-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/parafi-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/parafi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/parafi-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parafi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parafi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://parafi.com/
- group: company
  title: ''
  type: Blog
  url: https://parafi.com/library
created: '2026-07-17'
description: ParaFi is a blockchain and digital-asset investment firm (ParaFi Capital) whose technology division, ParaFi Tech (parafi.tech), operates staking validators across Solana, Ethereum, Avalanche, and Aptos and publishes a free, public, read-only REST API for on-chain staking and network data. The ParaFi Tech API (OpenAPI 3.0.3, 23 GET operations, no authentication) serves validator APY/APR and MEV contribution, Solana delegator rewards by staker/validator/epoch, active-stake and delegator breakdowns, real-time and historical network health (TPS, block time, compute units, leader slots), Ethereum and Avalanche network stats, and CoinGecko-backed token prices. It is explicitly designed for dashboards, AI agents, and programmatic integrations, shipping llms.txt, an extended llms-full.txt, and a skill.md agent guide alongside the OpenAPI.
image: https://parafi.tech/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: parafi-mcp.yml
  slug: parafi-mcpyml
modified: '2026-07-20'
name: Parafi
nav: Providers
network: true
overview: 'Parafi publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Avalanche API, Ethereum API, Market API, and 1 more. Tagged areas include Company, Fintech, Blockchain, Digital Assets, and Staking.


  Parafi''s developer surface includes documentation, API reference, getting-started guide, support, authentication, engineering blog, and 15 more developer resources.'
random_paper: 27
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 47.7
    developer_ergonomics: 60.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parafi/refs/heads/main/screenshots/parafi-2026-08-07T191404.png
security:
- kind: authentication
  name: Parafi Authentication
  slug: parafi-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Parafi Domain Security
  slug: parafi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: parafi
tags:
- Company
- Fintech
- Blockchain
- Digital Assets
- Staking
- Validators
- Solana
- Ethereum
- Avalanche
- DeFi
- Market Data
website: https://parafi.com/
---
