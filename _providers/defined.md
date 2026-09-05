---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Codex is Defined''s unified GraphQL API for real-time blockchain data: token prices, OHLCV bars, trades, liquidity pools, holders, wallet analytics, prediction markets and launchpad data across 100+ EV'
  name: Codex GraphQL API
  slug: codex-graphql-api
artifact_total: 5
asyncapis:
- description: ''
  name: Defined Webhooks
  slug: defined-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defined-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.codex.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codex.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.codex.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codex.io/get-started.md
- group: company
  title: ''
  type: Blog
  url: https://www.codex.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.codex.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.codex.io/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.codex.io/dashboard
- group: operate
  title: ''
  type: Support
  url: https://docs.codex.io/extra/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Codex-Data
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashboard.codex.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dashboard.codex.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codex.io/
- group: build
  title: ''
  type: SDKs
  url: packages/defined-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/defined-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/defined-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/defined-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/defined-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/defined-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/defined-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/defined-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/defined-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/defined-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/defined-webhooks.yml
created: '2026-07-17'
description: 'Defined (defined.fi) is a real-time, multi-chain crypto trading terminal and blockchain-data company backed by Version One Ventures. The consumer product is a customizable "Boards" trading workspace covering tokens, perps, predictions, launchpads and smart-money wallet tracking across every major network. Defined''s data is exposed to developers through Codex (codex.io), its industry-leading blockchain data API: a single GraphQL endpoint serving real-time token prices, OHLCV charts, trades, liquidity pools, holder balances, wallet analytics, launchpad activity and prediction-market data for 70M+ tokens across 100+ EVM and non-EVM networks, used by Coinbase, TradingView, Uniswap and Magic Eden.'
image: https://docs.codex.io/favicon.ico
layout: provider
mcp_servers:
- description: Codex (Defined's developer API) operates an official remote, hosted MCP server that lets AI coding tools search and reference the Codex GraphQL API documentation — queries, subscriptions, types and gu
  name: Defined MCP Server
  slug: defined-mcp-server
modified: '2026-07-18'
name: Defined
nav: Providers
network: true
overview: 'Defined publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Blockchain, DeFi, and Market Data.


  The Defined catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Defined''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 19 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 50.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defined/refs/heads/main/screenshots/defined-2026-07-25T211823.png
security:
- kind: authentication
  name: Defined Authentication
  slug: defined-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Defined Domain Security
  slug: defined-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: defined
tags:
- Company
- Cryptocurrency
- Blockchain
- DeFi
- Market Data
- Trading
- GraphQL
- Web3
- Prediction Markets
website: https://www.codex.io/
---
