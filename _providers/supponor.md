---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.supponor.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supponor.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://supponor.com/get-in-touch/
- group: company
  title: ''
  type: Blog
  url: https://supponor.com/insight/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supponor-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/supponor
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supponor-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/supponor-plans-pricing.yml
coverage:
  checked: '2026-08-12'
  detail: Supponor sells AIR, HUB and Data Room as a managed enterprise service to leagues and broadcasters and publishes no developer program at all — api/developer/docs/developers .supponor.com do not resolve, the eight-page WordPress site has no developer, pricing or terms page, and the only machine surface that exists is the Supponor Hub SPA's own private AWS AppSync GraphQL backend, which returns 401 UnauthorizedException to anonymous introspection and is application plumbing rather than a published API.
  evidence:
  - status: 0
    url: https://api.supponor.com/
  - status: 0
    url: https://developer.supponor.com/
  - status: 404
    url: https://supponor.com/openapi.json
  - status: 404
    url: https://supponor.com/llms.txt
  - status: 404
    url: https://supponor.com/.well-known/agent-card.json
  - status: 404
    url: https://hub.supponor.com/.well-known/agent-card.json
  - status: 401
    url: https://otxjbsi6mnb4fd5dpijwg776fy.appsync-api.eu-central-1.amazonaws.com/graphql
  - status: 200
    url: https://supponor.com/page-sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Supponor is a virtual advertising technology company for live sports broadcasting, now part of TGI Sport. Its software digitally replaces and inserts in-venue brand placements with real-time overlays, letting broadcasters serve region-targeted advertising across multiple feeds, languages, surfaces, and camera angles. Core products include AIR, an AI-driven virtual advertising platform for live broadcast; HUB, a pre-event suite for fixtures, inventory, playlists, creative and approvals; and Data Room, a post-event analytics platform for reporting, video storage, and performance metrics. Supponor works across any sport and surface with remotely deployable, all-weather technology, and is used by organizations including FC Bayern, the NHL, The FA, Serie A, and La Liga. Added to the API Evangelist network as a portfolio company of Northzone; it publishes a corporate and careers web presence but no public developer API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/supponor.png
layout: provider
modified: '2026-08-12'
name: Supponor
nav: Providers
network: true
overview: 'Supponor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Advertising, AdTech, and Sports.


  Supponor''s developer surface includes support, engineering blog, and 6 more developer resources.'
plans:
- name: Supponor Plans Pricing
  plan_count: 0
  slug: supponor-plans-pricing
random_paper: 8
score:
  band: minimal
  composite: 9.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Supponor Domain Security
  slug: supponor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: supponor
tags:
- Company
- Enterprise
- Advertising
- AdTech
- Sports
- Broadcasting
- Media
- Virtual Advertising
- Video
website: https://www.supponor.com
---
