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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Vehicle computing API documented at the developer portal.
  name: Autolink API
  slug: autolink-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/autolink/refs/heads/main/well-known/autolink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autolink-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autolink/refs/heads/main/hosts/autolink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autolink-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.auto-link.com.cn/privacy_policy.html
- group: company
  title: ''
  type: Newsroom
  url: https://en.auto-link.com.cn/news/details_539_2712.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autolink/refs/heads/main/security/autolink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autolink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.auto-link.com.cn
- group: docs
  title: ''
  type: Documentation
  url: https://en.auto-link.com.cn/develop/index.html
coverage:
  checked: 2026-09-26
  detail: API spec at https://dev.auto-link.com.cn/openapi.json returns 401 token required.
  evidence:
  - status: 401
    url: https://dev.auto-link.com.cn/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-26'
description: Autolink, also known as Wuxi Autolink Intelligence Tech Co., Ltd, provides vehicle computing solutions integrating software and hardware for intelligent cockpits, ADAS, and zone controllers. The company offers a full-stack in‑house R&D platform, advanced manufacturing, and a collaborative ecosystem to support software‑defined vehicle architectures and smart mobility.
layout: provider
modified: '2026-09-26'
name: Autolink
nav: Providers
network: true
overview: 'Autolink publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Vehicle Computing, Intelligent Cockpit, and ADAS.


  Autolink''s developer surface includes documentation and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Autolink Domain Security
  slug: autolink-domain-security
  summary_line: TLSv1.3 · HSTS
slug: autolink
tags:
- Company
- Automotive
- Vehicle Computing
- Intelligent Cockpit
- ADAS
website: https://en.auto-link.com.cn
---
