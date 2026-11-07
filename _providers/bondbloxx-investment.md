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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Bondbloxx Investment ETF data and operations.
  name: Bondbloxx Investment API
  slug: bondbloxx-investment-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bondbloxx-investment/hosts/bondbloxx-investment-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bondbloxx-investment-hosts.yml
- group: other
  href: https://artifacts.apis.io/bondbloxx-investment/vendors/bondbloxx-investment-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bondbloxx-investment-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bondbloxxetf.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bondbloxxetf.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://bondbloxxetf.com/newsroom/
- group: auth
  href: https://artifacts.apis.io/bondbloxx-investment/security/bondbloxx-investment-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bondbloxx-investment-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bondbloxxetf.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Bondbloxx Investment is a provider of specialized fixed‑income exchange‑traded funds (ETFs) focused on U.S. Treasuries, corporate bonds, private credit, and tax‑aware strategies. The firm offers a suite of ETFs designed for precise income generation, capital preservation, and diversified exposure to various credit markets, serving institutional and retail investors seeking tailored bond market solutions.
image: https://bondbloxxetf.com/wp-content/uploads/2024/06/bondbloxx_meta_image_2024.png
layout: provider
modified: '2026-10-02'
name: Bondbloxx Investment
nav: Providers
network: true
overview: Bondbloxx Investment is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, ETFs, Fixed Income, Investment, and Asset Management.
random_paper: 10
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 9.0
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bondbloxx-investment/bondbloxx-investment-2026-11-03T122201.png
security:
- kind: domain-security
  name: Bondbloxx Investment Domain Security
  slug: bondbloxx-investment-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bondbloxx-investment
tags:
- Finance
- ETFs
- Fixed Income
- Investment
- Asset Management
website: https://bondbloxxetf.com/
---
