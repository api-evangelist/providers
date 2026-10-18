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
  href: https://raw.githubusercontent.com/api-evangelist/cleanrobotics/refs/heads/main/hosts/cleanrobotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleanrobotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cleanrobotics/refs/heads/main/vendors/cleanrobotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleanrobotics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://cleanrobotics.co.jp/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cleanrobotics/refs/heads/main/security/cleanrobotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleanrobotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleanrobotics.co.jp
coverage:
  checked: '2026-10-09'
  detail: No OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract found on discovered hosts.
  evidence:
  - status: 0
    url: https://api.co.jp/openapi.json
  - status: 404
    url: https://cleanrobotics.co.jp/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: CleanRobotics, Inc. (株式会社CleanRobotics) is a Tokyo‑based company founded in 2025 that applies AI and IoT to modernize energy infrastructure. Their platform combines physical sensors with cloud‑based analytics to enable predictive maintenance, real‑time optimization, and open‑grid management for power plants and renewable assets worldwide. The mission is to make energy infrastructure accessible, efficient, and environmentally sustainable through intelligent automation.
layout: provider
modified: '2026-10-08'
name: Cleanrobotics
nav: Providers
network: true
overview: Cleanrobotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Artificial Intelligence, IoT, and Infrastructure.
random_paper: 20
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleanrobotics Domain Security
  slug: cleanrobotics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cleanrobotics
tags:
- Company
- Energy
- Artificial Intelligence
- IoT
- Infrastructure
website: https://cleanrobotics.co.jp
---
