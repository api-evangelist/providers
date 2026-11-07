---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Real-time streaming service for MAX Exchange. Public channels cover order book (book), trade, ticker, kline, market_status and m-wallet pool_quota; private channels stream order snapshots/updates, tra
  name: MAX Exchange WebSocket API
  slug: maicoin-max-websocket
- description: Unauthenticated system status endpoint reporting whether the MAX API is online or in maintenance, with an ISO 8601 last_changed_at timestamp. Documented in the MAX V3 API reference; status updates may
  name: MAX System Status API
  slug: maicoin-max-status
- baseURL: https://max-api.maicoin.com
  baseurl_source: declared
  description: Operations about Converts
  name: MaiCoin Convert API
  slug: maicoin-convert-api
- baseURL: https://max-api.maicoin.com
  baseurl_source: declared
  description: Requires authentication
  name: MaiCoin Order API
  slug: maicoin-order-api
- baseURL: https://max-api.maicoin.com
  baseurl_source: declared
  description: Public endpoints
  name: MaiCoin Public API
  slug: maicoin-public-api
- baseURL: https://max-api.maicoin.com
  baseurl_source: declared
  description: Requires authentication
  name: MaiCoin Trade API
  slug: maicoin-trade-api
- baseURL: https://max-api.maicoin.com
  baseurl_source: declared
  description: Requires authentication
  name: MaiCoin Transaction API
  slug: maicoin-transaction-api
- baseURL: https://max-api.maicoin.com
  baseurl_source: declared
  description: Operations about Users
  name: MaiCoin User API
  slug: maicoin-user-api
- baseURL: https://max-api.maicoin.com
  baseurl_source: declared
  description: Requires authentication
  name: MaiCoin Wallet API
  slug: maicoin-wallet-api
artifact_total: 19
asyncapis:
- description: 'Real-time streaming for MAX Exchange (MaiCoin). One WebSocket endpoint carries both public market-data channels and, after authentication, private account channels. Field names are abbreviated on the '
  name: MAX Exchange WebSocket API
  slug: maicoin-max-websocket-asyncapi
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.maicoin.com/feed/
- group: other
  href: https://artifacts.apis.io/maicoin/capabilities/maicoin-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/maicoin-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/maicoin/security/maicoin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/maicoin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://max.maicoin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://campaign.maicoin.com/en/api
- group: docs
  title: ''
  type: Documentation
  url: https://campaign.maicoin.com/en/api-document
- group: docs
  title: ''
  type: APIReference
  url: https://max-api.maicoin.com/doc/v3.html
- group: start
  title: ''
  type: GettingStarted
  url: https://campaign.maicoin.com/en/api
- group: operate
  title: ''
  type: Support
  url: https://support.maicoin.com
- group: company
  title: ''
  type: Blog
  url: https://blog.maicoin.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maicoin
- group: operate
  title: ''
  type: StatusPage
  url: https://status-max.maicoin.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://campaign.maicoin.com/en/vip
- group: start
  title: ''
  type: SignUp
  url: https://max.maicoin.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.maicoin.com/max/MAX-Terms-of-Use.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assets.maicoin.com/max/max-privacy-policy.html
- group: agent
  href: https://artifacts.apis.io/maicoin/llms/maicoin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/maicoin-llms.txt
- group: build
  href: https://artifacts.apis.io/maicoin/packages/maicoin-packages.yml
  title: ''
  type: Packages
  url: packages/maicoin-packages.yml
- group: build
  href: https://artifacts.apis.io/maicoin/packages/maicoin-packages.yml
  title: ''
  type: SDKs
  url: packages/maicoin-packages.yml
- group: auth
  href: https://artifacts.apis.io/maicoin/authentication/maicoin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/maicoin-authentication.yml
- group: design
  href: https://artifacts.apis.io/maicoin/conventions/maicoin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/maicoin-conventions.yml
- group: design
  href: https://artifacts.apis.io/maicoin/conventions/maicoin-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/maicoin-conventions.yml
- group: design
  href: https://artifacts.apis.io/maicoin/errors/maicoin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/maicoin-problem-types.yml
- group: design
  href: https://artifacts.apis.io/maicoin/errors/maicoin-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/maicoin-error-codes.yml
- group: design
  href: https://artifacts.apis.io/maicoin/lifecycle/maicoin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/maicoin-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/maicoin/changelog/maicoin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/maicoin-changelog.yml
- group: operate
  href: https://artifacts.apis.io/maicoin/rate-limits/maicoin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/maicoin-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/maicoin/plans/maicoin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/maicoin-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/maicoin/data-model/maicoin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/maicoin-data-model.yml
- group: design
  href: https://artifacts.apis.io/maicoin/conformance/maicoin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/maicoin-conformance.yml
- group: docs
  href: https://artifacts.apis.io/maicoin/asyncapi/maicoin-max-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/maicoin-max-websocket-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/maicoin/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/maicoin/overlays/maicoin-max-v3-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/maicoin-max-v3-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/maicoin/mcp/maicoin-mcp.yml
  title: ''
  type: MCPCandidate
  url: mcp/maicoin-mcp.yml
created: '2026-08-25'
description: MaiCoin is a Taiwan-based digital asset group that operates MAX (MaiCoin Assets eXchange), a regulated cryptocurrency exchange offering spot trading, margin borrowing (m-wallet), staking, and fiat TWD on/off-ramps. MAX publishes a public V3 RESTful trading API with 54 operations spanning public market data (markets, tickers, order book depth, k-line, public trades), order management, trade history, wallet and account balances, deposits and withdrawals, internal transfers, currency conversion, and margin loan/repayment/liquidation. A companion WebSocket streaming service delivers real-time order book, ticker, k-line, trade, market status and private order/trade/account events. Authentication uses HMAC-SHA256 request signing over a base64 payload with X-MAX-ACCESSKEY, X-MAX-PAYLOAD and X-MAX-SIGNATURE headers.
finops:
- has_sources: true
  method: derived
  name: Maicoin Finops
  primary_unit: ''
  service_category: ''
  slug: maicoin-finops
  template: true
image: https://cdn.prod.website-files.com/61c42c1d462b6844a0915d9b/6a7160b6139bc8cdd5e3cf27_logo_MAX.png
layout: provider
modified: '2026-10-06'
name: MaiCoin
nav: Providers
network: true
overview: 'MaiCoin publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Convert API, Order API, Public API, and 6 more. Tagged areas include Company, Cryptocurrency, Digital Assets, Exchange, and Trading.


  The MaiCoin catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  MaiCoin''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Maicoin Plans Pricing
  plan_count: 10
  slug: maicoin-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 6
  name: Maicoin Rate Limits
  slug: maicoin-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: MaiCoin API Rules
  rule_count: 54
  severity_counts:
    error: 44
    hint: 0
    info: 3
    warn: 7
  slug: maicoin-rules
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 51.4
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 65.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 59.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/maicoin/maicoin-2026-09-02T150513.png
security:
- kind: authentication
  name: Maicoin Authentication
  slug: maicoin-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Maicoin Domain Security
  slug: maicoin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: maicoin-authenticate-private-channels
  slug: maicoin-authenticate-private-channels
- name: maicoin-place-and-confirm-order
  slug: maicoin-place-and-confirm-order
- name: maicoin-stream-market-data
  slug: maicoin-stream-market-data
slug: maicoin
tags:
- Company
- Cryptocurrency
- Digital Assets
- Exchange
- Trading
- Financial Services
- Market Data
- Blockchain
- Taiwan
- WebSocket
- Real-Time
website: https://max.maicoin.com
---
