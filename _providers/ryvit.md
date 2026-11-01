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
  href: https://artifacts.apis.io/ryvit/hosts/ryvit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ryvit-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ryvit/security/ryvit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ryvit-domain-security.yml
created: '2026-10-21'
description: Ryvit provides a platform for managing and optimizing renewable energy assets, offering tools for data analytics, performance monitoring, and predictive maintenance. The company focuses on delivering scalable solutions to energy producers, enabling better operational efficiency and sustainability outcomes across solar, wind, and storage projects.
layout: provider
modified: '2026-10-21'
name: Ryvit
nav: Providers
network: true
overview: Ryvit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Renewable Energy, Asset Management, Data Analytics, and Predictive Maintenance.
random_paper: 22
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 8
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ryvit Domain Security
  slug: ryvit-domain-security
  summary_line: no transport/DNS hardening detected
slug: ryvit
tags:
- Company
- Renewable Energy
- Asset Management
- Data Analytics
- Predictive Maintenance
---
