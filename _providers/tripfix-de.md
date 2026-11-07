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
- description: Public API for TripFix expense reporting platform
  name: TripFix API
  slug: tripfix-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/tripfix-de/security/tripfix-de-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tripfix-de-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/tripfix-de/hosts/tripfix-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tripfix-de-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.tripfix.de/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tripfix.de/changelog
- group: auth
  href: https://artifacts.apis.io/tripfix-de/security/tripfix-de-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tripfix-de-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tripfix-de/security/tripfix-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tripfix-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tripfix.de/
created: '2026-10-30'
description: TripFix is a German SaaS platform that simplifies travel expense reporting for freelancers, self‑employed professionals, and small businesses. It offers automated calculation of per‑diem rates, mileage, accommodation costs, and integrates with German tax regulations for 2026. Users can create accounts, submit trips, and generate compliant expense reports without manual spreadsheets. The service includes a public pricing page, detailed guides, and a developer portal for API access.
image: https://www.tripfix.de/opengraph-image?0f9887d7ebc9ffb6
layout: provider
modified: '2026-10-30'
name: tripfix-de
nav: Providers
network: true
overview: 'tripfix-de is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Expenses, Software-as-a-Service, Germany, and Freelancers.


  tripfix-de''s developer surface includes changelog and 6 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tripfix-de/tripfix-de-2026-11-03T145102.png
security:
- kind: domain-security
  name: Tripfix De Domain Security
  slug: tripfix-de-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tripfix De Vulnerability Disclosure
  slug: tripfix-de-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tripfix-de
tags:
- Travel
- Expenses
- Software-as-a-Service
- Germany
- Freelancers
website: https://tripfix.de/
---
