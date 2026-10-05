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
  href: https://raw.githubusercontent.com/api-evangelist/bmfprecision/refs/heads/main/hosts/bmfprecision-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bmfprecision-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.bmftec3d.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bmfprecision/refs/heads/main/security/bmfprecision-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmfprecision-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bmftec3d.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bmfprecision
  reason: no-developer-program
  state: none
created: '2026-09-29'
description: Bmfprecision (BMF Precision Tech Inc.) is a leading manufacturer of micro‑precision 3D printers and advanced additive manufacturing solutions. Founded in 2016, the company specializes in Projection Micro‑Stereolithography (PµSL) technology, offering a range of high‑resolution printers, materials, and services for sectors such as precision electronics, medical devices, microfluidics, and biomedicine. The website provides product details, technical resources, case studies, and contact information for customers worldwide.
layout: provider
modified: '2026-09-29'
name: Bmfprecision
nav: Providers
network: true
overview: Bmfprecision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Printing, Additive Manufacturing, Precision Electronics, Medical Devices, and Microfluidics.
random_paper: 5
score:
  band: minimal
  composite: 3.5
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
    discoverability: 46.4
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bmfprecision Domain Security
  slug: bmfprecision-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bmfprecision
tags:
- 3D Printing
- Additive Manufacturing
- Precision Electronics
- Medical Devices
- Microfluidics
- Materials
- Custom Manufacturing
website: https://www.bmftec3d.com
---
