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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 37
  human_in_the_loop: 2
  name: Recall Labs Agentic Access
  operation_count: 87
  slug: recall-labs-agentic-access
  summary_line: 87 operations · 37 acting · 2 human-in-the-loop
api_count: 13
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
artifact_total: 17
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
  name: recall-labs-mcp.yml
  slug: recall-labs-mcpyml
modified: '2026-07-21'
name: Recall Labs
nav: Providers
network: true
overview: 'Recall Labs publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Agent API, Agents API, and 10 more. Tagged areas include Company, Infra Devtools, Artificial Intelligence, AI Agents, and Trading.


  Recall Labs'' developer surface includes documentation, API reference, engineering blog, changelog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 46
score:
  band: developing
  composite: 43.4
  delta: -0.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 57.1
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 43.9
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
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
