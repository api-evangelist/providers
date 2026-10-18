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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Chinese mobile karaoke platform API (no public spec discovered)
  name: Changba API
  slug: changba-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/changba/refs/heads/main/hosts/changba-hosts.yml
  title: ''
  type: Hosts
  url: hosts/changba-hosts.yml
- group: operate
  title: ''
  type: Support
  url: http://changba.com/now/help/helpcenter.php?typeid=1
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/changba/refs/heads/main/security/changba-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/changba-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://changba.com
coverage:
  checked: '2026-10-08'
  detail: The main site returns a JavaScript shell and no machine‑readable API documentation was found.
  evidence:
  - status: 200
    url: https://changba.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-08'
description: Changba (唱吧) is a Chinese mobile karaoke platform offering a large community for singing, sharing performances, and discovering music. The service provides a mobile app across iOS, Android, and Windows Phone, featuring millions of high‑quality backing tracks, user‑generated recordings, live streaming, and social interaction. It operates under Beijing CoolTech Technology Co., Ltd., with a focus on music entertainment and user‑generated content, and maintains a comprehensive website changba.com that showcases its features, licensing, and corporate information.
layout: provider
modified: '2026-10-08'
name: Changba
nav: Providers
network: true
overview: 'Changba is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Karaoke, Mobile App, Community, and Entertainment.


  Changba''s developer surface includes support and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 4.9
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
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Changba Domain Security
  slug: changba-domain-security
  summary_line: TLSv1.2
slug: changba
tags:
- Music
- Karaoke
- Mobile App
- Community
- Entertainment
website: https://changba.com
---
