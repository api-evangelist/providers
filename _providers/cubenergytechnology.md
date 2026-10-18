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
  href: https://raw.githubusercontent.com/api-evangelist/cubenergytechnology/refs/heads/main/hosts/cubenergytechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cubenergytechnology-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cubenergy.com/about/privacy.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.cubenergy.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cubenergytechnology/refs/heads/main/security/cubenergytechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cubenergytechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cubenergy.com
coverage:
  checked: '2026-10-11'
  detail: No public developer documentation or API specifications were found on the company's website.
  evidence:
  - status: 200
    url: https://www.cubenergy.com
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Cubenergytechnology, operating as Cubenergy, is a global manufacturer of utility‑scale and commercial‑and‑industrial Battery Energy Storage Systems (BESS). The company designs, builds, and services integrated AC/DC storage solutions, offering products such as PowerCombo‑E5, FlexCombo‑D2, and FlexCube‑C1, along with a comprehensive BMS and O&M platform. With over 450 projects deployed across more than 40 countries, Cubenergy aims to accelerate the transition to reliable, affordable, and sustainable energy through advanced storage technology.
image: https://www.cubenergy.com/uploads/image/20240618/5318f747799636ef1e659da074a569bc.png
layout: provider
modified: '2026-10-11'
name: Cubenergytechnology
nav: Providers
network: true
overview: Cubenergytechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Battery Energy Storage, Utility Storage, Commercial Storage, BESS, and Energy Storage Systems.
random_paper: 2
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cubenergytechnology Domain Security
  slug: cubenergytechnology-domain-security
  summary_line: TLSv1.3
slug: cubenergytechnology
tags:
- Battery Energy Storage
- Utility Storage
- Commercial Storage
- BESS
- Energy Storage Systems
- Grid Resilience
website: https://www.cubenergy.com
---
