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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/opendata-barcelona/refs/heads/main/security/opendata-barcelona-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opendata-barcelona-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://opendata-ajuntament.barcelona.cat/
coverage:
  checked: 2026-09-21
  detail: OpenAPI endpoint returns a bot detection HTML page, preventing machine-readable spec.
  evidence:
  - status: 200
    url: https://opendata-ajuntament.barcelona.cat/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: Barcelona Open Data is the official open data portal of the Barcelona City Council, providing free access to a wide range of datasets covering transportation, environment, demographics, public services, and more. The platform enables developers, researchers, and citizens to discover, explore, and reuse municipal data through APIs and downloadable resources, fostering transparency, innovation, and data‑driven decision making across the city.
layout: provider
modified: '2026-09-21'
name: Barcelona Open Data
nav: Providers
network: true
overview: Barcelona Open Data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Data, Barcelona, Government, and Data Portal.
random_paper: 20
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 3
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
  previous_composite: 3.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Opendata Barcelona Domain Security
  slug: opendata-barcelona-domain-security
  summary_line: TLSv1.3 · DMARC
slug: opendata-barcelona
tags:
- Company
- Open Data
- Barcelona
- Government
- Data Portal
website: https://opendata-ajuntament.barcelona.cat/
---
