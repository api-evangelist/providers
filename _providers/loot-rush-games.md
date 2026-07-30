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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-07-28'
api_count: 4
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
artifact_total: 7
common:
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
image: https://www.lootrush.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: loot-rush-games-mcp.yml
  slug: loot-rush-games-mcpyml
modified: '2026-07-20'
name: Loot Rush Games
nav: Providers
network: true
overview: 'Loot Rush Games publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Connect API, History API, MCP API, and 1 more. Tagged areas include Company, Cryptocurrency, Blockchain, Gaming, and Fintech.


  Loot Rush Games'' developer surface includes documentation, API reference, getting-started guide, authentication, support, and 13 more developer resources.'
random_paper: 35
score:
  band: thin
  composite: 37.6
  delta: -2.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 60.6
    developer_ergonomics: 60.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 40.1
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Agent-Ready
website: https://www.lootrush.com/
---
