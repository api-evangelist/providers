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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/tuio/llms/tuio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tuio-llms.txt
- group: other
  href: https://artifacts.apis.io/tuio/hosts/tuio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tuio-hosts.yml
- group: other
  href: https://artifacts.apis.io/tuio/vendors/tuio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tuio-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.tuio.com/hc/es
- group: auth
  href: https://artifacts.apis.io/tuio/security/tuio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tuio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://app.tuio.com/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://app.tuio.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://app.tuio.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.tuio.com/developer
- group: company
  title: ''
  type: Blog
  url: https://app.tuio.com/blog
created: '2026-10-24'
description: Tuio provides a cloud‑based platform that enables businesses to integrate real‑time location data and IoT device management into their applications. The service offers APIs for device onboarding, geofencing, event streaming, and analytics, helping clients build location‑aware solutions across logistics, retail, and smart‑city use cases. Tuio emphasizes security, scalability, and developer-friendly documentation, supporting RESTful endpoints and WebSocket streams for live data.
layout: provider
modified: '2026-10-24'
name: Tuio
nav: Providers
network: true
overview: 'Tuio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Real-time, Location, Device Management, and Cloud Platform.


  Tuio''s developer surface includes support, documentation, pricing, engineering blog, and 6 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 44.6
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
  name: Tuio Domain Security
  slug: tuio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tuio
tags:
- IoT
- Real-time
- Location
- Device Management
- Cloud Platform
- Company
website: https://app.tuio.com/welcome
---
