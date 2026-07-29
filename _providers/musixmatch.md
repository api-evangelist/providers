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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Musixmatch Agentic Access
  operation_count: 16
  slug: musixmatch-agentic-access
  summary_line: 16 operations
api_count: 6
apis:
- description: The Album API from Musixmatch — 2 operation(s) for album.
  name: Musixmatch Album API
  slug: musixmatch-album-api
- description: The Artist API from Musixmatch — 4 operation(s) for artist.
  name: Musixmatch Artist API
  slug: musixmatch-artist-api
- description: The Lyrics API from Musixmatch — 2 operation(s) for lyrics.
  name: Musixmatch Lyrics API
  slug: musixmatch-lyrics-api
- description: The Snippets API from Musixmatch — 1 operation(s) for snippets.
  name: Musixmatch Snippets API
  slug: musixmatch-snippets-api
- description: The Subtitle API from Musixmatch — 2 operation(s) for subtitle.
  name: Musixmatch Subtitle API
  slug: musixmatch-subtitle-api
- description: The Track API from Musixmatch — 5 operation(s) for track.
  name: Musixmatch Track API
  slug: musixmatch-track-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/musixmatch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/musixmatch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/musixmatch-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/musixmatch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/musixmatch
- group: start
  title: ''
  type: Portal
  url: https://developer.musixmatch.com/
- group: start
  title: ''
  type: Login
  url: https://developer.musixmatch.com/login
- group: company
  title: ''
  type: Blog
  url: https://blog.musixmatch.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://about.musixmatch.com/privacy-policy
created: '2024-06-07'
description: Musixmatch is an Italian music data company and platform for users to search and share song lyrics with translations. Musixmatch has 80 million users, 8 million songs with their respective lyrics, and 115+ employees.
finops:
- name: Musixmatch Finops
  service_category: API
  slug: musixmatch-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Musixmatch API. The schema is derived from the [Musixmatch REST API documentation](https://developer.musixmatch.com/documentation) and repre
  name: Musixmatch GraphQL Schema
  slug: musixmatch-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/musixmatch.png
layout: provider
modified: '2026-05-19'
name: Musixmatch
nav: Providers
network: true
overview: 'Musixmatch publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Album API, Artist API, Lyrics API, and 3 more. Tagged areas include Lyrics, Music, and Translations.


  Musixmatch''s developer surface includes authentication, developer portal, engineering blog, and 6 more developer resources.'
plans:
- name: Musixmatch Plans Pricing
  plan_count: 3
  slug: musixmatch-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Musixmatch Rate Limits
  slug: musixmatch-rate-limits
score:
  band: thin
  composite: 41.0
  delta: 0.3
  facets:
    commercial_clarity: 63.2
    contract_quality: 48.2
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/musixmatch/refs/heads/main/screenshots/musixmatch-2026-06-20T185906.png
security:
- kind: authentication
  name: Musixmatch Authentication
  slug: musixmatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Musixmatch Domain Security
  slug: musixmatch-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: musixmatch
tags:
- Lyrics
- Music
- Translations
website: https://developer.musixmatch.com/
---
