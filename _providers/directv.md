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
- group: agent
  href: https://artifacts.apis.io/directv/llms/directv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/directv-llms.txt
- group: other
  href: https://artifacts.apis.io/directv/hosts/directv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/directv-hosts.yml
- group: other
  href: https://artifacts.apis.io/directv/vendors/directv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/directv-vendors.yml
- group: auth
  href: https://artifacts.apis.io/directv/security/directv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/directv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://directv.com/
created: '2026-10-28'
description: DirecTV is a satellite television service provider offering subscription-based direct broadcast satellite (DBS) television and streaming services. It delivers a range of programming, including live TV, on-demand movies, and exclusive sports packages, primarily in the United States. The company operates under the AT&T brand and provides both traditional satellite receivers and internet-based streaming platforms for its customers. DirecTV also offers bundled services with internet and phone, and maintains a network of retail locations and customer support channels.
image: https://upload.wikimedia.org/wikipedia/commons/5/5c/DirecTV_logo.svg
layout: provider
modified: '2026-10-28'
name: DirecTV
nav: Providers
network: true
overview: DirecTV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Satellite, Television, Media, Entertainment, and Streaming.
random_paper: 9
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
  name: Directv Domain Security
  slug: directv-domain-security
  summary_line: TLSv1.3 · DMARC
slug: directv
tags:
- Satellite
- Television
- Media
- Entertainment
- Streaming
website: https://directv.com/
---
