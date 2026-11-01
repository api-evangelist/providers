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
  href: https://artifacts.apis.io/cytesi/hosts/cytesi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cytesi-hosts.yml
- group: other
  href: https://artifacts.apis.io/cytesi/vendors/cytesi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cytesi-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cytesi/security/cytesi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cytesi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cytesi.com
coverage:
  checked: '2026-10-22'
  detail: No machine‑readable API specification (OpenAPI/AsyncAPI/GraphQL) was found on any discovered host.
  evidence:
  - status: 200
    url: https://www.cytesi.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: CyteSi Inc provides a software-defined wet‑lab platform that digitizes laboratory automation. Their Bio Processing Unit (BPU) replaces traditional robotics with a programmable interface, enabling high‑throughput workflows for NGS library preparation, drug discovery, and reagent synthesis. The platform offers AI‑ready lab‑in‑the‑loop capabilities, reducing reagent use by up to 75% and cutting processing time by over 50%, while scaling without additional hardware.
image: http://static1.squarespace.com/static/67d084ee6f07c23c50e5a8bd/t/6981a3e3735c06322e69b1fe/1770103779930/logo.png?format=1500w
layout: provider
modified: '2026-10-21'
name: CyteSi
nav: Providers
network: true
overview: CyteSi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Automation, Labware, Artificial Intelligence, and Software.
random_paper: 9
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cytesi Domain Security
  slug: cytesi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cytesi
tags:
- Biotechnology
- Automation
- Labware
- Artificial Intelligence
- Software
website: https://www.cytesi.com
---
