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
  href: https://artifacts.apis.io/adiabatic-machines/hosts/adiabatic-machines-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adiabatic-machines-hosts.yml
- group: other
  href: https://artifacts.apis.io/adiabatic-machines/vendors/adiabatic-machines-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adiabatic-machines-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://adiabaticmachines.com/team/
- group: auth
  href: https://artifacts.apis.io/adiabatic-machines/security/adiabatic-machines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adiabatic-machines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adiabaticmachines.com/
coverage:
  checked: '2026-10-24'
  detail: The provider's documentation site is a JavaScript‑rendered Next.js application, preventing machine‑readable extraction of an API contract.
  evidence:
  - status: 200
    url: https://adiabaticmachines.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Adiabatic Machines builds computers for AI that replace conventional semiconductor GPUs with superconducting chips, cutting the power needed for AI inference by 10‑100×. Their technology leverages adiabatic quantum‑computing principles to deliver ultra‑low‑energy, high‑throughput processors for modern artificial‑intelligence workloads, targeting data‑center scale deployments and edge AI applications.
image: https://adiabaticmachines.com/chip-tweezers.jpg
layout: provider
modified: '2026-10-24'
name: Adiabatic Machines
nav: Providers
network: true
overview: Adiabatic Machines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Supercomputing, Quantum Computing, and Low Power.
random_paper: 23
score:
  band: minimal
  composite: 3.7
  coverage:
    artifact_dirs: 6
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
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adiabatic Machines Domain Security
  slug: adiabatic-machines-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adiabatic-machines
tags:
- Company
- AI
- Supercomputing
- Quantum Computing
- Low Power
website: https://adiabaticmachines.com/
---
