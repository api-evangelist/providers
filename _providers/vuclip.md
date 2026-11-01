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
  href: https://artifacts.apis.io/vuclip/hosts/vuclip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vuclip-hosts.yml
- group: other
  href: https://artifacts.apis.io/vuclip/vendors/vuclip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vuclip-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.pccw.com/PCCWCorpsite/media-centre/news/index.page?
- group: other
  title: ''
  type: Leadership
  url: https://www.pccw.com/PCCWCorpsite/about-us/leadership/board-of-directors.page?
- group: auth
  href: https://artifacts.apis.io/vuclip/security/vuclip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vuclip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vuclip.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.vuclip.com/mcp
  - status: 200
    url: https://www.vuclip.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Vuclip is a mobile video on demand (VOD) service targeting emerging markets. Founded in July 2008 and headquartered in Milpitas, California, it operates in India, Indonesia, Malaysia, Thailand, Egypt, United Arab Emirates and other regions. The company provides a searchable library of short-form video content optimized for low‑bandwidth devices, delivering millions of video streams per quarter. Vuclip was acquired by PCCW Media in 2015 and continues to expand its catalog and distribution partnerships across Asia and the Middle East.
image: http://www.pccw.com/assets/PCCW Corporate Website/img/ourbusiness/pccw_logo_en.svg
layout: provider
modified: '2026-10-22'
name: Vuclip
nav: Providers
network: true
overview: Vuclip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Video-on-Demand, Emerging-Market, Mobile, and Streaming.
random_paper: 11
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 5
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
    discoverability: 51.8
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
  name: Vuclip Domain Security
  slug: vuclip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vuclip
tags:
- Company
- Video-on-Demand
- Emerging-Market
- Mobile
- Streaming
website: https://www.vuclip.com/
---
