---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 10
  human_in_the_loop: 10
  name: Gladia Agentic Access
  operation_count: 21
  slug: gladia-agentic-access
  summary_line: 21 operations · 10 acting · 10 human-in-the-loop
api_count: 9
apis:
- description: WebSocket API for real-time live audio transcription with sub-second latency, supporting multi-language detection, live speaker diarization, and streaming audio intelligence. Individual sessions are c
  name: Gladia Live (Real-time) API
  slug: gladia-live-real-time-api
- description: The AudioToText API from Gladia — 1 operation(s) for audiototext.
  name: Gladia AudioToText API
  slug: gladia-audiototext-api
- description: The File Management API from Gladia — 1 operation(s) for file management.
  name: Gladia File Management API
  slug: gladia-file-management-api
- description: The Job History API from Gladia — 1 operation(s) for job history.
  name: Gladia Job History API
  slug: gladia-job-history-api
- description: The Live V2 API from Gladia — 3 operation(s) for live v2.
  name: Gladia Live V2 API
  slug: gladia-live-v2-api
- description: The OpenRouter API from Gladia — 1 operation(s) for openrouter.
  name: Gladia OpenRouter API
  slug: gladia-openrouter-api
- description: The Pre-recorded V2 API from Gladia — 3 operation(s) for pre-recorded v2.
  name: Gladia Pre-recorded V2 API
  slug: gladia-pre-recorded-v2-api
- description: The Transcription V1 API from Gladia — 2 operation(s) for transcription v1.
  name: Gladia Transcription V1 API
  slug: gladia-transcription-v1-api
- description: The Transcription V2 API from Gladia — 3 operation(s) for transcription v2.
  name: Gladia Transcription V2 API
  slug: gladia-transcription-v2-api
artifact_total: 36
collections:
- collection_type: postman
  name: Gladia Control AudioToText API
  slug: postman-gladia-audiototext-api
- collection_type: postman
  name: Gladia Control AudioToText File Management API
  slug: postman-gladia-file-management-api
- collection_type: postman
  name: Gladia Control AudioToText Job History API
  slug: postman-gladia-job-history-api
- collection_type: postman
  name: Gladia Control AudioToText Live V2 API
  slug: postman-gladia-live-v2-api
- collection_type: postman
  name: Gladia Control AudioToText OpenRouter API
  slug: postman-gladia-openrouter-api
- collection_type: postman
  name: Gladia Control AudioToText Pre-recorded V2 API
  slug: postman-gladia-pre-recorded-v2-api
- collection_type: postman
  name: Gladia Control AudioToText Transcription V1 API
  slug: postman-gladia-transcription-v1-api
- collection_type: postman
  name: Gladia Control AudioToText Transcription V2 API
  slug: postman-gladia-transcription-v2-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/gladia/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gladia-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gladia-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gladia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gladia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gladia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gladia.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gladia.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gladiaio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gladia-io
- group: other
  title: ''
  type: X
  url: https://x.com/gladia_io
- group: company
  title: ''
  type: Blog
  url: https://www.gladia.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.gladia.io/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gladia.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gladia.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/gladia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gladia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gladia-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/gladia-control-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gladia-init-transcription-request.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gladia-audio-upload-response.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gladia-init-pre-recorded-transcription-response.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gladia-diarization-config.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/gladia-live-event-payload.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/gladia-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/gladia-context.jsonld
created: 2026-06-12
description: Gladia is an AI audio infrastructure platform that offers speech-to-text transcription via both REST and WebSocket APIs, supporting asynchronous pre-recorded audio processing and real-time live transcription. The platform provides speaker diarization, automatic language detection across 100+ languages, word-level timestamps, and audio intelligence features powered by large language models. Authentication uses an API key passed via the x-gladia-key HTTP header against the base URL https://api.gladia.io/v2/. Gladia offers a free tier with 10 hours per month, metered paid plans starting at $0.61/hour for async and $0.75/hour for real-time, and custom enterprise pricing with zero data retention and SLA guarantees.
examples:
- key_count: 11
  name: Gladia Initiate Transcription
  slug: gladia-initiate-transcription
- key_count: 7
  name: Gladia Live Session Config
  slug: gladia-live-session-config
- key_count: 3
  name: Gladia Transcription Job Response
  slug: gladia-transcription-job-response
- key_count: 1
  name: Gladia Upload Audio Url
  slug: gladia-upload-audio-url
finops:
- name: Gladia Finops
  service_category: ''
  slug: gladia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gladia.png
json_schemas:
- name: AudioUploadResponse
  property_count: 2
  slug: gladia-audio-upload-response
- name: DiarizationConfigDTO
  property_count: 3
  slug: gladia-diarization-config
- name: InitPreRecordedTranscriptionResponse
  property_count: 2
  slug: gladia-init-pre-recorded-transcription-response
- name: InitTranscriptionRequest
  property_count: 26
  slug: gladia-init-transcription-request
- name: LiveEventPayload
  property_count: 1
  slug: gladia-live-event-payload
jsonld:
- class_count: 0
  name: Gladia Context
  property_count: 30
  slug: gladia-context
layout: provider
modified: 2026-06-12
name: Gladia
nav: Providers
network: true
overview: 'Gladia publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Live (Real-time) API, AudioToText API, File Management API, and 6 more. Tagged areas include Speech-to-Text, Transcription, Audio Intelligence, Real-Time, and Speaker Diarization.


  The Gladia catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gladia''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 21 more developer resources.'
plans:
- name: Gladia Plans Pricing
  plan_count: 3
  slug: gladia-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 8
  name: Gladia Rate Limits
  slug: gladia-rate-limits
rules:
- name: Gladia API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gladia-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.4
  delta: -3.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 64.1
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gladia/refs/heads/main/screenshots/gladia-2026-06-20T181856.png
security:
- kind: authentication
  name: Gladia Authentication
  slug: gladia-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gladia Domain Security
  slug: gladia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Gladia Vulnerability Disclosure
  slug: gladia-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Gladia Trust Center
  slug: gladia-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: gladia
tags:
- Speech-to-Text
- Transcription
- Audio Intelligence
- Real-Time
- Speaker Diarization
- Translation
- WebSocket
- REST
website: https://www.gladia.io/
---
