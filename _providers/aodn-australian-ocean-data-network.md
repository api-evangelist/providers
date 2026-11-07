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
  href: https://artifacts.apis.io/aodn-australian-ocean-data-network/hosts/aodn-australian-ocean-data-network-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aodn-australian-ocean-data-network-hosts.yml
- group: other
  href: https://artifacts.apis.io/aodn-australian-ocean-data-network/vendors/aodn-australian-ocean-data-network-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aodn-australian-ocean-data-network-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imos.org.au/terms-of-use
- group: company
  title: ''
  type: Newsroom
  url: https://imos.org.au/news
- group: auth
  href: https://artifacts.apis.io/aodn-australian-ocean-data-network/security/aodn-australian-ocean-data-network-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aodn-australian-ocean-data-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://imos.org.au/data/about-the-australian-ocean-data-network
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.aodn.org.au/
coverage:
  checked: '2026-10-23'
  detail: Documentation pages at https://portal.aodn.org.au/ return HTML shells and 404 for spec files, preventing machine-readable contract discovery.
  evidence:
  - status: 404
    url: https://portal.aodn.org.au/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: AODN - Australian Ocean Data Network (AODN) provides a collaborative, distributed data infrastructure for marine and oceanographic research in Australia. It aggregates, curates, and makes accessible a wide range of ocean data, including physical, chemical, biological, and geological datasets, through web services and portals. AODN supports scientists, policymakers, and the public by offering tools for data discovery, visualization, and download, fostering open science and informed decision‑making about marine environments.
image: https://imos.org.au/wp-content/uploads/2024/06/ryan-wilson-YdpDztAnW9w-unsplash.jpg
layout: provider
modified: '2026-10-23'
name: AODN - Australian Ocean Data Network
nav: Providers
network: true
overview: AODN - Australian Ocean Data Network is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Oceanography, Data, Research, and Australia.
random_paper: 20
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 49.1
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
  previous_composite: 8.2
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/aodn-australian-ocean-data-network/aodn-australian-ocean-data-network-2026-11-03T120903.png
security:
- kind: domain-security
  name: Aodn Australian Ocean Data Network Domain Security
  slug: aodn-australian-ocean-data-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aodn-australian-ocean-data-network
tags:
- Company
- Oceanography
- Data
- Research
- Australia
website: https://imos.org.au/data/about-the-australian-ocean-data-network
---
