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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Inworld Ai Agentic Access
  operation_count: 16
  slug: inworld-ai-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 6
apis:
- description: Discover available models.
  name: Inworld AI Models API
  slug: inworld-ai-models-api
- description: Realtime speech-to-speech sessions.
  name: Inworld AI Realtime API
  slug: inworld-ai-realtime-api
- description: Transcribe audio to text.
  name: Inworld AI Speech To Text API
  slug: inworld-ai-speech-to-text-api
- description: Synthesize speech from text using Inworld voice models.
  name: Inworld AI Text To Speech API
  slug: inworld-ai-text-to-speech-api
- description: Voice cloning, design, and lifecycle.
  name: Inworld AI Voices API
  slug: inworld-ai-voices-api
- description: OpenAI-compatible chat completions through the LLM Router.
  name: Inworld AI Chat Completions API
  slug: inworld-ai-chat-completions-api
- description: Named reusable routers with provider, conditional, and split rules.
  name: Inworld AI Routers API
  slug: inworld-ai-routers-api
artifact_total: 66
asyncapis:
- description: 'AsyncAPI description of Inworld AI''s publicly documented runtime WebSocket surface. Inworld exposes three independent WebSocket endpoints: * **TTS streaming** — bidirectional text-to-speech synthesis '
  name: Inworld AI Runtime WebSocket APIs
  slug: inworld-ai-asyncapi
collections:
- collection_type: postman
  name: Inworld Models API
  slug: postman-inworld-ai-models-api
- collection_type: postman
  name: Inworld Models Realtime API
  slug: postman-inworld-ai-realtime-api
- collection_type: postman
  name: Inworld Models Speech To Text API
  slug: postman-inworld-ai-speech-to-text-api
- collection_type: postman
  name: Inworld Models Text To Speech API
  slug: postman-inworld-ai-text-to-speech-api
- collection_type: postman
  name: Inworld Models Voices API
  slug: postman-inworld-ai-voices-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inworld LLM Router Chat Completions API
  slug: open-inworld-ai-chat-completions-api
- collection_type: open
  name: Inworld Models API
  slug: open-inworld-ai-models-api
- collection_type: open
  name: Inworld Models Realtime API
  slug: open-inworld-ai-realtime-api
- collection_type: open
  name: Inworld LLM Router Routers API
  slug: open-inworld-ai-routers-api
- collection_type: open
  name: Inworld Models Speech To Text API
  slug: open-inworld-ai-speech-to-text-api
- collection_type: open
  name: Inworld Models Text To Speech API
  slug: open-inworld-ai-text-to-speech-api
- collection_type: open
  name: Inworld Models Voices API
  slug: open-inworld-ai-voices-api
- collection_type: open
  name: Inworld Models API
  slug: open-inworld-models-api
- collection_type: open
  name: Inworld Realtime API
  slug: open-inworld-realtime-api
- collection_type: open
  name: Inworld STT API
  slug: open-inworld-stt-api
- collection_type: open
  name: Inworld TTS API
  slug: open-inworld-tts-api
- collection_type: open
  name: Inworld Voice API
  slug: open-inworld-voice-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/inworld-ai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inworld-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/inworld-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inworld-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inworld-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://inworld.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inworld.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inworld.ai/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inworld.ai/api-reference/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inworld.ai/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inworld.ai/llms-full.txt
- group: start
  title: ''
  type: Signup
  url: https://platform.inworld.ai
- group: auth
  title: ''
  type: Authentication
  url: https://platform.inworld.ai/api-keys
- group: start
  title: ''
  type: Sandbox
  url: https://platform.inworld.ai/tts-playground
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inworld.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inworld-ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/inworld-ai/tts
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/inworld-api-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/inworld-nodejs-jwt-sample-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/inworld-runtime-templates-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/voice-agent-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/voice-agent-avatar-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/inworld-ai/livekit_agents
- group: build
  title: ''
  type: SDKs
  url: https://github.com/inworld-ai/livekit_agents_js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/inworld-ai/pipecat
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/langchain-voice-agent-node
- group: build
  title: ''
  type: Tools
  url: https://github.com/inworld-ai/voice-migration-tool
- group: build
  title: ''
  type: Tools
  url: https://github.com/inworld-ai/inworld-tts-onprem
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/multimodal-companion-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/runtime-multimodal-companion-unity
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/living-memories-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/living-memories-unity
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/comic-generator-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/greeting-card-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/zoom-demeanor-evaluator-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/language-learning-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/llm-to-tts-node
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/inworld-ai/runtime-chat-with-docs
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.inworld.ai/resources/rate-limits
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.inworld.ai/tts/resources/billing
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.inworld.ai/stt/resources/billing
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.inworld.ai/realtime/resources/billing
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.inworld.ai/router/resources/billing
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.inworld.ai/portal/billing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inworld.ai/portal/usage
- group: auth
  title: ''
  type: Security
  url: https://docs.inworld.ai/tts/resources/zero-data-retention
- group: other
  title: ''
  type: Deployment
  url: https://docs.inworld.ai/tts/on-premises
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.inworld.ai/release-notes/tts
- group: operate
  title: ''
  type: Migration
  url: https://docs.inworld.ai/tts/resources/elevenlabs-migration
