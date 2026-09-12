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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advanced-ionics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://advanced-ionics.com/
coverage:
  checked: '2026-09-07'
  detail: Advanced Ionics manufactures Symbion water-vapor electrolyzers as physical industrial hardware, and certificate-transparency logs show only the apex domain advanced-ionics.com has ever been issued a certificate — no api, docs, developer or portal host has ever existed — with no GitHub organization and no package in any public registry to accompany one.
  evidence:
  - status: 200
    url: https://crt.sh/?q=%25.advanced-ionics.com&output=json
  - status: 404
    url: https://api.github.com/orgs/advanced-ionics
  - status: 202
    url: https://advanced-ionics.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: Advanced Ionics is a Milwaukee, Wisconsin based clean-energy hardware company developing the Symbion water-vapor electrolyzer, a green hydrogen production technology that uses process and waste heat together with low-cost renewable or nuclear electricity to cut the energy needed per kilogram of hydrogen to roughly 35 kWh, well below the 50-plus kWh required by conventional commercial electrolyzers. Founded in 2017 and relocated to Milwaukee in 2018, the company targets decarbonization of heavy industry — steel, ammonia, refining and other hydrogen-intensive sectors — and has run pilot and demonstration projects with Shell through its GameChanger program and with the Entrepreneurs Fund of the Repsol Foundation, and signed a collaboration MOU with ACWA Power. Advanced Ionics manufactures electrolyzer hardware; it does not operate a public developer program, and no public API, SDK, or machine-readable specification was found.
layout: provider
modified: '2026-09-07'
name: Advanced Ionics
nav: Providers
network: true
overview: Advanced Ionics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Hydrogen, Clean Energy, and Electrolyzer.
random_paper: 0
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advanced Ionics Domain Security
  slug: advanced-ionics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: advanced-ionics
tags:
- Company
- Energy
- Hydrogen
- Clean Energy
- Electrolyzer
- Manufacturing
- Industrial
- Hardware
- Climate Tech
website: https://advanced-ionics.com/
---
