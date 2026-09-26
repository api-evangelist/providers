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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Tencent Docs for QQ Music API
  name: QQ Music API
  slug: qq-music-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qq-music/refs/heads/main/llms/qq-music-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qq-music-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qq-music/refs/heads/main/well-known/qq-music-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qq-music-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qq-music/refs/heads/main/hosts/qq-music-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qq-music-hosts.yml
- group: start
  title: ''
  type: Sandbox
  url: https://sj.qq.com/tag/sandbox
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.qq.com/mb/policy/tencent-privacypolicy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qq-music/refs/heads/main/security/qq-music-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qq-music-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://y.qq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.qq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open.qq.com/
- group: operate
  title: ''
  type: Support
  url: https://support.qq.com/product/35224
coverage:
  checked: 2026-09-23
  detail: Docs at https://docs.qq.com/ are a JavaScript‑rendered SPA, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://docs.qq.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: QQ Music (QQ音乐) is a leading Chinese online music streaming service operated by Tencent. It offers a massive catalog of high‑quality, lossless tracks, personalized playlists, and social sharing features. Users can stream, download, and enjoy curated recommendations across web and mobile platforms, making it a central hub for music entertainment in China.
layout: provider
modified: '2026-09-23'
name: QQ Music
nav: Providers
network: true
overview: 'QQ Music publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Streaming, Tencent, and China.


  QQ Music''s developer surface includes sandbox, documentation, support, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 60.7
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 14.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Qq Music Domain Security
  slug: qq-music-domain-security
  summary_line: TLSv1.3 · DMARC
slug: qq-music
tags:
- Company
- Music
- Streaming
- Tencent
- China
- Entertainment
website: https://y.qq.com/
---
