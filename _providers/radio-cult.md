---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Radio Cult Agentic Access
  operation_count: 18
  slug: radio-cult-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 7
apis:
- description: The Artists API from Radio Cult — 3 operation(s) for artists.
  name: Radio Cult Artists API
  slug: radio-cult-artists-api
- description: The Media API from Radio Cult — 4 operation(s) for media.
  name: Radio Cult Media API
  slug: radio-cult-media-api
- description: The Playlists API from Radio Cult — 3 operation(s) for playlists.
  name: Radio Cult Playlists API
  slug: radio-cult-playlists-api
- description: The Recordings API from Radio Cult — 2 operation(s) for recordings.
  name: Radio Cult Recordings API
  slug: radio-cult-recordings-api
- description: The Schedule API from Radio Cult — 2 operation(s) for schedule.
  name: Radio Cult Schedule API
  slug: radio-cult-schedule-api
- description: The Streaming API from Radio Cult — 1 operation(s) for streaming.
  name: Radio Cult Streaming API
  slug: radio-cult-streaming-api
- description: The Tags API from Radio Cult — 1 operation(s) for tags.
  name: Radio Cult Tags API
  slug: radio-cult-tags-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Radio Cult Artists API
  slug: open-radio-cult-artists-api
- collection_type: open
  name: Radio Cult Artists Media API
  slug: open-radio-cult-media-api
- collection_type: open
  name: Radio Cult Artists Playlists API
  slug: open-radio-cult-playlists-api
- collection_type: open
  name: Radio Cult Artists Recordings API
  slug: open-radio-cult-recordings-api
- collection_type: open
  name: Radio Cult Artists Schedule API
  slug: open-radio-cult-schedule-api
- collection_type: open
  name: Radio Cult Artists Streaming API
  slug: open-radio-cult-streaming-api
- collection_type: open
  name: Radio Cult Artists Tags API
  slug: open-radio-cult-tags-api
- collection_type: open
  name: Radio Cult API
  slug: open-radio-cult
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/radio-cult-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/radio-cult-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/radio-cult-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/radio-cult
- group: company
  title: ''
  type: Blog
  url: https://www.radiocult.fm/blog
created: '2025-02-12'
description: Are you looking to power your online radio stations website with the Radio Cult API? If so, you're in the right place.
finops:
- name: Radio Cult Finops
  service_category: API
  slug: radio-cult-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radio-cult.png
layout: provider
modified: '2026-05-19'
name: Radio Cult
nav: Providers
network: true
overview: 'Radio Cult publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Artists API, Media API, Playlists API, and 4 more. Tagged areas include Radio, Streaming, Audio, Music, and Broadcasting.


  Radio Cult''s developer surface includes authentication, engineering blog, and 3 more developer resources.'
plans:
- name: Radio Cult Plans Pricing
  plan_count: 3
  slug: radio-cult-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Radio Cult Rate Limits
  slug: radio-cult-rate-limits
score:
  band: emerging
  composite: 25.4
  delta: -0.5
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 14.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/radio-cult/refs/heads/main/screenshots/radio-cult-2026-06-20T192517.png
security:
- kind: authentication
  name: Radio Cult Authentication
  slug: radio-cult-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Radio Cult Domain Security
  slug: radio-cult-domain-security
  summary_line: TLSv1.3 · HSTS
slug: radio-cult
tags:
- Radio
- Streaming
- Audio
- Music
- Broadcasting
---
