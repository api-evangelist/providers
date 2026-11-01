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
  href: https://artifacts.apis.io/swarm-aero/hosts/swarm-aero-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swarm-aero-hosts.yml
- group: other
  href: https://artifacts.apis.io/swarm-aero/vendors/swarm-aero-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swarm-aero-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.swarm.aero/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.swarm.aero/news
- group: auth
  href: https://artifacts.apis.io/swarm-aero/security/swarm-aero-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swarm-aero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.swarm.aero/
coverage:
  checked: '2026-10-22'
  detail: No machine‑readable API specification found on the website.
  evidence:
  - status: 200
    url: https://www.swarm.aero/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: 'Swarm Aero is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by coatue) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.prod.website-files.com/6670a5ab5768bd53190746a5/66ab002fe2d654e95199f8d6_image-globe.png
layout: provider
modified: '2026-10-22'
name: Swarm Aero
nav: Providers
network: true
overview: Swarm Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Long‑Range Strike, Defense, C2 Autonomy, Modular Payload, and Mass Production.
random_paper: 14
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Swarm Aero Domain Security
  slug: swarm-aero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swarm-aero
tags:
- Long‑Range Strike
- Defense
- C2 Autonomy
- Modular Payload
- Mass Production
website: https://www.swarm.aero/
---
