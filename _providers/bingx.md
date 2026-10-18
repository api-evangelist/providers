---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-10-17'
api_count: 13
apis:
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Account API from BingX — 13 operation(s) for account.
  name: BingX Account API
  slug: bingx-account-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Agent API from BingX — 8 operation(s) for agent.
  name: BingX Agent API
  slug: bingx-agent-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Coin-M Futures API from BingX — 21 operation(s) for coin-m futures.
  name: BingX Coin-M Futures API
  slug: bingx-coin-m-futures-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Copy Trading API from BingX — 11 operation(s) for copy trading.
  name: BingX Copy Trading API
  slug: bingx-copy-trading-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Fund API from BingX — 1 operation(s) for fund.
  name: BingX Fund API
  slug: bingx-fund-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Other API from BingX — 1 operation(s) for other.
  name: BingX Other API
  slug: bingx-other-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Perpetual Futures (USDT-M) API from BingX — 53 operation(s) for perpetual futures (usdt-m).
  name: BingX Perpetual Futures (USDT-M) API
  slug: bingx-perpetual-futures-usdt-m-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Social API from BingX — 1 operation(s) for social.
  name: BingX Social API
  slug: bingx-social-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Spot API from BingX — 28 operation(s) for spot.
  name: BingX Spot API
  slug: bingx-spot-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Sub-Account API from BingX — 8 operation(s) for sub-account.
  name: BingX Sub Account API
  slug: bingx-sub-account-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The User Data Stream API from BingX — 1 operation(s) for user data stream.
  name: BingX User Data Stream API
  slug: bingx-user-data-stream-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Wallet API from BingX — 11 operation(s) for wallet.
  name: BingX Wallet API
  slug: bingx-wallet-api
- baseURL: https://open-api.bingx.com
  baseurl_source: declared
  description: The Wealth API from BingX — 5 operation(s) for wealth.
  name: BingX Wealth API
  slug: bingx-wealth-api
artifact_total: 15
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://bingx.com/en/price
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bingx/refs/heads/main/rules/bingx-rules.yml
  title: ''
  type: Spectral
  url: rules/bingx-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bingx/refs/heads/main/conformance/bingx-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bingx-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bingx/refs/heads/main/well-known/bingx-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bingx-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bingx/refs/heads/main/hosts/bingx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bingx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bingx/refs/heads/main/vendors/bingx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bingx-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bingx/refs/heads/main/security/bingx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bingx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bingx.com
- group: docs
  title: ''
  type: Documentation
  url: https://bingx-api.github.io/docs-v3/
- group: docs
  title: ''
  type: APIReference
  url: https://bingx-api.github.io/docs-v3/
- group: company
  title: ''
  type: Blog
  url: https://bingx.com/en/blog
- group: company
  title: ''
  type: Newsroom
  url: https://bingx.com/en/news
- group: start
  title: ''
  type: Login
  url: https://bingx.com/en/accounts/login
- group: start
  title: ''
  type: SignUp
  url: https://bingx.com/en/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bingx.com/en/support/articles/360034388413
- group: operate
  title: ''
  type: Support
  url: https://bingx.com/en/help
created: '2026-10-13'
description: BingX is a cryptocurrency exchange offering spot, perpetual futures (USDT-M and Coin-M), copy trading and wealth products. It exposes a public REST trading API at open-api.bingx.com and WebSocket market data streams, authenticated with an API key header and HMAC SHA256 request signatures.
image: https://static-app.bb-os.com/fe-common/assets/share_card.png?v=20240123
layout: provider
modified: '2026-10-13'
name: BingX
nav: Providers
network: true
overview: 'BingX is listed with 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agent API, Coin-M Futures API, and 10 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Financial Services.


  The BingX catalog on APIs.io includes 1 Spectral governance ruleset.


  BingX''s developer surface includes pricing, documentation, API reference, engineering blog, signup flow, support, and 10 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: BingX API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: bingx-rules
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 43.8
    catalog_earned_first_party: 0.0
    catalog_gap: 71.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 15.9
    contract_quality: 11.9
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Bingx Domain Security
  slug: bingx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bingx
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Financial Services
website: https://bingx.com
---
