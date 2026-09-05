---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Token-authenticated WebSocket streaming API for real-time market data. Two endpoints — wss://quote.alltick.co/quote-stock-b-ws-api for equities and wss://quote.alltick.co/quote-b-ws-api for forex, cry
  name: AllTick WebSocket Streaming API
  slug: alltick-websocket-streaming-api
- baseURL: https://quote.alltick.co
  baseurl_source: declared
  description: The Quote B Api API from AllTick API — 4 operation(s) for quote b api.
  name: AllTick API Quote B API
  slug: alltick-api-quote-b-api-api
- baseURL: https://quote.alltick.co
  baseurl_source: declared
  description: The Quote Stock B Api API from AllTick API — 5 operation(s) for quote stock b api.
  name: AllTick API Quote Stock B API
  slug: alltick-api-quote-stock-b-api-api
- baseURL: https://quote.alltick.co
  baseurl_source: declared
  description: The Suspension API from AllTick API — 3 operation(s) for suspension.
  name: AllTick API Suspension API
  slug: alltick-api-suspension-api
artifact_total: 9
asyncapis:
- description: ''
  name: Alltick Api Event Surface
  slug: alltick-api-event-surface
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/alltick-api-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alltick-api-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.alltick.co/en
- group: docs
  title: ''
  type: Documentation
  url: https://en.apis.alltick.co/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.alltick.co/en/api-reference/stock/kline
- group: start
  title: ''
  type: GettingStarted
  url: https://en.apis.alltick.co/integration-process/process-description
- group: operate
  title: ''
  type: Support
  url: https://alltick.co/#contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://alltick.co/faqs
- group: company
  title: ''
  type: Blog
  url: https://blog.alltick.co/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.alltick.co/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alltick
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/alltick/alltick-realtime-forex-crypto-stock-tick-finance-websocket-api
- group: commercial
  title: ''
  type: Pricing
  url: https://alltick.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://alltick.co/register
- group: start
  title: ''
  type: Login
  url: https://alltick.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alltick.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alltick.co/policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alltick.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/alltick-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alltick-api-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alltick-api-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alltick-api-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alltick-api-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alltick-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alltick-api-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alltick-api-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/alltick-api-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/alltick-api-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alltick-api-llms.txt
created: '2026-08-18'
description: AllTick (AllTick PTE. LTD., Singapore) sells real-time and historical financial market tick data through a token-authenticated HTTPS query API and two WebSocket streams, covering forex, Hong Kong / US / A-share equities, indices, precious metals, crude oil and cryptocurrencies across roughly 100,000 symbols. The HTTP surface returns candlesticks (1-minute through monthly, with ex-rights and forward-adjusted variants), latest trade ticks, order-book depth, equity reference data and SSE/NYSE/NASDAQ trading-halt listings; the WebSocket surface pushes tick-by-tick trades and order-book updates. Sold self-serve in USDT on a per-symbol-basket or whole-market basis, with a permanent free tier limited to ten demo symbols. Built for exchanges, brokers, quantitative teams, trading platforms and fintech developers.
image: https://alltick.co/images/logo.png
layout: provider
modified: '2026-08-18'
name: AllTick API
nav: Providers
network: true
overview: 'AllTick API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Quote B API, Quote Stock B API, and Suspension API. Tagged areas include Financial market data, Real-Time Data, stock-market-data, forex-data, and Cryptocurrency Data.


  The AllTick API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AllTick API''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Alltick Api Plans Pricing
  plan_count: 8
  slug: alltick-api-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 13
  name: Alltick Api Rate Limits
  slug: alltick-api-rate-limits
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 58.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 57.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alltick-api/refs/heads/main/screenshots/alltick-api-2026-09-02T144121.png
security:
- kind: authentication
  name: Alltick Api Authentication
  slug: alltick-api-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alltick Api Domain Security
  slug: alltick-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: alltick-api
tags:
- Financial market data
- Real-Time Data
- stock-market-data
- forex-data
- Cryptocurrency Data
- commodities-data
- Tick Data
- websocket-streaming
- Fintech
- Quantitative Trading
- market-data-api
- trading-halts
website: https://apis.alltick.co/en
---
