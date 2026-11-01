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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/droneit/hosts/droneit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/droneit-hosts.yml
- group: other
  href: https://artifacts.apis.io/droneit/vendors/droneit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/droneit-vendors.yml
- group: auth
  href: https://artifacts.apis.io/droneit/security/droneit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/droneit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/droneit
created: '2026-10-24'
description: Droneit is a technology company that provides drone-based data collection and analytics services for various industries, including agriculture, construction, and environmental monitoring. The platform offers APIs for managing drone fleets, retrieving flight telemetry, accessing processed imagery, and integrating with third‑party GIS and data analysis tools. Droneit aims to simplify aerial data acquisition, enable real‑time insights, and support automated workflows for enterprise customers.
layout: provider
modified: '2026-10-24'
name: Droneit
nav: Providers
network: true
overview: Droneit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Drone, DataAnalytics, AerialImaging, and GIS.
random_paper: 13
score:
  band: minimal
  composite: 3.1
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
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Droneit Domain Security
  slug: droneit-domain-security
  summary_line: TLSv1.3 · DMARC
slug: droneit
tags:
- Company
- Drone
- DataAnalytics
- AerialImaging
- GIS
website: https://equityzen.com/company/droneit
---
