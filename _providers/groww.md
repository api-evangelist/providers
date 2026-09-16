---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-09-15'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Groww Agentic Access
  operation_count: 20
  slug: groww-agentic-access
  summary_line: 20 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.groww.in
  baseurl_source: declared
  description: Access-token generation for API key + secret and TOTP flows.
  name: Groww Authentication API
  slug: groww-authentication-api
- baseURL: https://api.groww.in
  baseurl_source: declared
  description: Historical candle data.
  name: Groww Historical Data API
  slug: groww-historical-data-api
- baseURL: https://api.groww.in
  baseurl_source: declared
  description: Real-time LTP, quote, OHLC, option chain and greeks.
  name: Groww Live Data API
  slug: groww-live-data-api
- baseURL: https://api.groww.in
  baseurl_source: declared
  description: Available margin and per-order margin requirements.
  name: Groww Margin API
  slug: groww-margin-api
- baseURL: https://api.groww.in
  baseurl_source: declared
  description: Place, modify, cancel and track orders and trades.
  name: Groww Orders API
  slug: groww-orders-api
- baseURL: https://api.groww.in
  baseurl_source: declared
  description: Holdings and positions.
  name: Groww Portfolio API
  slug: groww-portfolio-api
artifact_total: 25
collections:
- collection_type: postman
  name: Groww Trading Authentication API
  slug: postman-groww-authentication-api
- collection_type: postman
  name: Groww Trading Authentication Historical Data API
  slug: postman-groww-historical-data-api
- collection_type: postman
  name: Groww Trading Authentication Live Data API
  slug: postman-groww-live-data-api
- collection_type: postman
  name: Groww Trading Authentication Margin API
  slug: postman-groww-margin-api
- collection_type: postman
  name: Groww Trading Authentication Orders API
  slug: postman-groww-orders-api
- collection_type: postman
  name: Groww Trading Authentication Portfolio API
  slug: postman-groww-portfolio-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Groww Trading Authentication API
  slug: open-groww-authentication-api
- collection_type: open
  name: Groww Trading Authentication Historical Data API
  slug: open-groww-historical-data-api
- collection_type: open
  name: Groww Trading Authentication Live Data API
  slug: open-groww-live-data-api
- collection_type: open
  name: Groww Trading Authentication Margin API
  slug: open-groww-margin-api
- collection_type: open
  name: Groww Trading Authentication Orders API
  slug: open-groww-orders-api
- collection_type: open
  name: Groww Trading Authentication Portfolio API
  slug: open-groww-portfolio-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/groww/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://groww.in/trade-api
- group: docs
  title: ''
  type: Documentation
  url: https://groww.in/trade-api/docs
- group: docs
  title: ''
  type: APIReference
  url: https://groww.in/trade-api/docs/curl
- group: start
  title: ''
  type: GettingStarted
  url: https://groww.in/trade-api/docs/python-sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://groww.in/trade-api
- group: start
  title: ''
  type: SignUp
  url: https://groww.in/trade-api/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://groww.in/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://groww.in/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://groww.in/help
- group: company
  title: ''
  type: Blog
  url: https://groww.in/blog
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/openapi/_original/groww-trade-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/groww-trade-api-openapi.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/authentication/groww-authentication.yml
  title: ''
  type: Authentication
  url: authentication/groww-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/scopes/groww-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/groww-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/conventions/groww-conventions.yml
  title: ''
  type: Conventions
  url: conventions/groww-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/conventions/groww-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/groww-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/rate-limits/groww-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/groww-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/errors/groww-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/groww-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/lifecycle/groww-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/groww-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/lifecycle/groww-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/groww-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/conformance/groww-conformance.yml
  title: ''
  type: Conformance
  url: conformance/groww-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/data-model/groww-data-model.yml
  title: ''
  type: DataModel
  url: data-model/groww-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/security/groww-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/groww-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/agentic-access/groww-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/groww-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/well-known/groww-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/groww-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/packages/groww-packages.yml
  title: ''
  type: Packages
  url: packages/groww-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/packages/groww-packages.yml
  title: ''
  type: SDKs
  url: packages/groww-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/mcp/groww-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/groww-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/llms/groww-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/groww-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/overlays/groww-trade-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/groww-trade-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://groww.in/
created: '2026-07-17'
description: Groww is an Indian fintech company offering investing and trading in stocks, futures & options, mutual funds, ETFs, IPOs and more through its consumer app and web platform. Backed by Iconiq Capital, Ribbit Capital and Y Combinator, Groww also operates the Groww Trading API — an official programmatic interface for algorithmic trading that covers order management (place/modify/cancel), portfolio holdings and positions, margin calculation, live market data (LTP, full quote, OHLC, option chain and greeks) and historical candle data across the CASH (equity) and FNO (derivatives) segments on Indian exchanges. Requests hit https://api.groww.in, are versioned with the X-API-VERSION header, and are authenticated with a daily Bearer access token generated via an API key + secret checksum, a TOTP flow, or an OAuth2 authorization-code flow.
image: https://groww.in/favicon.ico
layout: provider
modified: '2026-07-19'
name: Groww
nav: Providers
network: true
overview: 'Groww publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Historical Data API, Live Data API, and 3 more. Tagged areas include Company, Fintech, Trading, Investing, and Stock Broking.


  Groww''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 25 more developer resources.'
plans:
- name: Groww Plans
  plan_count: 1
  slug: groww-plans
random_paper: 20
rate_limits:
- limit_count: 7
  name: Groww Rate Limits
  slug: groww-rate-limits
scopes:
- name: Groww Scopes
  scope_count: 0
  slug: groww-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 57.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 53.4
    developer_ergonomics: 67.3
    discoverability: 75.9
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 57.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/groww/refs/heads/main/screenshots/groww-2026-07-25T220530.png
security:
- kind: authentication
  name: Groww Authentication
  slug: groww-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Groww Domain Security
  slug: groww-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: groww
tags:
- Company
- Fintech
- Trading
- Investing
- Stock Broking
- Market Data
- Algorithmic Trading
- India
website: https://groww.in/
---
