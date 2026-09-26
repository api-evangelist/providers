---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-09-25'
api_count: 3
apis:
- description: REST API for trading, order management, RFQ, account balances and transactions, transfers/deposits/withdrawals, custody (sFOX SAFE), staking, post-trade settlement, market data, and reporting. Bearer-
  name: sFOX REST API
  slug: sfox-rest-api
- baseURL: https://ws.sfox.com
  baseurl_source: declared
  description: Real-time streaming API for market data (order book, trades, ticker) and private account data (open orders, trades, balances, post-trade settlement). Authenticate then subscribe to feeds.
  name: sFOX WebSocket API
  slug: sfox-websocket-api
- description: 'White-label REST + WebSocket API for businesses: end-user management, KYC/KYB and Enhanced Due Diligence, bank-account linking (Plaid), ACH (Dwolla) and wire payments, withdrawals, transfers, monetiza'
  name: sFOX Connect API
  slug: sfox-connect-api
artifact_total: 7
asyncapis:
- description: 'Real-time streaming API for sFOX. Clients connect over WSS, authenticate with their API key (for private feeds), then subscribe/unsubscribe to feeds via a JSON control message: { "type": "subscribe", '
  name: sFOX WebSocket API
  slug: sfox-websocket-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.sfox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sfox.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sfox.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sfox.com/rest-api/rest-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sfox.com/introduction/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.sfox.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.sfox.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://trade.sfox.com/signup
- group: start
  title: ''
  type: Login
  url: https://trade.sfox.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sfox.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sfox.com/privacy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/authentication/sfox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sfox-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/llms/sfox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sfox-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/mcp/sfox-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sfox-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/well-known/sfox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sfox-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/errors/sfox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sfox-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/lifecycle/sfox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sfox-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/rate-limits/sfox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sfox-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/conventions/sfox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sfox-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/conformance/sfox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sfox-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/data-model/sfox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sfox-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/sandbox/sfox-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sfox-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/security/sfox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sfox-domain-security.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/changelog/sfox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sfox-changelog.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/asyncapi/sfox-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/sfox-websocket-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/asyncapi/sfox-websocket-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/sfox-websocket-asyncapi.yml
created: '2026-07-17'
description: sFOX is a unified crypto prime brokerage and infrastructure platform for professional and institutional investors — asset managers, hedge funds, family offices, and financial institutions. It aggregates liquidity from 30+ providers across 80+ markets for smart-routed best execution, and combines that with bankruptcy-remote custody (sFOX SAFE, via SAFE Trust Company), staking, credit, and post-trade settlement in one platform. sFOX exposes a REST API, a WebSocket streaming API, and a FIX API for trading, account management, RFQ, transfers, custody, staking, market data, and reporting; a separate white-label "Connect" API covers end-user onboarding, KYC/KYB, bank linking (Plaid/Dwolla), payments, withdrawals, and SSO for businesses building crypto products.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sfox.png
layout: provider
modified: '2026-07-21'
name: Sfox
nav: Providers
network: true
overview: 'Sfox publishes 3 APIs on the [APIs.io](https://apis.io/) network, including REST API, WebSocket API, and 1 more. Tagged areas include Company, Cryptocurrency, Prime Brokerage, Trading, and Digital Asset Custody.


  The Sfox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sfox''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 2
  name: Sfox Rate Limits
  slug: sfox-rate-limits
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 43.8
    developer_ergonomics: 47.6
    discoverability: 78.6
    operational_transparency: 44.7
  previous_composite: 44.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/sfox/refs/heads/main/screenshots/sfox-2026-08-17T081823.png
security:
- kind: authentication
  name: Sfox Authentication
  slug: sfox-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sfox Domain Security
  slug: sfox-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sfox
tags:
- Company
- Cryptocurrency
- Prime Brokerage
- Trading
- Digital Asset Custody
- Liquidity
- Staking
- Institutional
- Financial Services
- Market Data
- WebSocket
- FIX
- Real-Time
website: https://www.sfox.com/
---
