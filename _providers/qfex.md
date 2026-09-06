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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: wss://mds.qfex.com
  baseurl_source: declared
  description: 'Multiplexed WebSocket gateway for all QFEX real-time market data streams: order book, trades, candles, BBO, mark price, funding rate, open interest, market stats and reference data. Documented as Asyn'
  name: QFEX Market Data WebSocket (MDS)
  slug: qfex-market-data-websocket-mds
- baseURL: wss://trade.qfex.com
  baseurl_source: declared
  description: 'Multiplexed WebSocket gateway for QFEX order entry and account streams: add / modify / cancel orders, stop orders, TWAPs, close position, leverage, balances, positions, fills and order responses. Requ'
  name: QFEX Trade WebSocket
  slug: qfex-trade-websocket
- baseURL: https://api.qfex.com
  baseurl_source: declared
  description: The market-data API from Qfex — 9 operation(s) for market-data.
  name: Qfex market-data API
  slug: qfex-market-data-api
- baseURL: https://api.qfex.com
  baseurl_source: declared
  description: The pnl API from Qfex — 1 operation(s) for pnl.
  name: Qfex pnl API
  slug: qfex-pnl-api
- baseURL: https://api.qfex.com
  baseurl_source: declared
  description: The user API from Qfex — 15 operation(s) for user.
  name: Qfex user API
  slug: qfex-user-api
artifact_total: 15
asyncapis:
- description: Single WebSocket gateway for all QFEX real‑time streams. Clients publish subscription and order commands here, and receive all updates over the same endpoint.
  name: QFEX Multiplexed WebSocket API
  slug: qfex-combined-asyncapi
- description: Single WebSocket gateway for all QFEX real‑time streams. Clients publish subscription and order commands here, and receive all updates over the same endpoint.
  name: QFEX Multiplexed WebSocket API
  slug: qfex-mds-asyncapi
- description: Single WebSocket gateway for all QFEX real‑time streams. Clients publish subscription and order commands here, and receive all updates over the same endpoint.
  name: QFEX Multiplexed WebSocket API
  slug: qfex-trade-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: QFEX REST market-data API
  slug: open-qfex-market-data-api
- collection_type: open
  name: QFEX REST market-data pnl API
  slug: open-qfex-pnl-api
- collection_type: open
  name: QFEX REST market-data user API
  slug: open-qfex-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/qfex-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qfex-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qfex.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qfex.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qfex.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qfex.com/api-reference/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/qfex-authentication.yml
- group: build
  title: ''
  type: CLI
  url: cli/qfex-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/qfex-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qfex-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qfex-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/qfex-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.qfex.com/websocket/rate
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qfex-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qfex-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qfex.com
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/qfex-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qfex-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/qfex-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qfex-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qfex-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qfex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.qfex.com/legal/bug-bounty
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QFEX-org
- group: company
  title: ''
  type: Blog
  url: https://blog.qfex.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@qfex.com
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.qfex.com/qfex/fees
- group: start
  title: ''
  type: SignUp
  url: https://www.qfex.com/signup
- group: start
  title: ''
  type: Login
  url: https://www.qfex.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.qfex.com/legal/client-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.qfex.com/legal/privacy-policy
created: '2026-07-17'
description: QFEX is the first 24/7 exchange built exclusively for US equities, commodities, and FX, offering high-leverage perpetual futures on traditional assets without a broker. Founded by former Tower Research and Citadel engineers who met studying mathematics at Cambridge, QFEX gives retail and institutional traders direct, high-frequency access to markets around the clock. Its developer platform exposes a REST API for historic market data and account operations, two multiplexed WebSocket gateways (market data and trading) documented with AsyncAPI 3.0, and a JSON-native CLI purpose-built for agentic trading workflows. Authentication uses HMAC-SHA256 request signing with public/secret API key pairs.
image: https://qfex.com/qfex-logo-with-text-for-metadata.png
layout: provider
modified: '2026-07-20'
name: Qfex
nav: Providers
network: true
overview: 'Qfex publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Market Data WebSocket (MDS), Trade WebSocket, market-data API, and 2 more. Tagged areas include Company, Trading, Exchange, Perpetual Futures, and Market Data.


  The Qfex catalog on APIs.io includes 3 event-driven AsyncAPI specifications.


  Qfex''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, sandbox, changelog, and 25 more developer resources.'
random_paper: 16
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 58.7
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 44.7
  previous_composite: 53.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qfex/refs/heads/main/screenshots/qfex-2026-08-17T081412.png
security:
- kind: authentication
  name: Qfex Authentication
  slug: qfex-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Qfex Domain Security
  slug: qfex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Qfex Vulnerability Disclosure
  slug: qfex-vulnerability-disclosure
  summary_line: contact published
slug: qfex
tags:
- Company
- Trading
- Exchange
- Perpetual Futures
- Market Data
- WebSocket
- FX
- Commodities
- Equities
- Financial-Services
- CLI
- Fintech
- Real-Time
website: https://docs.qfex.com
---
