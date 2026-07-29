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
    agent_skills: true
    agentic_access: derived
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
  score: 56.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pyth Agentic Access
  operation_count: 23
  slug: pyth-agentic-access
  summary_line: 23 operations
api_count: 5
apis:
- description: The Price Differences API from Pyth — 1 operation(s) for price differences.
  name: Pyth Price Differences API
  slug: pyth-price-differences-api
- description: The Price Feeds API from Pyth — 2 operation(s) for price feeds.
  name: Pyth Price Feeds API
  slug: pyth-price-feeds-api
- description: The rest API from Pyth — 11 operation(s) for rest.
  name: Pyth rest API
  slug: pyth-rest-api
- description: Routes for TradingView Data Integration.
  name: Pyth TradingView API
  slug: pyth-tradingview-api
- description: The Updates API from Pyth — 2 operation(s) for updates.
  name: Pyth Updates API
  slug: pyth-updates-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://pyth.network
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pyth.network/home
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pyth.network
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pyth.network/price-feeds/core/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pyth.network/price-feeds/core/getting-started
- group: company
  title: ''
  type: Blog
  url: https://pyth.network/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pyth-network
- group: start
  title: ''
  type: SignUp
  url: https://pythdata.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pyth.network/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pyth.network/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pyth.network
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.pyth.network/price-feeds/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pyth-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pyth-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/pyth-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pyth-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pyth-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pyth-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pyth-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pyth-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pyth-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pyth-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pyth-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pyth-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pyth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pyth-domain-security.yml
created: '2026-07-17'
description: Pyth Network is a first-party financial oracle delivering real-time market data — 500+ price feeds spanning crypto, equities, FX, metals, rates, and commodities — to 100+ blockchains. Its pull-based Pyth Core oracle lets applications fetch signed prices from the Hermes service and verify them on-chain in a single transaction with 400ms updates, while Pyth Pro (Lazer) offers enterprise low-latency WebSocket streaming. Additional products include Entropy for on-chain randomness and Express Relay for MEV protection. Pyth exposes public REST/SSE APIs (Hermes, Benchmarks), first-party SDKs across TypeScript, Rust, Python and Solidity, a hosted MCP server, and a published agent-integration skill. Surfaced as a portfolio company of Multicoin Capital.
image: https://pyth.network/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: pyth-mcp.yml
  slug: pyth-mcpyml
modified: '2026-07-20'
name: Pyth
nav: Providers
network: true
overview: 'Pyth publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Price Differences API, Price Feeds API, rest API, and 2 more. Tagged areas include Company, Crypto Web3, Oracle, Price Feeds, and Market Data.


  Pyth''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, authentication, and 20 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 49.1
  delta: -1.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 47.6
    developer_ergonomics: 76.1
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Pyth Authentication
  slug: pyth-authentication
  summary_line: none/http · 3 schemes
- kind: domain-security
  name: Pyth Domain Security
  slug: pyth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pyth
tags:
- Company
- Crypto Web3
- Oracle
- Price Feeds
- Market Data
- DeFi
- Blockchain
- Financial Data
website: https://pyth.network
---
