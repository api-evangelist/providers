---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Bitvavo Agentic Access
  operation_count: 41
  slug: bitvavo-agentic-access
  summary_line: 41 operations · 12 acting
api_count: 2
apis:
- description: Real-time WebSocket API for market data, trading, transfers, and account management on Bitvavo.
  name: Bitvavo WebSocket API
  slug: websocket-api
- description: Market Data Pro WebSocket API published by Bitvavo.
  name: Bitvavo Market Data Pro WebSocket API
  slug: market-data-pro-api
- description: FIX protocol API; the FIX dictionary is published at docs.bitvavo.com/api-specs/2026-04-28.fix.xml.
  name: Bitvavo FIX API
  slug: fix-api
- baseURL: https://api.bitvavo.com/v2
  baseurl_source: declared
  description: Get information about your Bitvavo account.
  name: Bitvavo Account API
  slug: bitvavo-account-api
- baseURL: https://api.bitvavo.com/v2
  baseurl_source: declared
  description: Create and manage multiple subaccounts under one main account and transfer funds between them.
  name: Bitvavo Account Management API
  slug: bitvavo-account-management-api
- baseURL: https://api.bitvavo.com/v2
  baseurl_source: declared
  description: Get the latest information about markets, trades, and candles on Bitvavo.
  name: Bitvavo Market data API
  slug: bitvavo-market-data-api
- baseURL: https://api.bitvavo.com/v2
  baseurl_source: declared
  description: Get information about your subaccounts and manage orders.
  name: Bitvavo Subaccounts API
  slug: bitvavo-subaccounts-api
- baseURL: https://api.bitvavo.com/v2
  baseurl_source: declared
  description: Synchronize markets and assets data with your app.
  name: Bitvavo Synchronization API
  slug: bitvavo-synchronization-api
- baseURL: https://api.bitvavo.com/v2
  baseurl_source: declared
  description: Manage your orders and trades on Bitvavo.
  name: Bitvavo Trading API
  slug: bitvavo-trading-api
- baseURL: https://api.bitvavo.com/v2
  baseurl_source: declared
  description: Deposit and withdraw funds on Bitvavo.
  name: Bitvavo Transfer API
  slug: bitvavo-transfer-api
artifact_total: 16
asyncapis:
- description: Real-time WebSocket API for market data, trading, transfers, and account management on Bitvavo.
  name: Bitvavo WebSocket API
  slug: bitvavo-exchange-websocket-asyncapi
- description: Low-latency WebSocket feed for real-time market data on Bitvavo. Provides order book snapshots, ticker prices, trades, and streaming subscriptions for book updates, ticker events, and trade events.
  name: Bitvavo WS Market Data Pro API
  slug: bitvavo-market-data-pro-asyncapi
common:
- group: agent
  href: https://artifacts.apis.io/bitvavo/agentic-access/bitvavo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bitvavo-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bitvavo/rules/bitvavo-rules.yml
  title: ''
  type: Spectral
  url: rules/bitvavo-rules.yml
- group: design
  href: https://artifacts.apis.io/bitvavo/vocabulary/bitvavo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitvavo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bitvavo/conventions/bitvavo-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/bitvavo-conventions.yml
- group: design
  href: https://artifacts.apis.io/bitvavo/conventions/bitvavo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bitvavo-conventions.yml
- group: design
  href: https://artifacts.apis.io/bitvavo/errors/bitvavo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bitvavo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bitvavo/conformance/bitvavo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitvavo-conformance.yml
- group: auth
  href: https://artifacts.apis.io/bitvavo/well-known/bitvavo-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitvavo-www-security.txt
- group: agent
  href: https://artifacts.apis.io/bitvavo/well-known/bitvavo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitvavo-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitvavo/hosts/bitvavo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitvavo-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitvavo/vendors/bitvavo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitvavo-vendors.yml
- group: build
  href: https://artifacts.apis.io/bitvavo/packages/bitvavo-packages.yml
  title: ''
  type: SDKs
  url: packages/bitvavo-packages.yml
- group: build
  href: https://artifacts.apis.io/bitvavo/packages/bitvavo-packages.yml
  title: ''
  type: Packages
  url: packages/bitvavo-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bitvavo.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitvavo
- group: auth
  href: https://artifacts.apis.io/bitvavo/authentication/bitvavo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitvavo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://bitvavo.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bitvavo.com/
- group: agent
  href: https://artifacts.apis.io/bitvavo/llms/bitvavo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitvavo-llms.txt
- group: start
  title: ''
  type: Portal
  url: https://account.bitvavo.com/user/api
- group: auth
  href: https://artifacts.apis.io/bitvavo/security/bitvavo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitvavo-domain-security.yml
created: '2026-10-13'
description: Bitvavo is a Netherlands-based European cryptocurrency exchange. It publishes a REST API, a WebSocket API, a Market Data Pro WebSocket API, an Institutional API and a FIX API for spot trading, market data, transfers and account management, authenticated with HMAC-SHA256 signed requests.
layout: provider
modified: '2026-10-13'
name: Bitvavo
nav: Providers
network: true
overview: 'Bitvavo publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including WebSocket API, Market Data Pro WebSocket API, Account API, and 7 more. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Market Data.


  The Bitvavo catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 1 Spectral governance ruleset.


  Bitvavo''s developer surface includes API reference, authentication, documentation, developer portal, and 17 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Bitvavo API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: bitvavo-rules
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.8
    developer_ergonomics: 45.2
    discoverability: 53.6
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bitvavo Authentication
  slug: bitvavo-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Bitvavo Domain Security
  slug: bitvavo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bitvavo
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Market Data
- Netherlands
website: https://bitvavo.com
---
