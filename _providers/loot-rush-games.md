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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Connect API from Loot Rush Games — 1 operation(s) for connect.
  name: Loot Rush Games Connect API
  slug: loot-rush-games-connect-api
- description: The History API from Loot Rush Games — 1 operation(s) for history.
  name: Loot Rush Games History API
  slug: loot-rush-games-history-api
- description: The MCP API from Loot Rush Games — 1 operation(s) for mcp.
  name: Loot Rush Games MCP API
  slug: loot-rush-games-mcp-api
- description: The Withdrawals API from Loot Rush Games — 2 operation(s) for withdrawals.
  name: Loot Rush Games Withdrawals API
  slug: loot-rush-games-withdrawals-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LootRush Partner Connect API
  slug: open-loot-rush-games-connect-api
- collection_type: open
  name: LootRush Partner Connect History API
  slug: open-loot-rush-games-history-api
- collection_type: open
  name: LootRush Partner Connect MCP API
  slug: open-loot-rush-games-mcp-api
- collection_type: open
  name: LootRush Partner Connect Withdrawals API
  slug: open-loot-rush-games-withdrawals-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/loot-rush-games-partner-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lootrush.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lootrush.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lootrush.com/api-reference/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lootrush.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loot-rush-games-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loot-rush-games-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loot-rush-games-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loot-rush-games-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loot-rush-games-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loot-rush-games-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loot-rush-games-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lootrush.com/
- group: design
  title: ''
  type: DataModel
  url: data-model/loot-rush-games-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loot-rush-games-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@lootrush.com
- group: company
  title: ''
  type: Website
  url: https://www.lootrush.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smelthq
created: '2026-07-17'
description: LootRush (Loot Rush Games) is a San Francisco company, backed by a16z, Paradigm and Y Combinator, that operates a crypto-native "global operating account" — wallets, cards, cryptocurrency withdrawals and transaction history for gamers and marketplaces. It began as a Steam-like platform for blockchain games with NFT rentals and has grown into a consumer crypto account and card product. For developers, LootRush publishes a Partner API (OpenAPI 3.1) exposing Withdraw, History and Connect (OAuth-style, consent-based user data) APIs, plus an official hosted, read-only Model Context Protocol (MCP) server that gives AI assistants scoped access to a user's own balances, cards, card transactions and account history.
layout: provider
mcp_servers:
- description: ''
  name: Loot Rush Games MCP Server
  slug: loot-rush-games-mcp-server
modified: '2026-07-20'
name: Loot Rush Games
nav: Providers
network: true
overview: 'Loot Rush Games publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connect API, History API, MCP API, and 1 more. Tagged areas include Company, Cryptocurrency, Blockchain, Gaming, and Fintech.


  Loot Rush Games'' developer surface includes documentation, API reference, getting-started guide, authentication, support, and 14 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 56.1
    developer_ergonomics: 56.5
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 33.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loot-rush-games/refs/heads/main/screenshots/loot-rush-games-2026-07-25T225531.png
security:
- kind: authentication
  name: Loot Rush Games Authentication
  slug: loot-rush-games-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Loot Rush Games Domain Security
  slug: loot-rush-games-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loot-rush-games
tags:
- Company
- Cryptocurrency
- Blockchain
- Gaming
- Fintech
- Wallets
- Cards
- Payments
- Withdrawals
- MCP
- Agent Ready
website: https://www.lootrush.com/
---
