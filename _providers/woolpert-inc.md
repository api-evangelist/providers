---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/woolpert-inc/well-known/woolpert-inc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/woolpert-inc-well-known.yml
- group: other
  href: https://artifacts.apis.io/woolpert-inc/hosts/woolpert-inc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/woolpert-inc-hosts.yml
- group: other
  href: https://artifacts.apis.io/woolpert-inc/vendors/woolpert-inc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/woolpert-inc-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://woolpert.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://woolpert.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://woolpert.com/about/leadership/
- group: company
  title: ''
  type: Blog
  url: https://woolpert.com/blog/port-tampa-bay/
- group: auth
  href: https://artifacts.apis.io/woolpert-inc/security/woolpert-inc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/woolpert-inc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://woolpert.com/
coverage:
  checked: '2026-10-23'
  detail: The website serves HTML shells for attempted OpenAPI URLs, no machine‑readable spec found.
  evidence:
  - status: 404
    url: https://woolpert.com/openapi.json
  - status: 200 (HTML shell)
    url: https://woolpert.com/.well-known/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Woolpert, Inc. is a multidisciplinary architecture, engineering, and geospatial services firm delivering innovative solutions across sectors such as aviation, defense, healthcare, and infrastructure. The company provides planning, consulting, data and technology services, and integrates advanced design and geospatial analytics to support clients worldwide. Woolpert’s expertise spans architecture, engineering, geospatial, data technology, and project delivery, emphasizing sustainability and cutting‑edge technology.
image: https://woolpert.com/wp-content/uploads/2026/01/DefaultFeature.jpg
layout: provider
modified: '2026-10-23'
name: Woolpert, Inc.
nav: Providers
network: true
overview: 'Woolpert, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, Engineering, Geospatial, Consulting, and Infrastructure.


  Woolpert, Inc.''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Woolpert Inc Domain Security
  slug: woolpert-inc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: woolpert-inc
tags:
- Architecture
- Engineering
- Geospatial
- Consulting
- Infrastructure
website: https://woolpert.com/
---
