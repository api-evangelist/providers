---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The iHeartRadio Catalog API provides search and discovery capabilities across the iHeartRadio content catalog, including live broadcast radio stations, digital-only stations, podcasts, artists, tracks
  name: iHeartRadio Catalog API
  slug: iheartradio-catalog-api
- description: The iHeartRadio Live Stations API provides access to live broadcast radio station information including station metadata, market information, genre classification, and streaming URLs across multiple f
  name: iHeartRadio Live Stations API
  slug: iheartradio-live-stations-api
- description: The iHeartRadio Podcasts API enables search and discovery of podcasts available on the iHeartRadio platform, along with retrieval of individual podcast episode listings and direct audio stream URLs fo
  name: iHeartRadio Podcasts API
  slug: iheartradio-podcasts-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iheart-radio-domain-security.yml
- group: operate
  title: ''
  type: Press Release
  url: https://www.iheartmedia.com/press/clear-channel-radio-launches-developer-program-iheartradio
- group: company
  title: ''
  type: Website
  url: https://www.iheart.com
- group: operate
  title: ''
  type: Help
  url: https://help.iheart.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iheart.com/content/terms-of-use/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/iheartradio
- group: company
  title: ''
  type: Tech Blog
  url: https://tech.iheart.com
- group: commercial
  title: ''
  type: Pricing
  url: https://help.iheart.com/hc/en-us/articles/20310091985549-iHeart-Plans
- group: operate
  title: ''
  type: Status
  url: https://instatus.com/now/iheart.com
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/iheart-radio/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/iheart-radio/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/iheart-radio/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: iHeartRadio is a digital radio platform operated by iHeartMedia that provides access to over 800 live broadcast and digital-only radio stations from more than 150 U.S. cities, podcasts, artist-based custom stations, and curated music content. The platform offers REST APIs enabling programmatic access to live station streams, catalog search across stations, podcasts, artists and tracks, and podcast episode retrieval with direct audio stream URLs.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iheart-radio.png
layout: provider
modified: '2026-06-13'
name: iHeartRadio
nav: Providers
network: true
overview: 'iHeartRadio publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Live Stations API, and Podcasts API. Tagged areas include Radio, Podcasts, Music, Streaming, and Audio.


  iHeartRadio''s developer surface includes GitHub presence, pricing, status page, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 75
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 28.3
  delta: -3.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iheart-radio/refs/heads/main/screenshots/iheart-radio-2026-06-20T183223.png
security:
- kind: domain-security
  name: Iheart Radio Domain Security
  slug: iheart-radio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iheart-radio
tags:
- Radio
- Podcasts
- Music
- Streaming
- Audio
- Live Radio
- Digital Media
website: https://www.iheart.com
---
