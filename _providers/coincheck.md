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
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-10-17'
api_count: 2
apis:
- baseURL: https://coincheck.com/api
  baseurl_source: declared
  description: Authenticated account and trading
  name: Coincheck Private API
  slug: coincheck-private-api
- baseURL: https://coincheck.com/api
  baseurl_source: declared
  description: Unauthenticated market data
  name: Coincheck Public API
  slug: coincheck-public-api
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/rules/coincheck-rules.yml
  title: ''
  type: Spectral
  url: rules/coincheck-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/vocabulary/coincheck-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coincheck-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/conformance/coincheck-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coincheck-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/hosts/coincheck-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coincheck-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/vendors/coincheck-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coincheck-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/packages/coincheck-packages.yml
  title: ''
  type: SDKs
  url: packages/coincheck-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/packages/coincheck-packages.yml
  title: ''
  type: Packages
  url: packages/coincheck-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coincheck.com/info/terms
- group: company
  title: ''
  type: Newsroom
  url: https://corporate.coincheck.com/news
- group: start
  title: ''
  type: Login
  url: https://coincheck.com/sessions/signin
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/coincheck/refs/heads/main/security/coincheck-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coincheck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coincheck.com
- group: docs
  title: ''
  type: Documentation
  url: https://coincheck.com/documents/exchange/api
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://assets.coincheck.com/mcp
  - status: 200
    url: https://coincheck.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Coincheck is a Japanese cryptocurrency exchange. It documents a REST Exchange API (public market data plus HMAC-signed private trading, account, deposit and withdrawal endpoints) and WebSocket market feeds.
image: https://coincheck.com/images/ogp/coincheck_ogp_large.png
layout: provider
modified: '2026-10-13'
name: Coincheck
nav: Providers
network: true
overview: 'Coincheck is listed with 2 APIs on the [APIs.io](https://apis.io/) network: Private API and Public API. Tagged areas include Company, Cryptocurrency, Exchange, Trading, and Japan.


  The Coincheck catalog on APIs.io includes 1 Spectral governance ruleset.


  Coincheck''s developer surface includes documentation and 12 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Coincheck API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: coincheck-rules
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 22.0
    contract_quality: 11.6
    developer_ergonomics: 16.7
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
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
  name: Coincheck Domain Security
  slug: coincheck-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coincheck
tags:
- Company
- Cryptocurrency
- Exchange
- Trading
- Japan
website: https://coincheck.com
---
