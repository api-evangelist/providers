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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
api_count: 9
apis:
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Accounts API from CEX.IO — 4 operation(s) for accounts.
  name: CEX.IO Accounts API
  slug: cex-io-accounts-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Fees API from CEX.IO — 3 operation(s) for fees.
  name: CEX.IO Fees API
  slug: cex-io-fees-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Funding API from CEX.IO — 5 operation(s) for funding.
  name: CEX.IO Funding API
  slug: cex-io-funding-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The History API from CEX.IO — 2 operation(s) for history.
  name: CEX.IO History API
  slug: cex-io-history-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Market Data API from CEX.IO — 4 operation(s) for market data.
  name: CEX.IO Market Data API
  slug: cex-io-market-data-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Orders API from CEX.IO — 4 operation(s) for orders.
  name: CEX.IO Orders API
  slug: cex-io-orders-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Private API from CEX.IO — 16 operation(s) for private.
  name: CEX.IO Private API
  slug: cex-io-private-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Public API from CEX.IO — 11 operation(s) for public.
  name: CEX.IO Public API
  slug: cex-io-public-api
- baseURL: https://trade.cex.io/api/spot/rest
  baseurl_source: declared
  description: The Public Market Data API from CEX.IO — 8 operation(s) for public market data.
  name: CEX.IO Public Market Data API
  slug: cex-io-public-market-data-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/cex-io/rate-limits/cex-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cex-io-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cex-io/rules/cex-io-rules.yml
  title: ''
  type: Spectral
  url: rules/cex-io-rules.yml
- group: design
  href: https://artifacts.apis.io/cex-io/vocabulary/cex-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cex-io-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/cex-io/authentication/cex-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cex-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/cex-io/errors/cex-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cex-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cex-io/conformance/cex-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cex-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cex-io/llms/cex-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cex-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/cex-io/well-known/cex-io-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cex-io-support-security.txt
- group: agent
  href: https://artifacts.apis.io/cex-io/well-known/cex-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cex-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/cex-io/hosts/cex-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cex-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/cex-io/vendors/cex-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cex-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/cex-io/packages/cex-io-packages.yml
  title: ''
  type: SDKs
  url: packages/cex-io-packages.yml
- group: build
  href: https://artifacts.apis.io/cex-io/packages/cex-io-packages.yml
  title: ''
  type: Packages
  url: packages/cex-io-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cex.io/press
- group: other
  title: ''
  type: Leadership
  url: https://cex.io/team
- group: auth
  href: https://artifacts.apis.io/cex-io/security/cex-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cex-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cex.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cex.io/
- group: docs
  title: ''
  type: APIReference
  url: https://trade.cex.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.cex.io/en/articles/4383397-getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.cex.io/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://cex.io/prices
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cex.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cex.io/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://blog.cex.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cexiolabs
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://cex.io
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'CEX.IO is a cryptocurrency exchange founded in 2013 offering spot trading, buying and selling crypto with cards and bank transfers, staking and earn products, and a Prime brokerage service. It publishes two developer surfaces: the CEX.IO Spot Trading API (REST and WebSocket under trade.cex.io/api/spot) and the legacy CEX.IO Exchange API (REST under cex.io/api and WebSocket at ws.cex.io), both authenticated with API keys and HMAC signatures.'
image: https://static.cex.io/img/landing-img/index.png
layout: provider
modified: '2026-10-13'
name: CEX.IO
nav: Providers
network: true
overview: 'CEX.IO is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Fees API, Funding API, and 6 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Market Data.


  The CEX.IO catalog on APIs.io includes 1 Spectral governance ruleset.


  CEX.IO''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, engineering blog, and 19 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 4
  name: Cex Io Rate Limits
  slug: cex-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: CEX.IO API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cex-io-rules
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 47.1
    developer_ergonomics: 36.9
    discoverability: 80.4
    operational_transparency: 44.7
  previous_composite: 45.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cex-io/cex-io-2026-11-03T123738.png
security:
- kind: authentication
  name: Cex Io Authentication
  slug: cex-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cex Io Domain Security
  slug: cex-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cex-io
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Market Data
- WebSocket
- Financial Services
website: https://cex.io
---
