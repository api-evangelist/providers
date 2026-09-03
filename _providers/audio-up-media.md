---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audio-up-media-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.audioup.com/
- group: company
  title: ''
  type: About
  url: https://www.audioup.com/about
- group: company
  title: ''
  type: Press
  url: https://www.audioup.com/press
- group: company
  title: ''
  type: Newsletter
  url: https://www.audioup.com/subscribe
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/audio-up-media-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Audio Up is a podcast and music production studio whose entire public surface is a 21-page Squarespace marketing site of shows, music and brand case studies — there is no developer section, and api.audioup.com, developer.audioup.com and docs.audioup.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://www.audioup.com/developers
  - status: 404
    url: https://www.audioup.com/openapi.json
  - status: 404
    url: https://www.audioup.com/.well-known/agent-card.json
  - status: 404
    url: https://www.audioup.com/llms.txt
  - status: 200
    url: https://www.audioup.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Audio Up Media is a Los Angeles based podcast studio, music company and audio entertainment network founded in 2020 by Jared Gutstadt, the founder of Jingle Punks. The company develops and produces scripted and unscripted audio series, original music IP and branded audio campaigns, and adapts that intellectual property into television, film and live formats. Its catalog includes scripted titles such as Strawberry Spring, Make It Up As We Go, Where the Bodies Are Buried and Maejor Frequency, alongside branded case-study work for consumer brands. Audio Up is a content studio rather than a software platform: it publishes a marketing site and distributes its shows through third-party podcast platforms, and does not operate a developer program, public API, SDK or machine-readable specification of its own.'
image: https://static1.squarespace.com/static/5e58415fbeb4f12253bdd839/t/5e644fc0d9214e538125939b/1583632324497/Social+Preview_Audio_Up.jpg?format=1500w
layout: provider
modified: '2026-08-06'
name: Audio Up Media
nav: Providers
network: true
overview: Audio Up Media is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Media, Entertainment, Podcasting, and Audio.
random_paper: 17
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audio-up-media/refs/heads/main/screenshots/audio-up-media-2026-08-07T161927.png
security:
- kind: domain-security
  name: Audio Up Media Domain Security
  slug: audio-up-media-domain-security
  summary_line: TLSv1.3 · HSTS
slug: audio-up-media
tags:
- Company
- Media
- Entertainment
- Podcasting
- Audio
- Music
- Content Production
- Advertising
website: https://www.audioup.com/
---
