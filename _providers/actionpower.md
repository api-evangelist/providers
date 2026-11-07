---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Actionpower Agentic Access
  operation_count: 40
  slug: actionpower-agentic-access
  summary_line: 40 operations · 28 acting
api_count: 4
apis:
- description: Bidirectional gRPC streaming speech recognition served from apis.daglo.ai. The provider publishes the proto3 service definition (package dagloapis.speech.v1, rpc StreamingRecognize) in its developer g
  name: daglo Realtime Streaming STT (gRPC)
  slug: daglo-realtime-streaming-stt-grpc
- baseURL: https://apis.daglo.ai
  baseurl_source: declared
  description: The Image API from Actionpower — 7 operation(s) for image.
  name: Actionpower Image API
  slug: actionpower-image-api
- baseURL: https://apis.daglo.ai
  baseurl_source: declared
  description: The NLP API from Actionpower — 7 operation(s) for nlp.
  name: Actionpower NLP API
  slug: actionpower-nlp-api
- baseURL: https://apis.daglo.ai
  baseurl_source: declared
  description: The STT API from Actionpower — 5 operation(s) for stt.
  name: Actionpower STT API
  slug: actionpower-stt-api
- baseURL: https://apis.daglo.ai
  baseurl_source: declared
  description: The TTS API from Actionpower — 1 operation(s) for tts.
  name: Actionpower TTS API
  slug: actionpower-tts-api
- baseURL: https://apis.daglo.ai
  baseurl_source: declared
  description: The Video API from Actionpower — 10 operation(s) for video.
  name: Actionpower Video API
  slug: actionpower-video-api
artifact_total: 18
asyncapis:
- description: ''
  name: Actionpower Daglo Webhooks
  slug: actionpower-daglo-webhooks
common:
- group: other
  href: https://artifacts.apis.io/actionpower/capabilities/actionpower-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/actionpower-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/actionpower/agentic-access/actionpower-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/actionpower-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://daglo.ai/
- group: company
  title: ''
  type: Website
  url: https://actionpower.kr/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.daglo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.daglo.ai/guide/en/
- group: docs
  title: ''
  type: APIReference
  url: https://apis.daglo.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.daglo.ai/guide/en/Quick-Speech-Voice-To-Text.html
- group: operate
  title: ''
  type: Support
  url: https://developers.daglo.ai/guide/en/FAQ.html
- group: company
  title: ''
  type: Blog
  url: https://daglo.ai/d/ko/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://daglo.ai/d/ko/blog/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/actionpower
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.daglo.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://daglo.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://developers.daglo.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daglo.ai/d/en/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daglo.ai/d/en/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://daglo.ai/d/en/enterprise
- group: agent
  href: https://artifacts.apis.io/actionpower/llms/actionpower-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/actionpower-llms.txt
- group: build
  href: https://artifacts.apis.io/actionpower/packages/actionpower-packages.yml
  title: ''
  type: Packages
  url: packages/actionpower-packages.yml
- group: build
  href: https://artifacts.apis.io/actionpower/packages/actionpower-packages.yml
  title: ''
  type: SDKs
  url: packages/actionpower-packages.yml
- group: agent
  href: https://artifacts.apis.io/actionpower/mcp/actionpower-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/actionpower-mcp.yml
- group: design
  href: https://artifacts.apis.io/actionpower/conventions/actionpower-conventions.yml
  title: ''
  type: Conventions
  url: conventions/actionpower-conventions.yml
- group: design
  href: https://artifacts.apis.io/actionpower/conformance/actionpower-conformance.yml
  title: ''
  type: Conformance
  url: conformance/actionpower-conformance.yml
- group: design
  href: https://artifacts.apis.io/actionpower/errors/actionpower-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/actionpower-problem-types.yml
- group: design
  href: https://artifacts.apis.io/actionpower/lifecycle/actionpower-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/actionpower-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/actionpower/changelog/actionpower-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/actionpower-changelog.yml
