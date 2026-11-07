---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Radio Cult Agentic Access
  operation_count: 18
  slug: radio-cult-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.radiocult.fm
  baseurl_source: declared
  description: The Artists API from Radio Cult — 3 operation(s) for artists.
  name: Radio Cult Artists API
  slug: radio-cult-artists-api
- baseURL: https://api.radiocult.fm
  baseurl_source: declared
  description: The Media API from Radio Cult — 4 operation(s) for media.
  name: Radio Cult Media API
  slug: radio-cult-media-api
- baseURL: https://api.radiocult.fm
  baseurl_source: declared
  description: The Playlists API from Radio Cult — 3 operation(s) for playlists.
  name: Radio Cult Playlists API
  slug: radio-cult-playlists-api
- baseURL: https://api.radiocult.fm
  baseurl_source: declared
  description: The Recordings API from Radio Cult — 2 operation(s) for recordings.
  name: Radio Cult Recordings API
  slug: radio-cult-recordings-api
- baseURL: https://api.radiocult.fm
  baseurl_source: declared
  description: The Schedule API from Radio Cult — 2 operation(s) for schedule.
  name: Radio Cult Schedule API
  slug: radio-cult-schedule-api
- baseURL: https://api.radiocult.fm
  baseurl_source: declared
  description: The Streaming API from Radio Cult — 1 operation(s) for streaming.
  name: Radio Cult Streaming API
  slug: radio-cult-streaming-api
- baseURL: https://api.radiocult.fm
  baseurl_source: declared
  description: The Tags API from Radio Cult — 1 operation(s) for tags.
  name: Radio Cult Tags API
  slug: radio-cult-tags-api
artifact_total: 22
collections:
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
- group: commercial
  href: https://artifacts.apis.io/radio-cult/plans/radio-cult-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/radio-cult-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/radio-cult/rate-limits/radio-cult-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/radio-cult-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/radio-cult/finops/radio-cult-finops.yml
  title: ''
  type: FinOps
  url: finops/radio-cult-finops.yml
- group: company
  title: ''
  type: Website
  url: https://radiocult.fm
- group: other
  href: https://artifacts.apis.io/radio-cult/capabilities/radio-cult-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/radio-cult-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/radio-cult/agentic-access/radio-cult-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/radio-cult-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/radio-cult/security/radio-cult-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/radio-cult-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/radio-cult/authentication/radio-cult-authentication.yml
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
- has_sources: false
  method: generated
  name: Radio Cult Finops
  primary_unit: request
  service_category: API
  slug: radio-cult-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/radio-cult.png
layout: provider
modified: '2026-09-16'
name: Radio Cult
nav: Providers
network: true
overview: 'Radio Cult publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artists API, Media API, Playlists API, and 4 more. Tagged areas include Radio, Streaming, Audio, Music, and Broadcasting.


  The Radio Cult catalog on APIs.io includes 1 Spectral governance ruleset.


  Radio Cult''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Radio Cult Plans Pricing
  plan_count: 3
  slug: radio-cult-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Radio Cult Rate Limits
  slug: radio-cult-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Radio Cult API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: radio-cult-rules
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 44.1
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 24.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/radio-cult/radio-cult-2026-06-20T192517.png
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
website: https://radiocult.fm
---
