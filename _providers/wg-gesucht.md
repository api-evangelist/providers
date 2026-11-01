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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/wg-gesucht/hosts/wg-gesucht-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wg-gesucht-hosts.yml
- group: auth
  href: https://artifacts.apis.io/wg-gesucht/security/wg-gesucht-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wg-gesucht-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wg-gesucht.de/
coverage:
  checked: '2026-10-28'
  detail: No public API documentation or machine‑readable contract was found for WG‑Gesucht.
  evidence:
  - status: 301
    url: https://api.wg-gesucht.de/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: WG-Gesucht is Germany’s leading online marketplace for shared flat (WG) rooms and apartments. It connects renters and landlords, offering a comprehensive platform with listings, search filters, and services such as credit checks, legal advice, and moving assistance. Users can browse available rooms, post ads, and access tools for tenancy agreements, making the search for suitable housing faster and more transparent across the country.
image: https://www.wg-gesucht.de/img/preview/wg-gesucht-7.jpg
layout: provider
modified: '2026-10-28'
name: WG-Gesucht
nav: Providers
network: true
overview: WG-Gesucht is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Housing, Marketplace, Germany, Rentals, and SharedFlat.
random_paper: 14
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wg Gesucht Domain Security
  slug: wg-gesucht-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wg-gesucht
tags:
- Housing
- Marketplace
- Germany
- Rentals
- SharedFlat
website: https://wg-gesucht.de/
---
