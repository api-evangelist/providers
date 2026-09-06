---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - '{''url'': ''https://podcastle.ai'', ''status'': 308, ''note'': ''declared website redirects to https://async.com/ — a different registrable domain (podcastle.ai -> async.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- acting_count: 5
  human_in_the_loop: 0
  name: Podcastle Agentic Access
  operation_count: 5
  slug: podcastle-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- description: Transcription and speech-to-text are Podcastle platform features (multi-language transcription with speaker identification) available in the product, console, and credit-based plans. A standalone tran
  name: Podcastle Transcription
  slug: transcription
- baseURL: https://api.async.com
  baseurl_source: declared
  description: Synthesize speech from text in batch, streaming, or with word timestamps.
  name: Podcastle Text to Speech API
  slug: podcastle-text-to-speech-api
- baseURL: https://api.async.com
  baseurl_source: declared
  description: Browse the voice library and create instant voice clones.
  name: Podcastle Voices API
  slug: podcastle-voices-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Async (Podcastle) Voice Text to Speech API
  slug: open-podcastle-text-to-speech-api
- collection_type: open
  name: Async (Podcastle) Voice Text to Speech Voices API
  slug: open-podcastle-voices-api
- collection_type: open
  name: Async (Podcastle) Voice API
  slug: open-podcastle
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/podcastle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podcastle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podcastle-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://podcastle.ai/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podcastle-ai
- group: company
  title: ''
  type: Website
  url: https://podcastle.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.async.com
- group: commercial
  title: ''
  type: Plans
  url: plans/podcastle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/podcastle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/podcastle-finops.yml
created: '2026-06-21'
description: Podcastle is an AI audio and podcast creation platform whose developer engine, Async, exposes a low-latency Voice API for human-like text-to-speech, a browsable voice library, and instant voice cloning from a short audio sample. The API is served from https://api.async.com and authenticated with an x-api-key header plus a version header. Transcription is a Podcastle platform feature; no standalone transcription endpoint is documented in the public Voice API.
finops:
- name: Podcastle Finops
  service_category: AI and Machine Learning
  slug: podcastle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podcastle.png
layout: provider
modified: '2026-06-21'
name: Podcastle
nav: Providers
network: true
overview: 'Podcastle publishes 2 APIs on the [APIs.io](https://apis.io/) network: Text to Speech API and Voices API. Tagged areas include Artificial Intelligence, Audio, Text-to-Speech, Voice Cloning, and Podcasting.


  Podcastle''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Podcastle Plans Pricing
  plan_count: 6
  slug: podcastle-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Podcastle Rate Limits
  slug: podcastle-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 10
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
    contract_quality: 57.8
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.5
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
screenshot: https://raw.githubusercontent.com/api-evangelist/podcastle/refs/heads/main/screenshots/podcastle-2026-09-02T151614.png
security:
- kind: authentication
  name: Podcastle Authentication
  slug: podcastle-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Podcastle Domain Security
  slug: podcastle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: podcastle
tags:
- Artificial Intelligence
- Audio
- Text-to-Speech
- Voice Cloning
- Podcasting
website: https://podcastle.ai
---
