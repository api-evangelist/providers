---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-17'
api_count: 11
apis:
- description: The Velma 2 Accent Batch API from Modulate — 1 operation(s) for velma 2 accent batch.
  name: Modulate Velma 2 Accent Batch API
  slug: modulate-velma-2-accent-batch-api
- description: The Velma 2 Ai Music Detection Batch API from Modulate — 1 operation(s) for velma 2 ai music detection batch.
  name: Modulate Velma 2 Ai Music Detection Batch API
  slug: modulate-velma-2-ai-music-detection-batch-api
- description: The Velma 2 Batch API from Modulate — 2 operation(s) for velma 2 batch.
  name: Modulate Velma 2 Batch API
  slug: modulate-velma-2-batch-api
- description: The Velma 2 Emotion Batch API from Modulate — 1 operation(s) for velma 2 emotion batch.
  name: Modulate Velma 2 Emotion Batch API
  slug: modulate-velma-2-emotion-batch-api
- description: The Velma 2 Language Detection Batch API from Modulate — 1 operation(s) for velma 2 language detection batch.
  name: Modulate Velma 2 Language Detection Batch API
  slug: modulate-velma-2-language-detection-batch-api
- description: The Velma 2 Music Detection Batch API from Modulate — 1 operation(s) for velma 2 music detection batch.
  name: Modulate Velma 2 Music Detection Batch API
  slug: modulate-velma-2-music-detection-batch-api
- description: The Velma 2 Pii Phi Redaction Batch API from Modulate — 1 operation(s) for velma 2 pii phi redaction batch.
  name: Modulate Velma 2 Pii Phi Redaction Batch API
  slug: modulate-velma-2-pii-phi-redaction-batch-api
- description: The Velma 2 Stt Batch API from Modulate — 1 operation(s) for velma 2 stt batch.
  name: Modulate Velma 2 Stt Batch API
  slug: modulate-velma-2-stt-batch-api
- description: The Velma 2 Stt Batch English Vfast API from Modulate — 1 operation(s) for velma 2 stt batch english vfast.
  name: Modulate Velma 2 Stt Batch English Vfast API
  slug: modulate-velma-2-stt-batch-english-vfast-api
- description: The Velma 2 Stt Batch Multilingual Vfast API from Modulate — 1 operation(s) for velma 2 stt batch multilingual vfast.
  name: Modulate Velma 2 Stt Batch Multilingual Vfast API
  slug: modulate-velma-2-stt-batch-multilingual-vfast-api
- description: The Velma 2 Synthetic Voice Detection Batch API from Modulate — 1 operation(s) for velma 2 synthetic voice detection batch.
  name: Modulate Velma 2 Synthetic Voice Detection Batch API
  slug: modulate-velma-2-synthetic-voice-detection-batch-api
artifact_total: 35
asyncapis:
- description: 'Real-time AI music detection over WebSocket. The client streams audio and receives per-window vocal AI verdicts as they become available, followed by a final clip-level summary including instrumental '
  name: Velma 2 AI Music Detection Streaming API
  slug: modulate-ai-music-detection-streaming-asyncapi
- description: Real-time frame-level music and speech classification over WebSocket. The client streams audio and receives per-frame probabilities as they become available, followed by a final summary on completion.
  name: Velma 2 Music Detection Streaming API
  slug: modulate-music-detection-streaming-asyncapi
- description: Real-time speech-to-text with PII/PHI redaction over WebSocket. Provides live transcription with automatic language detection, PII/PHI detection and text redaction, and a redacted MP3 audio clip along
  name: Velma 2 PII/PHI Redaction Streaming API
  slug: modulate-pii-phi-redaction-streaming-asyncapi
- description: Real-time speech-to-text over WebSocket. Provides live multilingual transcription with automatic per-utterance language detection, delivering each utterance as it is completed. Optional capabilities -
  name: Velma 2 STT Streaming API
  slug: modulate-stt-streaming-asyncapi
- description: Low-latency English speech-to-text over WebSocket. Pure transcription only - no diarization, emotion detection, accent detection, or PII/PHI tagging. Streams interim partial transcripts while audio ar
  name: Velma 2 STT Streaming English v2 API
  slug: modulate-stt-streaming-english-v2-asyncapi
- description: Real-time synthetic voice detection for single-speaker audio over WebSocket. The client streams audio and receives per-frame verdicts as they become available.
  name: Velma 2 Synthetic Voice Detection Streaming API
  slug: modulate-synthetic-voice-detection-streaming-asyncapi
