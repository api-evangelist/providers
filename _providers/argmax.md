---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: A local transcription server for macOS that is API-compatible with the Deepgram Speech-to-Text (Live) API, exposing a WebSocket streaming interface (default ws://localhost:50060) driven by the officia
  name: Argmax Local Server
  slug: argmax-local-server
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argmax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.argmaxinc.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.argmaxinc.com
- group: docs
  title: ''
  type: Documentation
  url: https://app.argmaxinc.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.argmaxinc.com/docs/guides/using-local-server
- group: start
  title: ''
  type: GettingStarted
  url: https://app.argmaxinc.com/docs/guides/upgrading-to-pro-sdk
- group: other
  title: ''
  type: Models
  url: https://app.argmaxinc.com/docs/models
- group: commercial
  title: ''
  type: Pricing
  url: https://www.argmaxinc.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.argmaxinc.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/argmaxinc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.argmaxinc.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://app.argmaxinc.com/docs/changelog
- group: start
  title: ''
  type: Sandbox
  url: https://testflight.apple.com/join/Q1cywTJw
- group: operate
  title: ''
  type: Support
  url: mailto:pro-sdk-support@argmaxinc.com
- group: start
  title: ''
  type: SignUp
  url: https://app.argmaxinc.com
- group: start
  title: ''
  type: Login
  url: https://app.argmaxinc.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.argmaxinc.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.argmaxinc.com/privacy
- group: build
  title: ''
  type: Packages
  url: packages/argmax-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/argmax-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/argmax-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/argmax-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/argmax-llms.txt
created: '2026-07-17'
description: 'Argmax, Inc. builds on-device inference infrastructure that lets developers run foundation models locally on user devices for privacy, real-time performance, and predictable per-device costs. Its products are commercial Pro SDKs on top of open-source cores: WhisperKit (speech-to-text with file transcription, real-time streaming, word timestamps, and subtitle export), SpeakerKit (speaker recognition, diarization, and voice-activity detection), DiffusionKit (image generation for Flux.1 and Stable Diffusion on Apple Silicon), and TTSKit. Argmax also ships the Argmax Local Server for macOS, a local transcription server that is API-compatible with the Deepgram Speech-to-Text (Live) API and driven by an official Node client (@argmaxinc/local-server). Devices are licensed through the ArgmaxSDK (ax_-prefixed API keys) with device-based billing measured by unique licenseId. Backed by General Catalyst.'
image: https://cdn.prod.website-files.com/677fd5c33a098b58d447e17b/678ec5cb674cb149d3c4c026_Argmax-OpenGraph.png
layout: provider
modified: '2026-07-18'
name: Argmax
nav: Providers
network: true
overview: 'Argmax publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Artificial Intelligence, Machine-Learning, and On-Device Inference.


  Argmax''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, changelog, sandbox, and 16 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/argmax/refs/heads/main/screenshots/argmax-2026-07-25T201142.png
security:
- kind: authentication
  name: Argmax Authentication
  slug: argmax-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Argmax Domain Security
  slug: argmax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argmax
tags:
- Company
- Enterprise
- Artificial Intelligence
- Machine-Learning
- On-Device Inference
- Speech Recognition
- Speech-to-Text
- Transcription
- Speaker Diarization
- Image-Generation
- SDK
- Apple Silicon
- Edge AI
website: https://www.argmaxinc.com
---
