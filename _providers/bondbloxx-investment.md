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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Bondbloxx Investment ETF data and operations.
  name: Bondbloxx Investment API
  slug: bondbloxx-investment-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bondbloxx-investment/refs/heads/main/hosts/bondbloxx-investment-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bondbloxx-investment-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bondbloxx-investment/refs/heads/main/vendors/bondbloxx-investment-vendors.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/bondbloxx-investment/refs/heads/main/security/bondbloxx-investment-domain-security.yml
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
overview: Bondbloxx Investment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, ETFs, Fixed Income, Investment, and Asset Management.
random_paper: 10
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 13.0
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
