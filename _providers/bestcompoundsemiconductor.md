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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bestcompoundsemiconductor/refs/heads/main/hosts/bestcompoundsemiconductor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestcompoundsemiconductor-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bestcompoundsemiconductor/refs/heads/main/security/bestcompoundsemiconductor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestcompoundsemiconductor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.bestcompsemi.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bestcompoundsemiconductor
  reason: no-developer-program
  state: none
created: '2026-09-27'
description: Best Compound Semiconductor Co., Ltd. provides high‑quality manufacturing of SiC/SiC and GaN/Si epitaxy wafers, targeting high‑voltage and high‑power applications. Founded in 2019 and based in Nanjing, China, the company aims to be a global leader in wide‑bandgap semiconductor wafer services, offering custom solutions for device foundries and specialized customers.
layout: provider
modified: '2026-09-27'
name: Bestcompoundsemiconductor
nav: Providers
network: true
overview: Bestcompoundsemiconductor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Manufacturing, WideBandgap, and China.
random_paper: 0
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 5
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
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestcompoundsemiconductor Domain Security
  slug: bestcompoundsemiconductor-domain-security
  summary_line: no transport/DNS hardening detected
slug: bestcompoundsemiconductor
tags:
- Company
- Semiconductors
- Manufacturing
- WideBandgap
- China
website: http://www.bestcompsemi.com
---
