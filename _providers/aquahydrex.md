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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquahydrex/refs/heads/main/hosts/aquahydrex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aquahydrex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aquahydrex/refs/heads/main/vendors/aquahydrex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aquahydrex-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aquahydrex/refs/heads/main/security/aquahydrex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aquahydrex-domain-security.yml
coverage:
  checked: 2026-09-25
  detail: No API documentation or machine‑readable contract was found on AquaHydrex's site.
  evidence:
  - status: 200
    url: https://www.nasdaqprivatemarket.com/company/aquahydrex/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: AquaHydrex was a green-hydrogen technology company that developed a redesigned high-pressure alkaline water electrolysis system for large-scale hydrogen production. Founded in 2012 as a spin-out of the University of Wollongong and Monash University (ARC Centre of Excellence for Electromaterials Science), it opened its North American headquarters in Louisville, Colorado in 2015 and raised about $25 million, including a January 2023 round led by AP Ventures with Aramco Ventures. It filed for Chapter 7 bankruptcy in October 2023 (D. Colo. 1:23-bk-14706). It published no API. It was harvested from a Nasdaq Private Market listing, which an earlier pass mistook for the company and described as a liquidity and secondary-market platform.
layout: provider
modified: '2026-09-25'
name: AquaHydrex
nav: Providers
network: true
overview: AquaHydrex is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Hydrogen, Green Hydrogen, and Clean Energy.
random_paper: 6
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 3.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aquahydrex Domain Security
  slug: aquahydrex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aquahydrex
tags:
- Company
- Defunct
- Hydrogen
- Green Hydrogen
- Clean Energy
---
