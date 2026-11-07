---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 134
  human_in_the_loop: 134
  name: Ditto Audio Agentic Access
  operation_count: 248
  slug: ditto-audio-agentic-access
  summary_line: 248 operations · 134 acting · 134 human-in-the-loop
api_count: 1
apis:
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Admin — generic DB browser
  name: Ditto Audio Admin/db API
  slug: ditto-audio-admin-db-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Admin — inspect & manage inference jobs
  name: Ditto Audio Admin/inference API
  slug: ditto-audio-admin-inference-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Admin — manage voice models & uploads
  name: Ditto Audio Admin/models API
  slug: ditto-audio-admin-models-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Create, rename & revoke the bearer keys used on /v1/audio/*
  name: Ditto Audio API Keys API
  slug: ditto-audio-api-keys-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: THE public inference API — streaming text→speech, the voice catalogue & the supported languages. Authenticate with an API key.
  name: Ditto Audio Audio API
  slug: ditto-audio-audio-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Sign up, sign in (email + Google), email verification & password reset
  name: Ditto Audio Auth API
  slug: ditto-audio-auth-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Content-addressed rendered-audio chunk store (the reader backend’s S3 cache)
  name: Ditto Audio Chunks API
  slug: ditto-audio-chunks-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The machine-readable OpenAPI documents these docs are generated from
  name: Ditto Audio Docs API
  slug: ditto-audio-docs-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The favorites API from Ditto Audio — 2 operation(s) for favorites.
  name: Ditto Audio Favorites API
  slug: ditto-audio-favorites-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Service liveness probe
  name: Ditto Audio Health API
  slug: ditto-audio-health-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The pure text+model→audio inference service — stateless, no book/persistence awareness
  name: Ditto Audio Inference API
  slug: ditto-audio-inference-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The license (native client) API from Ditto Audio — 3 operation(s) for license (native client).
  name: Ditto Audio license (native client) API
  slug: ditto-audio-license-native-client-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: ditto-native desktop app — license activation & heartbeat
  name: Ditto Audio Licenses API
  slug: ditto-audio-licenses-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Voice-model catalog — browse, download & upload custom voices
  name: Ditto Audio Models API
  slug: ditto-audio-models-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The oauth API from Ditto Audio — 10 operation(s) for oauth.
  name: Ditto Audio OAuth API
  slug: ditto-audio-oauth-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Distributed render offload — nodes, jobs, assignments & live presence
  name: Ditto Audio Pre Render API
  slug: ditto-audio-pre-render-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The pre-render-cloud API from Ditto Audio — 6 operation(s) for pre-render-cloud.
  name: Ditto Audio Pre Render Cloud API
  slug: ditto-audio-pre-render-cloud-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Desktop products — the Ditto app & DAW plugins as one-time purchases; unlocked by any active plan too
  name: Ditto Audio Products API
  slug: ditto-audio-products-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Audiobooks — persist a book, render its narration in the background, stream the result
  name: Ditto Audio Reader API
  slug: ditto-audio-reader-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: ditto-native desktop app — update channels & release manifests
  name: Ditto Audio Releases API
  slug: ditto-audio-releases-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: WebRTC signaling & TURN credentials (distributed render offload)
  name: Ditto Audio Rtc API
  slug: ditto-audio-rtc-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The web studio’s private per-user library of finished renders & conversions
  name: Ditto Audio Studio API
  slug: ditto-audio-studio-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Cloud plans, checkout & billing (Stripe)
  name: Ditto Audio Subscription API
  slug: ditto-audio-subscription-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Reader cloud sync — settings, push/pull delta
  name: Ditto Audio Sync API
  slug: ditto-audio-sync-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Reader cloud sync — bookmarks, annotations, models, audio
  name: Ditto Audio Sync/data API
  slug: ditto-audio-sync-data-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Reader cloud sync — books, reading progress, file backup
  name: Ditto Audio Sync/library API
  slug: ditto-audio-sync-library-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Voice-model training / cloning jobs
  name: Ditto Audio Training API
  slug: ditto-audio-training-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: The update (native client) API from Ditto Audio — 3 operation(s) for update (native client).
  name: Ditto Audio update (native client) API
  slug: ditto-audio-update-native-client-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Your own API usage & analytics — totals, time series and recent requests
  name: Ditto Audio Usage API
  slug: ditto-audio-usage-api
- baseURL: https://ditto.audio/v1
  baseurl_source: declared
  description: Account profile & management
  name: Ditto Audio Users API
  slug: ditto-audio-users-api
artifact_total: 47
common:
- group: agent
  href: https://artifacts.apis.io/ditto-audio/agentic-access/ditto-audio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ditto-audio-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ditto-audio/plans/ditto-audio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ditto-audio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ditto-audio/rules/ditto-audio-rules.yml
  title: ''
  type: Spectral
  url: rules/ditto-audio-rules.yml
- group: design
  href: https://artifacts.apis.io/ditto-audio/json-ld/ditto-audio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ditto-audio-context.jsonld
- group: design
  href: https://artifacts.apis.io/ditto-audio/vocabulary/ditto-audio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ditto-audio-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ditto-audio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ditto-audio/data-model/ditto-audio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ditto-audio-data-model.yml
- group: auth
  href: https://artifacts.apis.io/ditto-audio/authentication/ditto-audio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ditto-audio-authentication.yml
- group: design
  href: https://artifacts.apis.io/ditto-audio/errors/ditto-audio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ditto-audio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ditto-audio/conformance/ditto-audio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ditto-audio-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ditto-audio/well-known/ditto-audio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ditto-audio-well-known.yml
- group: other
  href: https://artifacts.apis.io/ditto-audio/hosts/ditto-audio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ditto-audio-hosts.yml
- group: other
  href: https://artifacts.apis.io/ditto-audio/vendors/ditto-audio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ditto-audio-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ditto.audio/terms
- group: operate
  title: ''
  type: Support
  url: https://ditto.audio/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ditto.audio/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://ditto.audio/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://ditto.audio/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ditto.audio/docs/reference
- group: auth
  href: https://artifacts.apis.io/ditto-audio/security/ditto-audio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ditto-audio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ditto.audio/
created: '2026-11-05'
description: 'ditto-audio is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://ditto.audio/share/ditto.png?v=8622417a52
json_schemas:
- name: CreateAudioBatchDto
  property_count: 11
  slug: ditto-audio-create-audio-batch-dto
- name: CreateCustomVoiceDto
  property_count: 13
  slug: ditto-audio-create-custom-voice-dto
- name: CreateVoiceModelDto
  property_count: 24
  slug: ditto-audio-create-voice-model-dto
- name: SpeechBatchDto
  property_count: 9
  slug: ditto-audio-speech-batch-dto
- name: SpeechDto
  property_count: 9
  slug: ditto-audio-speech-dto
- name: UpdateVoiceModelDto
  property_count: 24
  slug: ditto-audio-update-voice-model-dto
jsonld:
- class_count: 54
  name: Ditto Audio Context
  property_count: 124
  slug: ditto-audio-context
layout: provider
modified: '2026-11-05'
name: Ditto Audio
nav: Providers
network: true
overview: 'Ditto Audio publishes 30 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin/db API, Admin/inference API, Admin/models API, and 27 more. Tagged areas include Text-to-Speech, Voice Plugins, Audiobooks, Neural Voice, and On-Device AI.


  The Ditto Audio catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Ditto Audio''s developer surface includes authentication, support, pricing, documentation, API reference, and 16 more developer resources.'
plans:
- name: Ditto Audio Plans Pricing
  plan_count: 4
  slug: ditto-audio-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Ditto Audio API Rules
  rule_count: 49
  severity_counts:
    error: 37
    hint: 0
    info: 2
    warn: 10
  slug: ditto-audio-rules
score:
  band: developing
  composite: 41.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 35.1
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ditto Audio Authentication
  slug: ditto-audio-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ditto Audio Domain Security
  slug: ditto-audio-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: ditto-audio-create-custom-voice
  slug: ditto-audio-create-custom-voice
- name: ditto-audio-create-model-with-files
  slug: ditto-audio-create-model-with-files
- name: ditto-audio-products-download
  slug: ditto-audio-products-download
- name: ditto-audio-subscribe-to-tier
  slug: ditto-audio-subscribe-to-tier
- name: ditto-audio-upload-and-render-audiobook
  slug: ditto-audio-upload-and-render-audiobook
slug: ditto-audio
tags:
- Text-to-Speech
- Voice Plugins
- Audiobooks
- Neural Voice
- On-Device AI
website: https://ditto.audio/
---
