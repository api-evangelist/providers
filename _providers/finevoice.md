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
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
api_count: 7
apis:
- description: FineVoice provides a public API for AI voice generation, voice conversion, speech-to-text, sound effects, music generation and audio processing as documented in their Mintlify docs.
  name: FineVoice API
  slug: finevoice-api-2
- baseURL: https://apis.finevoice.ai
  baseurl_source: declared
  description: 'FineVoice (Fineshare) API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: FineVoice (Fineshare) API
  slug: finevoice-api
- baseURL: https://apis.finevoice.ai
  baseurl_source: declared
  description: This is the documentation for the FineVoice API. If you have any questions or need assistance, please contact support@finevoice.ai.
  name: FineVoice (Fineshare) Openapi API
  slug: finevoice-fineshare-openapi-api
- baseURL: https://voiceai.fineshare.net
  baseurl_source: declared
  description: API for modifying an audio file with various transformation parameters.
  name: FineVoice (Fineshare) Changeaudiofile API
  slug: finevoice-fineshare-changeaudiofile-api
- baseURL: https://models.fineshare.net
  baseurl_source: declared
  description: API to list user models with pagination support.
  name: FineVoice (Fineshare) Listmodels API
  slug: finevoice-fineshare-listmodels-api
- baseURL: https://converter.fineshare.net
  baseurl_source: declared
  description: API for retrieving a paginated list of voices with filtering options.
  name: FineVoice (Fineshare) Pagevoices API
  slug: finevoice-fineshare-pagevoices-api
- baseURL: https://converter.fineshare.net
  baseurl_source: declared
  description: API to retrieve detailed information about a specific voice.
  name: FineVoice (Fineshare) Getvoicedetail API
  slug: finevoice-fineshare-getvoicedetail-api
- baseURL: https://upload.fineshare.net
  baseurl_source: declared
  description: API for uploading audio files.
  name: FineVoice (Fineshare) Uploadaudiofile API
  slug: finevoice-fineshare-uploadaudiofile-api
- baseURL: https://voiceai.fineshare.net
  baseurl_source: declared
  description: API for managing audio file transformations.
  name: FineVoice (Fineshare) Createaudiofilechanger API
  slug: finevoice-fineshare-createaudiofilechanger-api
artifact_total: 32
common:
- group: design
  href: https://artifacts.apis.io/finevoice/errors/finevoice-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/finevoice-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/finevoice/plans/finevoice-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/finevoice-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/finevoice/rules/finevoice-rules.yml
  title: ''
  type: Spectral
  url: rules/finevoice-rules.yml
- group: design
  href: https://artifacts.apis.io/finevoice/json-ld/finevoice-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/finevoice-context.jsonld
- group: design
  href: https://artifacts.apis.io/finevoice/vocabulary/finevoice-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/finevoice-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/finevoice/data-model/finevoice-data-model.yml
  title: ''
  type: DataModel
  url: data-model/finevoice-data-model.yml
- group: operate
  href: https://artifacts.apis.io/finevoice/changelog/finevoice-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/finevoice-changelog.yml
- group: auth
  href: https://artifacts.apis.io/finevoice/authentication/finevoice-authentication.yml
  title: ''
  type: Authentication
  url: authentication/finevoice-authentication.yml
- group: design
  href: https://artifacts.apis.io/finevoice/conformance/finevoice-conformance.yml
  title: ''
  type: Conformance
  url: conformance/finevoice-conformance.yml
- group: agent
  href: https://artifacts.apis.io/finevoice/llms/finevoice-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/finevoice-llms.txt
- group: other
  href: https://artifacts.apis.io/finevoice/a2a/finevoice-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/finevoice-a2a.yml
- group: agent
  href: https://artifacts.apis.io/finevoice/well-known/finevoice-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/finevoice-well-known.yml
- group: other
  href: https://artifacts.apis.io/finevoice/hosts/finevoice-hosts.yml
  title: ''
  type: Hosts
  url: hosts/finevoice-hosts.yml
- group: other
  href: https://artifacts.apis.io/finevoice/vendors/finevoice-vendors.yml
  title: ''
  type: Vendors
  url: vendors/finevoice-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finevoice.ai/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finevoice.ai/privacy.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.finevoice.ai/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.finevoice.ai\
- group: docs
  title: ''
  type: APIReference
  url: https://api.finevoice.ai/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FineVoice
