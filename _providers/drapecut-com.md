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
- description: API for DrapeCut composite draping service
  name: DrapeCut API
  slug: drapecut-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/drapecut-com/conformance/drapecut-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drapecut-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/drapecut-com/hosts/drapecut-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drapecut-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/drapecut-com/vendors/drapecut-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drapecut-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/drapecut-com/security/drapecut-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drapecut-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drapecut.com/
- group: docs
  title: ''
  type: Documentation
  url: https://drapecut.com/docs/mcp
created: '2026-11-05'
description: DrapeCut offers a browser‑based composite draping tool that lets users upload STEP or STL files and simulate woven carbon, glass or aramid cloth draping over complex curves. The free‑while‑in‑beta service provides shear map visualisation, locking angle analysis, and exports flat cutting patterns as DXF files. It targets engineers needing accurate fabric layup simulations for manufacturing and design.
image: https://drapecut.com/static/og-image.png
layout: provider
modified: '2026-11-05'
name: DrapeCut
nav: Providers
network: true
overview: 'DrapeCut is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Engineering, Simulation, Composite, Fabric, and DXF.


  DrapeCut''s developer surface includes documentation and 5 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Drapecut Com Domain Security
  slug: drapecut-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: drapecut-com
tags:
- Engineering
- Simulation
- Composite
- Fabric
- DXF
website: https://drapecut.com/
---
