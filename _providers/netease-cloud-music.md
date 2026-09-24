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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/netease-cloud-music/refs/heads/main/well-known/netease-cloud-music-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netease-cloud-music-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/netease-cloud-music/refs/heads/main/hosts/netease-cloud-music-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netease-cloud-music-hosts.yml
- group: operate
  title: ''
  type: Support
  url: http://help.mail.163.com/service.html
- group: start
  title: ''
  type: Login
  url: https://music.163.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.163.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/netease-cloud-music/refs/heads/main/security/netease-cloud-music-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netease-cloud-music-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://music.163.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.music.163.com/st/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.music.163.com/st/developer/document
- group: commercial
  title: ''
  type: TermsOfService
  url: https://st.music.163.com/official-terms/service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://st.music.163.com/official-terms/privacy
- group: commercial
  title: ''
  type: ChildrenPrivacyPolicy
  url: https://st.music.163.com/official-terms/children
created: '2026-09-23'
description: NetEase Cloud Music (网易云音乐) is a leading Chinese music streaming service offering a vast library of songs, playlists, podcasts, and user‑generated content. Users can discover music, create personal playlists, follow artists, and access high‑quality audio via web and mobile apps. The platform provides APIs for searching tracks, retrieving album details, managing user libraries, and streaming content, serving both consumer and developer ecosystems.
image: http://p3.music.126.net/tBTNafgjNnTL1KlZMt7lVA==/18885211718935735.jpg
layout: provider
modified: '2026-09-23'
name: NetEase Cloud Music
nav: Providers
network: true
overview: 'NetEase Cloud Music is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Streaming, and Chinese.


  NetEase Cloud Music''s developer surface includes support, engineering blog, documentation, and 9 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 40.7
    operational_transparency: 0.0
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
  name: Netease Cloud Music Domain Security
  slug: netease-cloud-music-domain-security
  summary_line: TLSv1.3 · DMARC
slug: netease-cloud-music
tags:
- Company
- Music
- Streaming
- Chinese
website: https://music.163.com/
---
