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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
api_count: 8
apis:
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The Accounts API from NDAX — 9 operation(s) for accounts.
  name: NDAX Accounts API
  slug: ndax-accounts-api
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The Instruments API from NDAX — 2 operation(s) for instruments.
  name: NDAX Instruments API
  slug: ndax-instruments-api
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The Miscellaneous API from NDAX — 2 operation(s) for miscellaneous.
  name: NDAX Miscellaneous API
  slug: ndax-miscellaneous-api
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The OMS Orders API from NDAX — 15 operation(s) for oms orders.
  name: NDAX OMS Orders API
  slug: ndax-oms-orders-api
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The Products API from NDAX — 2 operation(s) for products.
  name: NDAX Products API
  slug: ndax-products-api
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The Tickets API from NDAX — 19 operation(s) for tickets.
  name: NDAX Tickets API
  slug: ndax-tickets-api
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The Trades API from NDAX — 5 operation(s) for trades.
  name: NDAX Trades API
  slug: ndax-trades-api
- baseURL: https://api.ndax.io:8443/AP
  baseurl_source: declared
  description: The Users API from NDAX — 24 operation(s) for users.
  name: NDAX Users API
  slug: ndax-users-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/ndax/authentication/ndax-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ndax-authentication.yml
- group: design
  href: https://artifacts.apis.io/ndax/errors/ndax-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/ndax-error-codes.yml
- group: design
  href: https://artifacts.apis.io/ndax/rules/ndax-rules.yml
  title: ''
  type: Spectral
  url: rules/ndax-rules.yml
- group: design
  href: https://artifacts.apis.io/ndax/vocabulary/ndax-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ndax-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ndax/conformance/ndax-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ndax-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ndax/llms/ndax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ndax-llms.txt
- group: other
  href: https://artifacts.apis.io/ndax/hosts/ndax-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ndax-hosts.yml
- group: other
  href: https://artifacts.apis.io/ndax/vendors/ndax-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ndax-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ndax/security/ndax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ndax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ndax.io
- group: docs
  title: ''
  type: Documentation
  url: https://apidoc.ndax.io
- group: docs
  title: ''
  type: APIReference
  url: https://apidoc.ndax.io
- group: company
  title: ''
  type: Blog
  url: https://ndax.io/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ndax.io/en/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ndax.io/en/legal/account-agreements
- group: commercial
  title: ''
  type: Legal
  url: https://ndax.io/en/legal
- group: company
  title: ''
  type: About
  url: https://ndax.io/en/about-us
- group: start
  title: ''
  type: SignUp
  url: https://portal.ndax.io/auth/sign-up
- group: operate
  title: ''
  type: Support
  url: https://ndax.io/support
created: '2026-10-13'
description: Ndax (Ndax Canada Inc.) is a Canadian cryptocurrency exchange and registered investment dealer offering crypto trading against CAD, funding and institutional services. Its Ndax Pro API, built on the AlphaPoint exchange platform, exposes market data, account, order, deposit and withdrawal functions as JSON-framed calls over a WebSocket gateway (wss://api.ndax.io/WSGateway/) and an HTTP gateway at api.ndax.io:8443/AP/.
image: https://imagedelivery.net/ymlbamkZ1Lun5qrrLrRWlQ/ebc8e984-23a7-4417-e6c4-f190b6834f00/lg
layout: provider
modified: '2026-10-13'
name: NDAX
nav: Providers
network: true
overview: 'NDAX is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Instruments API, Miscellaneous API, and 5 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Market Data.


  The NDAX catalog on APIs.io includes 1 Spectral governance ruleset.


  NDAX''s developer surface includes authentication, documentation, API reference, engineering blog, pricing, legal docs, signup flow, and 12 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: NDAX API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: ndax-rules
score:
  band: thin
  composite: 26.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 13.4
    developer_ergonomics: 35.7
    discoverability: 71.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ndax Authentication
  slug: ndax-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ndax Domain Security
  slug: ndax-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ndax
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Market Data
- WebSocket
- Canada
website: https://ndax.io
---
