---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Musixmatch Agentic Access
  operation_count: 16
  slug: musixmatch-agentic-access
  summary_line: 16 operations
api_count: 1
apis:
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Album API from Musixmatch — 2 operation(s) for album.
  name: Musixmatch Album API
  slug: musixmatch-album-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Artist API from Musixmatch — 4 operation(s) for artist.
  name: Musixmatch Artist API
  slug: musixmatch-artist-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Lyrics API from Musixmatch — 2 operation(s) for lyrics.
  name: Musixmatch Lyrics API
  slug: musixmatch-lyrics-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Snippets API from Musixmatch — 1 operation(s) for snippets.
  name: Musixmatch Snippets API
  slug: musixmatch-snippets-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Subtitle API from Musixmatch — 2 operation(s) for subtitle.
  name: Musixmatch Subtitle API
  slug: musixmatch-subtitle-api
- baseURL: https://api.musixmatch.com/ws/1.1/
  baseurl_source: declared
  description: The Track API from Musixmatch — 5 operation(s) for track.
  name: Musixmatch Track API
  slug: musixmatch-track-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Musixmatch Album API
  slug: open-musixmatch-album-api
- collection_type: open
  name: Musixmatch Album Artist API
  slug: open-musixmatch-artist-api
- collection_type: open
  name: Musixmatch Album Lyrics API
  slug: open-musixmatch-lyrics-api
- collection_type: open
  name: Musixmatch Album Snippets API
  slug: open-musixmatch-snippets-api
- collection_type: open
  name: Musixmatch Album Subtitle API
  slug: open-musixmatch-subtitle-api
- collection_type: open
  name: Musixmatch Album Track API
  slug: open-musixmatch-track-api
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
random_paper: 20
rate_limits:
- limit_count: 5
  name: Musixmatch Rate Limits
  slug: musixmatch-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 44.6
    developer_ergonomics: 33.3
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
