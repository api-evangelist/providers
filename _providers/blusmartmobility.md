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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blusmartmobility/refs/heads/main/hosts/blusmartmobility-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blusmartmobility-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blusmartmobility/refs/heads/main/vendors/blusmartmobility-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blusmartmobility-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blusmartmobility/refs/heads/main/security/blusmartmobility-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blusmartmobility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/blusmartmobility
- group: company
  title: ''
  type: Website
  url: https://blusmart.com
created: '2026-09-29'
description: BluSmart Mobility was an Indian ride‑sharing company offering all‑electric taxis across major cities. Founded in 2019, it grew to operate a fleet of over 3,000 EVs, providing a surge‑free, environmentally friendly alternative to traditional cabs. The startup faced financial difficulties and entered insolvency proceedings in 2025, marking the end of its operations.
layout: provider
modified: '2026-09-29'
name: Blusmartmobility
nav: Providers
network: true
overview: Blusmartmobility is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Mobility, Ridesharing, Electric Vehicles, India, and Startups.
random_paper: 9
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
      reason: venue_as_website
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blusmartmobility Domain Security
  slug: blusmartmobility-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blusmartmobility
tags:
- Mobility
- Ridesharing
- Electric Vehicles
- India
- Startups
website: https://equityzen.com/company/blusmartmobility
---
