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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-08-11'
api_count: 14
apis:
- description: The 11labs API from KugelAudio — 6 operation(s) for 11labs.
  name: KugelAudio 11labs API
  slug: kugelaudio-11labs-api
- description: The Audio API from KugelAudio — 1 operation(s) for audio.
  name: KugelAudio Audio API
  slug: kugelaudio-audio-api
- description: The billing API from KugelAudio — 2 operation(s) for billing.
  name: KugelAudio billing API
  slug: kugelaudio-billing-api
- description: The Dictionaries API from KugelAudio — 5 operation(s) for dictionaries.
  name: KugelAudio Dictionaries API
  slug: kugelaudio-dictionaries-api
- description: The Health API from KugelAudio — 1 operation(s) for health.
  name: KugelAudio Health API
  slug: kugelaudio-health-api
- description: The license API from KugelAudio — 12 operation(s) for license.
  name: KugelAudio license API
  slug: kugelaudio-license-api
- description: The Models API from KugelAudio — 1 operation(s) for models.
  name: KugelAudio Models API
  slug: kugelaudio-models-api
- description: The Normalize API from KugelAudio — 1 operation(s) for normalize.
  name: KugelAudio Normalize API
  slug: kugelaudio-normalize-api
- description: The Post Overrides API from KugelAudio — 1 operation(s) for post overrides.
  name: KugelAudio Post Overrides API
  slug: kugelaudio-post-overrides-api
- description: The Predict API from KugelAudio — 1 operation(s) for predict.
  name: KugelAudio Predict API
  slug: kugelaudio-predict-api
- description: The Ready API from KugelAudio — 1 operation(s) for ready.
  name: KugelAudio Ready API
  slug: kugelaudio-ready-api
- description: The Tts API from KugelAudio — 1 operation(s) for tts.
  name: KugelAudio Tts API
  slug: kugelaudio-tts-api
- description: The Vapi API from KugelAudio — 1 operation(s) for vapi.
  name: KugelAudio Vapi API
  slug: kugelaudio-vapi-api
- description: The Voices API from KugelAudio — 6 operation(s) for voices.
  name: KugelAudio Voices API
  slug: kugelaudio-voices-api
artifact_total: 18
asyncapis:
- description: API Evangelist description of KugelAudio's documented WebSocket streaming surface. KugelAudio publishes no AsyncAPI document of its own; this file is GENERATED from the provider's own published wire-f
  name: KugelAudio TTS Streaming API
  slug: kugelaudio-tts-asyncapi
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kugelaudio-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kugelaudio-tts-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kugelaudio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kugelaudio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kugelaudio.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kugelaudio.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kugelaudio.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kugelaudio.com/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:hello@kugelaudio.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kugelaudio
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kugelaudio.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.kugelaudio.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://www.kugelaudio.com/en/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kugelaudio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kugelaudio.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.kugelaudio.com/status
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.kugelaudio.com/api-reference/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/kugelaudio-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kugelaudio-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kugelaudio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kugelaudio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kugelaudio-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/kugelaudio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kugelaudio-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kugelaudio-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/kugelaudio-api-catalog.json
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kugelaudio-llms.txt
created: '2026-07-17'
description: KugelAudio is a Y Combinator-backed, Germany-based voice AI company (KugelAudio GmbH) offering low-latency text-to-speech built, trained, and hosted entirely in the European Union. Its kugel-3 and kugel-2-turbo models produce natural speech in 26+ languages with accent and dialect coverage, voice cloning from a short reference sample, per-project pronunciation dictionaries with IPA support, word-level timestamps, and inline break, spell, and prosody tags. The platform positions EU data sovereignty as its core differentiator, operating outside the reach of the US CLOUD Act and offering a direct EU endpoint plus on-premise and dedicated deployment. The developer surface is a REST API for generation, voices, models, and dictionaries plus three WebSocket streaming channels tuned for real-time voice agents, including token-by-token input, barge-in, and up to 20 concurrent contexts per connection. Drop-in compatibility surfaces let ElevenLabs-compatible SDKs, LiveKit, PipeCat, and
  Vapi integrations point at KugelAudio without rewrites.
image: https://www.kugelaudio.com/icon.png
layout: provider
mcp_servers:
- description: ''
  name: kugelaudio-mcp.yml
  slug: kugelaudio-mcpyml
modified: '2026-07-19'
name: KugelAudio
nav: Providers
network: true
overview: 'KugelAudio publishes 14 APIs on the [APIs.io](https://apis.io/) network, including 11labs API, Audio API, billing API, and 11 more. Tagged areas include Voice, Text to Speech, Speech Synthesis, Voice AI, and Voice Cloning.


  The KugelAudio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KugelAudio''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 21 more developer resources.'
random_paper: 22
score:
  band: developing
  composite: 50.3
  delta: 2.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 55.7
    developer_ergonomics: 65.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 48.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kugelaudio/refs/heads/main/screenshots/kugelaudio-2026-07-25T224326.png
security:
- kind: authentication
  name: Kugelaudio Authentication
  slug: kugelaudio-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Kugelaudio Domain Security
  slug: kugelaudio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kugelaudio
tags:
- Voice
- Text to Speech
- Speech Synthesis
- Voice AI
- Voice Cloning
- Audio
- Artificial Intelligence
- Machine Learning
- Streaming
- Real Time
- Conversational AI
- Europe
- Data Sovereignty
- GDPR
- Company
website: https://www.kugelaudio.com
---
