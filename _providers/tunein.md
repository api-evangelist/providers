---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.7
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: 'The TuneIn Platform API is a partner-facing REST API (OAuth 2.0) for embedding TuneIn''s full audio service into third-party devices and ecosystems. It exposes endpoints for categories, user profiles, '
  name: TuneIn Platform API
  slug: tunein-platform-api
- description: The Browse.ashx API from TuneIn — 1 operation(s) for browse.ashx.
  name: TuneIn Browse.ashx API
  slug: tunein-browse-ashx-api
- description: The Describe.ashx API from TuneIn — 1 operation(s) for describe.ashx.
  name: TuneIn Describe.ashx API
  slug: tunein-describe-ashx-api
- description: The Playing.ashx API from TuneIn — 1 operation(s) for playing.ashx.
  name: TuneIn Playing.ashx API
  slug: tunein-playing-ashx-api
- description: The Search.ashx API from TuneIn — 1 operation(s) for search.ashx.
  name: TuneIn Search.ashx API
  slug: tunein-search-ashx-api
- description: The Tune.ashx API from TuneIn — 1 operation(s) for tune.ashx.
  name: TuneIn Tune.ashx API
  slug: tunein-tune-ashx-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tunein-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tunein.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tunein.com/cfp_login
- group: other
  title: ''
  type: Broadcaster API
  url: https://tunein.com/broadcasters/api/
- group: operate
  title: ''
  type: Status
  url: https://status.tunein.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tunein
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/tunein/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/tunein/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/tunein/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: TuneIn is an internet radio and podcast platform providing REST and OPML-based APIs for accessing live radio stations, sports audio, news, podcasts, and searching audio content worldwide. The platform offers two primary API surfaces — the public OPML/RadioTime streaming API for browsing and tuning stations, and the AIR (Broadcaster) API for submitting real-time now-playing metadata.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tunein.png
jsonld:
- class_count: 0
  name: Tunein Context
  property_count: 0
  slug: tunein
layout: provider
modified: '2026-06-13'
name: TuneIn
nav: Providers
network: true
overview: 'TuneIn publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Browse.ashx API, Describe.ashx API, Playing.ashx API, and 2 more. Tagged areas include Radio, Internet Radio, Podcasts, Streaming Audio, and Sports Audio.


  The TuneIn catalog on APIs.io includes 1 JSON-LD context.


  TuneIn''s developer surface includes status page and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 27
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 32.5
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.2
    developer_ergonomics: 8.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tunein/refs/heads/main/screenshots/tunein-2026-06-20T195830.png
security:
- kind: domain-security
  name: Tunein Domain Security
  slug: tunein-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tunein
tags:
- Radio
- Internet Radio
- Podcasts
- Streaming Audio
- Sports Audio
- News Audio
- Music
website: https://tunein.com/
---
