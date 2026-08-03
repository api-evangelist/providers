---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Audd Agentic Access
  operation_count: 3
  slug: audd-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: The Lyrics API from AudD — 1 operation(s) for lyrics.
  name: AudD Lyrics API
  slug: audd-lyrics-api
- description: The Recognition API from AudD — 2 operation(s) for recognition.
  name: AudD Recognition API
  slug: audd-recognition-api
artifact_total: 9
collections:
- collection_type: open
  name: AudD Music Recognition API
  slug: open-audd
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/audd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/audd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/audd-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AudDMusic
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/audd-io
- group: company
  title: ''
  type: Website
  url: https://audd.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.audd.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/audd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/audd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/audd-finops.yml
created: '2026-06-21'
description: AudD is a music recognition service that identifies songs from audio files, URLs, or microphone input via a simple REST API. The api.audd.io API returns rich track metadata (artist, title, album, ISRC, links to Apple Music, Spotify, Deezer and more), supports recognition by humming/singing, lyrics search, and an enterprise endpoint for scanning long audio and video files.
finops:
- name: Audd Finops
  service_category: AI and Machine Learning
  slug: audd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/audd.png
layout: provider
modified: '2026-06-21'
name: AudD
nav: Providers
network: true
overview: 'AudD publishes 2 APIs on the [APIs.io](https://apis.io/) network: Lyrics API and Recognition API. Tagged areas include Music, Music Recognition, Audio, Fingerprinting, and Lyrics.


  AudD''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Audd Plans Pricing
  plan_count: 4
  slug: audd-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 4
  name: Audd Rate Limits
  slug: audd-rate-limits
score:
  band: thin
  composite: 38.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.1
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/audd/refs/heads/main/screenshots/audd-2026-07-25T201708.png
security:
- kind: authentication
  name: Audd Authentication
  slug: audd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Audd Domain Security
  slug: audd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: audd
tags:
- Music
- Music Recognition
- Audio
- Fingerprinting
- Lyrics
website: https://audd.io/
---
