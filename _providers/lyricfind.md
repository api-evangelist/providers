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
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Newsroom
  url: https://www.lyricfind.com/press
- group: start
  title: ''
  type: Login
  url: https://dashboard.lyricfind.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lyricfind/refs/heads/main/security/lyricfind-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lyricfind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lyricfind.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.lyricfind.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lyricfind.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lyricfind.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lyricfind.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.lyricfind.com/contact
coverage:
  checked: 2026-09-21
  detail: Documentation at https://docs.lyricfind.com/ returns 404 for common OpenAPI spec URLs.
  evidence:
  - status: 404
    url: https://docs.lyricfind.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-21'
description: LyricFind provides licensed lyrics and music‑related data services to businesses worldwide. Through its robust API platform, developers can integrate lyric search, display, translation, and licensing capabilities into applications across industries such as streaming, automotive, health & fitness, and retail. The company offers comprehensive data licensing, compliance tools, and analytics to ensure lawful use of copyrighted lyrics, supporting partners from major record labels to independent artists.
image: http://static1.squarespace.com/static/5f972a7c930e1b7910954135/t/67880a60a697a603507d0fa1/1736968801003/SocialShareImage_Generic.jpg?format=1500w
layout: provider
modified: '2026-09-21'
name: LyricFind
nav: Providers
network: true
overview: 'LyricFind is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Lyrics, and Data Licensing.


  LyricFind''s developer surface includes engineering blog, documentation, support, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 40.7
    operational_transparency: 0.0
  previous_composite: 14.3
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lyricfind Domain Security
  slug: lyricfind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lyricfind
tags:
- Company
- Music
- Lyrics
- Data Licensing
website: https://lyricfind.com/
---
