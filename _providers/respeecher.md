---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Respeecher Agentic Access
  operation_count: 54
  slug: respeecher-agentic-access
  summary_line: 54 operations · 29 acting
api_count: 1
apis:
- baseURL: https://api.respeecher.com/v1/public/tts/en-rt
  baseurl_source: declared
  description: Low-latency real-time text-to-speech that begins streaming audio in under 200ms via three transports - one-shot bytes (POST /tts/bytes, up to ~5,000 characters), HTTP SSE chunks (POST /tts/sse), and a
  name: Respeecher Space Real-Time TTS API
  slug: respeecher-space-realtime-tts-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The accents API from Respeecher — 1 operation(s) for accents.
  name: Respeecher Accents API
  slug: respeecher-accents-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The auth API from Respeecher — 3 operation(s) for auth.
  name: Respeecher Auth API
  slug: respeecher-auth-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The calibration API from Respeecher — 3 operation(s) for calibration.
  name: Respeecher Calibration API
  slug: respeecher-calibration-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The credits API from Respeecher — 1 operation(s) for credits.
  name: Respeecher Credits API
  slug: respeecher-credits-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The folders API from Respeecher — 2 operation(s) for folders.
  name: Respeecher Folders API
  slug: respeecher-folders-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The healtz API from Respeecher — 1 operation(s) for healtz.
  name: Respeecher Healtz API
  slug: respeecher-healtz-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The models API from Respeecher — 1 operation(s) for models.
  name: Respeecher Models API
  slug: respeecher-models-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The narration-styles API from Respeecher — 1 operation(s) for narration-styles.
  name: Respeecher Narration Styles API
  slug: respeecher-narration-styles-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The notes API from Respeecher — 1 operation(s) for notes.
  name: Respeecher Notes API
  slug: respeecher-notes-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The orders API from Respeecher — 2 operation(s) for orders.
  name: Respeecher Orders API
  slug: respeecher-orders-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The projects API from Respeecher — 4 operation(s) for projects.
  name: Respeecher Projects API
  slug: respeecher-projects-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The recordings API from Respeecher — 9 operation(s) for recordings.
  name: Respeecher Recordings API
  slug: respeecher-recordings-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The stats API from Respeecher — 3 operation(s) for stats.
  name: Respeecher Stats API
  slug: respeecher-stats-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The storage API from Respeecher — 1 operation(s) for storage.
  name: Respeecher Storage API
  slug: respeecher-storage-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The tts API from Respeecher — 1 operation(s) for tts.
  name: Respeecher Tts API
  slug: respeecher-tts-api
- baseURL: https://gateway.respeecher.com
  baseurl_source: declared
  description: The voices API from Respeecher — 4 operation(s) for voices.
  name: Respeecher Voices API
  slug: respeecher-voices-api
artifact_total: 41
asyncapis:
- description: AsyncAPI description of the Respeecher Space real-time text-to-speech WebSocket channel. A single persistent WebSocket connection carries multiple concurrent text-to-speech generations, differentiated
  name: Respeecher Space Real-Time TTS WebSocket API
  slug: respeecher-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voice Markertplace accents API
  slug: open-respeecher-accents-api
- collection_type: open
  name: Voice Markertplace accents auth API
  slug: open-respeecher-auth-api
- collection_type: open
  name: Voice Markertplace accents calibration API
  slug: open-respeecher-calibration-api
- collection_type: open
  name: Voice Markertplace accents credits API
  slug: open-respeecher-credits-api
- collection_type: open
  name: Voice Markertplace accents folders API
  slug: open-respeecher-folders-api
- collection_type: open
  name: Voice Markertplace accents healtz API
  slug: open-respeecher-healtz-api
- collection_type: open
  name: Voice Markertplace accents models API
  slug: open-respeecher-models-api
- collection_type: open
  name: Voice Markertplace accents narration-styles API
  slug: open-respeecher-narration-styles-api
- collection_type: open
  name: Voice Markertplace accents notes API
  slug: open-respeecher-notes-api
- collection_type: open
  name: Voice Markertplace accents orders API
  slug: open-respeecher-orders-api
- collection_type: open
  name: Voice Markertplace accents projects API
  slug: open-respeecher-projects-api
- collection_type: open
  name: Voice Markertplace accents recordings API
  slug: open-respeecher-recordings-api
- collection_type: open
  name: Voice Markertplace accents stats API
  slug: open-respeecher-stats-api
- collection_type: open
  name: Voice Markertplace accents storage API
  slug: open-respeecher-storage-api
- collection_type: open
  name: Voice Markertplace accents tts API
  slug: open-respeecher-tts-api
- collection_type: open
  name: Voice Markertplace accents voices API
  slug: open-respeecher-voices-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/respeecher/refs/heads/main/agentic-access/respeecher-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/respeecher-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/respeecher/refs/heads/main/security/respeecher-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/respeecher-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/respeecher
- group: company
  title: ''
  type: Website
  url: https://www.respeecher.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.respeecher.com/
- group: docs
  title: ''
  type: Documentation
  url: https://space.respeecher.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://marketplace.respeecher.com/account
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/respeecher/refs/heads/main/plans/respeecher-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/respeecher-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/respeecher/refs/heads/main/rate-limits/respeecher-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/respeecher-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/respeecher/refs/heads/main/finops/respeecher-finops.yml
  title: ''
  type: FinOps
  url: finops/respeecher-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://gateway.respeecher.com/api/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://www.respeecher.com/blog
created: '2026-07-11'
description: Respeecher is an AI voice company known for high-fidelity speech-to-speech (STS) voice conversion and text-to-speech (TTS) used across film, television, games, and advertising. It exposes two documented, self-service public APIs. The Voice Marketplace API (gateway.respeecher.com) provides voice discovery, speech-to-speech conversion orders, text-to-speech synthesis, calibration, recordings, projects/folders, credits, and statistics, secured with an API key. The newer Respeecher Space real-time TTS API (api.respeecher.com) streams lifelike audio in under 200ms via one-shot bytes, HTTP SSE, and a WebSocket channel, with English (en-rt) and Ukrainian (ua-rt) models, official Python and TypeScript SDKs, and LiveKit, Pipecat, Ultravox, and VAPI integrations. Bespoke, high-touch voice cloning for studios is delivered through the enterprise AI Voice Lab.
finops:
- name: Respeecher Finops
  service_category: ''
  slug: respeecher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/respeecher.png
layout: provider
modified: '2026-07-11'
name: Respeecher
nav: Providers
network: true
overview: 'Respeecher publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Space Real-Time TTS API, Accents API, Auth API, and 14 more. Tagged areas include Voice AI, Voice Cloning, Speech to Speech, Text-to-Speech, and Voice Conversion.


  The Respeecher catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Respeecher''s developer surface includes documentation, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Respeecher Plans Pricing
  plan_count: 6
  slug: respeecher-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Respeecher Rate Limits
  slug: respeecher-rate-limits
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: Respeecher API Rules
  rule_count: 2
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 1
  slug: respeecher-asyncapi-spectral-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 54.6
    catalog_earned_first_party: 0.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 36.3
    contract_governance: 11.4
    contract_quality: 51.3
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/respeecher/refs/heads/main/screenshots/respeecher-2026-09-02T153756.png
security:
- kind: domain-security
  name: Respeecher Domain Security
  slug: respeecher-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: respeecher
tags:
- Voice AI
- Voice Cloning
- Speech to Speech
- Text-to-Speech
- Voice Conversion
- Real-Time
- Media and Entertainment
website: https://www.respeecher.com
---
