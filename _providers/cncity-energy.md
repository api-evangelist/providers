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
  href: https://raw.githubusercontent.com/api-evangelist/cncity-energy/refs/heads/main/hosts/cncity-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cncity-energy-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cncity-energy/refs/heads/main/security/cncity-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cncity-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cncityenergy.com/
coverage:
  checked: '2026-10-09'
  detail: The company does not expose a public developer program or API documentation.
  evidence:
  - status: 403
    url: https://api.cncityenergy.com/
  reason: no-developer-program
  state: none
created: '2026-10-09'
description: CNCITY Energy Co., Ltd. is a South Korean integrated energy utility provider, delivering city gas, electricity, heat, and steam services to residential, commercial, and industrial customers in Daejeon and Gyeryong. Established in 1985, the company operates a 113 MW cogeneration plant and a district energy system, offering reliable and secure energy solutions across its service area.
layout: provider
modified: '2026-10-09'
name: CNCITY Energy
nav: Providers
network: true
overview: CNCITY Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Gas, Electricity, and DistrictHeating.
random_paper: 3
score:
  band: minimal
  composite: 3.2
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cncity Energy Domain Security
  slug: cncity-energy-domain-security
  summary_line: TLSv1.3
slug: cncity-energy
tags:
- Energy
- Utilities
- Gas
- Electricity
- DistrictHeating
- South Korea
website: https://www.cncityenergy.com/
---
