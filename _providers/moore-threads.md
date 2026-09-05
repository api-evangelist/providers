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
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-04'
api_count: 4
apis:
- description: HTTP and WebSocket speech synthesis. A non-streaming POST /api/v1/tts/generate returns a complete wav/mp3 for up to 300 characters; a WebSocket /api/v2/tts/stream_generate streams base64 PCM chunks wi
  name: Moore Threads AIBook Text-to-Speech API
  slug: moore-threads-aibook-text-to-speech-api
- description: 'Speech-to-text in two shapes. A realtime WebSocket at /api/v1/asr accepts 16 kHz mono audio and returns SentenceBegin / SentenceChanged / SentenceEnd events with optional punctuation, ITN, disfluency '
  name: Moore Threads AIBook Speech Recognition API
  slug: moore-threads-aibook-speech-recognition-api
- description: A WebSocket voice-conversion service at /api/v1/streaming_vc that re-timbres a live 16 kHz 16-bit mono PCM stream into a target voice and returns 48 kHz PCM. Interaction is StartConversion → binary au
  name: Moore Threads AIBook Streaming Voice Conversion API
  slug: moore-threads-aibook-streaming-voice-conversion-api
- description: An LLM inference endpoint operated on Moore Threads MTT S5000 GPUs and sold as a subscription for AI coding tools. It speaks two wire protocols from one host — the Anthropic Messages protocol at the r
  name: KUAE Cloud Coding Plan API
  slug: kuae-cloud-coding-plan-api
artifact_total: 9
asyncapis:
- description: ''
  name: Moore Threads Webhooks
  slug: moore-threads-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.mthreads.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mthreads.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mthreads.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mthreads.com/tts/stream-tts/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mthreads.com/kuaecloud/kuaecloud-doc-online/coding_plan/user_guide
- group: operate
  title: ''
  type: Support
  url: https://www.mthreads.com/support/FAQ
- group: company
  title: ''
  type: Blog
  url: https://blog.mthreads.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MooreThreads
- group: start
  title: ''
  type: SignUp
  url: https://coding-plan.kuaecloud.net/free_apply
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.mthreads.com/kuaecloud/kuaecloud-doc-online/terms/user_agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mthreads.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/moore-threads-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/moore-threads-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moore-threads-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moore-threads-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/moore-threads-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/moore-threads-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moore-threads-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moore-threads-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moore-threads-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moore-threads-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moore-threads-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moore-threads-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/moore-threads-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/moore-threads-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/moore-threads-components.yml
created: '2026-08-26'
description: 'Moore Threads (摩尔线程智能科技) is a Chinese GPU company founded in June 2020 that builds full-function GPUs and the MUSA (Meta-computing Unified System Architecture) software stack — a CUDA-alternative programming environment covering the MUSA SDK, muDNN, muBLAS, MCCL, Triton-MUSA and the Musify CUDA-porting toolkit. Alongside the silicon and the SDK it operates a small but real public API surface: the AIBook speech platform (HTTP and WebSocket text-to-speech, streaming and recording-file speech recognition, and streaming voice conversion on aibook-api.mthreads.com), the KUAE Cloud (夸娥云) Coding Plan — an OpenAI- and Anthropic-compatible LLM inference endpoint at coding-plan-endpoint.kuaecloud.net serving GLM-4.7 on MTT S5000 GPUs — and the "摩影元像" digital-human Web SDK distributed on npm as `mtai`. None of these surfaces publishes a machine-readable contract; every operation is documented as prose, parameter tables and curl/Python samples on docs.mthreads.com, and access tokens are
  issued by contacting sales.'
image: https://www.mthreads.com/favicon/logo.png
layout: provider
modified: '2026-08-26'
name: Moore Threads
nav: Providers
network: true
overview: 'Moore Threads publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, GPU, Artificial Intelligence, Machine-Learning, and Semiconductors.


  The Moore Threads catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Moore Threads'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
plans:
- name: Moore Threads Plans Pricing
  plan_count: 4
  slug: moore-threads-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 13
  name: Moore Threads Rate Limits
  slug: moore-threads-rate-limits
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 48.7
    commercial_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 58.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 46.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moore-threads/refs/heads/main/screenshots/moore-threads-2026-09-02T150738.png
security:
- kind: authentication
  name: Moore Threads Authentication
  slug: moore-threads-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Moore Threads Domain Security
  slug: moore-threads-domain-security
  summary_line: TLSv1.3 · HSTS
slug: moore-threads
tags:
- Company
- GPU
- Artificial Intelligence
- Machine-Learning
- Semiconductors
- Speech Recognition
- Text-to-Speech
- Voice
- LLM Inference
- Cloud Computing
- Developer Tools
- China
website: https://www.mthreads.com/
---
