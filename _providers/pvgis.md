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
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: API for PVGIS providing solar radiation and photovoltaic performance data
  name: PVGIS API
  slug: pvgis-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pvgis/refs/heads/main/hosts/pvgis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pvgis-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pvgis/refs/heads/main/security/pvgis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pvgis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://re.jrc.ec.europa.eu/pvg_tools/en/
coverage:
  checked: 2026-09-23
  detail: PVGIS documentation page is a JavaScript-heavy web app with no machine‑readable OpenAPI/GraphQL spec discovered.
  evidence:
  - status: 200
    url: https://re.jrc.ec.europa.eu/pvg_tools/en/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: PVGIS (Photovoltaic Geographical Information System) is a European Commission service providing free access to solar radiation and photovoltaic performance data worldwide. Users can input location, system parameters, and retrieve hourly, daily, monthly, and yearly solar irradiation, PV output, and performance metrics in various formats (CSV, JSON, PDF). The platform supports multiple PV technologies, mounting options, and includes tools for horizon and temperature data, aiding researchers, engineers, and policymakers in renewable energy planning and analysis.
layout: provider
modified: '2026-09-23'
name: PVGIS
nav: Providers
network: true
overview: PVGIS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Solar, Renewables, Data, and European Commission.
random_paper: 3
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 3.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pvgis Domain Security
  slug: pvgis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: pvgis
tags:
- Energy
- Solar
- Renewables
- Data
- European Commission
website: https://re.jrc.ec.europa.eu/pvg_tools/en/
---
