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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adbm-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adbmtech.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adbm-technologies-llc
coverage:
  checked: '2026-09-07'
  detail: adbmtech.com is a single-page marketing site (Home / Technology / Validation / About / Contact) for injection-molded HDPE Helmholtz-resonator noise abatement hardware that AdBm leases per offshore-wind pile-driving project; its only interactive element is a Formspree contact form, and no developer, API, data or documentation section exists anywhere on it or on any resolvable subdomain.
  evidence:
  - status: 200
    url: https://adbmtech.com/
  - status: 404
    url: https://adbmtech.com/openapi.json
  - status: 404
    url: https://adbmtech.com/llms.txt
  - status: 404
    url: https://adbmtech.com/.well-known/agent-card.json
  - status: 404
    url: https://www.adbmtech.com/graphql
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: AdBm Technologies is an Austin, Texas acoustical engineering company that designs and manufactures near-pile underwater noise mitigation systems for offshore wind construction. Its injection-molded HDPE Helmholtz resonators, mounted on an expandable steel framework and paired with an integrated bubble curtain, absorb and disperse the low-frequency sound energy generated during pile driving so contractors can meet underwater noise regulations while protecting marine life. The technology grew out of more than a decade of research at the University of Texas at Austin Applied Research Laboratories and has been deployed on offshore wind projects from the North Sea to the Atlantic coast of the United States. The company sells and leases hardware and project services; it publishes no public API, developer program, or machine-readable contract.
layout: provider
modified: '2026-09-07'
name: AdBm Technologies
nav: Providers
network: true
overview: AdBm Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Offshore Wind, Underwater Acoustics, Noise Mitigation, and Marine Construction.
random_paper: 11
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
  name: Adbm Technologies Domain Security
  slug: adbm-technologies-domain-security
  summary_line: TLSv1.2
slug: adbm-technologies
tags:
- Company
- Offshore Wind
- Underwater Acoustics
- Noise Mitigation
- Marine Construction
- Renewable Energy
- Hardware
website: https://adbmtech.com/
---
