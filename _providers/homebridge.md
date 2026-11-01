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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Plugin developer documentation and API reference for Homebridge.
  name: Homebridge Plugin API
  slug: homebridge-plugin-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/homebridge/hosts/homebridge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/homebridge-hosts.yml
- group: other
  href: https://artifacts.apis.io/homebridge/vendors/homebridge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/homebridge-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.homebridge.io/
- group: auth
  href: https://artifacts.apis.io/homebridge/security/homebridge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/homebridge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://homebridge.io/
coverage:
  checked: '2026-10-28'
  detail: The developer documentation is HTML only and provides no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://developers.homebridge.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Homebridge is an open-source platform that enables you to integrate non‑Apple devices with Apple HomeKit, allowing users to control a wide range of smart home accessories through Siri, the Home app, or automations. It acts as a lightweight Node.js server that bridges various plugins to expose devices as HomeKit accessories, supporting extensive customization and community‑driven extensions.
layout: provider
modified: '2026-10-28'
name: Homebridge
nav: Providers
network: true
overview: 'Homebridge is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Home Automation, Smart Home, Open Source, Node.js, and HomeKit Integration.


  Homebridge''s developer surface includes documentation and 4 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
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
  name: Homebridge Domain Security
  slug: homebridge-domain-security
  summary_line: TLSv1.3 · DMARC
slug: homebridge
tags:
- Home Automation
- Smart Home
- Open Source
- Node.js
- HomeKit Integration
- Community
website: https://homebridge.io/
---
