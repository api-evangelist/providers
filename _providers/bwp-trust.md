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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bwp-trust/hosts/bwp-trust-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bwp-trust-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bwp-trust/security/bwp-trust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bwp-trust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bwptrust.com.au/
- group: operate
  title: ''
  type: Support
  url: https://bwptrust.com.au/site/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bwptrust.com.au/site/utilities/privacy
- group: company
  title: ''
  type: InvestorRelations
  url: https://bwptrust.com.au/site/investor-centre
created: '2026-10-21'
description: BWP Trust ("BWP" or "the Trust") is an Australian real estate investment trust, established and listed on the Australian Securities Exchange (ASX) in 1998, that invests in and manages commercial properties throughout Australia. It is the largest owner of Bunnings Warehouse sites in Australia, alongside large format retail showroom and industrial properties. Its website (bwptrust.com.au) is an investor-relations site; it publishes no developer portal, API documentation or public API.
image: https://bwptrust.com.au/site/irmcustomizationfile/57/banner-new.jpg
layout: provider
modified: '2026-10-21'
name: BWP Trust
nav: Providers
network: true
overview: 'BWP Trust is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, REIT, Commercial Property, and Investor Relations.


  BWP Trust''s developer surface includes support and 5 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bwp-trust/bwp-trust-2026-11-03T122858.png
security:
- kind: domain-security
  name: Bwp Trust Domain Security
  slug: bwp-trust-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bwp-trust
tags:
- Company
- Real Estate
- REIT
- Commercial Property
- Investor Relations
- Australia
- ASX
website: https://bwptrust.com.au/
---