- description: Streaming velma-2 over WebSocket. Transcribes and analyzes a live audio stream against a client-supplied analysis configuration, emitting JSON events that describe clips and analysis results as they a
  name: Modulate Velma-2 Streaming Server
  slug: modulate-velma-2-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Velma 2 Accent Batch API
  slug: open-modulate-velma-2-accent-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Ai Music Detection Batch API
  slug: open-modulate-velma-2-ai-music-detection-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Batch API
  slug: open-modulate-velma-2-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Emotion Batch API
  slug: open-modulate-velma-2-emotion-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Language Detection Batch API
  slug: open-modulate-velma-2-language-detection-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Music Detection Batch API
  slug: open-modulate-velma-2-music-detection-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Pii Phi Redaction Batch API
  slug: open-modulate-velma-2-pii-phi-redaction-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Stt Batch API
  slug: open-modulate-velma-2-stt-batch-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Stt Batch English Vfast API
  slug: open-modulate-velma-2-stt-batch-english-vfast-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Stt Batch Multilingual Vfast API
  slug: open-modulate-velma-2-stt-batch-multilingual-vfast-api
- collection_type: open
  name: Velma 2 Accent Batch Velma 2 Synthetic Voice Detection Batch API
  slug: open-modulate-velma-2-synthetic-voice-detection-batch-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/modulate-velma-2-batch-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/modulate-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.modulate.ai/compliance
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modulate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/modulate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://modulate.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.modulate.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.modulate.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.modulate.ai/api-reference/velma/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.modulate.ai/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.modulate.ai/support
- group: company
  title: ''
  type: Blog
  url: https://www.modulate.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.modulate.ai/api-pricing
- group: start
  title: ''
  type: SignUp
  url: https://platform.modulate.ai/signup-request
- group: start
  title: ''
  type: Login
  url: https://platform.modulate.ai/dashboard/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.modulate.ai/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.modulate.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modulateai
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modulate-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/modulate-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/modulate-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/modulate-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/modulate-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/modulate-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/modulate-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/modulate-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/modulate-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/modulate-velma-2-streaming-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Modulate is a voice AI company based in Cambridge, Massachusetts, building audio-native voice intelligence for trust, safety, and conversation understanding. Its Velma-2 platform exposes a suite of REST (batch) and WebSocket (streaming) model APIs — multilingual and English speech-to-text transcription with speaker diarization, deepfake (synthetic voice) detection, emotion and accent detection, PII/PHI tagging and redaction, language detection, and music/speech and AI-music detection — alongside Velma conversation analysis (behaviors, topics, sentiment, participant roles) and the ToxMod voice-safety product for gaming and social platforms. Authentication is via an X-API-Key header (an api_key query parameter for WebSocket streams), billed per hour of audio processed. Backed by Sierra Ventures.
image: https://cdn.prod.website-files.com/67ed675f8e30d86d14c51adb/6a0c34c788a0bb22111adc3a_Modulate%20Thumbnail%20master.png
layout: provider
mcp_servers:
- description: ''
  name: modulate-mcp.yml
  slug: modulate-mcpyml
modified: '2026-07-20'
name: Modulate
nav: Providers
network: true
overview: 'Modulate publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Velma 2 Accent Batch API, Velma 2 Ai Music Detection Batch API, Velma 2 Batch API, and 8 more. Tagged areas include Company, Ai, Voice AI, Speech to Text, and Transcription.


  The Modulate catalog on APIs.io includes 7 event-driven AsyncAPI specifications.


  Modulate''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
random_paper: 114
rate_limits:
- limit_count: 3
  name: Modulate Rate Limits
  slug: modulate-rate-limits
score:
  band: strong
  composite: 57.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 70.8
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 57.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/modulate/refs/heads/main/screenshots/modulate-2026-08-07T184031.png
security:
- kind: authentication
  name: Modulate Authentication
  slug: modulate-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Modulate Domain Security
  slug: modulate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Modulate Trust Center
  slug: modulate-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: modulate
tags:
- Company
- Ai
- Voice AI
- Speech to Text
- Transcription
- Deepfake Detection
- Content Moderation
- Trust and Safety
- Audio
- Machine Learning
- PII Redaction
- Voice Intelligence
website: https://modulate.ai/
---
