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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pyth Agentic Access
  operation_count: 23
  slug: pyth-agentic-access
  summary_line: 23 operations
api_count: 2
apis:
- baseURL: https://hermes.pyth.network
  baseurl_source: declared
  description: The Price Differences API from Pyth — 1 operation(s) for price differences.
  name: Pyth Price Differences API
  slug: pyth-price-differences-api
- baseURL: https://hermes.pyth.network
  baseurl_source: declared
  description: The Price Feeds API from Pyth — 2 operation(s) for price feeds.
  name: Pyth Price Feeds API
  slug: pyth-price-feeds-api
- baseURL: https://hermes.pyth.network
  baseurl_source: declared
  description: The rest API from Pyth — 11 operation(s) for rest.
  name: Pyth Rest API
  slug: pyth-rest-api
- baseURL: https://hermes.pyth.network
  baseurl_source: declared
  description: Routes for TradingView Data Integration.
  name: Pyth TradingView API
  slug: pyth-tradingview-api
- baseURL: https://hermes.pyth.network
  baseurl_source: declared
  description: The Updates API from Pyth — 2 operation(s) for updates.
  name: Pyth Updates API
  slug: pyth-updates-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Benchmarks Price Differences API
  slug: open-pyth-price-differences-api
- collection_type: open
  name: Benchmarks Price Differences Price Feeds API
  slug: open-pyth-price-feeds-api
- collection_type: open
  name: Benchmarks Price Differences rest API
  slug: open-pyth-rest-api
- collection_type: open
  name: Benchmarks Price Differences TradingView API
  slug: open-pyth-tradingview-api
- collection_type: open
  name: Benchmarks Price Differences Updates API
  slug: open-pyth-updates-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/overlays/pyth-benchmarks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pyth-benchmarks-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/changelog/pyth-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pyth-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/authentication/pyth-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pyth-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/packages/pyth-packages.yml
  title: ''
  type: Packages
  url: packages/pyth-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/packages/pyth-packages.yml
  title: ''
  type: SDKs
  url: packages/pyth-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/mcp/pyth-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pyth-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/llms/pyth-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pyth-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/lifecycle/pyth-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pyth-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/conventions/pyth-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pyth-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/sandbox/pyth-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pyth-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/errors/pyth-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pyth-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/conformance/pyth-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pyth-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/data-model/pyth-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pyth-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/agentic-access/pyth-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pyth-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/security/pyth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pyth-domain-security.yml
created: '2026-07-17'
description: Pyth Network is a first-party financial oracle delivering real-time market data — 500+ price feeds spanning crypto, equities, FX, metals, rates, and commodities — to 100+ blockchains. Its pull-based Pyth Core oracle lets applications fetch signed prices from the Hermes service and verify them on-chain in a single transaction with 400ms updates, while Pyth Pro (Lazer) offers enterprise low-latency WebSocket streaming. Additional products include Entropy for on-chain randomness and Express Relay for MEV protection. Pyth exposes public REST/SSE APIs (Hermes, Benchmarks), first-party SDKs across TypeScript, Rust, Python and Solidity, a hosted MCP server, and a published agent-integration skill. Surfaced as a portfolio company of Multicoin Capital.
image: https://pyth.network/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Pyth MCP Server
  slug: pyth-mcp-server
modified: '2026-07-20'
name: Pyth
nav: Providers
network: true
overview: 'Pyth publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Price Differences API, Price Feeds API, Rest API, and 2 more. Tagged areas include Company, Crypto Web3, Oracle, Price Feeds, and Market Data.


  Pyth''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, authentication, and 21 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 45.4
    developer_ergonomics: 73.8
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 20.0
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
    score: 23.1
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/pyth/refs/heads/main/screenshots/pyth-2026-08-17T081409.png
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
