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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://ya.cc/t/1cSZixjB3gkSva
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yandex-music/refs/heads/main/well-known/yandex-music-yandex-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yandex-music-yandex-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/yandex-music/refs/heads/main/well-known/yandex-music-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yandex-music-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/yandex-music/refs/heads/main/hosts/yandex-music-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yandex-music-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yandex-music/refs/heads/main/packages/yandex-music-packages.yml
  title: ''
  type: SDKs
  url: packages/yandex-music-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/yandex-music/refs/heads/main/packages/yandex-music-packages.yml
  title: ''
  type: Packages
  url: packages/yandex-music-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://yandex.ru/company/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yandex-music/refs/heads/main/security/yandex-music-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yandex-music-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/yandex-music/refs/heads/main/security/yandex-music-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yandex-music-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://music.yandex.ru/
- group: docs
  title: ''
  type: Documentation
  url: https://yandex.ru/support/music/ru/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://yandex.ru/support/music/ru/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://yandex.ru/support/music/ru/
coverage:
  checked: 2026-09-23
  detail: Music.yandex.ru returns a JavaScript shell and no machine‑readable OpenAPI spec was found despite probing common spec URLs.
  evidence:
  - status: 200
    url: https://music.yandex.ru/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Yandex Music is a Russian online music streaming service offering a vast catalog of songs, albums, playlists, and podcasts. Users can listen to music on-demand, create personal playlists, and discover new content through personalized recommendations. The platform provides both free ad‑supported and subscription‑based tiers, supporting multiple devices including web, mobile apps, and smart speakers. Yandex Music integrates with Yandex’s broader ecosystem, offering seamless access via Yandex ID and supporting social sharing features.
image: https://music.yandex.ru/pages/main/i/og/home.png?webp=false
layout: provider
modified: '2026-09-23'
name: Yandex Music
nav: Providers
network: true
overview: 'Yandex Music is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Streaming, Russian, and Entertainment.


  Yandex Music''s developer surface includes documentation, support, and 11 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 40.7
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yandex Music Domain Security
  slug: yandex-music-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yandex Music Vulnerability Disclosure
  slug: yandex-music-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yandex-music
tags:
- Music
- Streaming
- Russian
- Entertainment
website: https://music.yandex.ru/
---
