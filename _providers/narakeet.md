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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Narakeet Agentic Access
  operation_count: 6
  slug: narakeet-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: Check remaining account credits.
  name: Narakeet Account API
  slug: narakeet-account-api
- description: Build narrated audio (MP3, M4A, WAV) from text, SubRip, or WebVTT input.
  name: Narakeet Text to Speech API
  slug: narakeet-text-to-speech-api
- description: Build video from a Markdown script and assets packaged as a zip archive.
  name: Narakeet Video API
  slug: narakeet-video-api
- description: List the voices available for audio and video production.
  name: Narakeet Voices API
  slug: narakeet-voices-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Narakeet Account API
  slug: open-narakeet-account-api
- collection_type: open
  name: Narakeet Account Text to Speech API
  slug: open-narakeet-text-to-speech-api
- collection_type: open
  name: Narakeet Account Video API
  slug: open-narakeet-video-api
- collection_type: open
  name: Narakeet Account Voices API
  slug: open-narakeet-voices-api
- collection_type: open
  name: Narakeet API
  slug: open-narakeet
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/narakeet-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/narakeet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/narakeet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/narakeet-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/narakeet
- group: company
  title: ''
  type: Website
  url: https://www.narakeet.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.narakeet.com/docs/automating/
- group: commercial
  title: ''
  type: Plans
  url: plans/narakeet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/narakeet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/narakeet-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.narakeet.com/news/
created: '2026-07-11'
description: Narakeet turns text and Markdown scripts into realistic narrated audio and video using AI text-to-speech voices - 900 voices across 100 languages. Beyond its web app, Narakeet exposes a documented REST API (base https://api.narakeet.com) for building speech audio (MP3, M4A, WAV) from text, building video from Markdown scripts and assets, listing available voices, and checking account credits. Audio builds run either as a short-content streaming call that returns bytes directly or as a long-content asynchronous build that returns a status URL to poll; video builds always upload a zip, trigger a build, and poll for the finished MP4. All build requests authenticate with an x-api-key header, and API access requires a top-up or metered commercial account.
finops:
- name: Narakeet Finops
  service_category: AI and Machine Learning
  slug: narakeet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/narakeet.png
layout: provider
modified: '2026-07-11'
name: Narakeet
nav: Providers
network: true
overview: 'Narakeet publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Text to Speech API, Video API, and 1 more. Tagged areas include Text-to-Speech, TTS, Voice, Audio, and Video.


  Narakeet''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Narakeet Plans Pricing
  plan_count: 5
  slug: narakeet-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: Narakeet Rate Limits
  slug: narakeet-rate-limits
score:
  band: developing
  composite: 40.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 40.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/narakeet/refs/heads/main/screenshots/narakeet-2026-08-07T184630.png
security:
- kind: authentication
  name: Narakeet Authentication
  slug: narakeet-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Narakeet Domain Security
  slug: narakeet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: narakeet
tags:
- Text-to-Speech
- TTS
- Voice
- Audio
- Video
- Artificial Intelligence
- Media Generation
website: https://www.narakeet.com
---
