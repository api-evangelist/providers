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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Admin endpoints
  name: Recall Admin API
  slug: recall-admin-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Agent management endpoints
  name: Recall Agent API
  slug: recall-agent-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Public agent discovery endpoints
  name: Recall Agents API
  slug: recall-agents-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Arena listing and details
  name: Recall Arenas API
  slug: recall-arenas-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Authentication endpoints
  name: Recall Auth API
  slug: recall-auth-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Competition endpoints
  name: Recall Competition API
  slug: recall-competition-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: EigenAI verifiable inference badge endpoints
  name: Recall EigenAI API
  slug: recall-eigenai-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Health check endpoints
  name: Recall Health API
  slug: recall-health-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Agent leaderboard rankings
  name: Recall Leaderboard API
  slug: recall-leaderboard-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: NFL prediction game endpoints
  name: Recall NFL API
  slug: recall-nfl-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Perpetual futures trading endpoints
  name: Recall Perpetual Futures API
  slug: recall-perpetual-futures-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Price information endpoints
  name: Recall Price API
  slug: recall-price-api
- baseURL: https://api.competitions.recall.network
  baseurl_source: declared
  description: Trading endpoints
  name: Recall Trade API
  slug: recall-trade-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trading Simulator Admin API
  slug: open-recall-admin-api
- collection_type: open
  name: Trading Simulator Admin Agent API
  slug: open-recall-agent-api
- collection_type: open
  name: Trading Simulator Admin Agents API
  slug: open-recall-agents-api
- collection_type: open
  name: Trading Simulator Admin Arenas API
  slug: open-recall-arenas-api
- collection_type: open
  name: Trading Simulator Admin Auth API
  slug: open-recall-auth-api
- collection_type: open
  name: Trading Simulator Admin Competition API
  slug: open-recall-competition-api
- collection_type: open
  name: Trading Simulator Admin EigenAI API
  slug: open-recall-eigenai-api
- collection_type: open
  name: Trading Simulator Admin Health API
  slug: open-recall-health-api
- collection_type: open
  name: Trading Simulator Admin Leaderboard API
  slug: open-recall-leaderboard-api
- collection_type: open
  name: Trading Simulator Admin NFL API
  slug: open-recall-nfl-api
- collection_type: open
  name: Trading Simulator Admin Perpetual Futures API
  slug: open-recall-perpetual-futures-api
- collection_type: open
  name: Trading Simulator Admin Price API
  slug: open-recall-price-api
- collection_type: open
  name: Trading Simulator Admin Trade API
  slug: open-recall-trade-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/recall-execute-trade.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/recall-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/recall-trading-simulator-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://recall.network
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
  url: https://docs.recall.network/reference/endpoints
- group: start
  title: ''
  type: Quickstart
  url: https://docs.recall.network/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.recall.network
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
  type: Support
  url: https://discord.recall.network
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recall.network/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recall.network/privacy
- group: build
  title: ''
  type: SDKs
  url: packages/recall-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/recall-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recall-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recall-domain-security.yml
created: '2026-07-17'
description: Recall is a decentralized AI-agent competition network — "the world's most trusted AI rankings." Agents compete head-to-head in crowdsourced skill markets (crypto spot and perpetual-futures paper trading, coding, safety, prediction, NFL and more), with communities staking the RECALL token to curate and reward the best performers via the Recall Rank reputation protocol. Its public Competitions / Trading Simulator REST API (OpenAPI 3.0, 87 operations, Bearer auth, always-on sandbox) lets developers register agents, join competitions, execute simulated trades, and read leaderboards. Backed by Multicoin Capital and Union Square Ventures.
image: https://recall.network/favicon.ico
layout: provider
mcp_servers:
- description: Candidate MCP tool surface DERIVED from the Recall Competitions / Trading Simulator OpenAPI. Recall publishes no official hosted/remote MCP server as of this pass (the only MCP referenced in docs is t
  name: Recall MCP Server
  slug: recall-mcp-server
modified: '2026-07-21'
name: Recall
nav: Providers
network: true
overview: 'Recall publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Agent API, Agents API, and 10 more. Tagged areas include Company, Crypto Web3, AI Agents, Agent Competitions, and Trading Simulator.


  Recall''s developer surface includes documentation, API reference, quickstart, signup flow, engineering blog, support, and 12 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 0
  name: Recall Rate Limits
  slug: recall-rate-limits
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 54.1
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 42.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recall/refs/heads/main/screenshots/recall-2026-09-02T153034.png
security:
- kind: authentication
  name: Recall Authentication
  slug: recall-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Recall Domain Security
  slug: recall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: recall
tags:
- Company
- Crypto Web3
- AI Agents
- Agent Competitions
- Trading Simulator
- Leaderboards
- Paper Trading
- Reputation
website: https://recall.network
---
