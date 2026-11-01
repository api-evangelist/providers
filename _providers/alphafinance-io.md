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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/alphafinance-io/llms/alphafinance-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphafinance-io-llms.txt
- group: other
  href: https://artifacts.apis.io/alphafinance-io/hosts/alphafinance-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphafinance-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphafinance-io/vendors/alphafinance-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphafinance-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphafinance.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alphafinance.io/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://alphafinance.io/news/
- group: auth
  href: https://artifacts.apis.io/alphafinance-io/security/alphafinance-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphafinance-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alphafinance.io
- group: company
  title: ''
  type: Blog
  url: https://alphfinance.io/blog/
coverage:
  checked: '2026-10-26'
  detail: No public developer documentation or API specifications were found on the company's website.
  evidence:
  - status: 200
    url: https://alphfinance.io
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Alpha Finance provides a free crypto market data terminal offering real-time liquidation heatmaps, funding rates, ETF flows, corporate treasury insights, DeFi yields, and on-chain data. The platform aggregates diverse crypto market metrics into a single interface, enabling traders and analysts to monitor market dynamics, assess risk, and discover investment opportunities across multiple assets and exchanges.
image: https://alphafinance.io/assets/og/home.png
layout: provider
modified: '2026-10-25'
name: Alpha Finance
nav: Providers
network: true
overview: 'Alpha Finance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Data, Market, and Terminal.


  Alpha Finance''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alphafinance Io Domain Security
  slug: alphafinance-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alphafinance-io
tags:
- Company
- Crypto
- Data
- Market
- Terminal
website: https://alphafinance.io
---
