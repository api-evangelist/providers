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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/branchtechnology/refs/heads/main/hosts/branchtechnology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branchtechnology-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://branchtechnology.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/branchtechnology/refs/heads/main/security/branchtechnology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branchtechnology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branchtechnology.com
- group: docs
  title: ''
  type: Documentation
  url: https://branchtechnology.com/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://branchtechnology.com/policy/
coverage:
  checked: '2026-10-03'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on api.branchtechnology.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.branchtechnology.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-03'
description: Branchtechnology is a 3D printing construction technology company founded in 2014, specializing in freeform large‑scale additive manufacturing for building facades and off‑world structures. It combines industrial robotics, digital design, and patented processes to create sustainable, efficient construction solutions, offering products, approach, portfolio, and services for architects, developers, and space‑industry partners.
layout: provider
modified: '2026-10-03'
name: Branchtechnology
nav: Providers
network: true
overview: 'Branchtechnology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Construction Tech, Additive Manufacturing, and SpaceIndustry.


  Branchtechnology''s developer surface includes documentation and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 7.8
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
    developer_ergonomics: 9.5
    discoverability: 46.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Branchtechnology Domain Security
  slug: branchtechnology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: branchtechnology
tags:
- Company
- 3D Printing
- Construction Tech
- Additive Manufacturing
- SpaceIndustry
website: https://branchtechnology.com
---
