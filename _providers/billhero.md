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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billhero/refs/heads/main/llms/billhero-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/billhero-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billhero/refs/heads/main/hosts/billhero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billhero-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billhero/refs/heads/main/vendors/billhero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billhero-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billhero/refs/heads/main/security/billhero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billhero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://billhero.com.au
coverage:
  checked: '2026-09-28'
  detail: API host returns HTML pages for OpenAPI endpoints, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://api.com.au/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Billhero is an Australian energy‑bill management platform that helps households and small businesses understand, track, and reduce their utility costs. Through a suite of tools—including bill upload, usage analytics, and personalized energy‑coach advice—Billhero empowers users to avoid overpaying for electricity and gas, compare tariffs, and stay informed about industry changes. The service also offers a marketplace for energy‑saving products and a community forum for sharing tips.
layout: provider
modified: '2026-09-28'
name: Billhero
nav: Providers
network: true
overview: Billhero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Fintech, Software-as-a-Service, Australia, and Bill Management.
random_paper: 13
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 6
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
    discoverability: 51.8
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Billhero Domain Security
  slug: billhero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: billhero
tags:
- Energy
- Fintech
- Software-as-a-Service
- Australia
- Bill Management
website: https://billhero.com.au
---
