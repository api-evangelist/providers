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
api_count: 1
apis:
- description: Bwsensing provides sensor data integration APIs, but no machine‑readable contract was discovered.
  name: Bwsensing API
  slug: bwsensing-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bwsensing/refs/heads/main/hosts/bwsensing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bwsensing-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bwsensing/refs/heads/main/security/bwsensing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bwsensing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bwsensing.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.bwsensing.com/download.html
- group: operate
  title: ''
  type: Support
  url: https://www.bwsensing.com/faq.html
- group: company
  title: ''
  type: About
  url: https://www.bwsensing.com/aboutus.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bwsensing.com/privacy-policy.html
coverage:
  checked: '2026-10-06'
  detail: Documentation pages exist but no OpenAPI/AsyncAPI/GraphQL spec was found on any host.
  evidence:
  - status: 200
    url: https://www.bwsensing.com/download.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Bwsensing designs and manufactures high‑precision inertial measurement sensors, inclinometers, IMUs, and related solutions for industries such as construction, energy, transportation, and medical devices. Their products enable accurate orientation, motion tracking, and structural health monitoring, supporting smart infrastructure and autonomous systems. The company emphasizes advanced sensor technology, robust data analytics, and integration with IoT platforms to deliver reliable, real‑time insights for critical applications.
layout: provider
modified: '2026-10-06'
name: Bwsensing
nav: Providers
network: true
overview: 'Bwsensing is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sensor, Inertial Measurement, IoT, Industrial, and Construction.


  Bwsensing''s developer surface includes documentation, support, and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bwsensing Domain Security
  slug: bwsensing-domain-security
  summary_line: TLSv1.2
slug: bwsensing
tags:
- Sensor
- Inertial Measurement
- IoT
- Industrial
- Construction
website: https://www.bwsensing.com
---
