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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/buzzni/refs/heads/main/hosts/buzzni-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buzzni-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://buzzni.com/news
- group: company
  title: ''
  type: Blog
  url: https://buzzni.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buzzni
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/buzzni/refs/heads/main/security/buzzni-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buzzni-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buzzni.com
created: '2026-10-06'
description: Buzzni is a Korean AI-driven commerce technology company offering subscription-based AI solutions for e‑commerce, home‑shopping platforms, and digital marketing. It provides large‑scale product and review data, AI recommendation engines, and tools for video and image analysis, serving millions of users and partnering with major retailers.
image: https://thum.buzzni.com/unsafe/1280x0/https://buzzni-biz-strategy.s3-ap-northeast-1.amazonaws.com/cms/328/2022-05-16/d126521ddfea43d3967c8a2254c5e9b3.JPG
layout: provider
modified: '2026-10-06'
name: Buzzni
nav: Providers
network: true
overview: 'Buzzni is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Commerce, E-Commerce, and Data.


  Buzzni''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 4.7
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buzzni Domain Security
  slug: buzzni-domain-security
  summary_line: TLSv1.2 · DMARC
slug: buzzni
tags:
- Company
- Artificial Intelligence
- Commerce
- E-Commerce
- Data
website: https://buzzni.com
---