- group: auth
  href: https://artifacts.apis.io/actionpower/authentication/actionpower-authentication.yml
  title: ''
  type: Authentication
  url: authentication/actionpower-authentication.yml
- group: auth
  href: https://artifacts.apis.io/actionpower/security/actionpower-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/actionpower-domain-security.yml
- group: start
  href: https://artifacts.apis.io/actionpower/sandbox/actionpower-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/actionpower-sandbox.yml
- group: design
  href: https://artifacts.apis.io/actionpower/data-model/actionpower-data-model.yml
  title: ''
  type: DataModel
  url: data-model/actionpower-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/actionpower/plans/actionpower-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/actionpower-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/actionpower/rate-limits/actionpower-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/actionpower-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/actionpower/asyncapi/actionpower-daglo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/actionpower-daglo-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/actionpower/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/actionpower/grpc/actionpower-speech.proto
  title: ''
  type: Protobuf
  url: grpc/actionpower-speech.proto
- group: build
  href: https://artifacts.apis.io/actionpower/examples/actionpower-daglo-examples.yml
  title: ''
  type: Examples
  url: examples/actionpower-daglo-examples.yml
- group: other
  href: https://artifacts.apis.io/actionpower/overlays/actionpower-daglo-cloud-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/actionpower-daglo-cloud-api-overlay.yaml
created: '2026-09-06'
description: 'ActionPower Corp. (주식회사 액션파워) is a Seoul-based deep-tech AI company founded in 2016 that builds its own end-to-end speech recognition, speaker diarization, speech synthesis and small-language-model stack, and sells it two ways: as daglo, a voice-intelligence workspace that records, transcribes, summarizes and translates meetings, calls and lectures for more than two million users; and as the daglo Cloud API, a developer platform at apis.daglo.ai offering synchronous and asynchronous speech-to-text, bidirectional-streaming realtime STT over gRPC, chat completion, dialogue summarization, meeting minutes, paragraph splitting and text-to-speech. The company is ISO 27001 certified, ships an on-premise closed-network deployment for public sector, finance, healthcare and broadcast customers, and reports customers including LG Electronics, KT Skylife, NH Nonghyup Bank and the Daegu Metropolitan Government.'
finops:
- has_sources: true
  method: derived
  name: Actionpower Finops
  primary_unit: call
  service_category: ''
  slug: actionpower-finops
  template: false
image: https://daglo.ai/d/og-image
layout: provider
modified: '2026-09-06'
name: Actionpower
nav: Providers
network: true
overview: 'Actionpower publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Image API, NLP API, STT API, and 3 more. Tagged areas include Speech Recognition, Speech-to-Text, Text-to-Speech, Natural Language Processing, and Artificial Intelligence.


  The Actionpower catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Actionpower''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Actionpower Plans Pricing
  plan_count: 9
  slug: actionpower-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Actionpower Rate Limits
  slug: actionpower-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Actionpower API Rules
  rule_count: 59
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 2
  slug: actionpower-rules
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 67.5
    catalog_earned_first_party: 20.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 54.9
    developer_ergonomics: 63.7
    discoverability: 78.6
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 59.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 7.7
      derived: 1
      marker_coverage: 15.4
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/actionpower/actionpower-2026-10-11T092715.png
security:
- kind: authentication
  name: Actionpower Authentication
  slug: actionpower-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Actionpower Domain Security
  slug: actionpower-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: Stream realtime speech to text with daglo over gRPC
  slug: actionpower-realtime-streaming-stt
- name: Summarize a conversation and generate meeting minutes with daglo
  slug: actionpower-summarize-and-minutes
- name: Synthesize speech from text with daglo TTS
  slug: actionpower-synthesize-speech
- name: Transcribe long audio with the daglo Cloud API
  slug: actionpower-transcribe-long-audio
slug: actionpower
tags:
- Speech Recognition
- Speech-to-Text
- Text-to-Speech
- Natural Language Processing
- Artificial Intelligence
- Transcription
- Voice
- Meeting Intelligence
- gRPC
- South Korea
website: https://daglo.ai/
---
