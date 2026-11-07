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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/jones-martin/well-known/jones-martin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jones-martin-well-known.yml
- group: other
  href: https://artifacts.apis.io/jones-martin/hosts/jones-martin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jones-martin-hosts.yml
- group: other
  href: https://artifacts.apis.io/jones-martin/vendors/jones-martin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jones-martin-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jonesandmartinauctions.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jonesandmartinauctions.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/jones-martin/security/jones-martin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jones-martin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jonesandmartinauctions.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://jonesandmartinauctions.com
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: Jones & Martin Auctions, LLC is a premier auctioneering company based in Newville, Pennsylvania. They facilitate a wide range of auctions including real estate, collectibles, antiques, farm equipment, and other assets throughout Central Pennsylvania. The company provides online auction listings, broker participation forms, and comprehensive auction services, serving both private sellers and professional brokers. Their website offers detailed auction schedules, contact information, and resources for participants.
image: https://jonesandmartinauctions.com/wp-content/uploads/logo.webp
layout: provider
modified: '2026-10-26'
name: Jones, Martin
nav: Providers
network: true
overview: Jones, Martin is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Auctions, Real Estate, Collectibles, and Pennsylvania.
random_paper: 15
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/jones-martin/jones-martin-2026-11-03T134242.png
security:
- kind: domain-security
  name: Jones Martin Domain Security
  slug: jones-martin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jones-martin
tags:
- Company
- Auctions
- Real Estate
- Collectibles
- Pennsylvania
website: https://jonesandmartinauctions.com
---
