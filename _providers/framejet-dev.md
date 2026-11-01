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
  href: https://artifacts.apis.io/framejet-dev/hosts/framejet-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/framejet-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/framejet-dev/vendors/framejet-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/framejet-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/framejet-dev/security/framejet-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/framejet-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://framejet.dev/
created: '2026-10-30'
description: Framejet.dev is a developer-focused platform offering a suite of APIs for creating, managing, and delivering dynamic video frames and overlays. It provides tools for real-time video personalization, analytics, and integration with popular streaming services. The company aims to simplify video content customization for marketers, developers, and media companies, enabling scalable and programmable visual experiences across web and mobile applications.
layout: provider
modified: '2026-10-30'
name: framejet-dev
nav: Providers
network: true
overview: framejet-dev is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Video, API, DeveloperTools, Personalization, and Streaming.
random_paper: 10
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 5
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
  name: Framejet Dev Domain Security
  slug: framejet-dev-domain-security
  summary_line: TLSv1.3 · DMARC
slug: framejet-dev
tags:
- Video
- API
- DeveloperTools
- Personalization
- Streaming
website: https://framejet.dev/
---
