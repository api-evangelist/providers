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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: 'REST API for LunarCrush social and market intelligence. Endpoints cover trending topics, categories, creators, posts, coins, stocks, and NFTs, including summary snapshots, historical time series, top '
  name: LunarCrush API v4
  slug: lunarcrush-api-v4
- description: AI/agent-native interface to LunarCrush data at lunarcrush.ai. Exposes topics, categories, creators, posts, and search as clean machine-readable endpoints returning markdown by default (JSON with ?for
  name: LunarCrush.ai
  slug: lunarcrushai
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://lunarcrush.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lunarcrush.com/developers/api
- group: docs
  title: ''
  type: Documentation
  url: https://lunarcrush.com/developers/api/endpoints
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/lunarcrush/api
- group: auth
  title: ''
  type: Authentication
  url: authentication/lunarcrush-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lunarcrush-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/lunarcrush-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/lunarcrush-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lunarcrush-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lunarcrush-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lunarcrush-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lunarcrush-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lunarcrush-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunarcrush-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lunarcrush
- group: commercial
  title: ''
  type: Pricing
  url: https://lunarcrush.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://lunarcrush.com/signup
- group: company
  title: ''
  type: Blog
  url: https://lunarcrush.com/blog
- group: operate
  title: ''
  type: Support
  url: https://lunarcrush.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lunarcrush.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lunarcrush.com/privacy
created: '2026-07-17'
description: 'LunarCrush is a real-time social intelligence platform for crypto, stocks, and trending topics. It aggregates billions of public posts from X (Twitter), Reddit, YouTube, TikTok, Instagram, and News across 4,000+ assets, runs them through topic classification, spam/bot filtering, sentiment scoring, and creator weighting, and turns them into proprietary metrics such as Galaxy Score, AltRank, TopicRank, CreatorRank, Social Dominance, and Sentiment. LunarCrush exposes this data through two developer surfaces: the LunarCrush API v4 (a REST API at lunarcrush.com/api4 for topics, categories, creators, posts, coins, stocks, and NFTs) and lunarcrush.ai (an AI/agent-native interface returning markdown/JSON/CSV, with a hosted Model Context Protocol server and a first-party CLI). Both use Bearer-token API-key authentication.'
image: https://lunarcrush.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: LunarCrush MCP
  slug: lunarcrush-mcp
modified: '2026-07-20'
name: LunarCrush
nav: Providers
network: true
overview: 'LunarCrush publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Intelligence, Cryptocurrency, Stocks, and Sentiment Analysis.


  LunarCrush''s developer surface includes documentation, API reference, authentication, CLI, pricing, signup flow, engineering blog, and 15 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 29.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lunarcrush/refs/heads/main/screenshots/lunarcrush-2026-07-25T225725.png
security:
- kind: authentication
  name: Lunarcrush Authentication
  slug: lunarcrush-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lunarcrush Domain Security
  slug: lunarcrush-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lunarcrush
tags:
- Company
- Social Intelligence
- Cryptocurrency
- Stocks
- Sentiment Analysis
- Social-Media
- Market Data
- Analytics
- AI Agents
- MCP
website: https://lunarcrush.com/
---
