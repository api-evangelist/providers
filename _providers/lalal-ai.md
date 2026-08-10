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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 15
  human_in_the_loop: 2
  name: Lalal Ai Agentic Access
  operation_count: 15
  slug: lalal-ai-agentic-access
  summary_line: 15 operations · 15 acting · 2 human-in-the-loop
api_count: 4
apis:
- description: The Batch Stem Separation API from LALAL.AI — 3 operation(s) for batch stem separation.
  name: LALAL.AI Batch Stem Separation API
  slug: lalal-ai-batch-stem-separation-api
- description: The Common API from LALAL.AI — 6 operation(s) for common.
  name: LALAL.AI Common API
  slug: lalal-ai-common-api
- description: The Stem Separation API from LALAL.AI — 4 operation(s) for stem separation.
  name: LALAL.AI Stem Separation API
  slug: lalal-ai-stem-separation-api
- description: The Voice Change API from LALAL.AI — 2 operation(s) for voice change.
  name: LALAL.AI Voice Change API
  slug: lalal-ai-voice-change-api
artifact_total: 46
collections:
- collection_type: postman
  name: LALAL.AI Batch Stem Separation API
  slug: postman-lalal-ai-batch-stem-separation-api
- collection_type: postman
  name: LALAL.AI Batch Stem Separation Common API
  slug: postman-lalal-ai-common-api
- collection_type: postman
  name: LALAL.AI Batch Stem Separation API
  slug: postman-lalal-ai-stem-separation-api
- collection_type: postman
  name: LALAL.AI Batch Stem Separation Voice Change API
  slug: postman-lalal-ai-voice-change-api
- collection_type: open
  name: LALAL.AI API
  slug: open-lalal-ai-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/lalalai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lalal-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lalal-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lalal-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.lalal.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.lalal.ai/api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lalal.ai/api/v1/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.lalal.ai/api/help/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lalal.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.lalal.ai/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.lalal.ai/changelog/
- group: operate
  title: ''
  type: Support
  url: https://www.lalal.ai/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lalal.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lalal.ai/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OmniSaleGmbH
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/OmniSaleGmbH/lalalai
- group: operate
  title: ''
  type: ContactUs
  url: mailto:support@lalal.ai
- group: build
  title: ''
  type: SDKs
  url: https://github.com/OmniSaleGmbH/lalalai/tree/main/api-v1/python
- group: commercial
  title: ''
  type: Plans
  url: plans/lalal-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lalal-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lalal-ai-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: LALAL.AI is an AI-powered audio separation and voice technology platform operated by OmniSale GmbH. It uses proprietary neural networks (Andromeda, Perseus, Orion, Phoenix, Lyra, Lynx) to isolate vocals, instruments, drums, bass, guitars, piano, synth, strings, and wind from mixed audio, clean voice recordings, and clone or convert voices with consent. The company ships a web app, native desktop, iOS and Android apps, a VST plug-in for DAWs, and a production REST API (v1) for embedding stem separation and voice cloning into third-party SaaS, media, and post-production pipelines.
examples:
- key_count: 2
  name: Lalal Ai Change Voice Example
  slug: lalal-ai-change-voice-example
- key_count: 2
  name: Lalal Ai Check Example
  slug: lalal-ai-check-example
- key_count: 2
  name: Lalal Ai Multistem Example
  slug: lalal-ai-multistem-example
- key_count: 2
  name: Lalal Ai Split Stem Separator Example
  slug: lalal-ai-split-stem-separator-example
- key_count: 2
  name: Lalal Ai Upload Example
  slug: lalal-ai-upload-example
features:
- 'Six proprietary neural networks: Andromeda (6th-gen, 2025), Perseus (transformer), Orion, Phoenix, Lyra (dereverb / demuser), and Lynx'
- Stem separation for vocals, drum, bass, piano, electric guitar, acoustic guitar, synthesizer, strings, and wind instruments
- Single-task and batch (multi-file) variants for stem_separator, demuser, and voice_clean endpoints
- Multistem endpoint extracts up to six stems in a single request
- Demuser endpoint isolates music from non-music components
- Voice Clean endpoint removes background music and ambient noise from spoken-word audio with 3-level noise cancelling
- Change Voice endpoint applies legal artist Voice Packs (ALEX_KAYE, STASIA_FAYE, NICOLAAS_HAAS, NIK_ZEL, OLIA_CHEBO, YVAR_DE_GROOT, VETRANA) or user-trained custom Voice Packs from the Voice Cloner
- Voice Packs list endpoint returns user-trained packs with previews, language metadata, and ready-to-use state
- Dereverb option for vocals/voice stems plus accent intensity, pitch shifting, and tonality reference controls for voice conversion
- Lead/back vocal splitter via the multivocal parameter on stem separation
- Asynchronous job model — POST returns task_id, poll /check/ for progress (success, progress, error, cancelled) and signed download URLs for stem_track and back_track
- Cancel individual tasks or all running tasks; delete uploaded source files
- Limits endpoint returns remaining processing minutes and the plan tier
- Output formats MP3, WAV, FLAC, AAC, OGG (defaults to source format)
- Extraction levels Clear Cut and Deep Extraction on Perseus
- File upload via single-PUT or multipart for large files (up to 10 GB with valid license)
- 24-hour retention on uploaded source files
- Official OpenAPI 3.1 spec served at /api/v1/openapi.json with Swagger-style explorer at /api/v1/docs/
- Official Python example client maintained at github.com/OmniSaleGmbH/lalalai
- API access included on Pro and higher plans, with custom enterprise pricing available
finops:
- name: Lalal Ai Finops
  service_category: ''
  slug: lalal-ai-finops
image: https://www.lalal.ai/static/images/og/preview.png
json_schemas:
- name: LALAL.AI Split Task Result
  property_count: 12
  slug: lalal-ai-split-task
- name: LALAL.AI Upload Response
  property_count: 7
  slug: lalal-ai-upload
- name: LALAL.AI Voice Pack
  property_count: 6
  slug: lalal-ai-voice-pack
jsonld:
- class_count: 35
  name: Lalal Ai Context
  property_count: 5
  slug: lalal-ai-context
layout: provider
modified: '2026-05-25'
name: LALAL.AI
nav: Providers
network: true
overview: 'LALAL.AI publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Batch Stem Separation API, Common API, Stem Separation API, and 1 more. Tagged areas include AI, Artificial Intelligence, Audio, Audio Processing, and Stem Separation.


  The LALAL.AI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  LALAL.AI''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, changelog, and 14 more developer resources.'
plans:
- name: Lalal Ai Plans Pricing
  plan_count: 9
  slug: lalal-ai-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 0
  name: Lalal Ai Rate Limits
  slug: lalal-ai-rate-limits
rules:
- name: LALAL.AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lalal-ai-jsonschema-spectral-rules
- name: LALAL.AI API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 2
  slug: lalal-ai-rules
score:
  band: strong
  composite: 61.4
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 74.9
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lalal-ai/refs/heads/main/screenshots/lalal-ai-2026-06-20T184249.png
security:
- kind: authentication
  name: Lalal Ai Authentication
  slug: lalal-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lalal Ai Domain Security
  slug: lalal-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lalal-ai
tags:
- AI
- Artificial Intelligence
- Audio
- Audio Processing
- Stem Separation
- Vocal Removal
- Voice Cleaning
- Voice Cloning
- Voice Changer
- Music
- Machine Learning
- DSP
website: https://www.lalal.ai
---
