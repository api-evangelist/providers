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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/globalfoundries/refs/heads/main/well-known/globalfoundries-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/globalfoundries-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/globalfoundries/refs/heads/main/hosts/globalfoundries-hosts.yml
  title: ''
  type: Hosts
  url: hosts/globalfoundries-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/globalfoundries/refs/heads/main/vendors/globalfoundries-vendors.yml
  title: ''
  type: Vendors
  url: vendors/globalfoundries-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gf.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gf.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://gf.com/news-and-events/news/
- group: other
  title: ''
  type: Leadership
  url: https://gf.com/about-gf/leadership/
- group: company
  title: ''
  type: Blog
  url: https://gf.com/news-and-events/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/globalfoundries/refs/heads/main/security/globalfoundries-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/globalfoundries-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gf.com
created: '2026-10-13'
description: GlobalFoundries is a leading semiconductor foundry providing advanced manufacturing services for a wide range of technologies, including high-performance, power-efficient, and feature-rich solutions. The company serves diverse markets such as aerospace, automotive, data center, IoT, and mobile devices, offering technologies like FinFET, FD-SOI, advanced packaging, and quantum solutions. GlobalFoundries operates multiple fabs worldwide, supporting customers from design to production.
image: https://assets.gf.com/image/328833518282/image_huvicqfe4h30f9n8eu8dci4f2v/-B1920-FWEBP
layout: provider
modified: '2026-10-13'
name: GlobalFoundries
nav: Providers
network: true
overview: 'GlobalFoundries is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Foundry, Manufacturing, and Technology.


  GlobalFoundries'' developer surface includes engineering blog and 9 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 51.8
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Globalfoundries Domain Security
  slug: globalfoundries-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: globalfoundries
tags:
- Company
- Semiconductors
- Foundry
- Manufacturing
- Technology
website: https://gf.com
---
