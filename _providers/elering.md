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
api_count: 1
apis:
- description: Provides data and services for Estonia's electricity transmission grid.
  name: Elering API
  slug: elering-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/elering/hosts/elering-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elering-hosts.yml
- group: other
  href: https://artifacts.apis.io/elering/vendors/elering-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elering-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Elering
- group: auth
  href: https://artifacts.apis.io/elering/security/elering-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elering-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elering.ee/
- group: docs
  title: ''
  type: Documentation
  url: https://www.elering.ee/en/
- group: company
  title: ''
  type: Blog
  url: https://www.elering.ee/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elering.ee/en/price-list-and-standard-terms-and-conditions
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://dashboard.elering.ee/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Elering is Estonia’s transmission system operator, responsible for the operation, development and maintenance of the national electricity transmission grid. It ensures reliable power supply, manages cross‑border electricity flows, and supports market participants with grid services and data. The company also provides platforms for grid connection applications, metering data, and system balancing, serving both domestic and international stakeholders.
image: https://www.elering.ee/images/elering-og-image.jpg
layout: provider
modified: '2026-10-27'
name: Elering
nav: Providers
network: true
overview: 'Elering is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Transmission, Grid, Estonia, and Utilities.


  Elering''s developer surface includes documentation, engineering blog, pricing, and 5 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 57.1
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - estonia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.6
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/elering/elering-2026-11-03T131430.png
security:
- kind: domain-security
  name: Elering Domain Security
  slug: elering-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: elering
tags:
- Energy
- Transmission
- Grid
- Estonia
- Utilities
website: https://www.elering.ee/
---