- group: operate
  title: ''
  type: Migration
  url: https://docs.inworld.ai/router/migration/openrouter-to-inworld
- group: operate
  title: ''
  type: Migration
  url: https://docs.inworld.ai/router/migration/anthropic-to-inworld
- group: operate
  title: ''
  type: Support
  url: https://docs.inworld.ai/tts/resources/support
- group: commercial
  title: ''
  type: Pricing
  url: https://inworld.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://inworld.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://plans/inworld-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://rate-limits/inworld-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://finops/inworld-ai-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Inworld AI is a real-time voice AI infrastructure provider. The Inworld platform delivers text-to-speech, speech-to-text, an end-to-end speech-to-speech Realtime API, and an OpenAI- and Anthropic-compatible LLM Router behind one API surface and one billing relationship. Inworld's voice models lead the Artificial Analysis Speech Arena and are used to power voice agents, language-learning apps, AI companions, avatar experiences, game NPCs, and Twilio-backed phone agents. The platform supports instant and professional voice cloning, voice design from natural language, lipsync-grade phoneme alignment, on-premise TTS deployment, and zero-data-retention configurations for regulated workloads.
examples:
- key_count: 2
  name: Inworld Router Chat Completion Example
  slug: inworld-router-chat-completion-example
- key_count: 2
  name: Inworld Stt Transcribe Example
  slug: inworld-stt-transcribe-example
- key_count: 2
  name: Inworld Tts Synthesize Speech Example
  slug: inworld-tts-synthesize-speech-example
features:
- Realtime TTS-2 voice model — 100+ languages, natural-language steering, sub-200ms first-token latency
- Realtime TTS 1.5 Max —
- Realtime TTS 1.5 Mini — cost-optimized voice with ~120ms first-token latency
- Instant voice cloning from short audio samples
- Professional voice cloning with audio processing controls
- Voice design from natural-language descriptions plus optional reference audio
- Word-, character-, and phoneme-level alignment (visemes) for lipsync and avatar rendering
- Custom pronunciation, pause controls, voice tags, and long-text streaming synthesis
- WebSocket TTS for bidirectional streaming synthesis
- Speech-to-Text via multi-provider routing (Whisper variants on Groq) with 99+ languages, prompt biasing, word timestamps, and configurable end-of-turn detection
- Realtime API — speech-to-speech pipeline over WebSocket and WebRTC, OpenAI-Realtime compatible
- Twilio media-stream integration for inbound and outbound phone calls
- MCP server tunneling inside Realtime sessions
- JWT-based realtime authentication (separate Realtime-only API keys)
- LLM Router — OpenAI-and-Anthropic-compatible chat-completions over hundreds of provider models
- Named reusable routers with conditional routing, A/B traffic splitting, and provider routing
- Prompt caching, prompt compression, and integrated web search inside the Router
- Claude-Code-compatible mode for drop-in Claude Code substitution
- Zero Data Retention (ZDR) option for TTS and Realtime
- On-premise TTS deployment for regulated and air-gapped environments
- ElevenLabs voice-migration tool for batch-importing voice clones
- Open-source Python TTS model in the inworld-ai/tts repository
- Integrations with LiveKit Agents, Pipecat, LangChain, and HeyGen avatars
- Unity-side runtime templates for game and avatar use cases
finops:
- name: Inworld Ai Finops
  service_category: AI and Machine Learning
  slug: inworld-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inworld-ai.png
json_schemas:
- name: InworldRouterChatCompletionRequest
  property_count: 19
  slug: inworld-router-chat-completion
- name: InworldTtsSynthesizeRequest
  property_count: 9
  slug: inworld-tts-synthesis
jsonld:
- class_count: 0
  name: Inworld Ai Context
  property_count: 8
  slug: inworld-ai-context
layout: provider
modified: '2026-05-25'
name: Inworld AI
nav: Providers
network: true
overview: 'Inworld AI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Models API, Realtime API, Speech To Text API, and 4 more. Tagged areas include Artificial Intelligence, Voice, Text-to-Speech, Speech-to-Text, and Real-Time.


  The Inworld AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Inworld AI''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, sandbox, code examples, and 50 more developer resources.'
plans:
- name: Inworld Ai Plans Pricing
  plan_count: 5
  slug: inworld-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 4
  name: Inworld Ai Rate Limits
  slug: inworld-ai-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Inworld AI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: inworld-ai-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Inworld AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: inworld-ai-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Inworld AI API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: inworld-ai-rules
score:
  band: exemplar
  composite: 66.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 37.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 13.6
    contract_quality: 74.6
    developer_ergonomics: 76.2
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 78.9
  previous_composite: 66.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/inworld-ai/refs/heads/main/screenshots/inworld-ai-2026-06-20T183526.png
security:
- kind: authentication
  name: Inworld Ai Authentication
  slug: inworld-ai-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Inworld Ai Domain Security
  slug: inworld-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Inworld Ai Trust Center
  slug: inworld-ai-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: inworld-ai
tags:
- Artificial Intelligence
- Voice
- Text-to-Speech
- Speech-to-Text
- Real-Time
- LLM Routing
- Voice Cloning
- Conversational AI
- Game AI
website: https://inworld.ai
---
