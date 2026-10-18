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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/weibo/refs/heads/main/hosts/weibo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weibo-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/weibo/refs/heads/main/packages/weibo-packages.yml
  title: ''
  type: SDKs
  url: packages/weibo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/weibo/refs/heads/main/packages/weibo-packages.yml
  title: ''
  type: Packages
  url: packages/weibo-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weibo/refs/heads/main/security/weibo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weibo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weibo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.weibo.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://open.weibo.com
- group: docs
  title: ''
  type: APIReference
  url: https://open.weibo.com/wiki/API
coverage:
  checked: '2026-10-14'
  detail: API spec endpoints return 502 and the main site serves only a JavaScript shell, preventing machine-readable discovery.
  evidence:
  - status: 502
    url: https://api.weibo.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Weibo is a Chinese microblogging platform, often described as the Chinese equivalent of Twitter. It provides a social networking service where users can post, share, and interact with short messages, images, and videos. Weibo offers a range of data APIs for developers to access public posts, user profiles, trends, and analytics, supporting commercial and research use cases. The platform is operated by Sina Corporation and serves hundreds of millions of active users worldwide, making it a significant source of social media data.
layout: provider
modified: '2026-10-13'
name: Weibo
nav: Providers
network: true
overview: 'Weibo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media, Microblogging, and China.


  Weibo''s developer surface includes documentation, API reference, and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 35.7
    operational_transparency: 0.0
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
  name: Weibo Domain Security
  slug: weibo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weibo
tags:
- Company
- Social Media
- Microblogging
- China
website: https://weibo.com
---
