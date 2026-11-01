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
  href: https://artifacts.apis.io/dendra/hosts/dendra-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dendra-hosts.yml
- group: other
  href: https://artifacts.apis.io/dendra/vendors/dendra-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dendra-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dendra/security/dendra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dendra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/dendra
coverage:
  checked: '2026-10-23'
  detail: No public machine‑readable API specification could be found; attempts to fetch the company site and docs returned DNS errors.
  evidence:
  - status: DNS error
    url: https://dendra.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Dendra Systems is a UK‑based environmental technology company that provides an AI‑powered platform for ecosystem restoration, carbon accounting, and climate‑impact monitoring. Founded in 2014, it helps organizations measure, manage, and restore natural habitats through data‑driven tools and services, supporting sustainability initiatives and regulatory compliance across multiple sectors.
layout: provider
modified: '2026-10-22'
name: Dendra
nav: Providers
network: true
overview: Dendra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Environment, Climate Tech, Artificial Intelligence, EcosystemRestoration, and Sustainability.
random_paper: 22
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 4
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
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dendra Domain Security
  slug: dendra-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dendra
tags:
- Environment
- Climate Tech
- Artificial Intelligence
- EcosystemRestoration
- Sustainability
website: https://equityzen.com/company/dendra
---
