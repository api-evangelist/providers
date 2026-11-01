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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/kaufland/hosts/kaufland-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kaufland-hosts.yml
- group: other
  href: https://artifacts.apis.io/kaufland/vendors/kaufland-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kaufland-vendors.yml
- group: auth
  href: https://artifacts.apis.io/kaufland/security/kaufland-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kaufland-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kaufland.de/
created: '2026-10-28'
description: Kaufland is a German hypermarket chain operating a large network of stores across Europe. It offers a wide range of groceries, household goods, and consumer products both in physical locations and via its online shopping platform. The company provides digital services such as product catalogs, store locators, and e‑commerce APIs for partners, though public API documentation is currently protected by security measures.
layout: provider
modified: '2026-10-28'
name: Kaufland
nav: Providers
network: true
overview: Kaufland is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Grocery, E‑commerce, and Europe.
random_paper: 22
scopes:
- name: Kaufland Scopes
  scope_count: 0
  slug: kaufland-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 17
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
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kaufland Authentication
  slug: kaufland-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kaufland Domain Security
  slug: kaufland-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kaufland
tags:
- Company
- Retail
- Grocery
- E‑commerce
- Europe
website: https://kaufland.de/
---
