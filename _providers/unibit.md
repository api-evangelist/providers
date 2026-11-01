---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/unibit/hosts/unibit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unibit-hosts.yml
- group: other
  href: https://artifacts.apis.io/unibit/vendors/unibit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unibit-vendors.yml
- group: auth
  href: https://artifacts.apis.io/unibit/security/unibit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unibit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unibit.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://unibit.ai/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: UniBit provides a unified platform for managing and integrating IoT devices, offering developers a comprehensive set of APIs to monitor, control, and analyze data from a wide range of smart hardware. The service includes real‑time telemetry, device provisioning, firmware updates, and analytics dashboards, enabling enterprises to build scalable, secure, and interoperable IoT solutions. UniBit’s APIs are designed with RESTful principles, detailed documentation, and robust authentication mechanisms, supporting both cloud and edge deployments for diverse industry use cases.
image: https://unibit.ai/static/img/facebook_share.png
layout: provider
modified: '2026-10-21'
name: UniBit
nav: Providers
network: true
overview: UniBit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Device Management, API Platform, and Cloud Services.
random_paper: 3
score:
  band: minimal
  composite: 3.4
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
    discoverability: 48.2
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
  name: Unibit Domain Security
  slug: unibit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: unibit
tags:
- Company
- IoT
- Device Management
- API Platform
- Cloud Services
- Analytics
website: https://unibit.ai/
---
