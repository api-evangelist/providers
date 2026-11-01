---
access_model:
  confidence: high
  label: Freemium (3-day free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: Real-time streaming trades and quotes for US stocks, global stocks, forex, crypto, CFD indices, and ETFs over per-customer WebSocket URLs (assigned subdomain and port on finage.ws, socket-key token au
  name: Finage WebSocket Market Data Stream
  slug: finage-websocket-market-data-stream
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Bonds API from Finage — 1 operation(s) for bonds.
  name: Finage Bonds API
  slug: finage-bonds-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Canadian Stocks API from Finage — 2 operation(s) for canadian stocks.
  name: Finage Canadian Stocks API
  slug: finage-canadian-stocks-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Crypto API from Finage — 6 operation(s) for crypto.
  name: Finage Crypto API
  slug: finage-crypto-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Forex API from Finage — 6 operation(s) for forex.
  name: Finage Forex API
  slug: finage-forex-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Fundamentals API from Finage — 40 operation(s) for fundamentals.
  name: Finage Fundamentals API
  slug: finage-fundamentals-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Indian Stocks API from Finage — 2 operation(s) for indian stocks.
  name: Finage Indian Stocks API
  slug: finage-indian-stocks-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Indices API from Finage — 3 operation(s) for indices.
  name: Finage Indices API
  slug: finage-indices-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The Russian Stocks API from Finage — 2 operation(s) for russian stocks.
  name: Finage Russian Stocks API
  slug: finage-russian-stocks-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The UK Stocks API from Finage — 2 operation(s) for uk stocks.
  name: Finage UK Stocks API
  slug: finage-uk-stocks-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The US Stocks API from Finage — 5 operation(s) for us stocks.
  name: Finage US Stocks API
  slug: finage-us-stocks-api
- baseURL: https://api.finage.co.uk
  baseurl_source: declared
  description: The ETFs API from Finage — 3 operation(s) for etfs.
  name: Finage ET Fs API
  slug: finage-etfs-api
artifact_total: 23
asyncapis:
- description: 'Finage streams real-time market prices (US stocks, global stocks, forex, crypto, CFD indices, and ETFs) over WebSocket. Each customer is assigned a dedicated WebSocket URL (subdomain + port) shown in '
  name: Finage WebSocket Market Data Stream
  slug: finage-websocket-asyncapi
collections:
- collection_type: open
  name: Finage Market Data API
  slug: open-finage
common:
- group: other
  href: https://artifacts.apis.io/finage/overlays/finage-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/finage-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/finage/mcp/finage-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/finage-mcp.yml
- group: auth
  href: https://artifacts.apis.io/finage/authentication/finage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finage-authentication.yml
- group: auth
  href: https://artifacts.apis.io/finage/security/finage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finage-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finage.co.uk
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: build
  href: https://artifacts.apis.io/finage/packages/finage-packages.yml
  title: ''
  type: Packages
  url: packages/finage-packages.yml
- group: agent
  href: https://artifacts.apis.io/finage/well-known/finage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finage-well-known.yml
- group: agent
  href: https://artifacts.apis.io/finage/llms/finage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finage-llms.txt
- group: design
  href: https://artifacts.apis.io/finage/conformance/finage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finage-conformance.yml
- group: design
  href: https://artifacts.apis.io/finage/errors/finage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/finage-problem-types.yml
- group: design
  href: https://artifacts.apis.io/finage/lifecycle/finage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/finage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/finage/conventions/finage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/finage-conventions.yml
- group: design
  href: https://artifacts.apis.io/finage/components/finage-components.yml
  title: ''
  type: Components
  url: components/finage-components.yml
- group: design
  href: https://artifacts.apis.io/finage/data-model/finage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finage-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/finage/plans/finage-plans.yml
  title: ''
  type: Plans
  url: plans/finage-plans.yml
- group: operate
  href: https://artifacts.apis.io/finage/rate-limits/finage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/finage-rate-limits.yml
- group: docs
  href: https://artifacts.apis.io/finage/asyncapi/finage-websocket-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/finage-websocket-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/finage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Portal
  url: https://moon.finage.co.uk
- group: start
  title: ''
  type: SignUp
  url: https://moon.finage.co.uk/register
- group: docs
  title: ''
  type: Documentation
  url: https://finage.co.uk/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://finage.co.uk/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://finage.co.uk/pricing
- group: company
  title: ''
  type: Blog
  url: https://finage.co.uk/blog
- group: operate
  title: ''
  type: Support
  url: https://finage.co.uk/company/frequently-asked-questions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FinageLTD
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finage.co.uk/company/privacy-policy/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finage.co.uk/company/privacy-policy/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finageltd/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/finageltd
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCRUuqo17XKUVxPODKLsRvmA
created: '2026-05-28'
description: Finage is a London-based real-time and historical market data provider covering US and global stocks, forex, cryptocurrencies, CFD indices, ETFs, bonds, and company fundamentals. Data is delivered through a read-only REST API (api.finage.co.uk, API-key auth, 72 documented endpoints spanning quotes, trades, OHLCV aggregates, snapshots, financial statements, calendars, news, and technical indicators), dedicated per-customer WebSocket streams on finage.ws for real-time trades and quotes, and embeddable website widgets served from cdn.finage.co.uk. Plans range from a free 1,000 request/month tier through Basic API packages to Professional unlimited WebSocket feeds, with a 3-day free trial across all markets.
finops:
- has_sources: true
  method: derived
  name: Finage Finops
  primary_unit: subscription
  service_category: ''
  slug: finage-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finage.png
layout: provider
modified: '2026-07-22'
name: Finage
nav: Providers
network: true
overview: 'Finage publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including WebSocket Market Data Stream, Bonds API, Canadian Stocks API, and 9 more. Tagged areas include Finance, Market Data, Stocks, Foreign Exchange, and Cryptocurrency.


  The Finage catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finage''s developer surface includes authentication, developer portal, signup flow, documentation, API reference, pricing, engineering blog, and 25 more developer resources.'
plans:
- name: Finage Plans
  plan_count: 3
  slug: finage-plans
- name: Finage Price Estimates
  plan_count: 0
  slug: finage-price-estimates
random_paper: 18
rate_limits:
- limit_count: 3
  name: Finage Rate Limits
  slug: finage-rate-limits
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 24.3
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 44.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/finage/finage-2026-06-20T181209.png
security:
- kind: authentication
  name: Finage Authentication
  slug: finage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Finage Domain Security
  slug: finage-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Research company fundamentals with Finage
  slug: finage-company-fundamentals
- name: Pull historical OHLCV aggregates from Finage
  slug: finage-historical-aggregates
- name: Get real-time prices from Finage
  slug: finage-realtime-prices
slug: finage
tags:
- Finance
- Market Data
- Stocks
- Foreign Exchange
- Cryptocurrency
- ETFs
- Indices
- Fundamentals
- Real-Time Data
- Public APIs
- Real-Time
website: https://finage.co.uk
---
