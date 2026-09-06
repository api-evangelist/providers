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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1366-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cubicpv.com/
coverage:
  checked: '2026-09-05'
  detail: 1366 Technologies is a solar silicon wafer manufacturer that ceased to exist as an independent company when it merged into CubicPV in June 2021, and its own domain 1366tech.com has served a TLS certificate that expired on 2024-05-04 ever since, so there is no company web presence left to carry an API surface — the Website pointer now resolves to the surviving CubicPV host.
  evidence:
  - status: 0
    url: https://1366tech.com/
  - status: 202
    url: https://cubicpv.com/
  - status: 403
    url: https://forgeglobal.com/1366-technologies_stock/
  reason: defunct
  state: none
created: '2026-09-05'
description: '1366 Technologies was a Bedford, Massachusetts solar manufacturing company founded in 2008 out of MIT, best known for its patented Direct Wafer process — a kerfless method that casts multicrystalline silicon photovoltaic wafers directly from molten silicon in a mold, skipping the ingot-growing and wire-sawing steps that waste roughly half the silicon in conventional wafer production. The company raised venture funding from North Bridge Venture Partners, Polaris Partners, Hanwha, Tokuyama and Breakthrough Energy Ventures, and operated a demonstration line in Bedford. In June 2021 it merged with Dallas-based Hunt Perovskite Technologies to form CubicPV, combining Direct Wafer silicon with printed perovskite to pursue tandem modules; CubicPV cancelled its planned 10 GW US wafer factory in February 2024 and refocused on perovskite tandem development. 1366 Technologies is a materials and equipment manufacturer, not a software vendor: it never operated a developer program, public
  API, SDK or machine-readable API contract, and its own domain 1366tech.com has served an expired TLS certificate since May 2024.'
layout: provider
modified: '2026-09-05'
name: 1366 Technologies
nav: Providers
network: true
overview: 1366 Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar, Photovoltaics, Renewable Energy, and Manufacturing.
random_paper: 4
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
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 1366 Technologies Domain Security
  slug: 1366-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 1366-technologies
tags:
- Company
- Solar
- Photovoltaics
- Renewable Energy
- Manufacturing
- Semiconductors
- Materials Science
- Cleantech
website: https://cubicpv.com/
---
