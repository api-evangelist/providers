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
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Audd Agentic Access
  operation_count: 3
  slug: audd-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.audd.io
  baseurl_source: declared
  description: The Lyrics API from AudD — 1 operation(s) for lyrics.
  name: AudD Lyrics API
  slug: audd-lyrics-api
- baseURL: https://api.audd.io
  baseurl_source: declared
  description: The Recognition API from AudD — 2 operation(s) for recognition.
  name: AudD Recognition API
  slug: audd-recognition-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AudD Music Recognition Lyrics API
  slug: open-audd-lyrics-api
- collection_type: open
  name: AudD Music Lyrics Recognition API
  slug: open-audd-recognition-api
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
random_paper: 15
rate_limits:
- limit_count: 4
  name: Audd Rate Limits
  slug: audd-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
