---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Tiger Brokers platform providing market data and trading operations.
  name: Tiger Brokers API
  slug: tiger-brokers-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tiger-brokers/refs/heads/main/hosts/tiger-brokers-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tiger-brokers-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tiger-brokers/refs/heads/main/vendors/tiger-brokers-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tiger-brokers-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tiger-brokers/refs/heads/main/packages/tiger-brokers-packages.yml
  title: ''
  type: SDKs
  url: packages/tiger-brokers-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tiger-brokers/refs/heads/main/packages/tiger-brokers-packages.yml
  title: ''
  type: Packages
  url: packages/tiger-brokers-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.itiger.com/sg/info/terms-n-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.itiger.com/sg/help
- group: start
  title: ''
  type: SignUp
  url: https://www.itiger.com/signup
- group: company
  title: ''
  type: Newsroom
  url: https://www.itiger.com/sg/about/news
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tigerbrokers.com.sg/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.itigerup.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tiger-brokers/refs/heads/main/security/tiger-brokers-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tiger-brokers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tigerbrokers.com.sg
coverage:
  checked: '2026-10-14'
  detail: Developer portal pages are rendered via JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://developer.tigerbrokers.com.sg/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Tiger Brokers is a Singapore‑based online brokerage platform offering retail investors access to global stock, options, futures, ETFs, and other financial products. The company provides a mobile and web trading application, supporting markets in the United States, Hong Kong, China A‑shares, Singapore, and more. It emphasizes low‑cost trading, real‑time market data, and a suite of investment tools such as auto‑invest, fractional shares, and cash‑boost accounts. Tiger Brokers is regulated by the Monetary Authority of Singapore and serves both individual and institutional clients worldwide.
image: https://c1.itigergrowtha.com/portal5/static/media/og-logo.0a0bd8dc.png
layout: provider
modified: '2026-10-14'
name: Tiger Brokers
nav: Providers
network: true
overview: 'Tiger Brokers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Brokerage, Fintech, Trading, and Singapore.


  Tiger Brokers'' developer surface includes support, signup flow, documentation, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Tiger Brokers Domain Security
  slug: tiger-brokers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tiger-brokers
tags:
- Company
- Brokerage
- Fintech
- Trading
- Singapore
website: https://www.tigerbrokers.com.sg
---
