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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/air-works/hosts/air-works-hosts.yml
  title: ''
  type: Hosts
  url: hosts/air-works-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airworks.aero/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://airworks.aero/media-center/news
- group: auth
  href: https://artifacts.apis.io/air-works/security/air-works-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/air-works-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airworks.aero
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://airworks.aero
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Air Works provides comprehensive aviation maintenance, repair, and overhaul (MRO) services for airlines and cargo operators. Based in Gurgaon, India, the company offers base and line maintenance, component repair, avionics, CAMO, and 24/7 AOG support, serving a global clientele with certified expertise and a focus on safety and efficiency.
image: https://airworks.aero/media/00dah1rz/airworks-favicon.ico
layout: provider
modified: '2026-10-22'
name: Air Works
nav: Providers
network: true
overview: Air Works is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, MRO, Maintenance, India, and Services.
random_paper: 15
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.3
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
screenshot: https://apis.io/screenshots/air-works/air-works-2026-11-03T120519.png
security:
- kind: domain-security
  name: Air Works Domain Security
  slug: air-works-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: air-works
tags:
- Aviation
- MRO
- Maintenance
- India
- Services
website: https://airworks.aero
---
