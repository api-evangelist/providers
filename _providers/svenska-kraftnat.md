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
  href: https://artifacts.apis.io/svenska-kraftnat/hosts/svenska-kraftnat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/svenska-kraftnat-hosts.yml
- group: other
  href: https://artifacts.apis.io/svenska-kraftnat/vendors/svenska-kraftnat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/svenska-kraftnat-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.svk.se/sakerhet-och-beredskap/sakerhetsskydd/personalsakerhet/registerkontroll/
- group: company
  title: ''
  type: Newsroom
  url: https://www.svk.se/press-och-nyheter/press/
- group: auth
  href: https://artifacts.apis.io/svenska-kraftnat/security/svenska-kraftnat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/svenska-kraftnat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.svk.se/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://svk.se/
  reason: no-developer-program
  state: none
created: '2026-10-15'
description: Svenska kraftnät is Sweden’s national transmission system operator, responsible for the safe and efficient operation of the country’s high‑voltage electricity grid. It ensures reliable power delivery, balances supply and demand, and coordinates cross‑border electricity exchanges. The agency also provides information on system status, market operations, and regulatory frameworks, supporting both industry stakeholders and the public.
image: https://www.svk.se/4ab19d/globalassets/svk.se.jpg
layout: provider
modified: '2026-10-15'
name: Svenska kraftnät
nav: Providers
network: true
overview: 'Svenska kraftnät is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Transmission, Grid, Sweden, and Utilities.


  Svenska kraftnät''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 6.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/svenska-kraftnat/svenska-kraftnat-2026-11-03T144128.png
security:
- kind: domain-security
  name: Svenska Kraftnat Domain Security
  slug: svenska-kraftnat-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: svenska-kraftnat
tags:
- Energy
- Transmission
- Grid
- Sweden
- Utilities
- Company
website: https://www.svk.se/
---
