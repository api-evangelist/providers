---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
- acting_count: 8
  human_in_the_loop: 0
  name: Wellsaid Agentic Access
  operation_count: 16
  slug: wellsaid-agentic-access
  summary_line: 16 operations · 8 acting
api_count: 1
apis:
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Manage rendered clips.
  name: WellSaid Labs Clips API
  slug: wellsaid-clips-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Respelling suggestions and replacement libraries.
  name: WellSaid Labs Pronunciation API
  slug: wellsaid-pronunciation-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Render text to speech as clips or audio streams.
  name: WellSaid Labs Text-to-Speech API
  slug: wellsaid-text-to-speech-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Discover available voice avatars.
  name: WellSaid Labs Voices API
  slug: wellsaid-voices-api
- baseURL: https://api.wellsaidlabs.com/v1
  baseurl_source: declared
  description: Catalog of available AI voice avatars and their metadata.
  name: WellSaid Labs Voice Avatars API
  slug: wellsaid-labs-voice-avatars-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WellSaid Labs Clips API
  slug: open-wellsaid-clips-api
- collection_type: open
  name: WellSaid Labs Clips Pronunciation API
  slug: open-wellsaid-pronunciation-api
- collection_type: open
  name: WellSaid Labs Clips Text-to-Speech API
  slug: open-wellsaid-text-to-speech-api
- collection_type: open
  name: WellSaid Labs Clips Voices API
  slug: open-wellsaid-voices-api
- collection_type: open
  name: WellSaid Labs API
  slug: open-wellsaid
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wellsaid-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wellsaid-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellsaid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellsaid-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wellsaid-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wellsaid-labs
- group: company
  title: ''
  type: Website
  url: https://wellsaidlabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wellsaidlabs.com
- group: commercial
  title: ''
  type: Plans
  url: plans/wellsaid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellsaid-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wellsaid-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wellsaidlabs.com/docs/getting-started
created: '2026-06-21'
description: WellSaid Labs is an AI text-to-speech voice platform. Its REST API renders natural-sounding speech from text using studio-quality voice avatars, supporting synchronous clip creation, low-latency audio streaming, and word-level timing with subtitles, authenticated with an X-Api-Key header.
finops:
- name: Wellsaid Finops
  service_category: AI and Machine Learning
  slug: wellsaid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wellsaid.png
layout: provider
modified: '2026-06-21'
name: WellSaid Labs
nav: Providers
network: true
overview: 'WellSaid Labs publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Clips API, Pronunciation API, Text-to-Speech API, and 2 more. Tagged areas include Artificial Intelligence, Text-to-Speech, Voice, Audio, and TTS.


  WellSaid Labs'' developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Wellsaid Plans Pricing
  plan_count: 3
  slug: wellsaid-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Wellsaid Rate Limits
  slug: wellsaid-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 43.3
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wellsaid/refs/heads/main/screenshots/wellsaid-2026-09-02T170611.png
security:
- kind: authentication
  name: Wellsaid Authentication
  slug: wellsaid-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wellsaid Domain Security
  slug: wellsaid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wellsaid Trust Center
  slug: wellsaid-trust-center
  summary_line: SOC 2, GDPR
slug: wellsaid
tags:
- Artificial Intelligence
- Text-to-Speech
- Voice
- Audio
- TTS
website: https://wellsaidlabs.com
---
