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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/battlemotors/refs/heads/main/llms/battlemotors-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/battlemotors-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/battlemotors/refs/heads/main/hosts/battlemotors-hosts.yml
  title: ''
  type: Hosts
  url: hosts/battlemotors-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/battlemotors/refs/heads/main/vendors/battlemotors-vendors.yml
  title: ''
  type: Vendors
  url: vendors/battlemotors-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://battlemotors.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/battlemotors/refs/heads/main/security/battlemotors-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/battlemotors-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://battlemotors.com
coverage:
  checked: '2026-09-27'
  detail: No machine‑readable API specification was found on the provider's hosts or documentation pages.
  evidence:
  - status: 404
    url: https://api.battlemotors.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Battlemotors designs and manufactures vocational and refuse trucks, offering custom‑engineered platforms for waste collection, delivery, and specialized industrial applications. Their products emphasize durability, uptime, and integrated technology such as the Fortris Control Hub for fleet management and safety. Battlemotors serves a nationwide distribution network with parts support and service, targeting sectors like recycling, infrastructure, agriculture, and oil & gas.
image: https://battlemotors.com/images/logo.png
layout: provider
modified: '2026-09-27'
name: Battlemotors
nav: Providers
network: true
overview: Battlemotors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Trucks, Manufacturing, Vocational Vehicles, and Fleet Management.
random_paper: 14
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
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
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Battlemotors Domain Security
  slug: battlemotors-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: battlemotors
tags:
- Company
- Trucks
- Manufacturing
- Vocational Vehicles
- Fleet Management
website: https://battlemotors.com
---