- group: auth
  href: https://artifacts.apis.io/finevoice/security/finevoice-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/finevoice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://finevoice.ai
- group: docs
  title: ''
  type: Documentation
  url: https://api.finevoice.ai
- group: company
  title: ''
  type: Blog
  url: https://finevoice.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://finevoice.ai/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://api.finevoice.ai/quickstart.md
coverage:
  checked: '2026-10-22'
  detail: Mintlify documentation lists API endpoints but no OpenAPI/AsyncAPI/GraphQL spec is provided.
  evidence:
  - status: 404
    url: https://api.finevoice.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: FineVoice (Fineshare) provides a free, all‑in‑one AI voice generation platform that lets users create realistic, expressive speech, clone voices, and apply audio effects without sign‑up. The service offers text‑to‑speech, voice conversion, speech‑to‑text, and a suite of creative audio tools accessible via a public API documented at api.finevoice.ai.
json_schemas:
- name: ChangeAudioFileResponse
  property_count: 3
  slug: finevoice-change-audio-file-response
- name: CreateVoiceChangerReqModel
  property_count: 4
  slug: finevoice-create-voice-changer-req-model
- name: FileChangeReqModel
  property_count: 12
  slug: finevoice-file-change-req-model
- name: GetVoiceDetailRespModel
  property_count: 8
  slug: finevoice-get-voice-detail-resp-model
- name: ListMyModelRespModel
  property_count: 3
  slug: finevoice-list-my-model-resp-model
- name: MusicCoverRequest
  property_count: 15
  slug: finevoice-music-cover-request
- name: MusicGenerationByPromptRequest
  property_count: 10
  slug: finevoice-music-generation-by-prompt-request
- name: MusicGenerationRequest
  property_count: 8
  slug: finevoice-music-generation-request
- name: PageVoicesResponse
  property_count: 4
  slug: finevoice-page-voices-response
- name: PipelineRequest
  property_count: 21
  slug: finevoice-pipeline-request
- name: PostV1AudioSfxGenerationRequest
  property_count: 6
  slug: finevoice-post-v1-audio-sfx-generation-request
- name: PostV1AudioSttRequest
  property_count: 12
  slug: finevoice-post-v1-audio-stt-request
- name: PostV1EnhancerProcessPipelineRequest
  property_count: 21
  slug: finevoice-post-v1-enhancer-process-pipeline-request
- name: PostV1EnhancerSpeechEnhancementRequest
  property_count: 8
  slug: finevoice-post-v1-enhancer-speech-enhancement-request
- name: PostV1MusicCoverRequest
  property_count: 15
  slug: finevoice-post-v1-music-cover-request
- name: PostV1MusicMusicgenRequest
  property_count: 8
  slug: finevoice-post-v1-music-musicgen-request
- name: SpeechEnhancementRequest
  property_count: 8
  slug: finevoice-speech-enhancement-request
- name: SpeechToTextRequest
  property_count: 12
  slug: finevoice-speech-to-text-request
jsonld:
- class_count: 24
  name: Finevoice Context
  property_count: 102
  slug: finevoice-context
layout: provider
modified: '2026-10-22'
name: FineVoice (Fineshare)
nav: Providers
network: true
overview: 'FineVoice (Fineshare) publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Openapi API, Changeaudiofile API, and 7 more. Tagged areas include Company, Artificial Intelligence, Voice, Text-to-Speech, and Audio.


  The FineVoice (Fineshare) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  FineVoice (Fineshare)''s developer surface includes changelog, authentication, API reference, documentation, engineering blog, pricing, getting-started guide, and 19 more developer resources.'
plans:
- name: Finevoice Plans Pricing
  plan_count: 8
  slug: finevoice-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: FineVoice (Fineshare) API Rules
  rule_count: 60
  severity_counts:
    error: 50
    hint: 0
    info: 2
    warn: 8
  slug: finevoice-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 75.8
    catalog_earned_first_party: 12.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -15.9
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 32.1
    discoverability: 75.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/finevoice/finevoice-2026-11-03T132030.png
security:
- kind: authentication
  name: Finevoice Authentication
  slug: finevoice-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Finevoice Domain Security
  slug: finevoice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finevoice
tags:
- Company
- Artificial Intelligence
- Voice
- Text-to-Speech
- Audio
website: https://finevoice.ai
---
