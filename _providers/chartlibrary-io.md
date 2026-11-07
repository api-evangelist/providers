---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/chartlibrary-io/hosts/chartlibrary-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chartlibrary-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/chartlibrary-io/vendors/chartlibrary-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chartlibrary-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/chartlibrary-io/security/chartlibrary-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chartlibrary-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chartlibrary.io/
- group: docs
  title: ''
  type: Documentation
  url: https://chartlibrary.io/newsletter
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chartlibrary.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chartlibrary.io/terms
coverage:
  checked: '2026-11-03'
  detail: Chart Library provides a newsletter service with no public API surface.
  evidence:
  - status: 200
    url: https://chartlibrary.io/
  reason: tenant-only
  state: none
created: '2026-11-03'
description: Chart Library provides a weekday morning newsletter that highlights three gap stocks before the market opens, offering analysis of news impact and historical gap performance. The service is free for the first 30 days, then $5 per month, and includes detailed charts and historical data to help investors plan their opening trades.
image: https://chartlibrary.io/og-market-memory.png
layout: provider
modified: '2026-11-03'
name: Chart Library
nav: Providers
network: true
overview: 'Chart Library is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Newsletters, Stock Analysis, Market Data, and Free Trial.


  Chart Library''s developer surface includes documentation and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chartlibrary Io Domain Security
  slug: chartlibrary-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chartlibrary-io
tags:
- Finance
- Newsletters
- Stock Analysis
- Market Data
- Free Trial
website: https://chartlibrary.io/
---
