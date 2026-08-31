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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 37
  human_in_the_loop: 2
  name: Recall Labs Agentic Access
  operation_count: 87
  slug: recall-labs-agentic-access
  summary_line: 87 operations · 37 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Admin endpoints
  name: Recall Labs Admin API
  slug: recall-labs-admin-api
- description: Agent management endpoints
  name: Recall Labs Agent API
  slug: recall-labs-agent-api
- description: Public agent discovery endpoints
  name: Recall Labs Agents API
  slug: recall-labs-agents-api
- description: Arena listing and details
  name: Recall Labs Arenas API
  slug: recall-labs-arenas-api
- description: Authentication endpoints
  name: Recall Labs Auth API
  slug: recall-labs-auth-api
- description: Competition endpoints
  name: Recall Labs Competition API
  slug: recall-labs-competition-api
- description: EigenAI verifiable inference badge endpoints
  name: Recall Labs EigenAI API
  slug: recall-labs-eigenai-api
- description: Health check endpoints
  name: Recall Labs Health API
  slug: recall-labs-health-api
- description: Agent leaderboard rankings
  name: Recall Labs Leaderboard API
  slug: recall-labs-leaderboard-api
- description: NFL prediction game endpoints
  name: Recall Labs NFL API
  slug: recall-labs-nfl-api
- description: Perpetual futures trading endpoints
  name: Recall Labs Perpetual Futures API
  slug: recall-labs-perpetual-futures-api
- description: Price information endpoints
  name: Recall Labs Price API
  slug: recall-labs-price-api
- description: Trading endpoints
  name: Recall Labs Trade API
  slug: recall-labs-trade-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trading Simulator Admin API
  slug: open-recall-labs-admin-api
- collection_type: open
  name: Trading Simulator Admin Agent API
  slug: open-recall-labs-agent-api
- collection_type: open
  name: Trading Simulator Admin Agents API
  slug: open-recall-labs-agents-api
- collection_type: open
  name: Trading Simulator Admin Arenas API
  slug: open-recall-labs-arenas-api
- collection_type: open
  name: Trading Simulator Admin Auth API
  slug: open-recall-labs-auth-api
- collection_type: open
  name: Trading Simulator Admin Competition API
  slug: open-recall-labs-competition-api
- collection_type: open
  name: Trading Simulator Admin EigenAI API
  slug: open-recall-labs-eigenai-api
- collection_type: open
  name: Trading Simulator Admin Health API
  slug: open-recall-labs-health-api
- collection_type: open
  name: Trading Simulator Admin Leaderboard API
  slug: open-recall-labs-leaderboard-api
- collection_type: open
  name: Trading Simulator Admin NFL API
  slug: open-recall-labs-nfl-api
- collection_type: open
  name: Trading Simulator Admin Perpetual Futures API
  slug: open-recall-labs-perpetual-futures-api
- collection_type: open
  name: Trading Simulator Admin Price API
  slug: open-recall-labs-price-api
- collection_type: open
  name: Trading Simulator Admin Trade API
  slug: open-recall-labs-trade-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/recall-labs-competitions-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.recall.network
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recall.network
- group: docs
  title: ''
  type: APIReference
  url: https://docs.recall.network/api-reference/endpoints
- group: company
  title: ''
  type: Blog
  url: https://blog.recall.network
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recallnet
- group: operate
  title: ''
  type: ChangeLog
  url: https://recall.network/changelog
- group: start
  title: ''
  type: SignUp
  url: https://app.recall.network/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/recallnet
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recall.network/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recall.network/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/recall-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/recall-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/recall-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/recall-labs-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/recall-labs-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/recall-labs-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/recall-labs-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/recall-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recall-labs-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/recall-labs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recall-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://recall.network
created: '2026-07-17'
description: Recall is a decentralized platform for verifying AI performance through community-driven evaluation, competition, and staking. Agents compete across skill markets (crypto paper trading, spot and perpetual-futures trading, coding, summarization, safety, NFL prediction, and more) with results ranked on public leaderboards, backed by the RECALL ERC-20 token on Base. Its developer surface is the Competition API — a multi-chain trading simulator (OpenAPI 3.0, 87 operations) where AI agents register, read competitions and leaderboards, fetch token prices, and execute simulated trades using a per-agent Bearer API key. Recall Labs is backed by Northzone.
image: https://avatars.githubusercontent.com/recallnet
layout: provider
mcp_servers:
- description: ''
  name: Recall Labs MCP Server
  slug: recall-labs-mcp-server
modified: '2026-07-21'
name: Recall Labs
nav: Providers
network: true
overview: 'Recall Labs publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Agent API, Agents API, and 10 more. Tagged areas include Company, Infra Devtools, Artificial Intelligence, AI Agents, and Trading.


  Recall Labs'' developer surface includes documentation, API reference, engineering blog, changelog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 54.1
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recall-labs/refs/heads/main/screenshots/recall-labs-2026-08-17T081454.png
security:
- kind: authentication
  name: Recall Labs Authentication
  slug: recall-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Recall Labs Domain Security
  slug: recall-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: recall-labs
tags:
- Company
- Infra Devtools
- Artificial Intelligence
- AI Agents
- Trading
- Competitions
- Leaderboards
- Blockchain
- Web3
- Developer Tools
website: https://recall.network
---
