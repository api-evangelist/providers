---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Codex is Defined''s unified GraphQL API for real-time blockchain data: token prices, OHLCV bars, trades, liquidity pools, holders, wallet analytics, prediction markets and launchpad data across 100+ EV'
  name: Codex GraphQL API
  slug: codex-graphql-api
artifact_total: 8
asyncapis:
- description: ''
  name: Defined Webhooks
  slug: defined-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/defined/plans/defined-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/defined-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.codex.io/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://www.codex.io/
- group: auth
  href: https://artifacts.apis.io/defined/security/defined-domain-security.yml
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
  href: https://artifacts.apis.io/defined/packages/defined-packages.yml
  title: ''
  type: SDKs
  url: packages/defined-packages.yml
- group: build
  href: https://artifacts.apis.io/defined/packages/defined-packages.yml
  title: ''
  type: Packages
  url: packages/defined-packages.yml
- group: agent
  href: https://artifacts.apis.io/defined/mcp/defined-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/defined-mcp.yml
- group: agent
  href: https://artifacts.apis.io/defined/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/defined/llms/defined-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defined-llms.txt
- group: auth
  href: https://artifacts.apis.io/defined/authentication/defined-authentication.yml
  title: ''
  type: Authentication
  url: authentication/defined-authentication.yml
- group: design
  href: https://artifacts.apis.io/defined/conventions/defined-conventions.yml
  title: ''
  type: Conventions
  url: conventions/defined-conventions.yml
- group: operate
  href: https://artifacts.apis.io/defined/changelog/defined-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/defined-changelog.yml
- group: design
  href: https://artifacts.apis.io/defined/lifecycle/defined-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/defined-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/defined/lifecycle/defined-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/defined-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/defined/conformance/defined-conformance.yml
  title: ''
  type: Conformance
  url: conformance/defined-conformance.yml
- group: design
  href: https://artifacts.apis.io/defined/asyncapi/defined-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/defined-webhooks.yml
created: '2026-07-17'
description: 'Defined (defined.fi) is a real-time, multi-chain crypto trading terminal and blockchain-data company backed by Version One Ventures. The consumer product is a customizable "Boards" trading workspace covering tokens, perps, predictions, launchpads and smart-money wallet tracking across every major network. Defined''s data is exposed to developers through Codex (codex.io), its industry-leading blockchain data API: a single GraphQL endpoint serving real-time token prices, OHLCV charts, trades, liquidity pools, holder balances, wallet analytics, launchpad activity and prediction-market data for 70M+ tokens across 100+ EVM and non-EVM networks, used by Coinbase, TradingView, Uniswap and Magic Eden.'
finops:
- has_sources: true
  method: derived
  name: Defined Finops
  primary_unit: compute units
  service_category: ''
  slug: defined-finops
  template: false
image: https://docs.codex.io/favicon.ico
layout: provider
mcp_servers:
- description: Codex (Defined's developer API) operates an official remote, hosted MCP server that lets AI coding tools search and reference the Codex GraphQL API documentation — queries, subscriptions, types and gu
  name: Defined MCP Server
  slug: codex-docs
modified: '2026-10-06'
name: Defined
nav: Providers
network: true
overview: 'Defined is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Blockchain, DeFi, and Market Data.


  The Defined catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Defined''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 22 more developer resources.'
plans:
- name: Defined Plans Pricing
  plan_count: 3
  slug: defined-plans-pricing
random_paper: 23
score:
  band: strong
  composite: 57.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 71.4
    discoverability: 71.7
    operational_transparency: 50.0
  previous_composite: 57.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/defined/defined-2026-07-25T211823.png
security:
- kind: authentication
  name: Defined Authentication
  slug: defined-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Defined Domain Security
  slug: defined-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Codex API (blockchain data) skill
  slug: defined-codex-skill
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
